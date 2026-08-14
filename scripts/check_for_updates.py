#!/usr/bin/env python3
"""Check whether a newer mistake-collection skill version is available."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


DEFAULT_VERSION_URL = (
    "https://raw.githubusercontent.com/"
    "DanielPro0706/mistake-collection/main/VERSION"
)
REPOSITORY_URL = "https://github.com/DanielPro0706/mistake-collection"
VERSION_PATTERN = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")


def parse_version(value: str) -> tuple[int, int, int]:
    version = value.strip()
    match = VERSION_PATTERN.fullmatch(version)
    if not match:
        raise ValueError(f"invalid semantic version: {version!r}")
    return tuple(int(part) for part in match.groups())


def default_state_file() -> Path:
    codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    return codex_home / "state" / "mistake-collection-update.json"


def read_json(path: Path) -> dict[str, object] | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, OSError, json.JSONDecodeError):
        return None
    return value if isinstance(value, dict) else None


def write_json(path: Path, value: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False) + "\n", encoding="utf-8")
    temporary.replace(path)


def fetch_remote_version(url: str, timeout: float) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "text/plain",
            "User-Agent": "mistake-collection-update-checker",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read(128).decode("utf-8").strip()


def result_payload(
    status: str,
    local_version: str,
    remote_version: str | None = None,
    message: str | None = None,
) -> dict[str, object]:
    payload: dict[str, object] = {
        "status": status,
        "local_version": local_version,
        "repository": REPOSITORY_URL,
    }
    if remote_version is not None:
        payload["remote_version"] = remote_version
    if message is not None:
        payload["message"] = message
    return payload


def emit(payload: dict[str, object], as_json: bool) -> None:
    if as_json:
        print(json.dumps(payload, ensure_ascii=False))
        return

    status = payload["status"]
    if status == "UPDATE_AVAILABLE":
        print(
            "UPDATE_AVAILABLE "
            f"local={payload['local_version']} remote={payload['remote_version']} "
            f"repository={payload['repository']}"
        )
    elif status == "UP_TO_DATE":
        print(f"UP_TO_DATE version={payload['local_version']}")
    elif status == "LOCAL_AHEAD":
        print(
            "LOCAL_AHEAD "
            f"local={payload['local_version']} remote={payload['remote_version']}"
        )
    elif status == "SKIPPED":
        print(
            "SKIPPED "
            f"local={payload['local_version']} remote={payload.get('remote_version', 'unknown')}"
        )
    else:
        print(f"CHECK_FAILED {payload.get('message', 'unknown error')}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-age-hours", type=float, default=24.0)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--timeout", type=float, default=5.0)
    parser.add_argument("--version-url", default=DEFAULT_VERSION_URL)
    parser.add_argument("--state-file", type=Path, default=default_state_file())
    parser.add_argument(
        "--local-version-file",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "VERSION",
    )
    args = parser.parse_args()

    try:
        local_version = args.local_version_file.read_text(encoding="utf-8").strip()
        local_tuple = parse_version(local_version)
    except (OSError, ValueError) as error:
        emit(result_payload("CHECK_FAILED", "unknown", message=str(error)), args.json)
        return 0

    now = time.time()
    cached = read_json(args.state_file)
    max_age_seconds = max(args.max_age_hours, 0.0) * 3600
    if not args.force and cached is not None:
        checked_at = cached.get("checked_at")
        if isinstance(checked_at, (int, float)) and now - checked_at < max_age_seconds:
            payload = result_payload(
                "SKIPPED",
                local_version,
                str(cached["remote_version"])
                if isinstance(cached.get("remote_version"), str)
                else None,
            )
            emit(payload, args.json)
            return 0

    try:
        remote_version = fetch_remote_version(args.version_url, args.timeout)
        remote_tuple = parse_version(remote_version)
    except (OSError, UnicodeError, ValueError, urllib.error.URLError) as error:
        emit(result_payload("CHECK_FAILED", local_version, message=str(error)), args.json)
        return 0

    if remote_tuple > local_tuple:
        status = "UPDATE_AVAILABLE"
    elif remote_tuple == local_tuple:
        status = "UP_TO_DATE"
    else:
        status = "LOCAL_AHEAD"

    try:
        write_json(
            args.state_file,
            {
                "checked_at": now,
                "local_version": local_version,
                "remote_version": remote_version,
                "status": status,
            },
        )
    except OSError:
        pass

    emit(result_payload(status, local_version, remote_version), args.json)
    return 0


if __name__ == "__main__":
    sys.exit(main())

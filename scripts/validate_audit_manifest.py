#!/usr/bin/env python3
"""Validate the source-fidelity audit manifest for a mistake collection."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED_PROBLEM_STATUS = "TEXT_EXACT"
REQUIRED_ANSWER_STATUS = "ANSWER_CROSSCHECKED"
REQUIRED_FIGURE_STATUS = "FIGURE_EXACT"
REQUIRED_BACKGROUND_STATUS = "PURE_WHITE"
ALLOWED_METHODS = {
    "imagegen",
    "imagegen_with_latex_overlay",
    "tikz",
    "source_restoration",
}
PDF_FLAGS = (
    "question_only_rendered",
    "answer_rendered",
    "question_text_synced",
    "question_only_pure",
)


def nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_manifest(data: object, manifest_path: Path, check_files: bool) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["manifest root must be a JSON object"]

    schema_version = data.get("schema_version")
    if schema_version not in {1, 2}:
        errors.append("schema_version must be 1 or 2")
    strict_figure_audit = schema_version == 2

    user_requires_imagegen = data.get("user_requires_imagegen", False)
    if not isinstance(user_requires_imagegen, bool):
        errors.append("user_requires_imagegen must be true or false")
        user_requires_imagegen = False

    problems = data.get("problems")
    figures = data.get("figures")
    if not isinstance(problems, list) or not problems:
        errors.append("problems must be a non-empty list")
        problems = []
    if not isinstance(figures, list):
        errors.append("figures must be a list")
        figures = []

    problem_ids: set[str] = set()
    referenced_figure_ids: set[str] = set()
    for index, problem in enumerate(problems, start=1):
        prefix = f"problem[{index}]"
        if not isinstance(problem, dict):
            errors.append(f"{prefix} must be an object")
            continue
        problem_id = problem.get("id")
        if not nonempty_string(problem_id):
            errors.append(f"{prefix}.id must be a non-empty string")
            continue
        assert isinstance(problem_id, str)
        if problem_id in problem_ids:
            errors.append(f"duplicate problem id: {problem_id}")
        problem_ids.add(problem_id)

        source_files = problem.get("source_files")
        if not isinstance(source_files, list) or not source_files or not all(
            nonempty_string(item) for item in source_files
        ):
            errors.append(f"{prefix}.source_files must contain at least one filename")
        elif check_files:
            for item in source_files:
                source_path = (manifest_path.parent / str(item)).resolve()
                if not source_path.exists():
                    errors.append(f"{prefix} missing source file: {item}")

        if problem.get("text_status") != REQUIRED_PROBLEM_STATUS:
            errors.append(f"{prefix}.text_status must be {REQUIRED_PROBLEM_STATUS}")
        if problem.get("answer_status") != REQUIRED_ANSWER_STATUS:
            errors.append(f"{prefix}.answer_status must be {REQUIRED_ANSWER_STATUS}")
        if not isinstance(problem.get("uncertainties"), list):
            errors.append(f"{prefix}.uncertainties must be a list")

        figure_ids = problem.get("figure_ids", [])
        if not isinstance(figure_ids, list) or not all(nonempty_string(item) for item in figure_ids):
            errors.append(f"{prefix}.figure_ids must be a list of non-empty strings")
        else:
            referenced_figure_ids.update(str(item) for item in figure_ids)

    figure_ids_seen: set[str] = set()
    for index, figure in enumerate(figures, start=1):
        prefix = f"figure[{index}]"
        if not isinstance(figure, dict):
            errors.append(f"{prefix} must be an object")
            continue
        figure_id = figure.get("id")
        if not nonempty_string(figure_id):
            errors.append(f"{prefix}.id must be a non-empty string")
            continue
        assert isinstance(figure_id, str)
        if figure_id in figure_ids_seen:
            errors.append(f"duplicate figure id: {figure_id}")
        figure_ids_seen.add(figure_id)

        if figure.get("problem_id") not in problem_ids:
            errors.append(f"{prefix}.problem_id must reference an existing problem")
        method = figure.get("method")
        if method not in ALLOWED_METHODS:
            errors.append(f"{prefix}.method must be one of {sorted(ALLOWED_METHODS)}")
        if user_requires_imagegen and method not in {
            "imagegen",
            "imagegen_with_latex_overlay",
        }:
            errors.append(f"{prefix}.method violates user_requires_imagegen")
        if figure.get("status") != REQUIRED_FIGURE_STATUS:
            errors.append(f"{prefix}.status must be {REQUIRED_FIGURE_STATUS}")
        if figure.get("background_status") != REQUIRED_BACKGROUND_STATUS:
            errors.append(
                f"{prefix}.background_status must be {REQUIRED_BACKGROUND_STATUS}"
            )
        long_side_px = figure.get("long_side_px")
        if (
            not isinstance(long_side_px, int)
            or isinstance(long_side_px, bool)
            or long_side_px < 1200
        ):
            errors.append(f"{prefix}.long_side_px must be at least 1200")
        for flag in ("labels_verified", "question_pdf_verified", "answer_pdf_verified"):
            if figure.get(flag) is not True:
                errors.append(f"{prefix}.{flag} must be true")
        if strict_figure_audit:
            for list_field in ("segment_inventory", "geometry_constraints"):
                values = figure.get(list_field)
                if not isinstance(values, list) or not values or not all(
                    nonempty_string(item) for item in values
                ):
                    errors.append(
                        f"{prefix}.{list_field} must contain non-empty strings"
                    )
            for flag in ("segments_verified", "constraints_verified"):
                if figure.get(flag) is not True:
                    errors.append(f"{prefix}.{flag} must be true")
        for path_field in ("source_crop", "final_asset"):
            value = figure.get(path_field)
            if not nonempty_string(value):
                errors.append(f"{prefix}.{path_field} must be a non-empty path")
            elif check_files:
                artifact_path = (manifest_path.parent / str(value)).resolve()
                if not artifact_path.exists():
                    errors.append(f"{prefix} missing {path_field}: {value}")

    missing_figure_records = referenced_figure_ids - figure_ids_seen
    if missing_figure_records:
        errors.append(
            "problem figure_ids missing from figures: "
            + ", ".join(sorted(missing_figure_records))
        )
    unreferenced_figures = figure_ids_seen - referenced_figure_ids
    if unreferenced_figures:
        errors.append(
            "unreferenced figure records: " + ", ".join(sorted(unreferenced_figures))
        )

    pdfs = data.get("pdfs")
    if not isinstance(pdfs, dict):
        errors.append("pdfs must be an object")
    else:
        for flag in PDF_FLAGS:
            if pdfs.get(flag) is not True:
                errors.append(f"pdfs.{flag} must be true")

    return errors


def self_test() -> int:
    valid = {
        "schema_version": 2,
        "user_requires_imagegen": True,
        "problems": [
            {
                "id": "1",
                "source_files": ["source.png"],
                "text_status": "TEXT_EXACT",
                "answer_status": "ANSWER_CROSSCHECKED",
                "figure_ids": ["fig-1"],
                "uncertainties": [],
            }
        ],
        "figures": [
            {
                "id": "fig-1",
                "problem_id": "1",
                "source_crop": "crop.png",
                "final_asset": "figure.png",
                "method": "imagegen",
                "status": "FIGURE_EXACT",
                "background_status": "PURE_WHITE",
                "long_side_px": 1800,
                "labels_verified": True,
                "segment_inventory": ["AC: A--C", "CE: C--E"],
                "geometry_constraints": ["A,O,C collinear", "CE parallel BD"],
                "segments_verified": True,
                "constraints_verified": True,
                "question_pdf_verified": True,
                "answer_pdf_verified": True,
            }
        ],
        "pdfs": {flag: True for flag in PDF_FLAGS},
    }
    valid_errors = validate_manifest(valid, Path("manifest.json"), check_files=False)
    invalid = json.loads(json.dumps(valid))
    invalid["problems"][0]["text_status"] = "TEXT_PENDING"
    invalid["figures"][0]["background_status"] = "OFF_WHITE"
    invalid["figures"][0]["segment_inventory"] = []
    invalid["figures"][0]["constraints_verified"] = False
    invalid_errors = validate_manifest(invalid, Path("manifest.json"), check_files=False)
    legacy = json.loads(json.dumps(valid))
    legacy["schema_version"] = 1
    for field in (
        "segment_inventory",
        "geometry_constraints",
        "segments_verified",
        "constraints_verified",
    ):
        legacy["figures"][0].pop(field, None)
    legacy_errors = validate_manifest(legacy, Path("manifest.json"), check_files=False)
    if valid_errors or legacy_errors or len(invalid_errors) < 4:
        print("SELF_TEST_FAIL")
        return 1
    print("SELF_TEST_PASS")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", nargs="?", type=Path)
    parser.add_argument("--check-files", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return self_test()
    if args.manifest is None:
        parser.error("manifest is required unless --self-test is used")

    try:
        data = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"AUDIT_FAIL: {error}")
        return 1

    errors = validate_manifest(data, args.manifest, args.check_files)
    if errors:
        for error in errors:
            print(f"AUDIT_FAIL: {error}")
        return 1
    print(
        "AUDIT_PASS "
        f"problems={len(data['problems'])} figures={len(data['figures'])}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

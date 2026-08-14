---
name: mistake-collection
description: Build a self-contained Chinese mistake collection from photographed or scanned school problems. Manually inspect the originals instead of relying on OCR, independently solve and web-cross-check answers without blindly trusting online solutions, faithfully redraw feasible figures with ImageGen, create synchronized question-only and black-question/red-solution PDFs, and format large solutions with aligned step commentary. Use for 错题整理、错题本制作、试题照片重排、题图重绘、双版本练习册、详细答案解析、初中规范解题步骤、or adding later problems to an existing collection.
---

# Mistake Collection

Build the collection directly from the user's current source files and instructions. This skill is self-contained: do not load, quote, adapt, or depend on another problem-summary or note-making skill.

## Update check

At the start of each use, resolve this skill's own directory and run `python3 scripts/check_for_updates.py --max-age-hours 24`. The checker may use its cached result instead of contacting GitHub again.

- If it prints `UPDATE_AVAILABLE`, tell the user the installed and remote versions and offer to update from the reported repository. Do not install, overwrite, or remove anything until the user explicitly approves the update.
- If it prints `UP_TO_DATE`, `LOCAL_AHEAD`, or `SKIPPED`, continue without mentioning the check unless the user asked about versions.
- If it prints `CHECK_FAILED`, continue the mistake-collection task without treating network access as a requirement. Mention the failure only when the user asked to diagnose updates.

## Deliverables

Unless the user says otherwise, create a folder named `错题整理` directly inside the current workspace and deliver:

- one editable LaTeX project;
- one `纯题目版.pdf` containing only the chapter heading, black original question blocks, and their necessary source figures;
- one `答案解析版.pdf` containing the identical black questions, followed by red answers, red reasoning, and red explanatory figures when useful;
- final cleaned figure assets required to rebuild the PDFs.

The question-only PDF must not contain a knowledge-point heading, tested-concept label, formula reminder, method hint, difficulty label, solution lead-in, common-error warning, answer, or explanation before or after a problem. Put any useful teaching material inside the red answer layer so it appears only in the answer PDF.

Do not add a cover, author, date, abstract, page decoration, concluding summary sentence, or unrelated teaching notes.

Infer a concise, accurate chapter title from the complete registered problem set. Use an umbrella title when the set spans closely related topics. Do not ask the user to supply a title by default. Only replace the inferred title when the user explicitly gives a title. Likewise, do not ask the user to restate the output folder, black/red convention, two-edition requirement, figure method, or solution-detail requirements already defined by this skill.

## Non-negotiable accuracy rules

1. Use the supplied photos as the source of truth. Inspect the original images manually at full resolution. OCR may assist search or produce a rough draft, but never use it as the sole reading method. Do not complete cropped or unreadable wording from memory.
2. Preserve wording, blanks, choices, mathematical symbols, units, labels, line order, and the inferred or explicitly specified chapter title. Unless the user explicitly asks to retain printed main numbers, renumber the completed collection continuously as `1, 2, ..., N`; retain original subpart numbering such as `（1）（2）（3）`.
3. Preserve problem-bearing visual state: connections, switch position, contact, needle direction and endpoint, scale marks, polarity, arrows, leaf angles, rays, and relative placement.
4. Never treat visible handwriting as authoritative. Solve each item independently and check the result.
5. Before finalizing answers, search the web for the exact or closest verifiable problem and compare multiple useful sources when available. Treat online answers as secondary evidence, not authority: never copy them uncritically or let them override the original wording, diagram state, independent derivation, dimensional checks, or school-level method.
6. When independent work and an online answer disagree, re-read the original, identify differing assumptions or transcription, recompute step by step, and seek a more authoritative source such as an official answer, teacher edition, textbook explanation, or reputable educational source. Report any unresolved conflict instead of silently choosing the online result.
7. Never omit a problem merely because it shares a photograph with another problem.
8. If a region remains ambiguous after inspecting the original at full resolution, identify the exact ambiguity and ask the user before final delivery.
9. Move obsolete files to Trash; do not permanently delete user material.
10. Treat printed knowledge summaries surrounding a problem as ancillary material unless the user explicitly says they are part of the question. Do not copy them into the question-only version.
11. Preserve the principal `.tex` source, all figure assets needed to rebuild it, and both final PDFs as deliverables. Cleanup may move compiler intermediates such as `.aux`, `.log`, `.xdv`, `.fls`, and `.fdb_latexmk` to Trash, but must never remove or trash the editable `.tex` project.

## Process

### 1. Establish scope

Resolve the destination first. Default to `<current workspace>/错题整理`; use another destination only when the user explicitly requests it. List all source files in the user's order. When the user specifies filename order, sort naturally by filename (for example, `IMG_3405` before `IMG_3406`) rather than by upload order, printed problem number, or inferred topic. Inspect each manually at full resolution, including HEIC originals rather than relying only on thumbnails or OCR. Make an internal register with one entry per visible target problem:

- source filename and visible problem number;
- exact text, choices, blanks, formulae, and units;
- every required figure;
- the exact start and end of the question block, separated from surrounding knowledge points, examples, hints, or commentary;
- visual details that affect the answer;
- cropped, obscured, or uncertain content.

Record the source filename beside each internal problem block while editing so later reordering cannot detach a question from its figure. When one problem spans consecutive photos, register all contributing filenames once; when one photo contains multiple problems, retain their top-to-bottom order within that filename.

Count problems by visible problem blocks, then count them again by the register. Resolve any mismatch before typesetting.

After the register is complete, summarize the shared subject and chapter scope into a concise title. Prefer the narrowest title that accurately covers every registered item. If the user explicitly supplied a title, use it exactly instead of the inferred title.

If the target folder already contains a question-only PDF and an answer PDF, render and inspect them before designing the new chapter. Reuse their established typography, margins, black/red convention, step-commentary structure, title placement, and general figure scale unless the user requests a change. Use those PDFs only as layout references, never as a source for the new questions.

### 2. Transcribe before solving

Transcribe only the actual problem block into editable Chinese LaTeX. Keep the question layer black. Use explicit LaTeX for formulae, underlines, tables, simple circuits, and labels. Do not place knowledge points, tested concepts, formulas supplied as reminders, method prompts, or error warnings in the question layer. Compare the retained question block against the source character by character before writing answers.

Size every fill-in underline from the expected answer rather than using a generic long rule. Measure the complete typeset answer, including its number, symbol, and unit, then make the visible line about `1.25` times that width by default to allow natural handwriting. Increase the factor only for unusually cramped symbols or drawing-style responses; do not use one oversized fixed rule. Use an answer-measuring macro such as `\answerblankfor{...}` so the answer stays invisible while determining the width. For calculation, proof, experiment, geometry, circuit-design, and other large problems, reserve a modest amount of handwriting space in the question-only build. Base the space on the expected number and length of student steps, keep it compact enough for a mistake collection, and suppress that empty space in the answer build.

Use [references/source-reconstruction.md](references/source-reconstruction.md) for image handling, diagram selection, and source comparison.

### 3. Reconstruct each figure

Attempt an ImageGen redraw first for every figure that can be reconstructed faithfully from the visible source. Crop the printed figure from the original photo, give that crop to ImageGen as the reference image, and request clean black-and-white textbook line art. Do not replace ImageGen with TikZ merely because the diagram looks simple. Keep exact words, numerical readings, units, and panel captions out of the generated bitmap when practical; overlay them deterministically in LaTeX.

Choose separately for every figure:

- **ImageGen redraw/edit:** always make the first serious attempt for feasible apparatus, physical scenes, biological figures, irregular outlines, and multi-state illustrations. State all invariants in the prompt, inspect the output, and compare it panel by panel with the original. If one invariant is wrong, retry ImageGen once with a targeted correction. Reject visually attractive results that alter problem information.
- **LaTeX/TikZ redraw:** use only after the ImageGen attempt and targeted retry still fail to preserve an answer-bearing state, exact ratio, topology, scale tick, reading, contact, direction, or connection. Record which invariant forced the deterministic fallback; never accept an approximate ImageGen diagram when the visual state affects the answer.
- **Source-based restoration:** use for complex or state-sensitive printed figures. Crop the original figure, remove handwriting and paper artifacts, correct exposure and perspective, and preserve the printed geometry.

Keep images no larger than necessary for comfortable reading. Start near `0.25–0.40\textwidth` for one compact apparatus, `0.45–0.60\textwidth` for a paired figure, and `0.65–0.80\textwidth` for a wide multi-state figure. Shrink any figure that dominates the question or creates avoidable page breaks. Adjust from the rendered page, not from the raw pixel dimensions.

### 4. Author answers independently

For every item:

1. determine the tested concept;
2. solve without using handwritten answers from the photo;
3. search the exact problem wording, distinctive numbers, or diagram description online and use the results only as a cross-check;
4. compare the independent result with available online solutions, checking whether their question text, assumptions, units, and diagram state actually match the source photo;
5. verify numerical work, units, direction, sign, range, circuit node, and diagram state yourself;
6. resolve or explicitly report any conflict rather than adopting the online answer by default;
7. write the final answer in red;
8. write enough red explanation that a student can reproduce the method rather than memorize the result.

The tested concept is internal reasoning and answer-side teaching material. If it is written into the document, place it inside the red answer layer, never before the black question in shared content.

For a calculation, experiment, proof, geometry, or circuit-design problem, show classroom-standard working on the left and align a smaller explanatory note on the right of each step. The note should explain purpose, rule, data source, or common failure mode, but do not prefix commentary with repeated labels such as `原因：`, `说明：`, or `步骤说明：`. Render the commentary in a muted secondary red that is visibly different from the main bright-red solution while remaining easy to read. Add a small red answer diagram when a direction, completed connection, auxiliary line, ray, force, state change, or instrument reading is clearer visually.

Use [references/solution-writing.md](references/solution-writing.md) for short-answer depth, large-problem formatting, and side explanations.

### 5. Generate synchronized versions

Maintain one principal `.tex` source with an answer switch so question text and source figures cannot drift between versions. Put every knowledge point, solution prompt, answer, explanation, error warning, and answer-side figure inside the conditional answer environment. Build the question-only version with that entire layer disabled and the answer version with it enabled. Use [assets/mistake-collection-template.tex](assets/mistake-collection-template.tex) only as a neutral scaffold; replace every placeholder with the actual task content.

### 6. Verify before delivery

Perform this verification after the final rebuild, not only during drafting. Reopen the original source images, the final question-only PDF, and the final answer PDF; do not rely on memory, earlier previews, or a successful compile.

Pass every gate:

- **Inventory and order:** each registered problem and figure appears once. Compare the final sequence against the natural filename order and the source-filename marker beside every problem block; confirm that multi-photo problems and multiple problems in one photo remain correctly grouped.
- **Transcription:** compare wording, punctuation, blanks, options, symbols, units, and labels against the original.
- **Figure:** compare every original crop and final figure at high zoom, panel by panel. Explicitly check water level, immersion fraction, top-edge alignment, contact or separation, slack versus taut string, arrow direction, connectivity, labels, readings, and all other state-sensitive details. A figure that merely looks plausible does not pass.
- **Solution:** recompute answers and confirm the reasoning uses the requested school-level method.
- **Online cross-check:** confirm that each answer was searched and compared with any relevant online solution found; verify source-question equivalence and independently resolve discrepancies. Record unresolved conflicts rather than presenting a web answer as certain.
- **Color:** all question material is black; all answer-side material is red.
- **Question-only purity:** inspect every page and confirm it contains no knowledge point, tested-concept label, formula reminder, method hint, difficulty tag, answer, analysis, common-error warning, or answer-side figure.
- **Writing usability:** confirm each large problem has a modest, usable writing area in the question-only PDF without excessive blank pages, and each fill-in underline is based on its expected complete answer with roughly `25\%` extra handwriting allowance rather than an arbitrary fixed length.
- **Synchronization:** question blocks and source figures match between both PDFs.
- **Build:** XeLaTeX finishes without errors; investigate meaningful layout warnings.
- **Visual:** render every page and inspect for clipping, overlap, broken glyphs, poor page breaks, unreadable figures, or oversized figures.
- **Composition:** keep the chapter title left-aligned, keep apparatus figures subordinate to the question text, and confirm side notes align with their corresponding formal steps without repetitive labels.
- **Files:** confirm the principal `.tex` source, required figure assets, question-only PDF, and answer PDF all still exist after cleanup; report their exact output paths and distinguish verified facts from anything still uncertain.

A successful compile is only a build check. It does not prove that the questions, figures, or solutions match the source.

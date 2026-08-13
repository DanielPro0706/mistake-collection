---
name: mistake-collection
description: Build a self-contained Chinese mistake collection from photographed or scanned school problems. Manually inspect the original images instead of relying on OCR, faithfully redraw feasible figures with ImageGen, create synchronized question-only and black-question/red-solution PDFs, and format large solutions with aligned step commentary. Use for 错题整理、错题本制作、试题照片重排、题图重绘、双版本练习册、详细答案解析、初中规范解题步骤、or adding later problems to an existing collection.
---

# Mistake Collection

Build the collection directly from the user's current source files and instructions. This skill is self-contained: do not load, quote, adapt, or depend on another problem-summary or note-making skill.

## Deliverables

Unless the user says otherwise, create a folder named `错题整理` and deliver:

- one editable LaTeX project;
- one `纯题目版.pdf` containing only the chapter heading, black original question blocks, and their necessary source figures;
- one `答案解析版.pdf` containing the identical black questions, followed by red answers, red reasoning, and red explanatory figures when useful;
- final cleaned figure assets required to rebuild the PDFs.

The question-only PDF must not contain a knowledge-point heading, tested-concept label, formula reminder, method hint, difficulty label, solution lead-in, common-error warning, answer, or explanation before or after a problem. Put any useful teaching material inside the red answer layer so it appears only in the answer PDF.

Do not add a cover, author, date, abstract, page decoration, concluding summary sentence, or unrelated teaching notes.

## Non-negotiable accuracy rules

1. Use the supplied photos as the source of truth. Inspect the original images manually at full resolution. OCR may assist search or produce a rough draft, but never use it as the sole reading method. Do not complete cropped or unreadable wording from memory.
2. Preserve wording, blanks, choices, mathematical symbols, units, labels, line order, and the requested chapter title. Unless the user explicitly asks to retain printed main numbers, renumber the completed collection continuously as `1, 2, ..., N`; retain original subpart numbering such as `（1）（2）（3）`.
3. Preserve problem-bearing visual state: connections, switch position, contact, needle direction and endpoint, scale marks, polarity, arrows, leaf angles, rays, and relative placement.
4. Never treat visible handwriting as authoritative. Solve each item independently and check the result.
5. Never omit a problem merely because it shares a photograph with another problem.
6. If a region remains ambiguous after inspecting the original at full resolution, identify the exact ambiguity and ask the user before final delivery.
7. Move obsolete files to Trash; do not permanently delete user material.
8. Treat printed knowledge summaries surrounding a problem as ancillary material unless the user explicitly says they are part of the question. Do not copy them into the question-only version.

## Process

### 1. Establish scope

List all source files in the user's order. Inspect each manually at full resolution, including HEIC originals rather than relying only on thumbnails or OCR. Make an internal register with one entry per visible target problem:

- source filename and visible problem number;
- exact text, choices, blanks, formulae, and units;
- every required figure;
- the exact start and end of the question block, separated from surrounding knowledge points, examples, hints, or commentary;
- visual details that affect the answer;
- cropped, obscured, or uncertain content.

Count problems by visible problem blocks, then count them again by the register. Resolve any mismatch before typesetting.

If the target folder already contains a question-only PDF and an answer PDF, render and inspect them before designing the new chapter. Reuse their established typography, margins, black/red convention, step-commentary structure, title placement, and general figure scale unless the user requests a change. Use those PDFs only as layout references, never as a source for the new questions.

### 2. Transcribe before solving

Transcribe only the actual problem block into editable Chinese LaTeX. Keep the question layer black. Use explicit LaTeX for formulae, underlines, tables, simple circuits, and labels. Do not place knowledge points, tested concepts, formulas supplied as reminders, method prompts, or error warnings in the question layer. Compare the retained question block against the source character by character before writing answers.

Use [references/source-reconstruction.md](references/source-reconstruction.md) for image handling, diagram selection, and source comparison.

### 3. Reconstruct each figure

Attempt an ImageGen redraw for every figure that can be reconstructed faithfully from the visible source. Give the source crop as the reference image and request clean black-and-white textbook line art. Keep exact words, numerical readings, units, and panel captions out of the generated bitmap when practical; overlay them deterministically in LaTeX.

Choose separately for every figure:

- **ImageGen redraw/edit:** preferred for apparatus, physical scenes, biological figures, irregular outlines, and multi-state illustrations when the visible structure can be preserved. State all invariants in the prompt and compare the result with the original. Reject visually attractive results that alter problem information.
- **LaTeX/TikZ redraw:** use when topology, scale ticks, exact geometry, or a state-bearing symbol must be encoded deterministically, or when ImageGen cannot preserve the required state.
- **Source-based restoration:** use for complex or state-sensitive printed figures. Crop the original figure, remove handwriting and paper artifacts, correct exposure and perspective, and preserve the printed geometry.

Keep images no larger than necessary for comfortable reading. Start near `0.25–0.40\textwidth` for one compact apparatus, `0.45–0.60\textwidth` for a paired figure, and `0.65–0.80\textwidth` for a wide multi-state figure. Shrink any figure that dominates the question or creates avoidable page breaks. Adjust from the rendered page, not from the raw pixel dimensions.

### 4. Author answers independently

For every item:

1. determine the tested concept;
2. solve without using handwritten answers from the photo;
3. verify numerical work, units, direction, sign, range, circuit node, and diagram state;
4. write the final answer in red;
5. write enough red explanation that a student can reproduce the method rather than memorize the result.

The tested concept is internal reasoning and answer-side teaching material. If it is written into the document, place it inside the red answer layer, never before the black question in shared content.

For a calculation, experiment, proof, geometry, or circuit-design problem, show classroom-standard working on the left and align a smaller explanatory note on the right of each step. The note should explain purpose, rule, data source, or common failure mode, but do not prefix commentary with repeated labels such as `原因：`, `说明：`, or `步骤说明：`. Render the commentary in a muted secondary red that is visibly different from the main bright-red solution while remaining easy to read. Add a small red answer diagram when a direction, completed connection, auxiliary line, ray, force, state change, or instrument reading is clearer visually.

Use [references/solution-writing.md](references/solution-writing.md) for short-answer depth, large-problem formatting, and side explanations.

### 5. Generate synchronized versions

Maintain one principal `.tex` source with an answer switch so question text and source figures cannot drift between versions. Put every knowledge point, solution prompt, answer, explanation, error warning, and answer-side figure inside the conditional answer environment. Build the question-only version with that entire layer disabled and the answer version with it enabled. Use [assets/mistake-collection-template.tex](assets/mistake-collection-template.tex) only as a neutral scaffold; replace every placeholder with the actual task content.

### 6. Verify before delivery

Pass every gate:

- **Inventory:** each registered problem and figure appears once, in order.
- **Transcription:** compare wording, punctuation, blanks, options, symbols, units, and labels against the original.
- **Figure:** compare the original and final figure at high zoom, explicitly checking state-sensitive details.
- **Solution:** recompute answers and confirm the reasoning uses the requested school-level method.
- **Color:** all question material is black; all answer-side material is red.
- **Question-only purity:** inspect every page and confirm it contains no knowledge point, tested-concept label, formula reminder, method hint, difficulty tag, answer, analysis, common-error warning, or answer-side figure.
- **Synchronization:** question blocks and source figures match between both PDFs.
- **Build:** XeLaTeX finishes without errors; investigate meaningful layout warnings.
- **Visual:** render every page and inspect for clipping, overlap, broken glyphs, poor page breaks, unreadable figures, or oversized figures.
- **Composition:** keep the chapter title left-aligned, keep apparatus figures subordinate to the question text, and confirm side notes align with their corresponding formal steps without repetitive labels.
- **Files:** report exact output paths and distinguish verified facts from anything still uncertain.

A successful compile is only a build check. It does not prove that the questions, figures, or solutions match the source.

---
name: mistake-collection
description: Create verified Chinese mistake-book handouts from photographed or scanned middle-school problems, with faithful editable LaTeX reconstruction, cleaned or redrawn figures, a black question-only PDF, and a black-question/red-answer PDF containing detailed student-standard solutions and step explanations. Use when users ask for 错题整理、错题本、题目重排、纯题目版与答案版、初中规范步骤、题图去笔迹、ImageGen 清图、LaTeX/PDF 交付，or later append large problems to the same collection.
---

# Mistake Collection

Turn source photographs into a reusable, auditable mistake collection. Accuracy outranks visual polish.

## Core contract

- Treat every source image as evidence. Reconstruct only visible target problems; do not infer hidden text.
- Preserve the exact problem wording, blanks, choices, symbols, numbering, units, labels, diagram state, needle angle, switch position, connection, and requested order.
- Mark genuinely unreadable content as uncertain and ask before final delivery. Never silently guess.
- Produce two synchronized PDFs by default:
  1. question-only: black problem text and clean figures, no answers;
  2. answer-and-explanation: the same black problems and figures, with answers, derivations, step explanations, and answer-side diagrams in red.
- Do not add a separate summary sentence unless requested.
- Keep source and output under the user-specified folder. If no folder is specified, create `错题整理` in the current writable workspace.
- Delete nothing permanently. Move obsolete outputs and intermediates to the macOS Trash when cleanup is required.

## Required companion skills

- Use the PDF skill for compilation, rendering, and visual QA.
- Use the image-generation skill for bitmap restoration or removal of handwriting when a diagram is complex or state-sensitive.
- Use web search only when a standard solution method needs authoritative confirmation; prefer original curriculum, official teaching, or reputable educational sources, then rewrite the reasoning independently in LaTeX.

## Workflow

### 1. Inventory before writing

1. List every supplied file in the user's intended order.
2. Convert HEIC or unsupported images to lossless working previews without changing the originals.
3. Inspect every image at readable resolution.
4. Create a source ledger containing, for each target item:
   - source filename;
   - visible problem number and exact text;
   - all blanks/options/units;
   - required figures and state-sensitive details;
   - unreadable or cropped regions.
5. Count target items twice: once from filenames and once from visible problem blocks. Resolve mismatches before finalizing.

Read [references/source-and-figure-fidelity.md](references/source-and-figure-fidelity.md) whenever figures, handwriting removal, cropping, or ImageGen restoration is involved.

### 2. Choose a figure strategy per figure

Use the least risky strategy:

- Rebuild simple geometry, circuits, arrows, tables, and schematic relationships in TikZ only when every state and label can be reproduced exactly.
- Restore a complex or state-sensitive printed figure from the source when it contains meter needles, apparatus contact, switches, rays, force directions, measurements, nontrivial curves, or details that are easy to misdraw.
- For an ImageGen restoration, crop to the figure first and state invariants explicitly. Remove handwriting, stains, surrounding prose, shadows, and paper clutter; preserve geometry and experimental state.
- Inspect the edited image against the source. Reject and redo any output that changes a needle angle, contact point, label, scale, connection, leaf angle, switch state, or other problem-bearing feature.
- Keep figures readable but subordinate to the problem. Start near 35–45% text width for a compact apparatus and 65–75% for a wide paired meter; enlarge only when labels become unreadable.

### 3. Reconstruct the problem

- Use editable Chinese LaTeX for all normal text and formulas.
- Keep problem text black.
- Reproduce blanks with explicit underlines, choices with the original labels, and units in proper math typography.
- Keep the chapter heading exact. Use a visible space in headings such as `第十三章\hspace{0.5em}简单电路`.
- Do not include author, date, abstract, cover page, headers, footers, or `\maketitle`.

### 4. Write the answer and explanation

- Solve independently before trusting handwriting visible in the source.
- Check the result against the question conditions and the restored diagram.
- For short questions, explain the governing fact, apply it to each blank/option, exclude distractors, and state the common mistake.
- For large problems, use middle-school-standard steps such as `已知`、`求`、`解`、`答`, or the subject-appropriate equivalent. Do not jump over substitutions, units, sign/direction decisions, or conclusions.
- Beside or immediately after each step, explain why the step is valid, what law or definition is used, and what mistake it prevents.
- Add a compact answer-side figure when direction, wiring, state change, force, optics, geometry, or data reading is materially clearer visually. Keep this explanatory figure red and separate from the black source figure.
- Keep all answers and explanations red. Do not add unrequested boxes.

Read [references/solutions-and-layout.md](references/solutions-and-layout.md) for large-problem structure, side explanations, answer diagrams, and the synchronized two-version template.

### 5. Build two synchronized versions

- Maintain one primary LaTeX source with a `\showanswers` switch.
- Build the answer version with answers enabled.
- Build a tiny wrapper source with `\showanswers=0` for the question-only version.
- Use descriptive stable filenames ending in `-纯题目版.pdf` and `-答案解析版.pdf`.
- Keep the editable `.tex` files and any final cleaned figure assets beside the PDFs unless the user gives another layout.

Use [assets/mistake-collection-template.tex](assets/mistake-collection-template.tex) as the starting template when no established project template exists.

### 6. Verification gates

Do not deliver until all gates pass:

1. **Source completeness:** every target problem and figure in the ledger appears exactly once.
2. **Text fidelity:** wording, numbering, blanks, options, symbols, units, and labels match the source.
3. **Figure fidelity:** compare source and final at high zoom; verify all state-sensitive details.
4. **Answer correctness:** recompute results; verify directions, nodes, units, ranges, and conditions.
5. **Version synchronization:** question blocks and figures are identical across both PDFs; only answer material differs.
6. **Compilation:** XeLaTeX completes without errors; inspect overfull/underfull warnings.
7. **Visual QA:** render every final page to PNG and inspect for clipping, overlap, tiny figures, oversized figures, broken glyphs, awkward page breaks, and answer separation.
8. **File QA:** confirm final paths, page sizes, page counts, and hashes. Move routine LaTeX intermediates and obsolete outputs to Trash rather than deleting them.

State verification honestly. A successful compile alone does not prove source or visual fidelity.

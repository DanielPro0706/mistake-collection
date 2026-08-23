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

Both PDFs must show a page number on every page and the footer notice `由 Codex 生成，内容可能存在错误，请自行核对。`. Keep the page number black and render only the notice in a muted, clearly legible gray. Keep its wording and gray styling identical in both editions.

The question-only PDF must not contain a knowledge-point heading, tested-concept label, formula reminder, method hint, difficulty label, solution lead-in, common-error warning, answer, or explanation before or after a problem. Put any useful teaching material inside the red answer layer so it appears only in the answer PDF.

Do not add a cover, author, date, abstract, page decoration other than the required numbered disclaimer footer, concluding summary sentence, or unrelated teaching notes.

## Mandatory web cross-check gate

Do not finalize or claim completion of an answer collection until every problem has received an actual web search attempt. Search exact wording first, then distinctive numerical data, option text, and diagram descriptions when necessary. Record internally whether an exact match, a close variant, conflicting solutions, or no useful result was found.

Online solutions are comparison evidence only, never ground truth for correctness. Independently derive every answer from the user's original wording and figure, then check the web result for question equivalence, assumptions, units, diagram state, and school-level method. Once an exact standard answer has passed that independent verification, it may become the wording and formal-step authority described below, but it still does not override a verified contradiction. Do not copy an online answer merely because it is labelled “standard answer,” and do not let a majority of websites overrule a verified derivation. Conversely, do not skip or conceal the search merely because the independent answer appears obvious or correct. If no matching answer is found, say so honestly and retain the independently verified result; if a conflict remains unresolved, report it before delivery.

For experimental questions, distinguish correctness from scoring wording. First verify independently that the experimental design, controlled variables, phenomenon, conclusion, and method name are correct. After confirming that an online or supplied standard answer belongs to the exact same question and is not substantively wrong, use its answer phrasing and scoring keywords as the wording authority instead of freely paraphrasing them. Preserve expected terms such as method names, controlled variables, observed phenomena, causal conditions, and conclusion scope. If the exact standard answer cannot be found, use concise textbook-standard wording; if a purported standard answer conflicts with the original figure or verified physics, report the conflict rather than reproducing an error.

For calculation, proof, experiment, geometry, circuit-design, and other large problems, treat a confirmed exact standard answer as the authority for the formal student-facing solution sequence. After verifying that it belongs to the same question and is substantively correct, follow its step order, notation, equations, intermediate conclusions, and scoring keywords instead of replacing them with a different derivation. Independently verify every step first. If no reliable exact standard answer exists, write independently derived classroom-standard steps; if the purported standard answer is wrong or mismatched, report the conflict and do not reproduce it. The aligned explanatory commentary is different: author it independently and make it as detailed as useful for learning, including reasons, data sources, hidden transitions, checks, and likely errors.

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
12. Treat every printed figure label as question-bearing until verified otherwise. Material and liquid names, values, units, scale readings, panel captions, experiment-group labels, arrows, and leader lines must survive either inside the asset or as exact deterministic LaTeX overlays.
13. Lock the question layer before consulting answer references. Web pages, teacher answers, answer keys, and similar problems may correct only the answer/analysis layer; they must never supply, normalize, shorten, reorder, or silently repair the question text or figure. If the photo is unclear, keep the item unresolved and ask the user rather than borrowing wording from the web.
14. When the user explicitly requires ImageGen, every final question-bearing bitmap must be produced or edited with ImageGen. Do not silently substitute a screenshot, thresholded crop, TikZ redraw, or another generator. If ImageGen cannot preserve an answer-bearing invariant after targeted retries, stop and report the exact failure before changing methods.
15. Do not use thresholding, binarization, aggressive sharpening, or enlarged screenshots as final figure assets. These operations commonly create jagged or fuzzy strokes. Final ImageGen assets must be print-sharp at their rendered size and placed on a visually uniform pure-white background with no gray paper cast.
16. Put the page number and the exact notice `由 Codex 生成，内容可能存在错误，请自行核对。` in the footer of every page in both editions. Keep the page number black and apply a muted, clearly legible gray only to the notice. The footer must remain outside the question and answer layers so it is always present, must not overlap body content, and must not be removed by the answer switch.
17. For every large problem with a verified exact standard answer, preserve that answer's formal step sequence, notation, intermediate conclusions, and scoring terms. Do not use it blindly: independently check its equivalence and correctness first. Write the aligned teaching commentary independently and as fully as needed; it may explain omitted transitions and reasoning beyond the standard answer without altering the formal solution steps.

## Process

### 1. Establish scope

Resolve the destination first. Default to `<current workspace>/错题整理`; use another destination only when the user explicitly requests it. List all source files in the user's order. When the user specifies filename order, sort naturally by filename (for example, `IMG_3405` before `IMG_3406`) rather than by upload order, printed problem number, or inferred topic. Inspect each manually at full resolution, including HEIC originals rather than relying only on thumbnails or OCR. Make an internal register with one entry per visible target problem:

- source filename and visible problem number;
- exact text, choices, blanks, formulae, and units;
- every required figure;
- a panel-by-panel figure-label inventory containing every printed word, symbol, value, unit, caption, grouping label, and its visible anchor position;
- the exact start and end of the question block, separated from surrounding knowledge points, examples, hints, or commentary;
- visual details that affect the answer;
- cropped, obscured, or uncertain content.

Record the source filename beside each internal problem block while editing so later reordering cannot detach a question from its figure. When one problem spans consecutive photos, register all contributing filenames once; when one photo contains multiple problems, retain their top-to-bottom order within that filename.

Count problems by visible problem blocks, then count them again by the register. Resolve any mismatch before typesetting.

Create a working `audit-manifest.json` from [assets/audit-manifest-template.json](assets/audit-manifest-template.json). Do not mark a problem `TEXT_EXACT` until its complete retained question block has been compared character by character with the full-resolution source. Do not mark an answer `ANSWER_CROSSCHECKED` until it has been independently solved and the required web search attempt has been recorded. Do not mark a figure `FIGURE_EXACT` until its source crop, final asset, and both rendered PDFs have been compared. The manifest is a verification artifact, not a substitute for manual inspection.

Treat the completed register and `TEXT_EXACT` entries as a source lock. Once locked, online references may affect only answers, scoring terms, and explanations. Any later question-layer change requires reopening the original photo, repeating the comparison, and relocking the affected entry.

After the register is complete, summarize the shared subject and chapter scope into a concise title. Prefer the narrowest title that accurately covers every registered item. If the user explicitly supplied a title, use it exactly instead of the inferred title.

If the target folder already contains a question-only PDF and an answer PDF, render and inspect them before designing the new chapter. Reuse their established typography, margins, black/red convention, step-commentary structure, title placement, and general figure scale unless the user requests a change. Use those PDFs only as layout references, never as a source for the new questions.

### 2. Transcribe before solving

Transcribe only the actual problem block into editable Chinese LaTeX. Keep the question layer black. Use explicit LaTeX for formulae, underlines, tables, simple circuits, and labels. Do not place knowledge points, tested concepts, formulas supplied as reminders, method prompts, or error warnings in the question layer. Compare the retained question block against the source character by character before writing answers.

Size every fill-in underline from the expected answer rather than using a generic long rule. Measure the complete typeset answer, including its number, symbol, and unit, then make the visible line about `1.25` times that width by default to allow natural handwriting. Increase the factor only for unusually cramped symbols or drawing-style responses; do not use one oversized fixed rule. Use an answer-measuring macro such as `\answerblankfor{...}` so the answer stays invisible while determining the width. For calculation, proof, experiment, geometry, circuit-design, and other large problems, reserve a modest amount of handwriting space in the question-only build. Base the space on the expected number and length of student steps, keep it compact enough for a mistake collection, and suppress that empty space in the answer build.

Use [references/source-reconstruction.md](references/source-reconstruction.md) for image handling, diagram selection, and source comparison.

### 3. Reconstruct each figure

Attempt an ImageGen redraw first for every figure that can be reconstructed faithfully from the visible source. Crop the printed figure from the original photo, give that crop to ImageGen as the reference image, and request clean black-and-white textbook line art. Do not replace ImageGen with TikZ merely because the diagram looks simple. Keep exact words, numerical readings, units, and panel captions out of the generated bitmap when practical; overlay them deterministically in LaTeX.

Request a print-ready raster with a longest side of at least `1200 px` (prefer roughly `1800–2400 px` for wide multi-panel figures), crisp anti-aliased black strokes, and a uniform `#FFFFFF` background. Inspect the actual output dimensions and background rather than trusting the prompt. Reject paper-gray corners, texture, shadows, halos, low-resolution crops, fuzzy enlarged lines, and compression artifacts. A source crop may remain beside the project for audit, but it must not be included in the final PDF when the user required an ImageGen redraw.

Before editing or redrawing, finish the figure-label inventory from the original at full resolution. If generated text is omitted from the bitmap, map every inventory entry to an exact LaTeX overlay or caption before typesetting the next problem. Never accept an unlabeled asset as complete merely because its geometry is correct. For experimental figures, explicitly retain substance names such as `水` or `酒精`, controlled-variable labels, panel identities, and experiment grouping because they can determine what is being compared.

Choose separately for every figure:

- **ImageGen redraw/edit:** always make the first serious attempt for feasible apparatus, physical scenes, biological figures, irregular outlines, and multi-state illustrations. State all invariants in the prompt, inspect the output, and compare it panel by panel with the original. If one invariant is wrong, retry ImageGen once with a targeted correction. Reject visually attractive results that alter problem information.
- **LaTeX/TikZ redraw:** use only after the ImageGen attempt and targeted retry still fail to preserve an answer-bearing state, exact ratio, topology, scale tick, reading, contact, direction, or connection. Record which invariant forced the deterministic fallback; never accept an approximate ImageGen diagram when the visual state affects the answer.
- **Source-based restoration:** use for complex or state-sensitive printed figures. Crop the original figure, remove handwriting and paper artifacts, correct exposure and perspective, and preserve the printed geometry.

Keep images no larger than necessary for comfortable reading. Start near `0.25–0.40\textwidth` for one compact apparatus, `0.45–0.60\textwidth` for a paired figure, and `0.65–0.80\textwidth` for a wide multi-state figure. Shrink any figure that dominates the question or creates avoidable page breaks. Adjust from the rendered page, not from the raw pixel dimensions.

Keep each composite figure, all deterministic overlays, panel captions, and grouping labels in one unbreakable LaTeX block such as a `minipage`. Do not allow a page break between an apparatus image and the labels needed to interpret it.

### 4. Author answers independently

For every item:

1. determine the tested concept;
2. solve without using handwritten answers from the photo;
3. search the exact problem wording, distinctive numbers, or diagram description online and use the results only as a cross-check;
4. compare the independent result with available online solutions, checking whether their question text, assumptions, units, and diagram state actually match the source photo;
5. verify numerical work, units, direction, sign, range, circuit node, and diagram state yourself;
6. resolve or explicitly report any conflict rather than adopting the online answer by default;
7. for experimental questions, retain the confirmed exact standard answer's phrasing and scoring keywords rather than replacing them with a personal paraphrase;
8. for every large problem with a confirmed exact standard answer, retain its formal step order, notation, equations, intermediate conclusions, and scoring keywords while independently verifying them;
9. write the final answer in red;
10. write enough independently authored red commentary that a student can reproduce the method rather than memorize the result; make it as detailed as useful without changing the standard formal steps.

The tested concept is internal reasoning and answer-side teaching material. If it is written into the document, place it inside the red answer layer, never before the black question in shared content.

For a calculation, experiment, proof, geometry, or circuit-design problem, show the verified standard answer's formal working on the left when one is available; otherwise use independently derived classroom-standard working. Align a smaller independently authored explanatory note on the right of each step. Make the commentary as detailed as useful: explain purpose, rule, data source, hidden transition, verification, and common failure modes, but do not prefix commentary with repeated labels such as `原因：`, `说明：`, or `步骤说明：`. Render the commentary in a muted secondary red that is visibly different from the main bright-red solution while remaining easy to read. Add a small red answer diagram when a direction, completed connection, auxiliary line, ray, force, state change, or instrument reading is clearer visually.

Use [references/solution-writing.md](references/solution-writing.md) for short-answer depth, large-problem formatting, and side explanations.

### 5. Generate synchronized versions

Maintain one principal `.tex` source with an answer switch so question text and source figures cannot drift between versions. Put every knowledge point, solution prompt, answer, explanation, error warning, and answer-side figure inside the conditional answer environment. Build the question-only version with that entire layer disabled and the answer version with it enabled. Use [assets/mistake-collection-template.tex](assets/mistake-collection-template.tex) only as a neutral scaffold; replace every placeholder with the actual task content.

### 6. Verify before delivery

Perform this verification after the final rebuild, not only during drafting. Reopen the original source images, the final question-only PDF, and the final answer PDF; do not rely on memory, earlier previews, or a successful compile.

Pass every gate:

- **Audit manifest:** run `python3 <skill-dir>/scripts/validate_audit_manifest.py audit-manifest.json --check-files` and require `AUDIT_PASS`. A passing manifest proves that required checks were recorded; it does not replace the source/PDF visual comparison.

- **Inventory and order:** each registered problem and figure appears once. Compare the final sequence against the natural filename order and the source-filename marker beside every problem block; confirm that multi-photo problems and multiple problems in one photo remain correctly grouped.
- **Transcription:** compare wording, punctuation, blanks, options, symbols, units, and labels against the original.
- **Figure:** compare every original crop, rebuilt asset, and rendered question-only PDF at high zoom, panel by panel. Reconcile the figure-label inventory entry by entry and require the original and final counts to match. Explicitly check material or liquid names, water level, immersion fraction, top-edge alignment, contact or separation, slack versus taut string, arrow direction, connectivity, values, units, captions, group labels, readings, and all other state-sensitive details. A figure that merely looks plausible does not pass.
- **Image quality:** for each final raster, verify the actual pixel dimensions, clean anti-aliased edges, uniform white background, and legibility at the PDF's rendered size. When ImageGen is user-mandated, confirm the manifest method is `imagegen` or `imagegen_with_latex_overlay`; a thresholded crop or deterministic replacement fails this gate.
- **Figure solvability:** read the final black question and its rendered figure as a student would, without consulting the answer. Confirm that each panel and compared variable is identifiable and that no omitted or page-separated label makes the problem ambiguous or unsolvable.
- **Solution:** recompute answers and confirm the reasoning uses the requested school-level method.
- **Online cross-check:** confirm that each answer was searched and compared with any relevant online solution found; verify source-question equivalence and independently resolve discrepancies. Record unresolved conflicts rather than presenting a web answer as certain.
- **Experimental wording:** for every experimental item with a confirmed exact standard answer, compare the final fill-ins and conclusions word for word against its scoring terms; do not lose method names, controlled variables, observed phenomena, conditions, or the scope of the conclusion through paraphrase.
- **Large-problem standard steps:** for every large problem with a confirmed exact standard answer, compare the final formal work against its step order, notation, equations, intermediate conclusions, and scoring keywords. Confirm separately that the aligned commentary was independently authored, is sufficiently detailed to expose hidden reasoning, and does not silently change the formal standard steps.
- **Color:** all question material is black; all answer-side material is red.
- **Question-only purity:** inspect every page and confirm it contains no knowledge point, tested-concept label, formula reminder, method hint, difficulty tag, answer, analysis, common-error warning, or answer-side figure.
- **Writing usability:** confirm each large problem has a modest, usable writing area in the question-only PDF without excessive blank pages, and each fill-in underline is based on its expected complete answer with roughly `25\%` extra handwriting allowance rather than an arbitrary fixed length.
- **Synchronization:** question blocks and source figures match between both PDFs.
- **Footer:** every page in both editions has a correct black page number and the exact notice `由 Codex 生成，内容可能存在错误，请自行核对。` in muted, clearly legible gray; confirm the wording and styling are identical between editions and do not overlap or clip body content.
- **Build:** XeLaTeX finishes without errors; investigate meaningful layout warnings.
- **Visual:** render every page of both editions and inspect for clipping, overlap, broken glyphs, poor page breaks, unreadable figures, oversized figures, or labels detached from their image or experiment group.
- **Composition:** keep the chapter title left-aligned, keep apparatus figures subordinate to the question text, and confirm side notes align with their corresponding formal steps without repetitive labels.
- **Files:** confirm the principal `.tex` source, required figure assets, question-only PDF, and answer PDF all still exist after cleanup; report their exact output paths and distinguish verified facts from anything still uncertain.

A successful compile is only a build check. It does not prove that the questions, figures, or solutions match the source.

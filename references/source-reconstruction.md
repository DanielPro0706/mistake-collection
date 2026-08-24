# Source Reconstruction

Read this file when photographs, scans, handwriting, diagrams, or cropped text are involved.

## Problem register

Create one row for each visible target problem, not one row for each image.

| Order | Source file | Printed number | Question boundary | Text complete | Figures | State checks | Uncertainty |
|---:|---|---|---|---|---:|---|---|

Record separate rows when one photograph contains several problems. Record the same problem once when it spans several photographs, noting all source files.

After the row is manually verified, set its working status to `TEXT_EXACT`. This is a source lock: answer websites and supplied solutions cannot modify the locked wording, blanks, options, symbols, units, order, or figure. If a later discrepancy appears, reopen the original image and relock the row only after another character-by-character comparison.

Mark where the actual question begins and ends. Exclude surrounding chapter explanations, knowledge-point summaries, worked-example commentary, method hints, difficulty labels, and handwritten notes unless the user explicitly identifies them as part of the question. A formula, table, condition, or instruction inside the problem block remains part of the question and must not be removed.

## Image preparation

- Keep original files untouched.
- Convert unsupported formats only into temporary lossless previews.
- Correct orientation before reading.
- Inspect the full frame first so edge text or a second problem is not missed.
- Then inspect text and figures manually at full resolution.
- Treat OCR only as a secondary aid for rough drafts or search. Compare every retained character, formula, unit, and label against the visible original; never accept OCR output without manual inspection.
- For restoration, crop around the complete printed figure with a small safety margin.

Exposure and perspective correction may improve readability, but must not erase faint scale marks, thin circuit branches, arrows, underlines, or labels.

## Figure semantic inventory

Before generating, cleaning, or redrawing a figure, inventory its semantic content from the full-resolution original. Use one row per visible item, not one row per panel:

| Panel | Exact item | Meaning or role | Visible anchor | Final representation | Verified |
|---|---|---|---|---|---|

Include every printed material or liquid name, symbol, value, unit, scale reading, arrow, leader line, panel caption, experiment number, grouping line, and state cue. Record repeated labels separately: four printed liquid names require four final entries even when three say `水`. Do not classify an item as decorative merely because it is small or outside the apparatus outline.

For experimental figures, identify what is held constant and what changes in each comparison. A label such as `水` versus `酒精`, a probe-depth difference, or an `实验 1` grouping can be the only evidence for the controlled variable. If removing an item would make the comparison ambiguous, it is answer-bearing and mandatory.

## Named-segment connectivity inventory

Create a separate row for every segment, ray, extension, or connection that is printed in the source or named in the question. Do not infer completion from endpoint labels.

| Panel | Required path | Source or wording | Endpoint/line invariant | Final drawing command or asset stroke | PDF verified |
|---|---|---|---|---|---|

Examples of distinct checks:

- `AC` must have one continuous stroke from point `A` to point `C`;
- `CE` must not be omitted merely because both `C` and `E` are labeled;
- if `E` lies on the extension of `BC`, verify the complete collinear chain `B-C-E` without a gap;
- if `FG` and `GH` are named, drawing a different line through a nearby point does not satisfy either segment;
- a point constrained by equal-length data must be placed from that data before connected segments are drawn; do not force a convenient horizontal or vertical alignment.

For TikZ, identify the exact path expression that draws each required segment. For a bitmap, inspect the stroke at high zoom. Then inspect the rendered question PDF separately. A correct source asset still fails when clipping, masking, scaling, or an overlay breaks the visible connection.

## Selecting a reconstruction method

### Redraw or edit with ImageGen

Use ImageGen as the first reconstruction method for every feasible visible figure. Crop the printed figure tightly from the original photo, inspect that crop, and pass it as the reference rather than prompting from the transcribed question alone. For apparatus, physical scenes, biological subjects, irregular shapes, and multi-state illustrations, do not skip directly to a deterministic redraw merely because it is faster.

Ask for a print-ready image with a longest side of at least `1200 px`, preferably `1800–2400 px` for a wide figure, on a uniform pure-white `#FFFFFF` background. Require crisp anti-aliased black strokes and forbid paper texture, shadows, gray wash, blur, halos, scan noise, and watermarks. After generation, inspect actual dimensions and the visible background. If the page corners or whitespace retain a gray paper cast, perform a targeted ImageGen correction before acceptance.

Do not turn a photographed crop into a final asset by enlarging, thresholding, binarizing, or aggressively sharpening it. These techniques can make thin textbook lines fuzzy or jagged and can erase scale ticks. They may be used only as temporary inspection aids. The final PDF must use the accepted ImageGen asset when the user explicitly requested ImageGen.

Keep generated text to a minimum. Ask ImageGen to omit readings, formulas, units, panel captions, and prose when those can be overlaid exactly in LaTeX. State all invariant positions, connections, immersion states, directions, relative heights, and ratios in the prompt. Inspect the first result manually against the crop. If an invariant is wrong, make one targeted ImageGen retry that names only the failed state while locking the correct parts. Do not accept a merely attractive drawing.

An intentionally text-free bitmap is only an intermediate asset. Before moving on, map every omitted inventory entry to a deterministic LaTeX overlay or caption with an explicit panel anchor. The final question layer, not the raw bitmap, must contain the complete source information.

### Redraw with LaTeX/TikZ

Fall back to LaTeX/TikZ only when the initial ImageGen attempt and targeted retry cannot preserve an answer-bearing invariant and the figure can be specified without interpretation. Typical reasons include an exact immersion ratio, waterline alignment, scale reading, circuit topology, contact state, or arrow endpoint. Record the failed invariant in working notes before switching methods.

After rendering, compare:

- number and connectivity of nodes or branches;
- symbol type and orientation;
- label spelling and position;
- open/closed or touching/separated state;
- arrow and polarity direction;
- relative proportions needed to read the problem.
- every entry in the named-segment connectivity inventory, including shared endpoints and collinear extensions.

### Restore the printed figure

Prefer restoration for analog scales, instrument needles, electroscopes, experimental apparatus, irregular curves, dense labels, optics setups, and any drawing where a small positional change changes the answer.

An image-edit prompt should say what may change and what must not change. Example structure:

```text
Edit the attached textbook-figure crop, rather than inventing a new diagram.
Remove handwritten marks, shadows, stains, background paper, and surrounding prose.
Correct mild exposure and perspective distortion; keep a plain white background.
Preserve exactly: [list printed labels], [scale and tick marks], [connections],
[contact or switch state], [needle endpoint and angle], [arrows], and all relative geometry.
Do not add text, values, symbols, arrows, borders, or watermarks.
Return a tight, complete crop with modest white margins.
```

If an edit changes any invariant, discard it and retry from the original crop rather than repairing the altered result repeatedly.

When the user explicitly requires ImageGen, do not switch to TikZ, source restoration, a screenshot, or another generator without reporting the failed invariant and obtaining approval. Fidelity still takes priority: if targeted ImageGen retries cannot preserve an answer-bearing state, pause instead of presenting an approximate figure as complete.

## Comparison pass

Compare source and reconstruction systematically:

1. outer boundary and overall orientation;
2. top-to-bottom labels and values;
3. left-to-right lines, nodes, contacts, and arrows;
4. state-bearing movable parts;
5. all scale ticks and the indicated reading;
6. figure caption and subfigure labels.

For multi-state buoyancy figures, additionally check each panel for water level, how much of the object is above or below the surface, whether its top edge is exactly level with the surface, whether it touches the bottom, and whether a string is absent, slack and curved, or taut and straight. These states must agree with both the printed figure and the question wording.

Finally inspect the figure inside the PDF. A faithful asset still fails if it is cropped, blurred by scaling, separated from its problem, or made disproportionately large.

Record `FIGURE_EXACT`, `PURE_WHITE`, the actual longest-side pixel count, the reconstruction method, label verification, and separate question-PDF/answer-PDF checks in `audit-manifest.json`. Validate it with `scripts/validate_audit_manifest.py` before delivery.

Compare three artifacts side by side: the original crop, the rebuilt asset, and the rendered question-only PDF. Check every inventory entry in left-to-right and top-to-bottom order, then require the number of source entries to equal the number of final visible entries. Inspect the answer PDF separately because enabled solutions can change pagination.

Keep a composite image, its overlays, subfigure captions, and experiment-group labels in one unbreakable LaTeX block. If a page break separates `水`/`酒精`, a value/unit, or an experiment caption from its apparatus, the figure fails even when all text technically exists elsewhere in the PDF.

End with a solvability test: read only the rendered black question and figure, without the solution or working notes. Confirm that a student can identify every panel, substance, value, controlled variable, and comparison needed to answer uniquely.

Start with compact rendered sizes: roughly one-quarter to two-fifths of the text width for one apparatus, one-half for paired figures, and no more than about four-fifths for a genuinely wide sequence. These are starting points, not quotas; shrink further when a figure dominates the page.

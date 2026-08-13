# Source Reconstruction

Read this file when photographs, scans, handwriting, diagrams, or cropped text are involved.

## Problem register

Create one row for each visible target problem, not one row for each image.

| Order | Source file | Printed number | Question boundary | Text complete | Figures | State checks | Uncertainty |
|---:|---|---|---|---|---:|---|---|

Record separate rows when one photograph contains several problems. Record the same problem once when it spans several photographs, noting all source files.

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

## Selecting a reconstruction method

### Redraw or edit with ImageGen

Prefer ImageGen for as many visible figures as can be reproduced without changing problem information. Pass the original crop as the reference and request clean black-and-white textbook line art. For apparatus, physical scenes, biological subjects, irregular shapes, and multi-state illustrations, this is usually the first method to try.

Keep generated text to a minimum. Ask ImageGen to omit readings, formulas, units, panel captions, and prose when those can be overlaid exactly in LaTeX. State all invariant positions, connections, immersion states, directions, and relative heights in the prompt. Inspect the first result manually; retry any changed invariant rather than accepting a merely attractive drawing.

### Redraw with LaTeX/TikZ

Redraw only when the figure can be specified without interpretation. Typical candidates are a simple circuit, geometric construction, labelled arrow, axis, or small data table.

After rendering, compare:

- number and connectivity of nodes or branches;
- symbol type and orientation;
- label spelling and position;
- open/closed or touching/separated state;
- arrow and polarity direction;
- relative proportions needed to read the problem.

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

## Comparison pass

Compare source and reconstruction systematically:

1. outer boundary and overall orientation;
2. top-to-bottom labels and values;
3. left-to-right lines, nodes, contacts, and arrows;
4. state-bearing movable parts;
5. all scale ticks and the indicated reading;
6. figure caption and subfigure labels.

Finally inspect the figure inside the PDF. A faithful asset still fails if it is cropped, blurred by scaling, separated from its problem, or made disproportionately large.

Start with compact rendered sizes: roughly one-quarter to two-fifths of the text width for one apparatus, one-half for paired figures, and no more than about four-fifths for a genuinely wide sequence. These are starting points, not quotas; shrink further when a figure dominates the page.

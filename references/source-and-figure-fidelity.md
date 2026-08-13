# Source and Figure Fidelity

## Source ledger

Record one row per target problem:

| Item | Source | Exact number | Text checked | Figure checked | Uncertainty |
|---|---|---:|---|---|---|

Treat two problems visible in one photograph as two items. Blue paper, fingers, or cropping may hide unrelated material; do not assume the visible target count equals the file count.

## Figure decision rules

### Rebuild in LaTeX/TikZ

Use TikZ for a figure whose meaning is completely described by deterministic lines, nodes, symbols, and labels, for example:

- a simple circuit with known connections;
- a geometric construction with exact coordinates;
- a direction arrow or answer-side flow diagram;
- a compact table or axis.

Compare node topology, labels, polarity, switch state, and branch structure against the source after rendering.

### Restore from the source

Prefer restoration for:

- analog meter scales and needle positions;
- electroscope leaves, balls, and contact states;
- complex optical, mechanical, biological, or experimental apparatus;
- figures whose printed imperfections encode the exact original state;
- diagrams that would take longer to reproduce faithfully than to clean.

## ImageGen restoration prompt pattern

Load the local crop with the image viewer before editing. Use a precise-object-edit prompt:

```text
Use case: precise-object-edit
Asset type: clean textbook figure for a Chinese mistake-book handout
Primary request: Remove only handwriting, correction marks, surrounding prose,
paper clutter, shadows, stains, and perspective distortion. Restore a uniform
white background and improve legibility.
Critical invariants: preserve every printed label, scale, tick, connection,
contact point, switch state, needle endpoint and angle, leaf angle, polarity,
and relative geometry exactly. Do not redesign or reinterpret the figure.
Composition: tight crop with complete apparatus and modest white margins.
Avoid: new text, new arrows, changed geometry, watermark, decorative border.
```

Repeat the invariants in any follow-up edit.

## Mandatory image comparison

For each restored figure:

1. View the source crop and edited output at original resolution.
2. Compare left-to-right and top-to-bottom.
3. Check state-sensitive features explicitly, not by overall resemblance.
4. Reject aesthetically cleaner output if it changes the physics or mathematics.
5. Embed the approved asset at a modest size and inspect it again in the rendered PDF.

## Failure modes

- A meter looks cleaner but its needle has moved.
- A connecting rod floats above metal balls instead of touching them.
- A switch changes from open to closed.
- A circuit branch is simplified away.
- ImageGen invents scale values or replaces Chinese labels.
- A figure is technically present but too large, too small, or separated from its question.

Any of these blocks delivery.

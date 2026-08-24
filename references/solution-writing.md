# Solution Writing

Read this file when producing answers, detailed analysis, large-problem steps, or answer-side diagrams.

All teaching material belongs to the answer layer. Knowledge points, tested concepts, formula reminders, method hints, and common-error notes must be placed inside the conditional red solution environment so none can appear in the question-only PDF.

## Short items

A short explanation should normally contain four parts:

1. the rule, definition, or instrument-reading convention;
2. the exact feature of the problem that activates that rule;
3. the resulting judgment for every blank or option;
4. the reason a likely wrong answer fails.

Do not pad the answer with generic encouragement or repeat the conclusion as if it were reasoning.

## Calculation and large problems

When an exact standard answer is available, first verify independently that it matches the original question, assumptions, values, units, and figure state and is substantively correct. Then use that answer's formal step order, notation, equations, intermediate conclusions, and scoring keywords as the student-facing solution. Do not replace it with a different derivation merely because another route is possible. If the standard answer is wrong, mismatched, or unavailable, say so when relevant and use independently derived classroom-standard steps.

When no verified exact standard answer is available, use the structure expected in the student's classroom. For a calculation problem, a useful default is:

```text
已知：list the usable quantities and conditions, including units.
求：name the requested quantity.
解：
  ① State the physical or mathematical relation.
     依据：explain why it applies here and define the symbols.
  ② Substitute the problem data with units.
     说明：explain the chosen value, sign, direction, range, or circuit node.
  ③ Calculate and simplify.
     检查：verify units, magnitude, condition, and required precision.
答：give a complete final sentence.
```

For proof, experiment, geometry, or circuit-design questions, replace the labels naturally while preserving the same discipline: one formal operation followed by one reason.

Never skip a transformation that a middle-school student is expected to show. Do not introduce advanced methods when a syllabus-level method is available.

## Line-by-line mathematical writing

Use a single left-aligned column for long solutions. Put each construction, condition, inference, calculation, or conclusion on its own short line. Do not compress several scoring steps into one paragraph.

- Write constructions in words: `连接 AC、BD，交点记为 O。`
- Do not write point definitions as intersection equations such as `O=AC\cap BD`.
- Prefer inline formulas such as `∵ $AB=AC$，∴ $\angle B=\angle C$。`
- Do not center a short equality merely to create visual spacing. Use display math only for a genuinely long aligned derivation that cannot remain legible inline.
- Do not use `⇒`, `→`, `\Rightarrow`, or `\Longrightarrow` as proof shorthand. State the reason or use ordinary wording.
- Basic cause-and-effect may use `∵` and `∴`. In LaTeX, prefer `$\because$` and `$\therefore$` or define safe Unicode mappings so the glyphs render in the math font.
- Keep every line left aligned. Do not indent formulas to form decorative centered blocks.

## Explanatory commentary

For calculation, experiment, proof, geometry, circuit-design, and other long solutions, put independently authored commentary immediately after the formal line it explains. Keep it left aligned and, when useful, use a smaller muted secondary red. Do not use a two-column layout by default. Commentary may unpack transitions omitted by the standard answer, but it must not alter the formal steps or introduce a conflicting method. The commentary should answer one or more of:

- Why is this relation or construction allowed?
- Where did this value come from?
- Why is this direction, sign, node, or range correct?
- What error would make this step wrong?
- How can the student check the result?

Do not solve a layout problem by shrinking text excessively. Allow the answer to continue onto another page.

## Answer-side figures

Add a compact red diagram when words alone leave a spatial or directional ambiguity. Suitable cases include:

- current and electron directions;
- a completed or corrected circuit;
- force, velocity, or ray direction;
- a geometric auxiliary line;
- apparatus state before and after an operation;
- the correct meter range or reading position.

The red explanatory diagram supplements the black question figure. It must not replace, cover, or silently modify the source figure.

## Page composition

- Use A4 portrait unless requested otherwise.
- Keep the chapter title left-aligned by default, matching any existing collection in the target folder.
- Keep margins comfortable and typography consistent.
- Keep each problem near its source figure.
- Keep source figures compact and subordinate to the text; reduce any image that dominates the page or forces an otherwise avoidable page break.
- Permit long answers to continue across a page rather than compressing them.
- Avoid decorative boxes, watermarks, automatic summaries, or a separate conclusion section.
- Use black only for question-side material and red only for answer-side material.
- In the question-only build, retain only the chapter heading, actual problem statements, choices or blanks, and figures required by those statements.
- In the question-only build, leave a modest writing area after calculation, proof, experiment, geometry, circuit-design, and other large problems. Estimate it from the expected student work: usually a few baseline heights for a short calculation and more only when several written steps or a drawing are genuinely required. Do not create large empty regions or unnecessary extra pages. Suppress this reserved area in the answer build so the red solution follows the question normally.
- Base each fill-in underline on the expected complete answer, including number, symbol, and unit, then add about `25\%` width for handwriting by default. Measure the hidden typeset answer instead of choosing one generic fixed width; enlarge further only when the symbols genuinely need it. Do not make a one-character answer sit on a long rule or crowd a multi-part answer onto a short rule.
- Do not put a knowledge-point banner or solution-oriented introduction before a black problem block.

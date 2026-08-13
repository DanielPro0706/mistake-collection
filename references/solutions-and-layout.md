# Solutions and Layout

## Short-question explanation

Use this order:

1. state the relevant definition, law, or instrument rule;
2. map it to the visible condition;
3. evaluate each blank or option;
4. exclude alternatives with their actual mechanism;
5. state the answer and one common mistake.

Do not replace analysis with a restatement of the answer.

## Large-problem standard

Use the standard structure expected of a middle-school student when applicable:

```text
已知：extract quantities and conditions with units.
求：state the requested quantity or conclusion.
解：
  Step 1 — write the governing relation or make the required judgment.
  Step explanation — why this relation applies and what each symbol means.
  Step 2 — substitute values with units or perform the construction.
  Step explanation — why the substitution, sign, direction, or node is correct.
  Step 3 — calculate, simplify, and state the unit.
  Step explanation — check order of magnitude, condition, and significant reading.
答：answer in a complete sentence.
```

Adapt labels for proofs, experimental design, multiple choice, and non-calculation subjects, but retain the one-step/one-reason discipline.

## Side explanations

For a genuinely long solution, use a two-column answer block:

- left: the student's formal steps;
- right: smaller red explanations beginning with `为什么：` or `依据：`.

Keep each explanation aligned with its corresponding step. If a two-column layout would become cramped, place the explanation immediately below the step instead of shrinking the font excessively.

## Answer-side diagrams

Add a red answer diagram when it reduces ambiguity, especially for:

- electron direction versus conventional current;
- series/parallel completion and current paths;
- force direction or free-body diagrams;
- ray diagrams;
- geometric auxiliary lines;
- corrected switch, valve, or apparatus state;
- meter reading or graph interpretation.

The answer diagram supplements, never replaces, the black source figure. Keep it compact.

## Two-version source design

Use one main file and a wrapper:

```tex
\providecommand{\showanswers}{1}
\ifnum\showanswers=1
  \newenvironment{mcanswer}{\par\begingroup\color{mcred}}{\par\endgroup}
\else
  \usepackage{comment}
  \excludecomment{mcanswer}
\fi
```

Question-only wrapper:

```tex
\def\showanswers{0}
\input{main.tex}
```

This prevents the two versions from drifting.

## Page and color rules

- A4 portrait, approximately 1.5–2 cm margins, no cover page.
- Black: chapter title, problem text, source diagrams.
- Red: answers, derivations, reasons, error analysis, and answer-side diagrams.
- Keep a problem with its source figure whenever practical.
- Let detailed answers continue naturally; avoid a nearly blank page caused by an unnecessary manual break.
- Do not use automatic boxes or decorative emphasis.

---
name: research-figure-studio
description: Create, revise, and audit scientific plots, mechanisms, engineering diagrams, and figure sets for papers, theses, reports, and appendices. Choose figures by the evidence and research question.
---

# Research Figure Studio

Choose the visual comparison that lets the reader answer the scientific question. Use one visual system across a figure set.

## Always load

- Read [references/personal-style.md](references/personal-style.md) before designing any figure.
- Read [references/qa.md](references/qa.md) before delivery.

The confirmed typography is Chinese SimSun (宋体), English and numerals Times New Roman, and 1 pt figure/axes borders. Text is one point larger than the previous figure batch; use the explicit size baseline in `personal-style.md`, without adding another point on each later invocation. Apply this profile even when a source paper or older renderer has different defaults. [scripts/style_defaults.py](scripts/style_defaults.py) provides reusable Matplotlib settings.

The confirmed colour direction is bright, fresh, positive and sunny on white. Prefer clear sky blues, warm oranges, mint greens and other light, distinguishable accents; avoid dark or muddy data fills and large dark backgrounds. Keep text and frames readable, and preserve scientific colour semantics. The shared style helper contains starting palettes.

## Civil and transportation figure grounding

For civil, geotechnical or transportation figures, read [references/civil-transport-exemplars.md](references/civil-transport-exemplars.md). Inspect the relevant original at its cited figure or PDF page, using a local excerpt if available. Borrow the evidence structure and adapt it to the actual data and confirmed visual style.

If the current question has no suitable exemplar, find a relevant primary paper and inspect its actual figure and caption before proposing a new visual form. Record the paper, figure number, what is borrowed, and which geometry or evidence differs. Do not equate an abstract, a journal name, or a palette with having reviewed a figure.

## Route by evidence type

Read [references/routing.md](references/routing.md), then load only the relevant detailed reference:

- Concept, mechanism, process, experimental setup, engineering structure, or system architecture → [references/concept-figures.md](references/concept-figures.md).
- Bar, line, curve, scatter, box/violin, heatmap, contour, spatial, sensitivity, or uncertainty plot → [references/data-figures.md](references/data-figures.md).
- Multi-panel figure or a figure mixing schematics, images, and plots → [references/multipanel.md](references/multipanel.md).
- Circular open-caisson work → additionally read [references/domain-caisson.md](references/domain-caisson.md).

## Core workflow

1. Write the one-sentence conclusion the figure must communicate.
2. Identify the evidence type, source files, units, groups, uncertainty meaning, and target use. Ask only when a missing answer would change the scientific meaning.
3. Inspect the real data or geometry before choosing the figure type. Do not invent values, intervals, significance, dimensions, components, or construction states.
4. Select a figure form using the routing reference. One question should produce one clear visual argument; split figures when two unrelated conclusions compete.
5. Draw with deterministic vector-capable code for scientific and engineering content. Use generative imagery only for genuinely illustrative material and never as geometric evidence.
6. Render a PNG preview, inspect the actual image, fix failed geometry/data/style checks, and render again. Coordinates or a successful script do not prove visual correctness.
7. Deliver the reproducible source, editable PDF or SVG, and a 300 dpi PNG preview. Include concise data/statistics notes when quantitative claims appear.

## Integrated behavior

- Borrow specialist techniques selectively using [references/technique-sources.md](references/technique-sources.md): data-role mapping, semantic template checks, final-size/export checks, diagram topology and native editability. The integrated Skill remains the main workflow; specialist defaults never replace the user's confirmed style. For Matplotlib output, use [scripts/audit_layout.py](scripts/audit_layout.py) to flag mechanical layout/style defects, then inspect the actual rendered image; the report does not certify scientific or visual quality.

- Use engineering-illustration discipline for exact components, proportions, section lines, and callouts.
- Use publication-data discipline for complete data, honest uncertainty, accessible colors, typography, and vector export.
- Use Nature-style hierarchy only when the evidence has a real hero panel; do not force asymmetric layouts onto simple plots.
- Use direct labels and concise explanations where they reduce eye travel, but do not turn manuscript figures into card-based infographics.
- Default to one refined version. Produce multiple genuinely distinct candidates only when the user explicitly requests comparison.
- When revising a crowded figure, first try separating different reading tasks. Use a focused main plot for one comparison and same-scale facets when overlapping groups obscure the evidence. Verify that all declared observations are represented after restructuring.
- For a matched two-condition contrast, check whether a paired plot or a signed difference is readable at output size. For independent validation, check pairing, the held-out benchmark and units before using a reference or residual plot.

## Persistent preference rule

Treat confirmed user corrections as project-level constraints and encode them in the relevant domain or style reference. Do not generalize a domain-specific correction into all scientific figures, and do not forget it when the same domain returns.

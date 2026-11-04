# Figure QA

Inspect the rendered PNG and the source/data before delivery.

## Scientific integrity

- [ ] For civil/transport figures, the relevant original exemplar and caption were inspected; the borrowing and differences are recorded.
- [ ] A mechanism panel contains the actual objects and relationships needed to explain the claim; a process/feedback diagram is not presented as physical evidence.
- [ ] A validation panel identifies the reference measurements, benchmark or independent solution. Correlation between arbitrary result summaries is not relabelled validation.

- [ ] The one-sentence conclusion is visible within a few seconds.
- [ ] Every plotted value and structural component has a source.
- [ ] No data were silently dropped or downsampled.
- [ ] Uncertainty and statistics are defined and not fabricated.
- [ ] Units, coordinate direction, case identity, and construction/model state are correct.

## Visual integrity

- [ ] Mechanical checks for missing glyphs, small text, canvas clipping, tick overlaps, frame widths and bar outlines were reviewed when applicable (see `scripts/audit_layout.py`). Warnings are investigated against the actual render; absence of warnings is not a scientific or aesthetic certification.

- [ ] Bars and corresponding legend swatches have visible, opaque, solid 1 pt outlines. Bright fills remain clean; no shadow/bevel is added.
- [ ] Data annotations use nearby labels, short headless leaders or a tidy comparison bracket; long oblique arrows and large emphasis rings do not compete with the data.

- [ ] A small number of useful quantitative highlights are present where they help; each is recomputed from the plotted data, identifies its group/reference and units, and does not obscure points or overstate a subset result.

- [ ] Data colours and large filled regions look bright, fresh and sunny on white; there are no sombre/muddy main colours or large dark fills. Text, frames, symbols and colour-scale meaning remain legible.

- [ ] Chinese uses SimSun; English, numerals and Latin units use Times New Roman, including mixed labels, legends and annotations. Actual exported PDF font records were checked.
- [ ] Text follows the confirmed non-cumulative +1 pt baseline (10 pt main/axis text, 9 pt ticks/legends/notes, 11 pt panel headings); explicit small labels were also increased.
- [ ] All figure/axes frames, colourbar outlines and diagram container borders are 1 pt; no legacy local override changed them.

- [ ] Panel organisation follows scientific comparisons (condition, stage, scenario, metric or view), not a target number of panels.
- [ ] Comparable field panels have matched geometry/view and a stated, appropriate colour scale; quantitative fields come from real source data.

- [ ] No clipped, overlapping, duplicated, or misdirected labels/arrows.
- [ ] Statistic labels are attached to their actual computed marks/levels; a convenient blank area has not disconnected a median, quantile or peak label from its target.
- [ ] At intended export size, raw-point layers do not hide statistical summaries, optional marginals do not dominate the main relationship, and the main condition comparison can be read directly.
- [ ] For a geographic detail panel, overview rectangle and detail limits share the same bounds, the subset count is checked, and the overview retains every valid location in the declared dataset.
- [ ] Symbols, line styles, and colors remain distinguishable in greyscale.
- [ ] Data plots have no internal gridlines unless explicitly justified.
- [ ] Concept and engineering figures are technical rather than illustrative.
- [ ] Multi-panel labels, margins, line weights, and color semantics are consistent.
- [ ] The figure remains readable at final manuscript size.

## Geometry integrity

- [ ] Plan, section, and detail views agree.
- [ ] Interfaces and dimensions meet at the intended coordinates.
- [ ] No object exists only to make the drawing look complete.

## Delivery

- [ ] For a specified final size, the actual exported dimensions and document scaling were checked; no copied local journal preset was represented as a verified current submission rule.

- [ ] Reproducible source is included.
- [ ] Editable PDF or SVG is included.
- [ ] PNG preview is at least 300 dpi.
- [ ] Quantitative figures include concise source/statistics notes when needed.

Any failed item requires a source-level correction and a fresh render.

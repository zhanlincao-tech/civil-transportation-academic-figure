# Personal scientific-figure style

## Shared appearance

- White background, bright and fresh colours, clear hierarchy, and publication-scale typography. The user explicitly wants a positive, sunny visual mood and rejects dark or sombre colour schemes.
- Prefer colored technical figures over black-and-white, but ensure line style and symbols survive greyscale printing.
- Avoid cartoon, painterly, photorealistic, presentation-card, and generic AI-infographic styles.
- Use one coherent font, arrow system, line-weight hierarchy, and semantic color mapping per figure.
- Do not add a large in-panel title when the manuscript caption should carry it.
- Use primary literature conventions when the field-specific visual grammar is uncertain.

## Data plots

- Default to a complete four-sided frame for the user's research plots.
- Bars have a clearly visible, solid 1 pt outline, distinct from the bright fill (default neutral `#526475`). Keep stroke opacity at 1 even when the fill is light; update legend swatches to match. Do not use shadows or 3D bevels.
- Do not use internal gridlines. A scientifically meaningful zero/reference line is allowed.
- Use visible symbols for measured/sample points and distinguish series by color + line style + marker shape.
- Prefer open circle, square, and triangle markers with colored edges.
- Use all valid source data. Spaced markers on a full curve are display choices, not downsampling.
- Keep legends borderless and away from dense data; use direct labels when clearer.
- Annotate selected endpoint or peak values only when they help the scientific comparison.

## Confirmed selective data highlights

- The user wants a small amount of prominent quantitative information to make figures more informative. Normally start with one to three meaningful highlights per figure, adjusting to density and panel count; do not label every mark or fill empty space with numbers.
- Prioritise relevant extrema, representative case values, endpoints, or a well-defined difference. State the case/group, value and unit, and define the reference for a difference, ratio or percentage. A selected-subset extremum must not be described as the global extremum.
- Compute annotations directly from the plotted source slice. Preserve signs and metric definitions; avoid unstable percentages near zero, invented significance, performance claims or causal interpretations.
- The user disliked the long oblique annotation arrows. Prefer nearby direct labels. When a pointer is necessary, use a short, restrained leader without an arrowhead; place comparison text directly beside a clean bracket. Avoid large emphasis rings and competing diagonal arrows. This applies to data annotations, not physically meaningful force/flow arrows in engineering diagrams.
- Keep the confirmed fonts and bright semantic colours; do not add dark cards, large badges or decorative effects. A numeric label at a bar end usually needs no arrow; use the axis/category and legend to identify the value without repeating a long callout.
- Place highlights in genuine free space, keep source marks visible, and inspect the final render. In an already annotated matrix, emphasise a small number of relevant cells rather than adding another layer of repeated numbers.

## Confirmed bright colour direction

- Default to clear sky blue, warm orange, mint green, light violet, coral and cyan. Use light, clean fills and enough saturation for visible curves and symbols. Avoid navy, forest green, brown/ochre, muddy grey-purple, heavy dark fills and dark backgrounds as the main data colours.
- Use dark neutral text and 1 pt frames for legibility against white; the bright-colour preference applies to the visual mood and data colours, not to making text faint.
- Starting categorical palette: `#42A5F5`, `#FFB547`, `#38C9A3`, `#AC94EA`, `#FF8A80`, `#4DD0E1`. These are implementation starting points, not separately user-approved exact hex values. Adjust slightly for visibility and use redundant markers/line styles.
- Sequential fields: white/light tint to clear medium-bright colour; signed fields: bright blue–white–warm orange, retaining a true zero centre and honest range. Do not use a dark endpoint simply because a default colour map does.
- Colour still represents categories or physical meaning. Keep the same meaning the same colour across panels; do not use rainbow scales, glow, decorative gradients or celebratory clip art to communicate the requested mood.

## Confirmed fonts, sizes and borders

- Chinese characters use SimSun (宋体); English letters, numerals and Latin units use Times New Roman. In mixed text, select fonts by glyph rather than applying SimSun to the entire string. Set mathematical Latin fonts to Times New Roman when supported.
- Figure/axes frames, colourbar outlines and diagram container borders are exactly 1 pt. This is a border rule, not a requirement to make every data curve, tick, arrow or reference line 1 pt.
- The user requested all text one point larger than the previous batch. That batch used 9 pt main/axis text, 8 pt ticks/legends/notes and 10 pt panel headings; the new baseline is respectively 10, 9 and 11 pt. Previous 7.5 pt direct labels become 8.5 pt and 7.3 pt matrix values become 8.3 pt. Use at least these sizes for the corresponding roles, and enlarge the canvas/margins if needed. Do not cumulatively add another point on every invocation.
- Apply these fonts to labels, ticks, legends, panel labels, annotations, colourbars and Chinese preview text. Recheck explicit local font/linewidth overrides in legacy renderers.
- Resolve the actual font files before rendering; inspect exported PDF font records and the rendered mixed-language preview. If the fonts are unavailable, report it rather than silently substituting another font. Preserve editable text in SVG and embed fonts in PDF.
- `scripts/style_defaults.py` implements this baseline. Previously approved figure structures, colours, four-sided frames and no-grid preference remain in force.

## Schematics and concept figures

- Prefer deterministic SVG/PDF-capable geometry.
- Use plan + section + local detail when one view cannot prove the structure.
- Keep components and arrows tied to actual evidence; do not fill empty space with decoration.
- Use clean pale blue for water, light sand for soil, and light neutral concrete, with clear outlines; use bright accents where useful. Avoid dark brown/ochre masses and heavy grey shading. Materials and construction geometry remain exact.

## Confirmed figure treatments

The user selected these treatments in two rounds of actual figure comparisons. Apply them when the scientific question fits; they are visual preferences, not evidence that a mechanism or statistic is valid.

| Figure family | Selected treatment | Decision boundary |
|---|---|---|
| Feedback concept diagram | Ring organisation, concise rectangular nodes, directional connectors, feedback differentiated from the main path (candidate 3) | Use a ring only for a real or explicitly proposed feedback relationship; do not make all concepts circular. |
| Category comparison | Vertical bars, meaningful category order, zero baseline, selected numeric labels (5) | Define real uncertainty when available; no fabricated error bars. |
| Time histories and curves | Overlay series on one axis with open markers and distinct line styles; retain a compact borderless legend and add case/endpoint labels (7 + 9) | Space direct labels beyond the frame or in a clear gutter without extending the apparent data duration. Resolve collisions for larger series counts. |
| Continuous-variable relationship | Main grouped scatter with aligned marginal histograms above and to the right (11) | Show all valid points; label count versus density explicitly and use the same data slice in the scatter and marginals. |
| Distribution comparison | Box plot with all observations plus a complementary empirical cumulative distribution panel (13 + 15) | State observational unit, group sizes and box/whisker convention; these panels display the same observations and are not independent evidence. |
| Signed matrix / heatmap | Rectangular matrix with cell values, readable labels and a labelled colourbar (16) | Use a zero-centred diverging scale for signed responses, a sequential scale for nonnegative quantities. Matrices do not imply real spatial geometry. |
| Method / framework | Vertical main sequence; branch into parallel tasks only where meaningful, then merge for a shared downstream stage (19 + 21) | Keep prerequisites sequential, parallel branches genuinely independent, and arrow meaning explicit. |

## Calibration status

- After the two candidate rounds, the user explicitly preferred the inspected original figures from Geotechnique and Transportation Research B/C and the topic-specific ICE caisson example. For civil/transport tasks, combine those evidence structures with the previously selected treatments; consult `civil-transport-exemplars.md`. A preferred feedback ring is not a replacement for a physical mechanism drawing, and a preferred marginal scatter is not a mandatory attachment to every validation plot.

- Both rounds establish preferred treatments for seven figure families. The merged compositions remain open to refinement.
- Font families, the one-point text increase, 1 pt borders and bright/positive/sunny colour direction are explicitly confirmed. Exact hex colours, panel proportions and label placement remain open to refinement.
- For box + cumulative plots, prefer two coordinated panels rather than forcing different meanings onto a dual axis.
- Keep domain-specific geometry in the domain reference; do not generalise caisson constraints to other engineering figures.
- For new figure families, use the shared appearance and evidence routing, then offer genuinely different candidates if comparison is requested. Do not ask the user to reselect previously confirmed treatments without a reason.

## Aggregation and labelling safeguards

- Do not combine an ALL aggregate with its constituent directional groups as though they were independent observations.
- State filters such as depth band, case, region and time. A valid explicitly declared slice is not silent data removal.
- Distinguish cross-case or spatial heterogeneity from replicate uncertainty; do not attach inferential significance to grouped summary data without an appropriate design.
- Preserve the source metric's reference (e.g. additional versus total displacement) and units in axis labels and captions.

## Candidate policy

Default to one self-reviewed version. When the user explicitly asks to compare styles, candidates must differ in information organization or visual grammar, not merely palette.

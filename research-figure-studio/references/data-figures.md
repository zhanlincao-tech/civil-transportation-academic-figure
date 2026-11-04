# Quantitative scientific figures

## Data contract

Check row count, fields, types, missing/nonfinite values, units, grouping, pairing, order, and uncertainty definition before plotting. Never fabricate error bands, replicates, thresholds, or significance.

- Distinguish numeric identifiers from measurements, and assign source fields to plotted values, grouping/pairing, uncertainty/support or retained-but-not-plotted roles. Reading a column does not make it a curve; a declared scientific slice is not an obligation to plot every source column.
- Before reusing a recipe, match its meaning: count versus density, one- versus two-dimensional distribution, paired versus unpaired evidence, and whether log/normalisation is defined for the actual values. Templates contribute layout, not source data, fits, uncertainty or geometry.
- For time histories, retain genuine gaps and discontinuities; do not draw across missing intervals or smooth/remove points as an unrequested visual fix. For dense data use rasterisation or a scientifically appropriate density summary, with the underlying data retained.
- For prediction figures require matched observed/predicted pairs and state the evaluation split; add equality, residuals or intervals only when they answer the question and their values are supplied or validly computed. For SHAP figures require corresponding feature and contribution arrays; an attractive template is not model evidence.

## Bar and dot plots

- Bars encode magnitude from a meaningful zero baseline.
- Define every error bar as SD, SEM, CI, range, or another explicit quantity.
- For small samples, show individual observations; consider dot/interval plots instead of mean-only bars.
- Sort categories only when order carries a scientific message.

## Line, curve, and time-series plots

- Draw the full valid curve. Mark actual observed/sample positions with symbols.
- Use solid/dashed/dash-dot lines plus different marker shapes for critical comparisons.
- Do not join unordered categories.
- Use confidence or variability bands only when the interval is computed from real data.
- Label important endpoints, extrema, events, or regime boundaries selectively.
- When the main question compares conditions, put the directly comparable series together before adding constituent breakdowns. Use smaller coordinated panels for composition when helpful; keep condition colours stable across panels and state differing axis ranges. Do not force this layout when the breakdown itself is the main question.
- Inspect a single-panel draft when the principal comparison is complete on its own. Place secondary breakdowns separately unless they explain a feature the reader needs in the same figure.

## Scatter and relationship plots

- Show all valid points; use alpha, rasterization, hexbin, or density contours for large n rather than subsampling.
- Add a regression/smoother and interval only when scientifically justified; report the model/statistic in the caption or notes.
- Keep equal aspect or reference lines when the comparison requires geometric equality.
- Choose marker size and opacity against actual point density at the intended export size. Keep optional marginal distributions subordinate through smaller panels and lighter fills while preserving the user's 1 pt bar outlines; all marginals must use the same declared observations. Do not use equality lines or validation statistics on unrelated-variable scatters merely to imitate an exemplar.
- If category overlap still masks the relationship, try one facet per group with matched limits, units and ticks. Check every group count and keep the full declared sample.

## Paired, interval and probability views

- Join only two values that share the same object identifier and units. Use point shape and a short connector to show pairing. State selection and ordering criteria when showing a ranked subset. If the difference is smaller than the marks at final size, consider a signed-difference view with a zero reference.
- Define what interval endpoints and the central mark represent. Distinguish modeled quantiles from confidence intervals and observation ranges. For probability curves, give the event definition, model parameters or source, and meaningful probability references. Use markers on computed curves only for defined quantities such as the intensity at 50% probability.

## Directed networks and time–frequency plots

- Draw directed edges from source identifiers and confirm that each arrow meets its correct nodes. Offset reciprocal edges enough to read both directions. State whether positions are schematic or geographic, and distinguish benchmark or simulated edge weights from observations.
- Align a time trace and spectrum by their actual time coordinates. Record sample spacing, window, overlap and transform. State the spectral quantity, normalization reference and display limits. The first and last valid window centers need not coincide with the signal boundaries.

## Distribution plots

- Choose box, violin, density, ridge, ECDF, or raw-point views according to sample size and the claim.
- Expose raw points for small or moderate n.
- State quartile, whisker, bandwidth, or normalization conventions when non-obvious.
- For box + raw-point views, let the box, median and whiskers remain clear above a restrained raw-point layer. Preserve every valid record rather than fixing clutter by sampling. A median or quantile callout must be anchored at the computed statistic; move its text into a nearby reserved gutter with a short headless leader when necessary, rather than putting it at an unrelated free height.

## Heatmaps and fields

- Use perceptually ordered sequential maps for one-direction quantities and centered diverging maps for signed quantities.
- Include a labeled colorbar with units; define normalization and clipping.
- Use real coordinates and aspect ratio for spatial/field plots.
- Never use rainbow, jet, or decorative 3D surfaces.

## Spatial point maps

- Let the map dominate when the question is spatial. Compact marginal counts rather than giving a few summary bars equal visual weight to a dense map.
- Inspect category occlusion and boundary legibility; adapt symbol sizes to density and use a clearly bounded geographic detail panel where it resolves overlap. Preserve real coordinates and all valid locations in the overview. Record the zoom bounds and included count, and derive the overview rectangle and detail limits from the same bounds. A zoom is a repeated subset, not additional independent observations.
- Identify display bins as such; do not imply station type, demand, current availability or a scientific threshold from an arbitrary capacity grouping.

## Statistics and reproducibility

Record n, observational unit, center, spread/interval, test, correction, metric definition, and source columns whenever relevant. Export source code and a clean data input or traceable data path.

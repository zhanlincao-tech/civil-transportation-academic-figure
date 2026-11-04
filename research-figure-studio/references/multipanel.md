# Multi-panel composition

Use panels only when each contributes unique evidence to one conclusion.

## Layout choice

- Equal evidence weight → regular grid with aligned axes and consistent dimensions.
- Mechanism leads, data validates → large schematic hero plus smaller quantitative panels.
- Dense field/heatmap leads → large overview plus targeted profiles or summaries.
- Images plus quantification → image plate and adjacent measurement panel with shared labels.

## Consistency

- Keep one semantic color dictionary across panels.
- Use consistent panel labels, font sizes, line weights, units, and legend strategy.
- Share axes where comparison benefits; do not force identical scales when units differ.
- Avoid repeating the same legend or conclusion in every panel.
- Preserve the same case/region ordering and a stable colour dictionary across a related figure set. Comparable scalar fields use the same definition, view and colour normalisation; independent scales must be stated. Repeated views of one dataset are complementary descriptions, not independent validation.

## Final-size test

Create the canvas at the target print width. Inspect the rendered figure at that physical size; fix unreadable text, clipped labels, excessive whitespace, and visual imbalance before export.

Do not copy a journal width or DPI from a local recipe as though it were a current submission requirement. Verify the actual target when compliance is requested. Record the intended width/height and check the exported PDF page or SVG dimensions; tight cropping can change them. If the document rescales a figure, check the resulting font sizes and border widths. Retain the user's confirmed sizes by adjusting layout rather than silently shrinking text.

For a manuscript-wide figure set, keep a lightweight manifest of figure ID, question, data slice, units, source/script, output files and verification status. Use the existing plan when available; a cosmetic edit need not restart planning or add a user confirmation step.

# Concept, mechanism, and engineering figures

## Before drawing

List the objects, their spatial or causal relationships, the view direction, and the single conclusion. Separate confirmed facts from inferred layout choices.

## Concept and mechanism diagrams

- Use 3–7 major modules unless the evidence requires more.
- Make arrow meaning consistent: material flow, causal influence, control, or feedback must not share ambiguous styling.
- Put the mechanism or conclusion at the visual center; supporting inputs and outcomes should be subordinate.
- Prefer concise labels next to objects over a detached legend.
- Use a loop or feedback arrow only when the scientific relationship is real.

## Experimental setups and engineering structures

- Use orthographic plan, elevation, section, exploded detail, or a justified combination.
- Show section lines in plan and make the corresponding section agree geometrically.
- Preserve component counts, relative positions, interfaces, dimensions, and construction states.
- Use hatching/fill to distinguish material or phase, with a small legend only when necessary.
- Do not use a perspective render as the only evidence for a critical geometric relation.

## System and method diagrams

- Group by scientific role rather than software layer unless the method itself is software architecture.
- Show inputs, transformations, outputs, and validation paths.
- Use color to encode role or state, not to decorate every box.
- Establish object IDs, component membership and a short edge list before layout. A moved node must keep the correct connector endpoint; a box placed over another is not sufficient to establish containment.
- Route dense technical connectors orthogonally or with a small number of deliberate bends; reduce crossings, attach to explicit ports and place edge labels in free space. Preserve physical arrow directions in engineering figures; data callout leaders follow the user's separate short/headless style.
- Deliver native diagram objects when the user asks for Draw.io or editable PowerPoint. An image or an entire SVG pasted into a slide is not proof that its individual labels and shapes are editable. Verify the requested application's actual output before claiming native editability.

## Output

Prefer SVG/PDF with editable text and shapes. Inspect arrow endpoints, label targets, overlaps, and view consistency after rendering.

# Circular open-caisson domain profile

Load only for caisson work.

- Default plan: circular caisson with an annular wall.
- Sinking-stage bottom: open; never add a connecting base slab.
- Diametric section: left and right cutting edges are separate, with inward-facing inclined cutting faces.
- Interior soil surface meets the upper endpoints of the cutting faces and does not extend upward to the grid beam.
- Excavated space above the soil surface contains water and no soil.
- Physical grid beam: approximately `H/5` above the cutting-edge bottom, thin relative to height, separated from soil.
- Construction plan: two longitudinal plus two transverse beams form a `#` system inside the circular clear opening, producing nine compartments clipped by the circular boundary.
- A section along one beam shows one continuous beam, not short false posts.
- Current numerical-model diagrams omit the physical beam and show only nine-zone control boundaries unless the model explicitly contains beam solids.
- Treat these as the confirmed construction-stage conventions of the original project. For a new structure, check the supplied geometry, excavation stage, and numerical-model assumptions before reusing them.

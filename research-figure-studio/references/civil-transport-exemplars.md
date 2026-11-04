# Civil and transportation figure exemplars

## Status and use

The user explicitly approved these inspected original-paper figures after rejecting generic stylistic variations. Six source PDFs were read with 18 figure pages visually inspected. These are examples for particular scientific questions, not a survey of all top journals or a claim about current journal rankings.

Inspect the cited figure and caption in the source PDF. If the named local excerpt is available under `assets/paper-references/`, use it for quick review. Publication dates refer to issue year where available. Cite the original when discussing an exemplar.

## Physical definition and mechanism: geotechnical / civil

### C1 — Geometry, interfaces and forces

- Royston, Sheil & Byrne, *Undrained bearing capacity of the cutting face for an open caisson*, Geotechnique 72(7), 632–641 (2022; online 2021), Fig. 1.
- DOI: https://doi.org/10.1680/jgeot.20.P.210
- Original PDF: https://ora.ox.ac.uk/objects/uuid%3A7319f2c9-2621-4b4f-b420-1142b381c50c/files/rpg15bf58n
- Inspect: C1 figure excerpt (local cache: C1_geometry.png), PDF page 2.
- Borrow: a local technical section with internal/external sides, geometric symbols, current/reference position, material region and force directions. Labels have physical targets.
- Adapt: derive the user's geometry and loads independently. This local footing definition is not a full circular-caisson cross-section or a complete construction stage.

### C2 — Comparative failure fields

- Same Royston et al. paper, Fig. 4, PDF page 4.
- Inspect: C2 field comparison (local cache: C2_fields.png).
- Borrow: rows encode cutting-face angles, columns encode interface conditions, with matching views. The field and geometric annotations explain the mechanism together.
- Adapt: use actual simulation variables with units and an explicitly defined colour scale. Choose a perceptual scale appropriate to the scalar; do not copy an old palette by default. Never manufacture a failure zone by shading a schematic.

### C6 — Full section plus local detail

- Templeman, Phillips & Sheil, *Cutting shoe design for open caissons in sand: influence on vertical bearing capacity*, ICE Geotechnical Engineering, Fig. 2. This is a directly relevant engineering supplement, not a claim of equal journal rank.
- DOI: https://doi.org/10.1680/jgeen.20.00218
- Accepted manuscript: https://ora.ox.ac.uk/objects/uuid%3A4349862d-8550-450a-8ff3-ed41a7836fea/files/r6h440s750
- Inspect: C6 section and detail (local cache: C6_section_detail.png), PDF page 26 / manuscript page 23.
- Borrow: a section establishing excavation level and open-bottom construction, with a geometrically corresponding local inset for cutting-face forces.
- Adapt: the paper's cutting shoe and lubricant-filled annulus are specific features, not automatic additions to the user's structure. Its problem definition sets the internal soil surface at the top of the cutting face. Apply the user's own confirmed soil, water, circular-plan and grid-beam constraints from `domain-caisson.md`.

## Numerical validation and methods

### C3 / C5 — Reference data and predictive checks

- Sheil & Templeman, *Bearing capacity of large-diameter open caissons embedded in sand*, Geotechnique 73(6), 495–505 (2023; online 2022), Figs. 4 and 15.
- DOI: https://doi.org/10.1680/jgeot.21.00089
- Accepted manuscript: https://ora.ox.ac.uk/objects/uuid%3A983d509f-c643-427b-8aa6-8ec1ffff32e2/files/s8g84mn00w
- Inspect: C3 reference comparison (local cache: C3_validation.png), PDF page 12; C5 prediction check (local cache: C5_prediction.png), PDF page 24.
- Borrow: distinguish numerical methods and literature results using line/marker semantics; for paired predictions use a meaningful equality reference and genuinely calculated error/spread, on scales appropriate to the range.
- Adapt: identify the actual benchmark. Do not imply independent validation when both axes are derived from the same result. Do not invent intervals or add logarithmic axes solely to imitate the source. Keep the user's colour and full-frame preferences.

### C4 — Actual algorithm and stopping condition

- Same Sheil & Templeman paper, Fig. 3, PDF page 11.
- Inspect: C4 remeshing flow (local cache: C4_method.png).
- Borrow: distinguish initial and repeated stages, include a real decision condition, and route feedback to the correct earlier operation.
- Adapt: use the user's actual method, variables and termination criteria. A generic sequence of 'input–method–output' boxes is inadequate when the algorithm contains specific decisions. Do not invent loops or parallelism to fill space.

## Transportation concepts, routes and result organisation

### T1 / T2 — Corresponding spaces and model validation

- Seo, Kawasaki, Kusakabe & Asakura, *Fundamental diagram estimation by using trajectories of probe vehicles*, Transportation Research Part B 122, 40–56 (2019), Figs. 2 and 7.
- DOI: https://doi.org/10.1016/j.trb.2019.02.005
- Author PDF: https://toruseo.jp/paper/seo2019probefd.pdf
- Inspect: T1 linked representations (local cache: T1_concept.png), PDF page 6; T2 observation-model comparison (local cache: T2_validation.png), PDF page 13.
- Borrow: physically meaningful trajectories and states, consistent identity across two representations, and observations shown with the corresponding model. Theory lines, samples and variability have separate meanings.
- Adapt: derive each object and interval from the user's actual model/data. The paper's gridlines are not a requirement; retain the user's no-grid preference.

### T3 / T4 / T5 — Input versus solution and coordinated panels

- Liu, *Routing battery-constrained delivery drones in a depot network: A business model and its optimization–simulation assessment*, Transportation Research Part C 152, 104147 (2023), Figs. 1, 7 and 8.
- DOI: https://doi.org/10.1016/j.trc.2023.104147
- Author PDF: https://yliu.eng.wayne.edu/research/trc_S0968090X23001365-main.pdf
- Inspect: T3 input and route solution (local cache: T3_routes.png), PDF page 5; T4 state comparison (local cache: T4_timeseries.png), PDF page 18; T5 grouped distributions (local cache: T5_boxplots.png), PDF page 19.
- Borrow: stable positions and arrow semantics across input/solution, panels aligned by scenario and state variable, and comparable groups across different measured outcomes.
- Adapt: use real depots, demands, paths and constraints. Use step plots when quantities are discrete states, not for arbitrary continuous signals. Distribution panels need defined groups and observational units; preserve raw points where useful as the user previously selected.

### T6 — Geography, demand and facilities

- Chauhan, Unnikrishnan & Figliozzi, *Maximum coverage capacitated facility location problem with range constrained drones*, Transportation Research Part C 99, 1–18 (2019), Fig. 2.
- DOI: https://doi.org/10.1016/j.trc.2018.12.001
- Author PDF: https://web.cecs.pdx.edu/~maf/Journals/2019_Maximum_Coverage_Facility_Location_Problem_with_Drones.pdf
- Inspect: T6 geographic context (local cache: T6_map.png), PDF page 8.
- Borrow: subdued real geographic context, clearly different demand/facility symbols and a concise legend. Reuse consistent map extent when comparing solutions.
- Adapt: respect real coordinates and location uncertainty. If no coordinates exist, label a topology as schematic rather than suggesting a real map.

## Directed networks, probability curves and time–frequency plots

- Salari et al., *Modeling the effect of sensor failure on the location of counting sensors for origin-destination (OD) estimation*, Transportation Research Part C 132 (2021), Fig. 8, PDF page 17. Inspect the [author repository PDF](https://ira.lib.polyu.edu.hk/bitstream/10397/95090/1/1-s2.0-S0968090X21003697-main.pdf#page=17). Borrow stable node IDs and distinct reciprocal arrows. Use real geometry only when the source supplies it.
- Crespi et al., *Fragility curves for the seismic vulnerability of a stock of Italian highway bridges*, Structures 78 (2025), Fig. 4, Table 1 and Eq. (2). Inspect the [published paper](https://re.public.polimi.it/handle/11311/1292605). Borrow stable encoding of mode and direction. If overlays crowd, use same-scale facets. Model quantiles computed from published parameters are probability landmarks.
- Kramer et al., *The Timing of Liquefaction and Its Utility in Liquefaction Hazard Evaluation*, 6ICEGE (2015), Fig. 4, PDF page 8. Inspect the [ISSMGE original](https://www.issmge.org/uploads/publications/59/60/379.00_Kramer.pdf#page=8). Borrow the aligned time axis for waveform and time–frequency view. State the actual transform, window and color normalization.

## Reusable design decisions

1. State the scientific question and comparison: geometry, mechanism, model/reference, scenario, stage, distribution or spatial plan.
2. Select the closest exemplar above and inspect the actual excerpt, not only this prose.
3. Write a short adaptation note: source paper and figure; borrowed relationship/organisation; differences in the user's geometry, evidence and construction state.
4. Apply confirmed user preferences where they fit. Do not force rings, marginal histograms, radar profiles, derivatives or correlations simply because they are available.
5. Organise paired panels by real comparative dimensions. For fields, match the view, physical region and appropriate colour limits; for quantitative references, define the benchmark and error meaning.
6. Inspect the rendered output for both scientific consistency and publication-scale readability. A structurally valid Skill or successfully parsed SVG is not proof of a good figure.

For figure families not covered here, obtain and inspect a suitable primary-source example. If access prevents visual inspection, describe that limitation and do not claim the source figure was studied.

# Research and technical presentations

For research and technical talks, start with a restrained visual direction unless the brief specifies otherwise. Use precise typography, generous figure space, disciplined annotation, and quiet backgrounds. A bright product-launch aesthetic is optional, not the default.

## Map the paper to an argument

Read the actual paper and relevant figures, not just its abstract. Distinguish the paper's claims from your explanation. Extract problem, assumptions, prior work, contribution, method, experimental setup, results, ablations, limitations, and open questions. Choose emphasis according to audience and time; a journal club and a conference talk have different purposes.

Provide a paper-to-slide mapping with section/page/figure/table IDs. Preserve original symbol definitions. When a source is incomplete, do not manufacture missing experiment settings, confidence intervals, computational costs, or baselines.

## Five useful evidence layouts

1. **Method overview:** clear pipeline or architecture occupying most of the slide; each labeled stage has an explicit input and output. Add a short explanation of the unusual step.
2. **Mechanism detail:** isolate the focal operation; show input → transformation → output; keep surrounding context as a small locator diagram only if helpful.
3. **Main experiment:** a readable plot or table with comparison conditions, metric direction, sample size/uncertainty when known, and the supported finding.
4. **Ablation or sensitivity:** matched panels or a controlled comparison identifying exactly what changed. Avoid a different scale for each panel unless necessary and clearly indicated.
5. **Limits and failure case:** show the actual failing example, boundary condition, or unresolved tradeoff. Do not replace it with a generic "future work" list.

## Figure integrity

Before laying out dense evidence, inventory the rows, conditions, labels, units, uncertainty and caveats that must remain visible. Prototype that full payload. First reclaim space from redundant titles, decoration and repeated legends. Then choose a readable native table, matched panels or an enlarged source panel according to the comparison. Split across existing slides only if the requested count and argument permit it. Notes and appendices cannot hide evidence the user requires on-slide. If the full payload still cannot be read, surface the specific count/readability conflict instead of silently dropping rows or shrinking essential labels.

Adapt a paper figure for a slide only when its meaning is preserved. Enlarging one relevant panel or separating panels can improve legibility; preserve axis labels, scale bars, legend, units, error information, and caveats needed to interpret it. Label adaptations and cite the original. If source data exists, redraw accurately and keep the data with the build. Without data, do not reconstruct quantitative points by guesswork. Any digitization must be explicit and include its uncertainty.

Before editing a figure, identify whether it is evidence, a schematic, or decoration. Do not erase an outlier, uncertainty band, comparator, or failure case to make the slide more persuasive. If a scientific plot must be rasterized for compatibility, use sufficient resolution, retain its reproducible plotting source, and report editability accurately.

## Equations and technical diagrams

Use an equation as a focal explanatory object, not a screenshot of a paragraph. Define symbols used on that slide, keep units consistent, and connect the equation to an intuitive or numerical example when useful. Prefer editable math if supported. If a vector/raster equation is necessary, retain the source formula and check all glyphs.

Define terms only at the level the source supports; mark conventional interpretations as assumptions when the formulation is unspecified. A weighted loss coefficient does not alone establish that term's percentage contribution, since the term magnitudes also matter.

Keep diagrams native and editable when required. Label edges with meaningful quantities/actions rather than relying on arrow direction alone. Use consistent colors for components across the whole deck. Schematics may simplify physical geometry but must not imply untrue scale, topology, or causality.

Specify what nodes represent (states, objects or operations) and what edges carry before choosing geometry. Distinguish a model state from the transformation that produces it. Preserve parallel branches, joins, auxiliary inputs and feedback loops; do not flatten a branched system into a linear sequence for stylistic convenience. Unspecified internals remain unspecified. For a failure result without a source image, show the supplied contrast and changed condition, labeling whether the values are measured or illustrative, rather than inventing a failure photograph or spectrogram.

For a substantial research visual, use [research-visuals.md](research-visuals.md). When the user requests execution of [paper-figure](https://github.com/JYS1025/paper-figure), read its current host entrypoint and follow the applicable creation, revision or review route. Adapting its principles and running the companion are distinct. It specializes in editable methodology and architecture figures; it does not replace deck planning or statistical plotting. It remains an optional companion.

For an existing diagram, write the required stage identities and directed relationships from the brief, map them to the latest saved objects, and check both attachments and the rendered arrow direction. Distinguish file diagnostics from visual or PowerPoint edit tests. Do not claim that an existing diagram was created through another skill's image-draft workflow merely because its review scripts were used later.

## Motion for technical comprehension

Good uses: reveal a pipeline stage, explain a state update, focus on one architecture component, expose an experimental control before its result. Keep the comparison frame and legend stable. Avoid hiding a baseline while emphasizing an improvement. A static or reduced-motion version must preserve the final explanatory state.

For loops, recurrence, or algorithms, plan a small number of named states. A transition between duplicate slides consumes slide count; do not add hidden duplicates to evade the count the user requested. Prefer within-slide reveals when the count is fixed and the native backend supports them.

## Source guidance

MIT's [AeroAstro slide design guide](https://mitcommlab.mit.edu/aeroastro/commkit/slide-design/) is useful for audience-specific technical depth and visual hierarchy. Its [paper-to-slide figure article](https://mitcommlab.mit.edu/cee/2024/01/15/redesigning-existing-figures-for-slides/) discusses figure adaptation. Its [NSE guide](https://mitcommlab.mit.edu/nse/commkit/slide-design/) describes controlling information delivery. These support selected principles; they do not mandate this skill's complete workflow or palettes.

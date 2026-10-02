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

Adapt a paper figure for a slide only when its meaning is preserved. Enlarging one relevant panel or separating panels can improve legibility; preserve axis labels, scale bars, legend, units, error information, and caveats needed to interpret it. Label adaptations and cite the original. If source data exists, redraw accurately and keep the data with the build. Without data, do not reconstruct quantitative points by guesswork. Any digitization must be explicit and include its uncertainty.

Before editing a figure, identify whether it is evidence, a schematic, or decoration. Do not erase an outlier, uncertainty band, comparator, or failure case to make the slide more persuasive. If a scientific plot must be rasterized for compatibility, use sufficient resolution, retain its reproducible plotting source, and report editability accurately.

## Equations and technical diagrams

Use an equation as a focal explanatory object, not a screenshot of a paragraph. Define symbols used on that slide, keep units consistent, and connect the equation to an intuitive or numerical example when useful. Prefer editable math if supported. If a vector/raster equation is necessary, retain the source formula and check all glyphs.

Keep diagrams native and editable when required. Label edges with meaningful quantities/actions rather than relying on arrow direction alone. Use consistent colors for components across the whole deck. Schematics may simplify physical geometry but must not imply untrue scale, topology, or causality.

## Motion for technical comprehension

Good uses: reveal a pipeline stage, explain a state update, focus on one architecture component, expose an experimental control before its result. Keep the comparison frame and legend stable. Avoid hiding a baseline while emphasizing an improvement. A static or reduced-motion version must preserve the final explanatory state.

For loops, recurrence, or algorithms, plan a small number of named states. A transition between duplicate slides consumes slide count; do not add hidden duplicates to evade the count the user requested. Prefer within-slide reveals when the count is fixed and the native backend supports them.

## Source guidance

MIT's [AeroAstro slide design guide](https://mitcommlab.mit.edu/aeroastro/commkit/slide-design/) is useful for audience-specific technical depth and visual hierarchy. Its [paper-to-slide figure article](https://mitcommlab.mit.edu/cee/2024/01/15/redesigning-existing-figures-for-slides/) discusses figure adaptation. Its [NSE guide](https://mitcommlab.mit.edu/nse/commkit/slide-design/) describes controlling information delivery. These support selected principles; they do not mandate this skill's complete workflow or palettes.

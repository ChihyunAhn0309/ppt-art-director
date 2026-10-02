# Production and backend selection

## Hosts with a presentation toolchain

If a Presentations skill is installed, read its implementation, current API quick start, and finalization references. In Codex desktop, use `load_workspace_dependencies` when available to discover runtime paths. Use `@oai/artifact-tool` only where provided and required by the installed skill; it is not bundled here. Follow the host's authoring, font, integrity, and finalization requirements.

Do not copy a PptxGenJS example into Artifact Tool: units, color syntax, object types, notes, charts, and export methods differ. Inspect the API documentation before using a feature. A generic style contract may be shared across backends; raw option objects may not.

## Other environments

Select a documented, available backend capable of the requested output. [PptxGenJS](https://gitbrent.github.io/PptxGenJS/) is a possible native PPTX backend (see its [installation](https://gitbrent.github.io/PptxGenJS/docs/installation/) and [quick start](https://gitbrent.github.io/PptxGenJS/docs/quick-start/)); a live Slides connector is appropriate for an explicitly requested Google Slides document. HTML is suitable only when it is the chosen deliverable or a clearly labeled preview. Do not silently return HTML in place of PowerPoint.

If an engine cannot create or preserve a required feature, do not assume import/export will carry it through. Test a small specimen before building the full deck. External model APIs are optional, never a prerequisite to use this skill; do not seek keys when available tools already solve the task.

## Build organization

Keep the work reproducible:

```text
work/<deck>/
  brief.json              # actual brief and explicit assumptions
  content.json            # stable Sxx IDs, copy, values, source pointers
  theme.json              # semantic palette, type, grid and component choices
  build.mjs               # shared helpers plus deck assembly
  assets/                 # original user/sourced/generated assets
  motion-plan.json        # only when motion applies
  renders/                # private QA renders
  qa/                     # package reports and defect log
outputs/
  slide-plan-v01.md
  <deck>-v01.pptx
  <deck>-preview.png       # useful optional contact sheet
```

Adapt to the task's established output paths. Keep generated files out of an existing source/template directory. Do not overwrite user originals unless requested.

Create the design tokens before the slide loop. Give motion targets unique meaningful names such as `S04-method-stage-2`; resolve actual exported object IDs/names with the audit helper. Do not infer IDs from authoring order.

## Template fidelity

For a discovered template, follow [template-search.md](template-search.md) to acquire a usable original and distinguish actual template editing from reference-led original composition. Determine whether an uploaded or downloaded deck is a design reference, a factual source, or both. Inspect master dimensions, recurring typography, layouts, spacing, image treatment, and reusable objects. Preserve those deliberately. Do not use the first template layout for every slide. Remove unused placeholder groups, not just their text.

For edits, inventory notes, hyperlinks, media, charts, embedded workbooks, and existing timing before transformation. Compare source and output. Do not globally rebuild a sophisticated template if the selected engine drops critical features. Use supported native editing or a feature-preserving file transformation instead.

## Motion pass ordering

1. Finish and validate the static deck using the supported authoring engine.
2. Inspect the final object's names/IDs and bind the motion plan to those exact objects.
3. Add native motion to a new file with a supported backend.
4. Run package/geometry checks on that actual motion file. Avoid an importer/exporter round-trip known to strip timing.
5. Verify expected timing targets and effect counts, then inspect playback if the player is accessible.

The static source stays available as a reduced-motion edition. Rebuild motion after any content change affecting object identity. A previous animation pass is not proof that the newly regenerated deck still has correct targets.

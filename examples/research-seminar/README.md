# Research seminar: English and Korean editions

| Edition | Animated | Static | Plan | Preview |
|---|---|---|---|---|
| English | [PPTX](animated.pptx) | [PPTX](static.pptx) | [Plan](slide-plan.md) | [Preview](preview.png) |
| Korean | [PPTX](animated-ko.pptx) | [PPTX](static-ko.pptx) | [Plan](slide-plan-ko.md) | [Preview](preview-ko.png) |

A five-slide, five-minute research talk about sensor-model compression. The original Korean example came from an independent one-shot test. These revised editions incorporate subsequent user feedback on typography, a less rigid visual style and English support. **All performance data are fictional**, not experimental findings or a model-quality benchmark.

English uses Segoe UI; Korean uses Noto Sans KR. Fonts were available on the rendering machine but are not embedded. If the recipient substitutes fonts, rerender and check line fitting. Previews are saved-file Microsoft PowerPoint renders at 1600 × 900, combined into a contact sheet; they show the complete slide, not animation playback.

## Design changes

- Warm ivory and teal, more breathing space and lighter headings.
- A topic-first typographic cover with meaningful numeric comparisons; no decorative artwork.
- Native model states joined by named transformations, a neutral table, and a native latency–F1 scatter plot with embedded data.
- Equal-size latency and F1 differences; no unexplained winner highlight. The scatter axes are explicitly bounded at 40–140 ms and .890–.915 F1 to reveal the differences, with no interpolation or uncertainty invented.
- A shorter closing takeaway on one line in both languages, without removing the visible fictional-data caveat.
- Separate localization of slide text, chart labels and speaker notes.

![Editable process slide rendered in PowerPoint](process-slide.png)

## Evidence contract

| Model | Latency (ms) | F1 | Size (MB) |
|---|---:|---:|---:|
| baseline | 120 | 0.910 | 48 |
| distilled | 72 | 0.902 | 18 |
| int8 | 54 | 0.896 | 12 |

Same device and data are assumed. Sample count, variance, dataset, architecture, training configuration and quantization scope were not supplied. The 55% latency reduction, 75% size reduction and 0.014 absolute F1 drop are arithmetic on these fictional inputs. No statistical significance or generalization claim is justified.

## paper-figure workflow

The user-selected [paper-figure skill](https://github.com/JYS1025/paper-figure/blob/363fb3b76003d919f797356d774e70161164a7a8/skills/paper-figure/SKILL.md) was used at revision `363fb3b76003d919f797356d774e70161164a7a8`. The prior bilingual redesign followed its full-composition image draft → reviewed transfer plan → editable reconstruction route for S02. The current local revision preserves that composition while clarifying model states and transformation labels; it did not generate a new draft.

[Selected generated draft](design/workflow-draft.png) · [Exact generation prompts](design/image-prompts.json) · [Pre-authoring transfer plan](design/transfer-plan.md)

The draft informed open columns, small stage markers, spacing and palette. Its unsupported “same knowledge” claim, slogan, architecture-like cubes and decorative extras were removed. The final process uses native labels, circles and connectors; the raster draft is not embedded. The unrelated cover artwork was removed. The historical diagram draft records the earlier authoring route; no generated image is embedded in the current PPTX. The reusable [research-visual guide](../../references/research-visuals.md) also supports a direct native route without requiring image generation.

The saved render was compared with the draft for hierarchy and space: the final retains the useful open process, reduces duplicate flow cues and keeps only contract-supported content. This is a presentation-scale comparison, not a paper-print-size or controlled authoring-method benchmark.

| Check | Evidence and limits |
|---|---|
| Required labels and directed relationships | [English contract](diagram-contract.json), [English inspection](diagram-inspect.json), [Korean contract](diagram-contract-ko.json), [Korean inspection](diagram-inspect-ko.json) |
| Connector attachment | [English audit](flow-audit.json), [Korean audit](flow-audit-ko.json); circular endpoints are outside this helper's automated rectangle geometry checks, so both connectors require rendered review |
| Visual review | Left-to-right direction, attachment to the circular markers, label association and readability inspected in the saved PowerPoint renders |
| Line fitting | [English](typography-check.json), [Korean](typography-check-ko.json): 55 text boxes per edition; intended and actual line counts match, including the two-line cover title and one-line closing takeaway |
| Data and native objects | [Data check](data-check.json): exact table values, paired chart coordinates (1e-12 F1 cache tolerance for Office float serialization), embedded workbook, arithmetic and animation targets for all four PPTX files |
| App editability | [PowerPoint check](powerpoint-check.json): text, table value, chart X/Y values and diagram label changed on separate copies, saved and reopened in both languages |
| Motion | [Plan](motion-plan.json): 12 Fade effects in two click groups; target, sequence, trigger and duration verified after saving. `playbackVerified` remains `false` |

The line checker covers named text boxes; it does not measure every native chart/table label. Those were checked in the rendered slides. Automated inspections do not assess aesthetics or scientific truth.

Public files remove only the Office last-modifier field in `docProps/core.xml`. Other ZIP parts are byte-identical to the final local deck used for rendering and app checks. [Data provenance](data-check.json) records original/public hashes and the exact changed part. Read-only public-file inspections were then rerun. [Checksums](checksums.json) identify the published files.

## Reproduce the structural checks

From this repository's root:

```shell
python scripts/verify_checksums.py examples/research-seminar/checksums.json
python scripts/pptx_audit.py examples/research-seminar/animated.pptx --expect-slides 5
python scripts/pptx_audit.py examples/research-seminar/static.pptx --expect-slides 5
python scripts/pptx_audit.py examples/research-seminar/animated-ko.pptx --expect-slides 5
python scripts/pptx_audit.py examples/research-seminar/static-ko.pptx --expect-slides 5
```

To repeat the companion checks, separately obtain the pinned paper-figure revision and its `lxml` dependency. Replace `PATH_TO_PAPER_FIGURE` and use new report paths. Its tools are not bundled or required for ordinary skill use. UTF-8 mode avoids platform-specific decoding of Korean contracts.

```shell
python -X utf8 PATH_TO_PAPER_FIGURE/skills/paper-figure/scripts/pptx.py inspect examples/research-seminar/animated.pptx --contract examples/research-seminar/diagram-contract.json --output new-inspect.json
python -X utf8 PATH_TO_PAPER_FIGURE/skills/paper-figure/scripts/flow_audit.py examples/research-seminar/animated.pptx --output new-flow-audit.json
```

See [VALIDATION.md](../../VALIDATION.md) for independent testing and remaining boundaries. Static geometry checks, saved-effect verification and observed slideshow playback are different levels of evidence.

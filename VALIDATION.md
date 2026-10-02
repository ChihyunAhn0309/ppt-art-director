# Validation record

Date: 2026-10-02 (Asia/Seoul). Independent agent sessions used separate work directories on the same machine. They were given the skill and test brief without the author's prior conclusions. This is not external certification or a controlled benchmark across model providers.

## Initial independent tests

| Test | Observed result |
|---|---|
| Default planning | A complete Korean five-slide, six-minute plan with actual copy, evidence, visuals, notes and timing; stopped for feedback |
| Feedback propagation | Changed A's latency from 78 to 76 ms, corrected the title and propagated the 24% reduction while preserving five slides and 360 seconds |
| Final feedback-test artifact | Native table, two native charts and two workbooks; five slides rendered and content inspected |
| One-shot | Produced a five-slide static PPTX and separate native-animated edition from fictional sensor-model data |
| App editing | On copies, changed text, a table value, chart data and a process label, saved and reopened |
| Motion | Original example's ten Fade effects and two click groups verified after saving; actual slideshow playback unverified |
| Helper code | Initially 22 tests; a Windows Unicode-console regression brought the suite to 23 |
| Package | Frontmatter, internal links and private-path checks within the tested scope |

The original feedback-test build returned exit code 1 after completion logs. It was not described as a successful process exit. Explicit finalizer success, final-file import, five renders and separate package/content checks established the artifact's state. The exit-code cause remains unconfirmed. This does not prove every authoring environment runs without errors.

## Independent defects reproduced and fixed

| Defect | Fix |
|---|---|
| Audit report could overwrite its input PPTX | Reject normalized identical paths and same-file aliases, including hardlinks |
| PowerShell relative output after `Set-Location` | Resolve against the current PowerShell location |
| Valid comments in relationship XML broke animation preflight | Select namespace-correct Element relationships |
| Empty palettes or color-pair lists passed | Validate nonempty structure and finite thresholds |
| UTF-16 bypassed text-based DTD/entity rejection | Reject DOCTYPE at the XML parser event level |
| Root-level custom-part relationships rejected | Support `_rels/custom.xml.rels` |
| Missing chart target still counted as native chart | Verify relationship ID, type, target and `chartSpace` |

The independent reviewer reproduced the fixes with regression inputs. See [regressions](tests/test_regressions.py) and [basic tests](tests/test_helpers.py). Earlier code review used Python 3.11.7; the final package check used Python 3.12.14. PowerShell preflight was exercised under Windows PowerShell 5.1 and PowerShell 7.6 without starting COM.

## Bilingual redesign

The user requested cleaner wrapping, a less rigid visual style, English support, English GitHub documentation and appropriate free design tools. The public example now has separate English and Korean static/animated editions. The revised skill adds deliberate line fitting, per-language render review, a concrete reference ledger and a task-specific free-tool guide.

- The author rendered all five final slides in each language using Microsoft PowerPoint and inspected their layout and the montage. Native line/bounds checks cover 53 named text boxes per edition; all intended line counts match, including the single-line closing takeaway.
- Native table data, chart data, embedded workbook values, arithmetic and expected motion targets were checked in all four public PPTX files. Public-file hashes and the metadata-only sanitization boundary are recorded with the [example](examples/research-seminar/README.md).
- Both language editions passed copy-edit/save/reopen checks for text, table, chart and diagram objects. S02 contains 12 Fade effects in two click groups. Saved effect targets, ordering, triggers and timing were verified; slideshow playback remains unverified.
- The user-selected paper-figure process was applied to the redesigned method slide: full generated composition draft, review and transfer decisions before authoring, native reconstruction, saved-render comparison and read-only inspections. Circle endpoints require manual geometry review in that helper; the reports retain that limitation.
- A fresh independent English plan-first session produced five detailed slides and 300 seconds from a Korean source fixture, preserving all fictional-data caveats. It inspected external Pitch and MIT slide pixels and recorded their application. It found an overlong metadata description; the description was shortened to meet the documented limit. It found no conflicting language, typography, plan-first, one-shot or free-tool instructions.
- A separate visual reviewer inspected all ten full-size redesigned slides, both montages, the generated process draft and the prior closing slide. It found no blocking clipping, wrapping, language or design issue. Its independent ZIP checks confirmed all 53 planned text boxes per language, table/chart/workbook values, directed connections and metadata-only sanitization for all four PPTXs. The reviewer noted a 0.15 pt text-bound excess on the large 55% label with no clipped pixels; the native bound check uses a documented 1 pt tolerance, not a claim that every glyph bound is strictly inside its frame.

The revised package passed all 23 helper tests and the skill frontmatter validator. The independent reviewer reran the previously failing package-link check after the Korean artifacts were staged; it passed. All four final example package audits reported no errors or warnings.

During redesign, one redundant Node rebuild exhausted local memory. The existing candidate was preserved; the border correction was finalized separately and the resulting files were reopened, rendered and inspected. A table-border correction after finalization was checked in the final PowerPoint renders and public package audits. These checks establish the delivered files, not a guarantee that every host has sufficient resources.

## CI history and reproduction

```shell
python -m unittest discover -s tests -v
python scripts/palette_check.py assets/palettes.json
```

Run the [behavioral scenarios](tests/scenarios.md) in fresh sessions to test planning, feedback and one-shot behavior. The CI workflow checks helpers, all four example packages and PowerShell syntax on Windows and Ubuntu. It does not install Office, render slides or assess aesthetics.

Two historical example-publication runs failed because Windows could not print Korean JSON to its console encoding. The fix prints lossless ASCII JSON escapes to the console while retaining readable UTF-8 in `--output` files; a regression checks round-trip preservation of Korean text, paths and palette names. [The subsequent repair run](https://github.com/ChihyunAhn0309/ppt-art-director/actions/runs/36976031639) passed on both operating systems. Historical red runs remain in Actions; check the newest commit's run for current status.

## Unverified boundaries

- Actual click-by-click slideshow playback was unavailable through the native UI tooling. Saved-file effect checks are not playback observation.
- Identical appearance or motion across PowerPoint versions, macOS, LibreOffice and Google Slides import is not guaranteed. The example's fonts are not embedded.
- The package checker is not a complete OOXML, accessibility, scientific-correctness or aesthetic validator.
- The free-tool guide documents options and boundaries; not every listed tool was executed in this example. Host image generation and licensed PowerPoint were used for this particular example, and are not presented as free services.
- No universal quality guarantee or Claude/Gemini superiority claim is made. Results depend on sources, model, tools and review.

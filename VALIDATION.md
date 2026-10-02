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

## Independent content-first review and published-repository audit

A new independent session audited the actual published commit `1d4c6f3b1811f1b3141d26ac6e3c014892cd6f59`, using a clean Git checkout, raw GitHub files and public Actions metadata. It reproduced all 23 then-existing tests, four package audits and the successful Windows/Ubuntu run. Independent XML/workbook extraction confirmed the example data and saved motion targets.

The audit found a real publication defect: **14 of 27 example checksum entries hashed CRLF text, while GitHub contained LF text**. All four PPTX and image hashes were correct. Prior local checks and CI did not cover this boundary. The release now canonicalizes UTF-8/LF before hashing, packaging and API publication. A new exact-byte checksum helper and CI step verify complete example-directory coverage. Eleven regression tests cover line-ending changes, tampering, coverage, malformed paths/manifests and platform link behavior. The local suite completed 34 tests: 32 passed, with two symlink tests skipped because this Windows host lacks symlink-creation privileges. Its Windows junction test passed. An independent code reviewer reran the suite; internal junction cycles fail closed with an I/O error rather than a false integrity pass, but are not detected at the earliest possible point.

A separate independent design review inspected all ten prior full-size slides and the skill's guidance. It found that the abstract ribbon conveyed no subject information, an unexplained INT8 highlight could imply a winner, and latency received stronger emphasis than the competing F1 cost. The user independently clarified the same content-first preference. The revised example removes the decorative cover, names the real topic, distinguishes model states from transformations, uses neutral table rows and shows paired latency/F1 coordinates in a native scatter plot. Latency and F1 differences now have equal-size callouts.

The same reviewer then inspected **all ten revised full-size slides**. It found no blocking clipping, wrapping, language or misleading scientific implication issue, and independently checked both chart axes and arithmetic. A small spacing refinement was noted as nonblocking. The author rendered both static and animated editions in PowerPoint, checked 55 named text boxes per language, and performed copy-edit/save/reopen probes for text, table, chart X/Y values and a process label. Required labels, chart caches/workbooks, arithmetic and saved motion targets were checked again in all four public files. This is scoped review, not an aesthetic guarantee.

An independent forward test exercised a different, denser brief at **plan level**: six slides, seven minutes, separate English/Korean copy, eight model rows with 24 values, a seven-node/seven-edge parallel method, an equation and a changed-condition failure. It preserved all specified rows, values, edges and qualifications, totaled 420 seconds and derived the F1 difference correctly. Actual external technical slide pixels were inspected. No PPTX was requested or generated in that test, so its proposed table fit, line counts, editability and playback remain unverified.

That test identified premature styling before content-density allocation as the main instruction gap. The updated skill puts evidence feasibility first, requires a compact completeness map where useful, selects references by the difficult communication problem and treats planned fit as provisional. A follow-up independent review found no blocking instruction conflict. Dense-evidence choices, visual emphasis, bilingual meaning/optics and equation assumptions were also clarified.

The requested paper-figure transfer was separately checked against upstream revision `fe628d9c05fb7a3cbcb906180c602effc72ce9fb`. The new [research-visual guide](references/research-visuals.md) adapts relationship planning, information-specific representations and saved-slide checks in original prose. It distinguishes this direct native route from actually executing a host-specific companion workflow; no paid image generation or copied upstream code is required. The historical diagram draft remains a truthful record of the earlier example workflow, not a claim that it was rerun for this revision.

During authoring, the finalizer caught default-font chart labels; explicit fonts fixed them. A subsequent receipt-path collision was resolved with fresh output/receipt paths and successful finalization. PowerPoint briefly remained running after automation shutdown; the next operation waited for it to exit rather than attaching to or terminating a session. These intermediate failures were not reported as successful validation.

## CI history and reproduction

```shell
python -m unittest discover -s tests -v
python scripts/palette_check.py assets/palettes.json
python scripts/verify_checksums.py examples/research-seminar/checksums.json
```

Run the [behavioral scenarios](tests/scenarios.md) in fresh sessions to test planning, feedback and one-shot behavior. The CI workflow checks helpers, exact-byte example checksums, all four example packages and PowerShell syntax on Windows and Ubuntu. It does not install Office, render slides or assess aesthetics.

Two historical example-publication runs failed because Windows could not print Korean JSON to its console encoding. The fix prints lossless ASCII JSON escapes to the console while retaining readable UTF-8 in `--output` files; a regression checks round-trip preservation of Korean text, paths and palette names. [The subsequent repair run](https://github.com/ChihyunAhn0309/ppt-art-director/actions/runs/36976031639) passed on both operating systems. Historical red runs remain in Actions; check the newest commit's run for current status.

## Unverified boundaries

- Actual click-by-click slideshow playback was unavailable through the native UI tooling. Saved-file effect checks are not playback observation.
- Identical appearance or motion across PowerPoint versions, macOS, LibreOffice and Google Slides import is not guaranteed. The example's fonts are not embedded.
- The package checker is not a complete OOXML, accessibility, scientific-correctness or aesthetic validator.
- The free-tool guide documents options and boundaries; not every listed tool was executed in this example. Host image generation and licensed PowerPoint were used for this particular example, and are not presented as free services.
- No universal quality guarantee or Claude/Gemini superiority claim is made. Results depend on sources, model, tools and review.

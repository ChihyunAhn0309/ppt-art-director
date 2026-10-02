# Behavioral evaluation scenarios

Run these in fresh agent sessions with the skill and the raw brief only. Do not provide previous conclusions or example output decks. Keep generated artifacts outside the skill repository. These checks complement helper unit tests; passing them is not a guarantee of aesthetic quality on every topic.

## Live template selection for a new topic

Request a plan only for a six-slide battery-health estimation talk, in separate English and Korean editions, with private constraints of eight minutes and an internal research meeting. Supply a fictional method: voltage/current/temperature measurements to windowed features, then a regression model and a state-of-health estimate. Supply fictional MAE values of 2.4 percentage points for a baseline and 1.7 for the proposed model under the same evaluation conditions; no sample size or uncertainty is available. Ask for refined, natural design from suitable free online templates, without decorative imagery, purchases or a hosted database.

Inspect whether the agent performs a fresh search, compares distinct plausible candidates and views relevant body-slide pixels. The plan should identify the selected source, current access/terms, inspected pages, specific layout-to-slide mappings and the actual production route. If adopting a downloaded template, check the original's native objects and preserve it separately; a flattened slide image does not establish editability. If suitable editable sources cannot be acquired, a truthful native-composition fallback is acceptable. For this internal-presentation brief, distinguish template-redistribution restrictions from permitted presentation use; consider removing decorative placeholders when allowed before rejecting a useful source. Exact bilingual copy must preserve the hypothetical-data label and the 0.7-percentage-point MAE difference, while private meeting metadata stays in the brief. Stop at the plan checkpoint without another template-picker gate. Do not call this a rendered-deck or animation test.

## 1. Planning checkpoint

Request a five-slide, six-minute Korean graduate-lab talk with restrained design. Supply explicitly hypothetical data: baseline latency 100 ms / accuracy 92.4%; A 78 ms / 92.1%; B 60 ms / 91.8%. State that board, input, and power mode are the same, and that repetitions and uncertainty are not available. Ask for the latency–accuracy tradeoff without a general superiority claim. Do not request one-shot production.

Inspect whether the agent produces a concrete five-slide plan and waits for feedback. Check exact copy, evidence, layout, notes, palette roles, slide count, hypothetical-data labels, missing-data handling, and reference inspection. It must not invent the methods' internal mechanisms or report an uncreated PPTX as verified.

## 2. Feedback continuation

Continue that session: correct A's latency to 76 ms, shorten S03's title to “지연 감소와 정확도 손실”, retain five slides and six minutes, and ask for the final editable deck. Keep the agreed static treatment.

Check the revised plan and actual PPTX. The correction must propagate to tables, charts, notes, labels, and conclusions. A's latency reduction is now 24%, while its accuracy difference remains 0.3 percentage points. Inspect native objects and all final slide renders. The agent should act on the implementation request without adding a redundant approval round.

## 3. One-shot production with motion

Request an editable five-slide Korean lab talk, completed without intermediate approval. Supply explicitly hypothetical sensor-model data: baseline latency 120 ms / F1 0.910 / model 48 MB; distilled 72 ms / 0.902 / 18 MB; INT8 54 ms / 0.896 / 12 MB. Do not provide sample size, variance, or a dataset name. Ask for restrained teal design and a baseline → distillation → INT8 process explanation with native PowerPoint animation where useful.

Inspect the plan, actual PPTX, every final render, numerical consistency, editability, and native timing. Distinguish verified file settings from visual slideshow playback. If a required backend is unavailable, the agent must state that limitation accurately and preserve a useful static deliverable.

## 4. Helper regression checks

Run the Python test suite and PowerShell preflight tests. Preserve input bytes when a report path aliases its source; reject empty contrast checks and non-finite thresholds; reject DTDs independently of XML encoding; handle valid relationship paths and comments; identify broken chart relationships; resolve output paths from the PowerShell working location. Preflight tests must not start PowerPoint.
# Bilingual typography and free-tool follow-up

Run these additions in fresh sessions after the original workflow scenarios.

## English output from Korean source

Supply Korean-language notes with explicitly fictional metrics: baseline 120 ms / F1 0.910 / 48 MB; distilled 72 / 0.902 / 18; int8 54 / 0.896 / 12. Request a five-slide, five-minute **English** research talk, plan-first. Expect exact English copy, labels, caveats and notes; correct 55% latency and 75% size reductions; an absolute F1 drop of 0.014; 300 seconds; deliberate title/takeaway line counts; and a stop for feedback. Source language must not override requested output language.

## Localized one-shot and clean wrapping

Request separate English and Korean editions in one shot. Expect both files, independent font/layout decisions, the same source data and caveats, and final renders from each edition. A concise closing takeaway must not inherit awkward source-language line breaks. Do not accept a passing overflow check as proof of good typography. Check actual title and focal line counts, table/chart labels and notes.

## External reference and free-tool selection

Request a restrained process slide and a scientific results slide without buying templates or using a paid image API. Expect actual visual-reference inspection, a record of the specific composition decisions transferred, and an available free-tool route. Native PPTX objects are appropriate for a simple process and common chart; a specialized scientific plot may justify Matplotlib. If a tool is unavailable, require a truthful fallback, not a fabricated execution claim. Do not require every listed tool or a decorative image.

## Dense content-first research plan

Request a plan only: exactly six slides, seven minutes, separate English and Korean editions for ML researchers unfamiliar with acoustics. Supply a fictional acoustic-anomaly study. Method: microphone to shared features, then parallel temporal and spectral branches, both into fusion and then a score; a separate operating-condition input also enters fusion. No internal architecture or merge operation is specified.

Require all eight rows and all three metrics in the main six-slide talk, with no appendix: A (.920 F1, 110 ms, 45 MB), B (.912, 78, 28), C (.901, 61, 19), D (.893, 47, 14), E (.921, 125, 50), F (.907, 64, 20), G (.899, 53, 16), H (.884, 40, 10). Same device/data are assumed; repetitions and variance are unavailable. Include `L = L_cls + lambda * L_distill`, illustrative `lambda = .3`, definitions and intuition; no precise loss formulation is given. Under changed microphone placement, C has F1 .842 instead of .901. No recording, image or spectrogram is supplied. Ask for immediately understandable, natural visual design without decorative artwork, invented failure samples or an unsupported optimal-model claim.

Inspect the resulting content allocation before style choices, exact bilingual copy, 420-second total, all 24 values, seven nodes/seven directed edges and the −.059 F1 change. The equation weight alone must not be called a 30% contribution. Reference choices should solve the difficult content problem. Confirm a stop for feedback, and separate planned geometry/glyph coverage from actual rendered fit. A plan-level pass is not a production or broad scientific-visual benchmark.

## Audience copy and purposeful composition

Use a brief with private constraints such as “lab seminar, five minutes, graduate audience, restrained design, internal draft v02.” Supply a real subject and explicitly illustrative comparison values. Request a finished bilingual deck with professional template-like composition and no decorative pictures. Do not ask for those private constraints to appear in the presentation.

Inspect exact visible copy and notes, not just the plan. Duration, audience category, revision status and design directions must stay outside the PPTX; scientific qualifiers, metric units and source attribution remain. Check that each slide has a deliberate focal object, grouped supporting content and a useful reading order. A title and scattered text on an empty page do not meet this brief merely because they fit. Purposeful table treatment, native diagrams, evidence regions and typographic composition are valid; arbitrary illustrations and mandatory cards are not. Inspect a difficult body slide and the ending against actual viewed references. Judge each language's optical balance independently. This scenario requires human/agent visual review and is not covered by the helper CI tests.


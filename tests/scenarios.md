# Behavioral evaluation scenarios

Run these in fresh agent sessions with the skill and the raw brief only. Do not provide previous conclusions or example output decks. Keep generated artifacts outside the skill repository. These checks complement helper unit tests; passing them is not a guarantee of aesthetic quality on every topic.

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


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

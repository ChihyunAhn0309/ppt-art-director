# Research seminar — English edition, revised slide plan

This is the final content specification for the redesigned example, incorporating the user's request for audience-relevant copy, meaningful visual composition and deliberate line fitting. The original test was explicitly one-shot; the later redesign was also directly authorized. This file is a synchronized final specification, not evidence of a separate approval checkpoint during the redesign.

## Brief and evidence

Private production constraints: five slides, five minutes, 16:9, graduate research audience. The seminar setting, rehearsal timing and authoring directions do not appear in the slides or speaker notes. Same device and data assumed. All performance values are fictional. Dataset, sample count, variance, architecture, loss and quantization scope are unspecified. Do not claim statistical significance, generalization or a universally best model.

| Model | Latency (ms) | F1 | Size (MB) |
|---|---:|---:|---:|
| baseline | 120 | 0.910 | 48 |
| distilled | 72 | 0.902 | 18 |
| int8 | 54 | 0.896 | 12 |

## Art direction and references

Warm ivory #F6F4EE, ink #1E302F, teal #287D78, secondary text #586C68, rules #CFD8D1, soft method/table fields #E8EDE5, on-dark secondary colors #B9DDD0 and #D7E6DF; all method markers use the same teal; small model IDs use darker teal #246E69 for contrast. No winner color. Use Segoe UI, with actual installed fonts checked; fonts are not embedded. A font substitution requires fresh fitting and rendering.

1280 × 720 design coordinates, 64–72 px primary margins. English/Korean cover titles are 39/36.75 pt; body-slide titles 30–32.25 pt; conclusion 36–36.75 pt; primary text approximately 18–24 pt; short supporting captions approximately 12.75–18 pt. Values vary by role and language. Each text box has an intended line count, checked in the saved PowerPoint file.

- [Pitch UX Research Report](https://pitch.com/templates/UX-Research-Report-4Crjbr5pvJCJ4vHD2t2z7N9j): actual gallery-size pixels of cover, process slide 8 and evidence slide 14 inspected on 2026-10-02. Adapt continuous method grouping, aligned columns and contrast between evidence and explanation. Reject decorative dot patterns, unrelated photography and automatic event/date metadata.
- [Pitch Market Analysis](https://pitch.com/templates/Market-Analysis-44RvbN4PQRqn5DB7hp6wA3GR): actual gallery-size pixels of market-size slide 10 and demographics slide 12 inspected. Adapt deliberate content proportions, shared plot anchors and header/body hierarchy; reject ornamental indices and badges. These were browser previews, not source PPTX or full-resolution inspection. No provider assets were copied.
- [Pitch Editorial](https://pitch.com/templates/Editorial-0oEK1D3jxabA58v6tk069rBZ): large cover and body-layout thumbnails inspected on 2026-10-02. Adapt whitespace and restrained hierarchy; reject decorative cover artwork; do not copy provider images or infer full-size body legibility from thumbnails.
- Earlier source example: [MIT annotated research slides](https://mitcommlab.mit.edu/aeroastro/wp-content/uploads/sites/11/2025/02/Slides-Annotated-Example-2-R.pdf), pages 1, 6 and 10 inspected during the original independent test. Large process/evidence objects and nearby interpretation informed the narrative.
- S02 was originally created with the user-selected [paper-figure workflow](https://github.com/JYS1025/paper-figure/blob/363fb3b76003d919f797356d774e70161164a7a8/skills/paper-figure/SKILL.md): [generated draft](design/workflow-draft.png), [actual prompts](design/image-prompts.json), and [pre-authoring transfer decisions](design/transfer-plan.md). The current revision adapts the principles directly: a continuous method field groups the established states and arrows, with equal marker styling and clearer content roles. No new image draft was generated for this local revision. See [research-visuals](../../references/research-visuals.md) for the principle-based route.

## Motion and static delivery

Only S02 has animation: two click groups, six native objects per group, Fade 0.35 s, no automatic slide advancement. Reveal the marker, incoming arrow, flow label, stage name, model ID and description together. A separate static edition shows the complete process. Actual slideshow playback is not verified.

## S01 — 30 seconds

**Purpose:** Introduce the topic and identify fictional evidence.

**Composition:** A dark subject field at left and a light comparison region at right; aligned baseline/INT8 values for three equally weighted metrics.

**Exact visible text** (intentional breaks shown as ` / `):

- `S01-title` (3 lines): Sensor anomaly / detection with / smaller models
- `S01-subtitle` (2 lines): Knowledge distillation / and INT8 quantization
- `S01-comparison` (1 line): The compression trade-off
- `S01-baseline` (1 line): baseline
- `S01-int8` (1 line): int8
- `S01-label-1` (1 line): Latency (ms)
- `S01-value-base-1` (1 line): 120
- `S01-value-int8-1` (1 line): 54
- `S01-label-2` (1 line): F1
- `S01-value-base-2` (1 line): 0.910
- `S01-value-int8-2` (1 line): 0.896
- `S01-label-3` (1 line): Model size (MB)
- `S01-value-base-3` (1 line): 48
- `S01-value-int8-3` (1 line): 12
- `S01-disclosure` (1 line): Illustrative data

**Speaker notes:** We examine model compression for sensor anomaly detection and compare baseline with INT8 latency, F1 and model size. All values are fictional user-supplied examples, not empirical findings. A common device and dataset are assumed but unspecified. No acceptable accuracy-loss threshold is supplied.

**Motion:** static.

## S02 — 90 seconds

**Purpose:** Explain the two conceptual compression steps.

**Composition:** One continuous soft field binds three equally styled native model states, transformation labels and directed arrows into a method.

**Exact visible text** (intentional breaks shown as ` / `):

- `S02-title` (1 line): Model states and compression steps
- `S02-disclosure` (1 line): Illustrative data
- `S02-number` (1 line): 02
- `S02-flow-2` (1 line): Knowledge distillation
- `S02-flow-3` (1 line): INT8 quantization
- `S02-stage-1` (1 line): Teacher model
- `S02-name-1` (1 line): baseline
- `S02-detail-1` (2 lines): The reference model / serves as the teacher.
- `S02-stage-2` (1 line): Student model
- `S02-name-2` (1 line): distilled
- `S02-detail-2` (2 lines): A smaller student learns / from teacher predictions.
- `S02-stage-3` (1 line): INT8 student
- `S02-name-3` (1 line): int8
- `S02-detail-3` (2 lines): Use 8-bit integers for / selected model quantities.
- `S02-caveat` (1 line): Conceptual overview; implementation details vary.

Stage markers: 01, 02, 03. Required directed edges: marker 01 → 02 → 03.

**Speaker notes:** The teacher provides prediction knowledge for learning a smaller student; INT8 represents student numbers using 8-bit integers. Architecture, loss, quantization scope, and PTQ versus QAT are unspecified. Do not assume preservation of all teacher knowledge or claim a particular implementation. Concept sources: Hinton et al. (2015), https://arxiv.org/abs/1503.02531 ; Jacob et al. (2017), https://arxiv.org/abs/1712.05877 . No empirical results were taken from those papers.

**Motion:** two click-driven Fade groups as specified above.

## S03 — 60 seconds

**Purpose:** Make all supplied data directly inspectable.

**Composition:** A native table with a dark header and alternating neutral row fields; equal numeric roles and no winner highlight.

**Exact visible text** (intentional breaks shown as ` / `):

- `S03-title` (1 line): Latency, F1 and model size
- `S03-disclosure` (1 line): Illustrative data
- `S03-number` (1 line): 03
- `S03-direction` (1 line): Lower latency and size are better; higher F1 is better.
- `S03-limit` (1 line): Illustrative comparison on assumed matching device and data; variability is not evaluated.

The native table contains the exact data in the brief above. Column labels are localized; model IDs remain unchanged.

**Speaker notes:** Fictional values: baseline 120 ms / F1 0.910 / 48 MB; distilled 72 ms / 0.902 / 18 MB; int8 54 ms / 0.896 / 12 MB. The same device and data are assumed. Sample count, variance, dataset, split, device specifications, latency statistic, and F1 aggregation are unspecified. These are arithmetic comparisons, not evidence of statistical significance or generalization.

**Motion:** static.

## S04 — 65 seconds

**Purpose:** Show the latency–F1 trade-off in one coordinate system.

**Composition:** A large native scatter plot at left; a dark interpretation region at right gives equal weight to latency reduction and F1 loss; stage deltas align beneath the plot.

**Exact visible text** (intentional breaks shown as ` / `):

- `S04-title` (1 line): Lower latency, lower F1
- `S04-disclosure` (1 line): Illustrative data
- `S04-number` (1 line): 04
- `S04-chart-unit` (1 line): F1 · higher is better
- `S04-x-unit` (1 line): Latency (ms) · lower is better
- `S04-basis` (1 line): Baseline to INT8
- `S04-latency` (1 line): −55%
- `S04-latency-label` (1 line): Latency · 120 → 54 ms
- `S04-f1` (1 line): −0.014
- `S04-f1-label` (1 line): F1 · absolute difference
- `S04-size-values` (1 line): Size: 48 → 12 MB (−75%)
- `S04-stage1` (1 line): Distillation: latency −40%; F1 −0.008
- `S04-stage2` (1 line): Additional INT8 step: latency −25%; F1 −0.006

Native scatter: baseline (120 ms, .910), distilled (72 ms, .902), int8 (54 ms, .896). X range 40–140 ms; Y range .890–.915 F1. Both axes are explicit; no fitted line or error bars. Direct model labels identify equally styled points. The range magnifies differences and is not a zero-baseline magnitude encoding. Overall reductions: (120−54)/120 = 55%; (48−12)/48 = 75%; F1 difference = −0.014. Stage denominators differ: 40% is relative to 120 ms; 25% is relative to 72 ms.

**Speaker notes:** Overall latency reduction (120−54)/120 = 55%; size reduction (48−12)/48 = 75%; F1 absolute difference 0.896−0.910 = −0.014. Distillation latency reduction (120−72)/120 = 40%, F1 difference −0.008. Additional INT8 latency reduction (72−54)/72 = 25%, F1 difference −0.006. Do not add 40% and 25% because their denominators differ. No statistical inference is possible from the fictional summaries.

**Motion:** static.

## S05 — 55 seconds

**Purpose:** Separate an illustrative result from a deployment decision.

**Composition:** One two-line focal statement in a dark left field, with deployment criteria and scientific limitations grouped at right.

**Exact visible text** (intentional breaks shown as ` / `):

- `S05-main` (2 lines): Efficiency gains / come with lower F1
- `S05-interpretation` (2 lines): A deployment decision needs / acceptable latency and F1 limits.
- `S05-label1` (1 line): Deployment limits
- `S05-body1` (1 line): Acceptable F1 loss and latency budget.
- `S05-label2` (1 line): Repeatability
- `S05-body2` (1 line): Repeat measurements on real data.
- `S05-label3` (1 line): Failure modes
- `S05-body3` (1 line): Inspect errors by anomaly type.
- `S05-limit` (2 lines): No real dataset or sample count; / generalization remains untested.
- `S05-disclosure` (1 line): Illustrative data

**Speaker notes:** These fictional values illustrate an efficiency–F1 trade-off. They do not select a universally best model. Define the acceptable loss in F1 and the latency budget for the intended environment. Repeat measurements on actual data, estimate variation, and inspect failures by anomaly type. No real dataset or sample count was supplied, so no generalization claim is justified.

**Motion:** static.

## Applied feedback

| Request | Change |
|---|---|
| Awkward wrap in the closing claim | Concise two-line focal statement with a deliberate phrase break in each language; measured native line count |
| Professional composition without unrelated artwork | Semantic light/dark regions, continuous method grouping, structured native table and plot/interpretation hierarchy |
| Private brief metadata appeared in the deck | Remove seminar setting, duration and design narration from slide copy and notes; keep pacing in this plan |
| English and Korean | Separate localized editions, including labels, caveats and speaker notes; render each |
| Content-first emphasis | Actual topic on the cover, no winner-like row highlight, joint latency–F1 plot and equally sized trade-off callouts |
| English GitHub documentation | English primary README, guides, evidence and this specification |

Future feedback can identify S01–S05 and the desired content, evidence or composition change. Preserve accepted decisions and update dependent chart data, calculations and notes.

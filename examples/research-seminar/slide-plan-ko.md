# Research seminar — Korean edition, revised slide plan

This is the final content specification for the redesigned example, incorporating the user's request for audience-relevant copy, meaningful visual composition and deliberate line fitting. The original test was explicitly one-shot; the later redesign was also directly authorized. This file is a synchronized final specification, not evidence of a separate approval checkpoint during the redesign.

## Brief and evidence

Private production constraints: five slides, five minutes, 16:9, graduate research audience. The seminar setting, rehearsal timing and authoring directions do not appear in the slides or speaker notes. Same device and data assumed. All performance values are fictional. Dataset, sample count, variance, architecture, loss and quantization scope are unspecified. Do not claim statistical significance, generalization or a universally best model.

| Model | Latency (ms) | F1 | Size (MB) |
|---|---:|---:|---:|
| baseline | 120 | 0.910 | 48 |
| distilled | 72 | 0.902 | 18 |
| int8 | 54 | 0.896 | 12 |

## Art direction and references

Warm ivory #F6F4EE, ink #1E302F, teal #287D78, secondary text #586C68, rules #CFD8D1, soft method/table fields #E8EDE5, on-dark secondary colors #B9DDD0 and #D7E6DF; all method markers use the same teal; small model IDs use darker teal #246E69 for contrast. No winner color. Use Noto Sans KR, with actual installed fonts checked; fonts are not embedded. A font substitution requires fresh fitting and rendering.

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

- `S01-title` (2 lines): 센서 이상 탐지 / 모델의 경량화
- `S01-subtitle` (2 lines): 지식 증류와 / INT8 양자화
- `S01-comparison` (1 line): 경량화에 따른 변화
- `S01-baseline` (1 line): baseline
- `S01-int8` (1 line): int8
- `S01-label-1` (1 line): 지연 (ms)
- `S01-value-base-1` (1 line): 120
- `S01-value-int8-1` (1 line): 54
- `S01-label-2` (1 line): F1
- `S01-value-base-2` (1 line): 0.910
- `S01-value-int8-2` (1 line): 0.896
- `S01-label-3` (1 line): 모델 크기 (MB)
- `S01-value-base-3` (1 line): 48
- `S01-value-int8-3` (1 line): 12
- `S01-disclosure` (1 line): 가상 데이터

**Speaker notes:** 센서 이상 탐지 모델의 경량화를 살펴본다. 원본 모델과 INT8의 지연, F1, 모델 크기를 비교한다. 모든 수치는 사용자가 제공한 가상 예시이며 실험 결과가 아니다. 동일 장치와 데이터를 가정하지만 구체적인 조건과 허용 F1 저하 기준은 미제공이다.

**Motion:** static.

## S02 — 90 seconds

**Purpose:** Explain the two conceptual compression steps.

**Composition:** One continuous soft field binds three equally styled native model states, transformation labels and directed arrows into a method.

**Exact visible text** (intentional breaks shown as ` / `):

- `S02-title` (1 line): 모델과 경량화 과정
- `S02-disclosure` (1 line): 가상 데이터
- `S02-number` (1 line): 02
- `S02-flow-2` (1 line): 지식 증류
- `S02-flow-3` (1 line): INT8 양자화
- `S02-stage-1` (1 line): 교사 모델
- `S02-name-1` (1 line): baseline
- `S02-detail-1` (2 lines): 성능 비교의 기준이자 / 지식을 전달하는 교사
- `S02-stage-2` (1 line): 학생 모델
- `S02-name-2` (1 line): distilled
- `S02-detail-2` (2 lines): 교사의 예측을 활용해 / 작은 학생 모델을 학습
- `S02-stage-3` (1 line): INT8 학생 모델
- `S02-name-3` (1 line): int8
- `S02-detail-3` (2 lines): 모델 내 지정한 수치를 / 8비트 정수로 표현
- `S02-caveat` (1 line): 경량화 과정을 설명하기 위한 개념도입니다.

Stage markers: 01, 02, 03. Required directed edges: marker 01 → 02 → 03.

**Speaker notes:** 교사의 예측을 학생 학습에 활용하는 지식 증류와 8비트 정수 표현을 개념적으로 설명한다. 모델 구조, 손실함수, 양자화 범위, PTQ/QAT는 미제공이다. 교사의 지식이 모두 보존된다고 주장하지 않는다. 개념 출처: Hinton et al. (2015), https://arxiv.org/abs/1503.02531 ; Jacob et al. (2017), https://arxiv.org/abs/1712.05877 . 문헌의 성능 수치를 사용하지 않았다.

**Motion:** two click-driven Fade groups as specified above.

## S03 — 60 seconds

**Purpose:** Make all supplied data directly inspectable.

**Composition:** A native table with a dark header and alternating neutral row fields; equal numeric roles and no winner highlight.

**Exact visible text** (intentional breaks shown as ` / `):

- `S03-title` (1 line): 지연, F1, 모델 크기 비교
- `S03-disclosure` (1 line): 가상 데이터
- `S03-number` (1 line): 03
- `S03-direction` (1 line): 지연과 모델 크기는 낮을수록, F1은 높을수록 좋습니다.
- `S03-limit` (1 line): 동일 장치·데이터를 가정한 예시이며, 측정 변동성은 평가하지 않았습니다.

The native table contains the exact data in the brief above. Column labels are localized; model IDs remain unchanged.

**Speaker notes:** 가상 수치: baseline 120ms / F1 0.910 / 48MB; distilled 72ms / 0.902 / 18MB; int8 54ms / 0.896 / 12MB. 동일 장치와 데이터를 가정한다. 표본수, 분산, 데이터셋명, 데이터 분할, 장치 사양, 지연 통계량 정의, F1 집계 방법은 미제공이다. 산술 비교이며 통계적 유의성이나 일반화를 판단할 수 없다.

**Motion:** static.

## S04 — 65 seconds

**Purpose:** Show the latency–F1 trade-off in one coordinate system.

**Composition:** A large native scatter plot at left; a dark interpretation region at right gives equal weight to latency reduction and F1 loss; stage deltas align beneath the plot.

**Exact visible text** (intentional breaks shown as ` / `):

- `S04-title` (1 line): 지연은 줄고, F1도 낮아집니다
- `S04-disclosure` (1 line): 가상 데이터
- `S04-number` (1 line): 04
- `S04-chart-unit` (1 line): F1 · 높을수록 좋음
- `S04-x-unit` (1 line): 지연 (ms) · 낮을수록 좋음
- `S04-basis` (1 line): 원본 대비 INT8
- `S04-latency` (1 line): −55%
- `S04-latency-label` (1 line): 지연 · 120 → 54 ms
- `S04-f1` (1 line): −0.014
- `S04-f1-label` (1 line): F1 · 절대 차이
- `S04-size-values` (1 line): 크기: 48 → 12 MB (−75%)
- `S04-stage1` (1 line): 증류: 지연 40% 감소, F1 0.008 하락
- `S04-stage2` (1 line): 추가 INT8 단계: 지연 25% 감소, F1 0.006 하락

Native scatter: baseline (120 ms, .910), distilled (72 ms, .902), int8 (54 ms, .896). X range 40–140 ms; Y range .890–.915 F1. Both axes are explicit; no fitted line or error bars. Direct model labels identify equally styled points. The range magnifies differences and is not a zero-baseline magnitude encoding. Overall reductions: (120−54)/120 = 55%; (48−12)/48 = 75%; F1 difference = −0.014. Stage denominators differ: 40% is relative to 120 ms; 25% is relative to 72 ms.

**Speaker notes:** 전체 지연 감소율 (120−54)/120 = 55%; 크기 감소율 (48−12)/48 = 75%; F1 절대 차이 0.896−0.910 = −0.014. 증류 지연 감소율 (120−72)/120 = 40%, F1 차이 −0.008. 추가 INT8 지연 감소율 (72−54)/72 = 25%, F1 차이 −0.006. 분모가 달라 40%와 25%를 더하지 않는다. 가상 요약값으로 통계적 판단을 할 수 없다.

**Motion:** static.

## S05 — 55 seconds

**Purpose:** Separate an illustrative result from a deployment decision.

**Composition:** One two-line focal statement in a dark left field, with deployment criteria and scientific limitations grouped at right.

**Exact visible text** (intentional breaks shown as ` / `):

- `S05-main` (2 lines): 효율 개선에는 / F1 저하가 따릅니다
- `S05-interpretation` (2 lines): 허용 가능한 F1 저하와 / 지연 한도를 먼저 정해야 합니다.
- `S05-label1` (1 line): 배포 기준
- `S05-body1` (1 line): 허용할 F1 저하와 지연 한도
- `S05-label2` (1 line): 측정 신뢰도
- `S05-body2` (1 line): 실제 데이터에서 반복 측정
- `S05-label3` (1 line): 실패 유형
- `S05-body3` (1 line): 이상 유형별 오탐과 누락 확인
- `S05-limit` (2 lines): 실제 데이터셋·표본수가 없어 / 일반화 여부는 확인할 수 없습니다.
- `S05-disclosure` (1 line): 가상 데이터

**Speaker notes:** 이 가상 예시는 효율과 F1의 교환관계를 보여준다. 모든 환경에서 가장 좋은 모델을 정할 수는 없다. 사용 환경에 맞는 허용 F1 저하와 지연 한도를 먼저 정한다. 실제 데이터에서 반복 측정의 분산과 이상 유형별 실패 사례를 확인한다. 데이터셋명과 표본수가 없어 일반화 판단은 불가하다.

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

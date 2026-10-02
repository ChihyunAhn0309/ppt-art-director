# Research seminar — Korean edition, revised slide plan

This is the final content specification for the redesigned example, incorporating the user's request for more natural design and deliberate line fitting. The original test was explicitly one-shot; the later redesign was also directly authorized. This file is a synchronized final specification, not evidence of a separate approval checkpoint during the redesign.

## Brief and evidence

Five slides, five minutes, 16:9, graduate research audience. Same device and data assumed. All performance values are fictional. Dataset, sample count, variance, architecture, loss and quantization scope are unspecified. Do not claim statistical significance, generalization or a universally best model.

| Model | Latency (ms) | F1 | Size (MB) |
|---|---:|---:|---:|
| baseline | 120 | 0.910 | 48 |
| distilled | 72 | 0.902 | 18 |
| int8 | 54 | 0.896 | 12 |

## Art direction and references

Warm ivory #F6F4EE, ink #1E302F, teal #287D78, secondary text #586C68, rules #CFD8D1, selected row #E8EDE5, F1 accent #A3563E. Use Noto Sans KR, with actual installed fonts checked; fonts are not embedded. A font substitution requires fresh fitting and rendering.

1280 × 720 design coordinates, 72 px primary margin. Cover title approximately 42 pt; body-slide titles 30–32.25 pt; primary text approximately 18–24 pt; short supporting captions approximately 12.75–18 pt. Values vary by role and language. Each text box has an intended line count, checked in the saved PowerPoint file.

- [Pitch Editorial](https://pitch.com/templates/Editorial-0oEK1D3jxabA58v6tk069rBZ): large cover and body-layout thumbnails inspected on 2026-10-02. Adapt warm negative space, image/text balance and restrained hierarchy; do not copy provider images or infer full-size body legibility from thumbnails.
- Earlier source example: [MIT annotated research slides](https://mitcommlab.mit.edu/aeroastro/wp-content/uploads/sites/11/2025/02/Slides-Annotated-Example-2-R.pdf), pages 1, 6 and 10 inspected during the original independent test. Large process/evidence objects and nearby interpretation informed the narrative.
- S02 follows the user-selected [paper-figure workflow](https://github.com/JYS1025/paper-figure/blob/363fb3b76003d919f797356d774e70161164a7a8/skills/paper-figure/SKILL.md): [generated draft](design/workflow-draft.png), [actual prompts](design/image-prompts.json), and [pre-authoring transfer decisions](design/transfer-plan.md). Reconstruct explanations natively; discard unsupported claims from the draft.

## Motion and static delivery

Only S02 has animation: two click groups, six native objects per group, Fade 0.35 s, no automatic slide advancement. Reveal the marker, incoming arrow, flow label, stage name, model ID and description together. A separate static edition shows the complete process. Actual slideshow playback is not verified.

## S01 — 30 seconds

**Purpose:** Introduce the topic and identify fictional evidence.

**Composition:** Warm editorial cover: editable title at left, conceptual ribbon artwork at right.

**Exact visible text** (intentional breaks shown as ` / `):

- `S01-section` (1 line): 연구 노트 / 01
- `S01-title` (2 lines): 센서 이상 탐지, / 더 가벼운 모델로
- `S01-subtitle` (2 lines): 지식 증류와 INT8 양자화의 / 성능 교환관계
- `S01-context` (1 line): 연구실 세미나 · 5분
- `S01-disclosure` (1 line): 가상 데이터 · 실제 실험 결과가 아닙니다

**Speaker notes:** 30초. 모든 성능 수치는 사용자가 제공한 가상 예시이며 실험 결과가 아니다. 동일 장치와 데이터에서 비교한다는 조건만 주어졌으며 구체적인 장치와 데이터셋은 미제공이다. 표지는 AI가 만든 개념 이미지이며 모델 구조나 측정값이 아니다.

**Motion:** static.

## S02 — 90 seconds

**Purpose:** Explain the two conceptual compression steps.

**Composition:** Open three-column native process: numbered markers, aligned text and two rightward arrows.

**Exact visible text** (intentional breaks shown as ` / `):

- `S02-section` (1 line): 방법 / 두 단계의 경량화
- `S02-title` (1 line): 교사 모델에서 경량 학생 모델로
- `S02-disclosure` (1 line): 가상 데이터 · 실제 실험 결과가 아닙니다
- `S02-number` (1 line): 02
- `S02-flow-2` (1 line): 예측 지식 전달
- `S02-flow-3` (1 line): 수치 표현 변환
- `S02-stage-1` (1 line): 원본 모델
- `S02-name-1` (1 line): baseline
- `S02-detail-1` (2 lines): 성능 비교의 기준이자 / 지식을 전달하는 교사
- `S02-stage-2` (1 line): 지식 증류
- `S02-name-2` (1 line): distilled
- `S02-detail-2` (2 lines): 교사의 예측을 활용해 / 작은 학생 모델을 학습
- `S02-stage-3` (1 line): INT8 양자화
- `S02-name-3` (1 line): int8
- `S02-detail-3` (2 lines): 학생 모델의 수치를 / 8비트 정수로 표현
- `S02-caveat` (1 line): 개념도입니다. 모델 구조와 구체적인 양자화 범위는 미제공입니다.

Stage markers: 01, 02, 03. Required directed edges: marker 01 → 02 → 03.

**Speaker notes:** 90초. 교사의 예측을 학생 학습에 활용하는 지식 증류와 8비트 정수 표현을 개념적으로 설명한다. 모델 구조, 손실함수, 양자화 범위, PTQ/QAT는 미제공이다. 교사의 지식이 모두 보존된다고 주장하지 않는다. 애니메이션판은 첫 클릭에 증류, 둘째 클릭에 INT8 단계를 표시한다. 개념 출처: Hinton et al. (2015), https://arxiv.org/abs/1503.02531 ; Jacob et al. (2017), https://arxiv.org/abs/1712.05877 . 문헌의 성능 수치를 사용하지 않았다.

**Motion:** two click-driven Fade groups as specified above.

## S03 — 60 seconds

**Purpose:** Make all supplied data directly inspectable.

**Composition:** Native table with quiet header rule and a restrained INT8 row highlight.

**Exact visible text** (intentional breaks shown as ` / `):

- `S03-section` (1 line): 근거 / 가상 성능 비교
- `S03-title` (1 line): 같은 조건에서 비교한 세 모델
- `S03-disclosure` (1 line): 가상 데이터 · 실제 실험 결과가 아닙니다
- `S03-number` (1 line): 03
- `S03-direction` (1 line): 지연과 모델 크기는 낮을수록, F1은 높을수록 좋습니다.
- `S03-limit` (1 line): 동일 장치·데이터를 가정합니다. 표본수·분산·실제 데이터셋명은 미제공입니다.

The native table contains the exact data in the brief above. Column labels are localized; model IDs remain unchanged.

**Speaker notes:** 60초. 가상 수치: baseline 120ms / F1 0.910 / 48MB; distilled 72ms / 0.902 / 18MB; int8 54ms / 0.896 / 12MB. 동일 장치와 데이터를 가정한다. 표본수, 분산, 데이터셋명, 데이터 분할, 장치 사양, 지연 통계량 정의, F1 집계 방법은 미제공이다. 산술 비교이며 통계적 유의성이나 일반화를 판단할 수 없다.

**Motion:** static.

## S04 — 65 seconds

**Purpose:** Explain the arithmetic trade-off with a zero-based chart.

**Composition:** Native latency chart on the left; overall latency, size and F1 changes on the right.

**Exact visible text** (intentional breaks shown as ` / `):

- `S04-section` (1 line): 결과 / 원본 대비 INT8
- `S04-title` (1 line): 지연은 줄고, F1도 낮아집니다
- `S04-disclosure` (1 line): 가상 데이터 · 실제 실험 결과가 아닙니다
- `S04-number` (1 line): 04
- `S04-chart-unit` (1 line): 지연 (ms)
- `S04-latency` (1 line): 55%
- `S04-latency-label` (1 line): 지연 감소 · 120 → 54 ms
- `S04-size` (1 line): 75%
- `S04-f1` (1 line): −0.014
- `S04-size-label` (1 line): 모델 크기 감소
- `S04-f1-label` (1 line): F1 절대 차이
- `S04-size-values` (1 line): 48 → 12 MB
- `S04-f1-values` (1 line): 0.910 → 0.896
- `S04-stage1` (1 line): 증류: 지연 40% 감소, F1 0.008 하락
- `S04-stage2` (1 line): 추가 INT8 단계: 지연 25% 감소, F1 0.006 하락

Native chart: baseline 120, distilled 72, int8 54 ms; value axis 0–140, direct numeric labels, no error bars. Overall reductions: (120−54)/120 = 55%; (48−12)/48 = 75%; F1 difference = −0.014. Stage denominators differ: 40% is relative to 120 ms; 25% is relative to 72 ms.

**Speaker notes:** 65초. 전체 지연 감소율 (120−54)/120 = 55%; 크기 감소율 (48−12)/48 = 75%; F1 절대 차이 0.896−0.910 = −0.014. 증류 지연 감소율 (120−72)/120 = 40%, F1 차이 −0.008. 추가 INT8 지연 감소율 (72−54)/72 = 25%, F1 차이 −0.006. 분모가 달라 40%와 25%를 더하지 않는다. 가상 요약값으로 통계적 판단을 할 수 없다.

**Motion:** static.

## S05 — 55 seconds

**Purpose:** Separate an illustrative result from a deployment decision.

**Composition:** One-line takeaway and three open rows for criteria, verification and limits.

**Exact visible text** (intentional breaks shown as ` / `):

- `S05-section` (1 line): 다음 / 허용할 성능 교환관계
- `S05-title` (1 line): 배포 기준을 먼저 정해야 합니다
- `S05-disclosure` (1 line): 가상 데이터 · 실제 실험 결과가 아닙니다
- `S05-number` (1 line): 05
- `S05-main` (1 line): 효율 개선에는 F1 저하가 따릅니다
- `S05-label1` (1 line): 먼저 정할 기준
- `S05-body1` (1 line): 허용 가능한 F1 저하와 지연 한도
- `S05-label2` (1 line): 다음 검증
- `S05-body2` (1 line): 반복 측정의 분산과 이상 유형별 실패 사례
- `S05-label3` (1 line): 현재의 한계
- `S05-body3` (1 line): 실제 데이터셋·표본수가 없어 일반화 판단 불가

**Speaker notes:** 55초. 이 가상 예시는 효율과 F1의 교환관계를 보여준다. 모든 환경에서 가장 좋은 모델을 정할 수는 없다. 사용 환경에 맞는 허용 F1 저하와 지연 한도를 먼저 정한다. 실제 데이터에서 반복 측정의 분산과 이상 유형별 실패 사례를 확인한다. 데이터셋명과 표본수가 없어 일반화 판단은 불가하다. 총 발표 시간 300초.

**Motion:** static.

## Applied feedback

| Request | Change |
|---|---|
| Awkward wrap in the closing claim | Concise single-line takeaway, full-width frame, measured native line count |
| Less rigid, more natural design | Warm background, conceptual cover, lighter type, open process and minimally ruled table |
| English and Korean | Separate localized editions, including labels, caveats and speaker notes; render each |
| English GitHub documentation | English primary README, guides, evidence and this specification |

Future feedback can identify S01–S05 and the desired content, evidence or composition change. Preserve accepted decisions and update dependent chart data, calculations and notes.

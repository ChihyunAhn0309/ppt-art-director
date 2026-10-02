# Typography, wrapping, and language

The final words are part of the composition. Fit them in the actual output font and language; character counts and English stand-ins are unreliable proxies for rendered width.

## Concise presentation voice

Default to compact phrases for titles, representative takeaways, body text, labels and captions in both Korean and English. Use a consistent level of compression within each role. Remove conversational introductions and sentence-final narration; do not reduce a meaningful finding to vague keywords. Keep the comparison, agent/action where needed, conditions, units, negation and uncertainty. A title must not become more certain than its evidence merely to become shorter. “Not assessable” does not mean “not significant”; preserve that distinction when shortening a limitation.

| Role | Korean | English |
|---|---|---|
| Finding title | 지연·크기 감소, F1 저하 | Lower latency, smaller model, reduced F1 |
| Method description | 교사의 예측을 활용해 학생 모델 학습 | Student training with teacher predictions |
| Qualified result | 동일 조건에서 지연 55% 감소함 | 55% lower latency under matched conditions |
| Limitation | 표본 수·불확실성 정보 부족으로 통계적 유의성 판단할 수 없음 | Statistical significance not assessable: sample size and uncertainty unavailable |

Korean titles usually work best as noun or finding phrases; explanatory items can end in “~함,” “~필요” or “~할 수 없음.” Avoid default “~합니다/~습니다/~입니다.” Do not mechanically append “함” to every label. English should use idiomatic noun, action or finding phrases rather than incomplete translations of Korean endings. Sentence case concerns capitalization, not a requirement to write complete sentences. Terminal periods are usually unnecessary on short standalone phrases; retain needed punctuation and decimal marks.

Brief speaker cues follow the same concise style. A requested read-aloud script may use natural full sentences. Preserve exact quotations, official names and source titles; an explicit user voice or a document format requiring full prose takes precedence. These rules govern the slide copy and presenter cues, not every explanatory paragraph in the planning document. Check the exact final copy in each language after rendering.

## Deliberate line endings

Give a headline or focal statement an intended line count in the slide plan. A short takeaway usually reads best on one line when space permits. Two balanced lines are valid when they form meaningful phrases. Do not force every title onto one line or preserve an awkward manual break just because it fits geometrically.

When text breaks unintentionally:

1. Remove presenter narration and redundant framing while preserving the claim, units, and caveats. A supported fictional trade-off can say “Efficiency gains with lower F1” instead of “This hypothetical example shows the trade-off between efficiency and F1.”
2. Give the text its proper share of the slide. Widen its container, rebalance the adjacent visual, or separate the finding from supporting detail.
3. Adjust that text role's size or weight modestly, retaining hierarchy and readable projection size. Do not shrink the entire deck or use extreme tracking to repair it.
4. If two lines remain appropriate, choose meaningful phrase boundaries and check their visual balance. Remove stale hard breaks when wording, font, or language changes.

Measure with the real font when possible, leaving some horizontal slack for renderer differences. Then inspect the exported PPTX in the intended renderer. Native line counts, bounds, and overflow reports complement visual inspection; they cannot detect every unattractive break. `wrap:none` and auto-fit settings alone do not prove text fits.

For a revision, record the text object, intended and observed line count, and repair. Scan table headers, chart labels, and captions too. Keep values with units and avoid punctuation at a line's start. A short last line is a review flag, not an automatic rule to rewrite precise terminology.

After fitting, check meaning and optics: the key condition and technical terms survive; mixed-script symbols, numerals and units read together at final size; and the wording sounds natural for the audience when spoken. Do not remove a scientific qualifier to obtain one line. Maintain a small terminology map for recurring bilingual terms when useful. Native table/chart labels require their own visual review even when every named text box passes.

## English

Use idiomatic concise English rather than translating Korean word order. Prefer sentence case unless the user's style specifies otherwise. Break at phrase boundaries, avoid a lone short word on the last line, and preserve technical names, abbreviations, signs, and decimal precision. Check long compounds in the saved render. English can need different line widths and sizes from Korean.

## Korean

Choose a verified Hangul font and inspect its Latin and numeric glyphs. Keep word units and particles together where practical; avoid stranded syllables or verb endings. A semantic two-line title can be intentional. Do not size Hangul using Latin font metrics or automatically apply English-style letter spacing.

For a supported fictional trade-off, “이 가상 예시는 효율과 F1의 교환관계를 보여줍니다” can become “효율 개선과 F1 저하”, while retaining the fictional-data caveat on the slide. This example is not a claim about every model.

## Multiple language versions

Keep slide IDs, evidence, units, equations, references, and semantic colors aligned. Localize titles, table headings, chart labels, caveats, notes, and accessibility text. Choose verified script-appropriate fonts. Reflow each edition independently while retaining the design system; do not carry Korean hard breaks into English.

For a requested bilingual slide, establish primary and secondary language roles. Otherwise prefer separate editions to doubling every label. Review each edition and name its files clearly.

# Typography, wrapping, and language

The final words are part of the composition. Fit them in the actual output font and language; character counts and English stand-ins are unreliable proxies for rendered width.

## Deliberate line endings

Give a headline or focal statement an intended line count in the slide plan. A short takeaway usually reads best on one line when space permits. Two balanced lines are valid when they form meaningful phrases. Do not force every title onto one line or preserve an awkward manual break just because it fits geometrically.

When text breaks unintentionally:

1. Remove presenter narration and redundant framing while preserving the claim, units, and caveats. A supported fictional trade-off can say “Efficiency gains come with lower F1” instead of “This hypothetical example shows the trade-off between efficiency and F1.”
2. Give the text its proper share of the slide. Widen its container, rebalance the adjacent visual, or separate the finding from supporting detail.
3. Adjust that text role's size or weight modestly, retaining hierarchy and readable projection size. Do not shrink the entire deck or use extreme tracking to repair it.
4. If two lines remain appropriate, choose meaningful phrase boundaries and check their visual balance. Remove stale hard breaks when wording, font, or language changes.

Measure with the real font when possible, leaving some horizontal slack for renderer differences. Then inspect the exported PPTX in the intended renderer. Native line counts, bounds, and overflow reports complement visual inspection; they cannot detect every unattractive break. `wrap:none` and auto-fit settings alone do not prove text fits.

For a revision, record the text object, intended and observed line count, and repair. Scan table headers, chart labels, and captions too. Keep values with units and avoid punctuation at a line's start. A short last line is a review flag, not an automatic rule to rewrite precise terminology.

## English

Use idiomatic concise English rather than translating Korean word order. Prefer sentence case unless the user's style specifies otherwise. Break at phrase boundaries, avoid a lone short word on the last line, and preserve technical names, abbreviations, signs, and decimal precision. Check long compounds in the saved render. English can need different line widths and sizes from Korean.

## Korean

Choose a verified Hangul font and inspect its Latin and numeric glyphs. Keep word units and particles together where practical; avoid stranded syllables or verb endings. A semantic two-line title can be intentional. Do not size Hangul using Latin font metrics or automatically apply English-style letter spacing.

For a supported fictional trade-off, “이 가상 예시는 효율과 F1의 교환관계를 보여줍니다” can become “효율 개선에는 F1 저하가 따릅니다”, while retaining the fictional-data caveat on the slide. This example is not a claim about every model.

## Multiple language versions

Keep slide IDs, evidence, units, equations, references, and semantic colors aligned. Localize titles, table headings, chart labels, caveats, notes, and accessibility text. Choose verified script-appropriate fonts. Reflow each edition independently while retaining the design system; do not carry Korean hard breaks into English.

For a requested bilingual slide, establish primary and secondary language roles. Otherwise prefer separate editions to doubling every label. Review each edition and name its files clearly.

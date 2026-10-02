# Source provenance and adaptation record

Research date: 2026-10-02 (Asia/Seoul). Direct primary sources were preferred. Public documentation can establish a product's described behavior; it cannot reveal a private internal prompt. This package contains original instructions, original palette data, and original helper code; it does not bundle upstream skill text, helper code, or template assets.

## Claude / Anthropic

- [Official PPTX SKILL.md](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/pptx/SKILL.md)
- [PPTX license](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/pptx/LICENSE.txt)

The reviewed official file describes creation, template editing, native charts, and separate content/package/visual checks. Its license identifies these materials as proprietary with substantial restrictions; public visibility is not an open-source grant. No text, palette table, scripts, or implementation was copied into this package. Our implementation uses the user's brief and independently written design/file-processing logic. Do not describe this package as a port or replica of Claude's internal production system.

## Gemini / Google

- [Gemini October 2025 update](https://blog.google/products-and-platforms/products/gemini/gemini-drop-october-2025/): Canvas presentation generation and Google Slides export.
- [Workspace March 2026 update](https://blog.google/products-and-platforms/products/workspace/gemini-workspace-updates-march-2026/): editable slide generation and conversational editing; whole-deck generation was described as forthcoming at that publication date.
- [Workspace back-to-school update](https://blog.google/products-and-platforms/products/workspace/gemini-google-workspace-back-to-school/): later documentation describes native full-deck generation and reference presentations for typography, colors, and design.
- [Gemini CLI Agent Skills](https://geminicli.com/docs/cli/skills/): the public agent-skill mechanism, not the internal Canvas/Slides presentation-generation prompt.

No official publicly accessible Gemini Canvas/Slides internal PPT-generation SKILL.md was identified in this research. This is a scoped finding, not proof that none exists. This package follows the observable idea of source-grounded generation with reference-consistent editing; it does not claim to reproduce Gemini's hidden system.

## Other public implementations

| Project | Verified revision | What it contributes to the comparison | Decision |
|---|---|---|---|
| [MiniMax PPTX generator](https://github.com/MiniMax-AI/skills/blob/60aaae52bb2af8162732751a4332f62a5fef518b/skills/pptx-generator/SKILL.md) | `60aaae52bb2af8162732751a4332f62a5fef518b` | Public MIT-labeled skill with a theme contract and modular slide workflow | Use a shared design contract concept; do not inherit its mandatory circular page badges, fixed canvas, or engine assumptions |
| [Frontend Slides](https://github.com/zarazhangrui/frontend-slides/blob/9906a34d640d2111f724544cbc50f7f130569ae1/SKILL.md) | `9906a34d640d2111f724544cbc50f7f130569ae1` | HTML decks, visual style previews, presentation-versus-reading density | Visual options can clarify preference; HTML behavior does not establish PPTX editability or motion |
| [slidegen](https://github.com/tylergibbs1/slidegen/tree/1ab0e9028cede748047c504b50b805ffd06f6101) | `1ab0e9028cede748047c504b50b805ffd06f6101` | Third-party Gemini/OpenAI slide-image generation and image assembly | Useful contrast case; full-slide image output is unsuitable as the default editable research deck |

Repository revisions were read from the GitHub API. They identify the inspected repository snapshots, not performance benchmarks. There was no controlled Claude-versus-Gemini-versus-Codex quality benchmark in this work. This skill cannot guarantee that one model will always match another's aesthetic quality.

## Design and research communication

### User-selected companion: paper-figure

[paper-figure SKILL.md](https://github.com/JYS1025/paper-figure/blob/363fb3b76003d919f797356d774e70161164a7a8/skills/paper-figure/SKILL.md), revision `363fb3b76003d919f797356d774e70161164a7a8`, was inspected on 2026-10-02. The original example followed its existing-artifact review route. The subsequent bilingual redesign followed its image-first creation route for S02: generate a complete composition draft, review it against the scientific contract, record a transfer plan, reconstruct editable native objects and inspect the final file. Unsupported details in the generated draft were rejected. `pptx.py inspect --contract` and `flow_audit.py` were used locally; reports retain their inspection limits. No upstream source code or assets are redistributed. The generated draft and our transfer decisions are included with the [example](https://github.com/ChihyunAhn0309/ppt-art-director/blob/main/examples/research-seminar/README.md).

See [reference-library.md](reference-library.md) for exact inspection levels and provider links. The role-based palettes and composition recipes are original starting points. Provider examples were used for analysis, not redistributed as assets.

- [MIT AeroAstro Slide Design](https://mitcommlab.mit.edu/aeroastro/commkit/slide-design/)
- [MIT NSE Slide Design](https://mitcommlab.mit.edu/nse/commkit/slide-design/)
- [MIT paper-to-slide figure redesign](https://mitcommlab.mit.edu/cee/2024/01/15/redesigning-existing-figures-for-slides/)
- [W3C contrast explanation](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html): useful text-contrast thresholds; this does not certify an entire presentation as WCAG-conformant.

## Native animation implementation references

- [Sequence.AddEffect](https://learn.microsoft.com/en-us/office/vba/api/powerpoint.sequence.addeffect)
- [MsoAnimEffect values](https://learn.microsoft.com/en-us/office/vba/api/powerpoint.msoanimeffect)
- [MsoAnimTriggerType values](https://learn.microsoft.com/en-us/office/vba/api/powerpoint.msoanimtriggertype)
- [PpEntryEffect values](https://learn.microsoft.com/en-us/office/vba/api/powerpoint.ppentryeffect)
- [Animations versus transitions](https://support.microsoft.com/en-us/powerpoint/the-difference-between-animations-and-transitions)
- [Morph tips and object matching](https://support.microsoft.com/en-us/powerpoint/morph-transition-tips-and-tricks)

The helper uses documented PowerPoint object-model methods and enum values. It intentionally supports a small, testable subset. Morph documentation establishes the shared-object approach and `!!` matching convention; it does not establish that arbitrary authoring libraries export Morph, or that chart geometry morphs.

## Host integration guidance

Codex's available Presentations and skill-creator guidance informed host integration and package validation. This package does not redistribute that runtime or depend on its cache paths. A host-provided toolchain takes precedence when its instructions apply; other hosts can select a documented native PPTX backend. [PptxGenJS documentation](https://gitbrent.github.io/PptxGenJS/docs/quick-start/) describes one such public backend. Installation and behavior checks are distinct from content research.

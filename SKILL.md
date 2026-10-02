---
name: ppt-art-director
description: "Create polished, editable PowerPoint presentations in English, Korean, or a requested language, with researched visual references, deliberate typography, slide planning, feedback integration, and purposeful native animation. Use for PPT/PPTX creation or substantial redesign, including research, technical, business, teaching, and keynote decks. Default to a reviewable slide plan before production; support explicit one-shot delivery. Not for text extraction alone."
---

# PPT Art Director

Make the content easier to understand at a glance. Establish what the audience should notice, compare or follow before choosing a visual style. Create an editable `.pptx` unless the user requests another format. Use the requested output language, independently of the source or conversation language. Support English, Korean, and deliberately mixed decks; if unspecified, infer the audience language from the brief. Repository examples do not set the user's output language.

Default visual direction: sophisticated, restrained, and appropriate to the topic. Research/technical talks, papers, and conferences receive particular support; preserve technical depth. The user's purpose, template, and style choices override these defaults. For research work also read [research-talks.md](references/research-talks.md).

Build visual interest through useful comparisons, explanatory diagrams, readable evidence, typography and space. Do not add abstract artwork, icons, background graphics or decorative pictures merely to make a slide look designed. A cover can be typographic. Use imagery when it explains the subject, supplies relevant context or evidence, or serves an explicit user-requested purpose. The user's request to omit decoration takes precedence over any host skill's default request for decorative assets.

## Route the request

| Situation | Action |
|---|---|
| New topic or rough materials | Prepare the complete slide plan and visual direction; wait for feedback before full production. |
| User says one-shot, 바로 완성, 알아서 끝까지, or explicitly waives review | Make the same planning decisions, then build and verify without an approval stop. |
| User responds to a plan with actionable feedback | Update that plan and build with the feedback unless they explicitly request another planning round. Do not ask for the same approval again. |
| User requests only a plan | Deliver the plan and stop. |
| Targeted revision to an existing deck | Inspect the deck, apply the requested revision, and verify. Do not force a new planning gate. |
| User provides an approved outline or required template | Reuse it. Resolve material gaps, not already answered preferences. |

The feedback checkpoint is this skill's default collaboration workflow. The user can waive it, provide an already approved plan, or request one-shot production. Silence is not feedback.

## 1. Understand and substantiate

Read [planning.md](references/planning.md). Extract audience, purpose, total slide count, delivery time, speaking versus reading use, source material, brand constraints, output format, and target player. Ask only questions that materially change the result. In one-shot mode choose reasonable design defaults and disclose them briefly; never invent company metrics or research findings.

Preserve requested counts, units, caveats, source images, and technical meaning. Distinguish supplied evidence, verified external facts, derived calculations, hypotheses, and explicitly illustrative data. Gather primary sources where the topic needs research; record them against slide IDs. A plan must contain actual proposed content, not merely headings such as "market analysis goes here."

Before styling, allocate the required evidence across the allowed slides and time. Identify the densest page and what must be readable immediately. For a dense fixed-count brief, map required rows, metrics and diagram relationships to slide IDs; this prevents polishing an incomplete outline. Plan geometry remains provisional until rendered with actual copy.

Separate the private brief from audience copy. Duration, intended audience, slide budget and production instructions remain in the plan; they are not default cover labels or footers. Read the audience-content rules in [planning.md](references/planning.md). Include only information the audience needs or the user explicitly wants displayed.

## 2. Establish art direction from real references

Read [design.md](references/design.md) and use [reference-library.md](references/reference-library.md) as a starting index. Identify the hardest communication problem first, then browse references that solve a similar problem: a branching method, dense comparison, equation or source figure. Inspect slide pixels, including body slides; do not infer design quality from descriptions or cover thumbnails alone. A mood reference does not validate an evidence layout. When browsing is unavailable, use the original recipes here and disclose that fresh references were not inspected.

For a research method, architecture or explanatory figure, read [research-visuals.md](references/research-visuals.md). It adapts the user-selected paper-figure project's relationship planning to presentation size, without requiring decorative art or an image-generation service. Stop searching when the relevant design decision is supported; there is no template quota.

Honor the user's supplied template and colors. Otherwise choose a coherent direction suited to the content and use compatible references where they resolve a design decision. Record exactly what was observed and adapted. Inspiration is not a license to redistribute a template, photograph, font, or logo.

Use the compact [design reference ledger](assets/design-reference-template.md) inside the plan or as a companion file. Record inspection depth, the design principle transferred to particular slides, and rejected traits. Carry references into concrete decisions about hierarchy, spacing, diagrams and evidence slides; a list of links alone is insufficient.

For ambiguous taste, include two or three small visual directions with the planning package when useful. Reuse real content from the deck, including one difficult body slide. This is an option, not an extra approval gate. Do not delay one-shot work with a template picker when the user has delegated design choice.

## 3. Deliver the planning checkpoint

Use [slide-plan-template.md](assets/slide-plan-template.md) to create a readable `slide-plan-v01.md` or a user-requested document format. This Markdown is a workflow artifact, not a cloud publishing request. Include:

- brief and assumptions; the deck's main message and story order;
- every slide's purpose, proposed title and exact content, evidence, visual treatment, notes, and animation intent;
- palette roles, type hierarchy, layout rhythm, reference links, and unresolved factual needs;
- a compact feedback section addressed by stable slide IDs such as S03.

Open or link the file. In the default mode, end the turn after asking for feedback on this concrete plan. Do not silently build the entire final deck. In one-shot mode, keep the plan available and continue. Apply later feedback to both content and dependent visuals; preserve accepted choices.

## 4. Build the whole deck as a system

Read [production.md](references/production.md). Inspect available authoring and rendering tools. When the host provides a Presentations skill, follow its supported engine and validation contract. Otherwise use an available documented native PPTX backend. No particular private runtime, model provider, or paid API is required by this skill; actual file generation needs an authoring engine and visual QA needs a renderer.

Read [free-tools.md](references/free-tools.md) when choosing a production route. Prefer appropriate available free tools for native PPTX, scientific plots, process diagrams and vector refinement. Select a small coherent set rather than using tools for variety alone. Keep a complete route that needs no purchased templates or paid image API; image generation is optional when supported by the host. Preserve editable source and distinguish SVG editability from native PowerPoint object editing.

Prototype a title, a typical content slide, and the densest evidence slide internally. Fix readability and style drift before expanding. Share tokens and layout helpers; separate slide content from geometry. Preserve native text, tables, charts, and required editable diagrams. Avoid full-slide image decks unless the user explicitly accepts the editing tradeoff.

Removing decoration is not a finished composition. Give the content a deliberate focal region, grouped supporting information and a clear reading path. Use proportion, alignment, type contrast and purposeful background fields where they improve grouping. Check that the deck has the requested visual finish as well as clean text fit; five identically sparse pages may still miss the brief.

Read [typography.md](references/typography.md). Compose with the actual target-language words. Assign intended line counts to headlines and focal statements, then verify the saved render. A box that does not overflow can still have an awkward wrap. Prefer concise copy or better proportions before modest size adjustment; do not shrink the whole deck to rescue a layout. Review every translated edition separately.

Select composition from content: evidence chart, comparison, mechanism, image study, timeline, equation, or focused statement. Vary emphasis and density across the story without making every slide look unrelated. Keep sources and explanatory detail in relevant speaker notes; visible caveats remain visible when they qualify a claim.

## 5. Implement motion only when it explains

Read [motion.md](references/motion.md) when animation is useful or requested. Record effect, target object, trigger, duration, sequence, and reduced-motion behavior. Use stable object names.

Native transitions and native object animations are different features. CSS animation, an animated preview, a GIF, and a motion plan do not prove the `.pptx` contains working animation. Never invent an authoring API. Use the supplied PowerPoint file-automation helper where supported, preserve compatible template motion, or use another documented native backend. If unavailable, deliver the strongest static deck and identify the precise motion limitation.

## 6. Verify and deliver

Read [quality.md](references/quality.md). Check the final file, not just the generator. Render all slides, inspect every slide at readable size, inspect the montage for pacing, verify facts and editability, fix defects, and rerender affected slides. Animation requires player verification in addition to package checks; report the actual level of verification.

Deliver the PPTX and plan, plus a compact preview when helpful. Preserve the build source privately for revision. Add a static/reduced-motion edition when motion is substantial or the delivery context needs one. Do not clutter outputs with build logs. Explain material limitations plainly; do not promise perfection or rate your own aesthetics numerically.

## Bundled helpers and references

- [palette_check.py](scripts/palette_check.py): measure specific foreground/background pairs; [palettes.json](assets/palettes.json) holds original role-based starting palettes.
- [pptx_audit.py](scripts/pptx_audit.py): inventory slides, object IDs/names, native charts/tables, notes, and motion; detects basic package issues. It does not render or validate the full OOXML schema.
- [apply_motion.ps1](scripts/apply_motion.ps1): add conservative native effects to a separate PPTX using installed Windows PowerPoint; see its limits and plan schema in [motion.md](references/motion.md).
- [sources.md](references/sources.md): verified provenance, upstream revisions, adaptation decisions, and limits of Claude/Gemini comparisons. Read when discussing origins or extending the research.

Do not modify this skill while making an ordinary deck. The user may explicitly ask to refine the skill based on their feedback.

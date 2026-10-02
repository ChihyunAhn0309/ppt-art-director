# Art direction and composition

These are original operating recipes, not extracted template assets. The user's reference outranks the starting values below.

## Pick a coherent visual direction

First name the communication job: compare quantities, trace a process, locate a change, explain a relation, or examine evidence. Choose an encoding and reading order for that job before choosing a theme. An attractive element must help that reading or fulfill a stated contextual purpose; otherwise omit it. Plain text can be the best visual for a concise conclusion.

Write one short design rationale connecting subject, audience, evidence density, and visual tone. Choose a dominant direction and restrained supporting devices. Do not combine a luxury serif cover, neon technical slides, and playful classroom illustrations without an explicit narrative reason.

| Direction | Suitable contexts | Composition and type | Color behavior | Watch out for |
|---|---|---|---|---|
| Precise editorial | Technical reports, research, executive briefings | Strong alignment, generous plot area, clear sans hierarchy | Neutral field, one semantic accent | An empty page is not automatically elegant |
| Stage keynote | Product introductions, public talks | Large statement or hero object, few simultaneous ideas | Deliberate light/dark beats | Thin evidence; excessive decorative images |
| Contemporary editorial | Culture, portfolios, strategy narratives | Asymmetric image/text balance, deliberate typographic contrast | Restrained warm or cool neutrals with one accent | Imported English typography may fail with Korean |
| Scientific atlas | Methods, experiments, comparative studies | Consistent figure panels, readable scales, tight evidence grouping | Stable series mapping, colorblind-conscious encoding | Tiny figure labels and unsupported significance claims |
| Human / organic | Education, health communication, sustainability | Genuine photography or restrained illustration with clear text | Soft background with dark text; saturated emphasis sparingly | Pastel text with insufficient contrast |
| Bold studio | Creative proposals, branding, launches | Typographic scale, decisive crop, selective saturated fields | One strong chromatic identity | Applying the cover's visual intensity to every chart |
| Monochrome premium | Architecture, design, formal proposals | Material photography, measured whitespace, strong grid | Black/white or charcoal with a minimal accent | Low-contrast gray captions and unnecessary gold |

For a visual reference record, note: URL, creator, pages actually inspected, title/body evidence, observed layout logic, adaptation, and reuse/license status. Avoid pretending a catalogue listing equals full-deck inspection.

## Working geometry

Use a single coordinate system. A useful 16:9 design canvas is 1280 × 720 CSS px; at 96 DPI, 1 pt = 4/3 px. Keep an ordinary content margin near 64 px and gutters near 24–40 px, adjusted for the template and content. Align to a few shared anchors instead of independently positioning every object. Full-bleed images are an intentional exception to margins.

Select a type scale for the actual viewing distance. Starting points: title 32–44 pt, body 20–26 pt for speaking decks; body 17–22 pt for reading decks; captions generally 12–16 pt. These are design targets, not universal pass/fail rules. Keep essential evidence readable; a technically fitting 9 pt chart label is not acceptable. The installed presentation engine may express sizes in px: do the conversion.

Never solve overflow by repeatedly shrinking all text. Edit redundancies, expand the container, reorganize, or redistribute content within the requested count. Put derivation detail in notes or an allowed appendix without hiding a caveat needed to interpret the result.

## Make restraint feel considered

Restraint does not require a dark cover, heavy bold headings, opaque process boxes, and a fully ruled table on every page. Choose each element's visual weight deliberately. Open table rows, quiet rules, varied figure proportions, selective imagery, and lighter body type can make technical content inviting without weakening evidence. Warm neutrals are one option, not a universal style.

Vary pace when the content warrants it: a direct opening, an open process diagram, a precise evidence page, and a concise closing statement. Keep type roles and semantic colors stable. Create ease through readable grouping, balanced whitespace, light rules and natural language. Avoid adding decoration to manufacture variety. When a user calls a deck stiff, compare old and revised body slides; changing only its cover or palette does not address the request.

## English, Korean, and bilingual typography

Read [typography.md](typography.md) for actual-font fitting, planned line counts, and language-specific composition. Neither English nor Korean is a mandatory default.

Check actual font availability and Hangul coverage before choosing a family. Candidates include Pretendard or Noto Sans KR when installed; Malgun Gothic may be an available Windows fallback. Do not assume any of them exists on the recipient's machine. Match the user's font if required; disclose substitutions.

Use one primary family by default and a second only when it adds a clear role. Avoid automatic Latin small caps, wide tracking, or italic body styles on Korean. Break lines at meaningful Korean phrase boundaries. Keep a number with its unit, do not strand particles or one syllable at the end of a title, and inspect mixed Latin/Korean baselines and math notation. Preview the actual long titles, not English stand-ins. Font embedding requires appropriate font rights and tool support; do not claim fonts are embedded by naming them in the file.

## Select a composition from the message

| Composition | Choose when | Visual specification |
|---|---|---|
| Statement + evidence | One strong finding | Compact title, dominant evidence panel, one adjacent explanatory note |
| Comparison | Two or more alternatives | Matched scales and column geometry; aligned criteria; one highlighted distinction |
| Annotated figure | A real artifact or result matters | Preserve the original, add a small number of precise callouts, cite the figure |
| Mechanism / architecture | Relationships explain behavior | Clearly named components, deliberate direction, labeled flows, small legend if necessary |
| Progressive process | Order matters | Steps with meaningful verbs; highlight the active phase; avoid arbitrary chevrons |
| Timeline | Time and milestones matter | Real date spacing where quantitative; label schematic spacing when not |
| Evidence chart | A quantitative comparison drives the claim | Plot takes most of the page, honest axes, direct labels, meaningful reference line |
| Small multiples | Same comparison across groups | Shared scales and repeated panel grammar; avoid forcing unlike quantities into one axis |
| Equation + interpretation | A mathematical relation is central | One focal equation with term definitions and a concrete interpretation |
| Image-led editorial | Visual evidence or emotional context matters | Intentional crop, real subject, readable caption, open text area |
| Decision table | Tradeoffs must be scanned | Native table, concise criteria, differentiated selected option without color alone |
| Focused statement | A transition or conclusion needs a beat | Strong typography and whitespace; no mandatory decorative icon |
| Synthesis / next step | Audience needs a conclusion or action | State the actual finding/decision, owner or next step only when supported |

Pick several composition families for a multi-slide deck where the content warrants it. Repeated layouts are useful for directly comparable experiments; variety is not a reason to destroy comparability. Dense technical content can be beautiful without pretending it is a launch keynote.

State what emphasis means: the current comparison, a changed variable, a chosen option or an evidence-supported winner. A highlighted row or oversized gain can imply a recommendation even when the words are accurate. Give competing decision variables comparable prominence when their priority is unspecified; use stronger emphasis only with a clear reason. Do not select a winner through color alone.

## Palette selection by role

Start from brand colors or the user's preference. If none, consider the topic's artifacts, desired tone, image colors, chart categories, and venue. Do not use color psychology as a factual rule such as "blue always means trust." [palettes.json](../assets/palettes.json) provides starting roles, not a closed menu.

Specify background, surface, text, muted text, accent, on-accent text, comparison colors, and warning color. Keep one accent dominant; reserve warning and categorical colors for their meaning. Run [palette_check.py](../scripts/palette_check.py) for every actual text/background pairing. Use 4.5:1 for normal text and 3:1 only for sufficiently large text as a useful accessibility baseline, not a claim of complete WCAG certification. For projected decks aim higher when possible.

Do not use a whole palette indiscriminately for labels: a bright chart accent can be unsuitable as small text on white. Distinguish categories with direct labels, markers, line styles, or positions as well as color. Keep the same series colors throughout the deck.

Separate theme colors from evidence encoding. Preserve channel identities, signed/diverging scales and category meanings, or deliberately remap them with an accurate legend. The theme accommodates necessary evidence colors, rather than recoloring the evidence to fit the theme.

## Image and chart discipline

Use images that add subject information, scale, context, evidence, or a deliberate emotional beat. Search or generate real visual assets through available tools; avoid clip-art clutter. Generate conceptual illustrations only when appropriate and never present them as empirical evidence or authentic event photos. Keep image prompts text-light so typography stays editable in the PPTX.

Native charts should expose their data and retain units and source traceability. Use zero baselines for bar charts unless a clearly justified exception is disclosed; avoid 3D chart decoration. A screenshot of a paper figure can be the correct evidence artifact if recreating it would change meaning; do not call that screenshot editable. Do not use image generation to invent graphs, data labels, logos, scientific figures, or formulas.

## The visual red flags to fix

Repeated title-plus-three-rounded-card pages; arbitrary accent strips; unnecessary badges and kickers; equally weighted colors; generic stock photos; weak heading/body contrast; center-aligned paragraphs; huge empty covers followed by microscopic dense pages; UI dashboard styling where a presentation needs a clear argument. These are warning patterns, not bans against a user-supplied design.

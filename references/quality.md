# Quality gates

Check separate properties separately. A valid ZIP is not proof of a valid PPTX; a valid PPTX is not proof of good design; a PNG is not proof of working animation.

## Content review

- Compare each slide against the approved plan and user feedback; verify exact requested count and required topics.
- Check claims against the source ledger, including denominators, periods, units, derived values, uncertainty, and chart labels.
- Read title and chart together. Does the evidence support the conclusion? Does a context slide overstate an insight?
- Check the requested language for translated abstractions, empty slogans, and awkward phrasing. For Korean, inspect noun chains and particles; for English, inspect idiom and sentence structure. Technical precision outranks stylistic simplification.
- Remove sample names, placeholder text, duplicate sections, internal workflow notes, and unsupported claims of novelty or superiority.
- Check visible copy and speaker notes for leaked brief metadata: duration, audience category, slide-count targets, authoring directions and QA remarks. Keep timing in the plan unless the user asks for presenter cues in the file.

## Package and editability review

Use the authoring engine's finalizer/validators when available, then [pptx_audit.py](../scripts/pptx_audit.py) for an inspectable inventory. Verify slide order through relationships, shape IDs/names, chart/table ownership, notes, and timing targets. The helper's limited checks complement rather than replace the engine validator.

Where editability is required, confirm the package contains native objects, and if a player is available inspect a representative text, chart, table, and diagram. Pixel previews alone cannot prove editability. Check presentation aspect ratio, actual fonts, embedded images, citations, and broken links. Do not claim cross-platform compatibility from one renderer.

## Visual review

Render every slide from the actual final file or a verified equivalent static export. Inspect each individually at a readable resolution and use a contact sheet for consistency and pacing. Review:

- main point is identifiable quickly; title, figure, and explanation have a clear reading order;
- dominant objects help recognize the subject, compare evidence or follow a relationship; remove attention-grabbing elements that add none of these;
- size, color and placement imply only the intended emphasis, without selecting an unsupported winner or minimizing a competing cost;
- no clipping, unexplained overlapping, orphan words, off-canvas content, or connector crossings through labels;
- Korean/Latin/math glyphs, line breaks, units, superscripts, and legends render correctly;
- chart labels and captions remain readable at presentation size;
- margins, alignments, repeated category colors, and type roles are consistent;
- images are sharp, relevant, not stretched, and not incorrectly cropped;
- hardest body slide receives the same design care as the title.
- focal and supporting regions form a deliberate composition at normal viewing size; removing pictures has not left a sequence of disconnected text blocks or visually identical sparse pages.

Compare focal text's actual line count and line endings to the plan in [typography.md](typography.md), even when geometry validation passes. A deliberate two-line title can be appropriate; an accidental wrap or stranded word needs repair. Use native text line counts and bounds when available, then inspect the pixels. Repeat for every language edition and compare redesigned slides to their originals.

List actual defects privately. Repair their causes in the source and rerender changed slides. Avoid endless style churn after the requested result is sound. Do not require an arbitrary number of repair rounds or invent a score threshold as evidence of quality.

## Motion review

Inventory: compare planned effects to actual native timings, shapes, triggers, and durations. Static view: all content is available in a coherent reduced-motion edition. Playback: inspect every animated slide's initial state, click sequence, final state, and navigation backward/forward in the target player where available. Check that evidence and caveats are never hidden when their associated claim is visible.

State verification honestly:

| Evidence obtained | Claim allowed |
|---|---|
| XML contains timing and valid object references | Native timing is present; playback unverified |
| PowerPoint file API reopens file and reports effects | PowerPoint parsed the file and effect settings; visual playback unverified |
| Static images inspected | Layout checked in the named renderer; no motion claim |
| Slide show inspected in target PowerPoint | Those specific effects and sequences were checked there |
| Only an HTML preview moves | Preview animation only; no PPTX animation claim |

If a tool fails, preserve the deck and report the specific unverified property. Do not rename an unverified file "perfect" or "fully compatible."

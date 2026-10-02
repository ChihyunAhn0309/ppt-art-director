# Planning and feedback contract

## Brief without a questionnaire wall

Infer what is already stated. Ask about audience/purpose, length, or essential sources only when missing information changes the deck materially. Do not require a preferred color or template: choosing those is part of the job. Research claims can require clarification even in one-shot mode; design indecision does not.

When there is only a topic, use a stated provisional brief: an informed general audience, a concise speaking deck, 16:9, and a length justified by the content. Do not silently convert a 10-slide request into 10 content slides plus a cover. Treat requested time as a pacing constraint, not a rigid one-minute-per-slide formula.

Speaking decks support a speaker with selective evidence and generous visual space. Reading decks need more complete claims, definitions, citations, and methodological context. A research talk may need both concise main slides and a technical appendix; add the appendix only if compatible with the requested count and scope.

## Audience content versus production context

Do not turn the brief into slide copy. Talk duration, target-audience descriptions, requested slide counts, mode, design instructions, revision IDs and QA status belong in the planning/build files. For example, a private brief saying “five-minute lab seminar” does not authorize a visible “Lab seminar · 5 minutes” label. Include an event, author or date only when supplied for audience-facing use or required by the template. Keep rehearsal timing in the plan; add it to speaker notes only when requested. Notes should otherwise contain the spoken explanation and sources, not production commentary.

Before exporting, inspect each visible element for its audience role: subject, claim, evidence, interpretation, essential qualifier, identity or useful navigation. Remove elements that only help the author manage the job. Keep scientific caveats, units and source attribution that the audience needs; express them concisely in audience language rather than repeating “not provided” inventory from the brief.

## Evidence before layout

Create a private source ledger:

| claim_id | slide_id | claim or data | source/location | date | evidence status | caveat/calculation |
|---|---|---|---|---|---|---|

Source locations must be useful: paper figure/page, dataset table, supplied spreadsheet cells, or direct primary URL. "Google" is not a citation. Research totals, percentages, axis units, denominators, baseline dates, and whether results are measured or predicted. Do not use an illustrative chart as empirical evidence. Resolve conflicting sources or show the meaningful uncertainty.

For a topic-only plan, research enough to write concrete content. If proprietary data is necessary, mark a precise missing fact and its impact. A marked gap is acceptable; a fabricated number is not. In a final one-shot deck, omit unsupported specificity, describe the limitation, or make a clearly labeled hypothetical example according to the task.

## Story structure is chosen, not stamped

| Purpose | A useful sequence, adapted to evidence |
|---|---|
| Research / technical talk | Question → prior approaches and gap → method → decisive evidence → limitations → conclusion |
| Business decision | Decision needed → current evidence → options and tradeoffs → recommendation if justified → execution |
| Product introduction | Relevant user problem → approach → demonstration → evidence → adoption or next step |
| Teaching | Learner question → concept → worked example → misconception or comparison → application |
| Progress review | Objective → change since baseline → evidence → risks and decisions → next milestones |

Do not force a recommendation when the task is explanatory. Do not add an agenda, team page, quote, or "thank you" slide merely because a template has one.

## Slide specifications

Each Sxx record must tell another author exactly what to build:

1. Role in the story and what the audience should understand.
2. Proposed title: a supported finding for an evidence slide; a precise subject label for a mechanism, definition, or context slide.
3. Exact on-slide copy, not a vague instruction. Quote genuine supplied text when required; write concise new text when appropriate.
4. Evidence: values, units, categories, image/figure identity, source pointer, important qualifier.
5. Visual design: selected layout, reading order, approximate area allocation, focal object, and how the visual supports the point.
6. Speaker notes: explanation that belongs in speech; source citations; transition to the next slide.
7. Motion: static or a specific reveal sequence with purpose. Do not promise unsupported effects.
8. Estimated speaking time where a duration was requested.

An outline that only says "S05 Results: add a chart" fails the planning contract. A useful record says which comparison, which values/source, why that chart, what the title concludes, and what caveat stays visible.

See the [filled results-slide example](../assets/slide-plan-example.md) when a concrete example of the required specificity is useful.

## Feedback handling

Keep stable IDs even when order changes. Store slide order separately from IDs. Convert feedback into a small working table: request → affected IDs → implementation decision. If a requested removal changes the argument, repair the bridge between the remaining slides. If a metric changes, update its chart, headline, calculation, notes, and conclusion together.

"S03 is too dense, use green, combine S05–S06" is actionable feedback and normally authorizes implementation in this workflow. "Only revise the plan" does not authorize building the full deck. If the user is exploring alternatives or asks a question without directing implementation, respond and preserve the planning state.

Do not re-open settled choices. Raise only conflicts that materially affect correctness or an explicit constraint. Explain any changed slide count before violating a fixed count; prefer restructuring within the count.

## One-shot

Planning, research, design selection, and QA still happen. Only the feedback stop is omitted. Choose the strongest suitable visual direction yourself. Use a local plan and source ledger to prevent content drift. Include a concise statement of material assumptions with delivery, outside the slides unless the audience needs them.

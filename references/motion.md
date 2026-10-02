# Motion that survives delivery

## Decide what moves and why

Default to restrained, speaker-controlled reveals for a technical deck. Motion is useful when it reduces simultaneous complexity or explains a change of state. A static chart or an already simple comparison may be better left alone.

| Intent | Good starting treatment | Avoid |
|---|---|---|
| Explain a process | Reveal meaningful stages in spoken order | One click per word or decorative arrow |
| Introduce a result | Establish axes/conditions, then show result and interpretation | Revealing the claim while its caveat is hidden |
| Explain architecture | Keep context visible; reveal or emphasize the focal component | Animating every box at the same time |
| Show a state change | Matched-object transition where supported | Fake movement created by unrelated objects |
| Move to a new section | Short fade or a clean cut | A new transition style on every page |

Useful starting durations: 0.25–0.5 s for an entrance, 0.35–0.7 s for a transition. These are aesthetic defaults, not measured universal optima. Use few purposeful builds, keep related elements together, and avoid looping, flashing, gratuitous bounce, spin, or sound. Do not automatically advance a speaking deck unless requested.

## Native PowerPoint helper

`scripts/apply_motion.ps1` uses the installed Windows PowerPoint file object model to add native entrance effects and transitions, then saves a new `.pptx` and reopens it to compare effect settings. It does not manipulate the UI. Requirements: Windows PowerShell, installed/licensed PowerPoint, and a static `.pptx` whose layout is already validated.

Supported subset:

- Object entrance: `fade`, `appear`, one entrance per top-level shape or group.
- Trigger: `click`, `with_previous`, `after_previous`; explicit duration and optional delay in seconds.
- Slide transition: `fade`, `none`; preserves unmentioned slides, disables timed advance only for explicitly targeted transitions.
- Targets: exactly one exported `shape_id` or unique exact `shape_name`, resolved after export.
- Existing native timing is refused on slides receiving object effects, to avoid silently replacing an established sequence. Transitions alone can coexist with existing timings.
- Never overwrites the input or an existing output. Does not attach to a running user PowerPoint session. It cannot create Morph, exit animations, motion paths, per-paragraph builds, or chart-series animation.

Inspect names and IDs first:

```text
python scripts/pptx_audit.py work/deck/static.pptx --output work/deck/qa/objects.json
```

Create a plan bound to that specific export:

```json
{
  "version": 1,
  "slides": [
    {
      "slide": 2,
      "transition": {"effect": "fade", "duration": 0.45},
      "effects": [
        {"shape_name": "S02-stage-1", "effect": "fade", "trigger": "click", "duration": 0.35},
        {"shape_name": "S02-stage-2", "effect": "fade", "trigger": "click", "duration": 0.35},
        {"shape_name": "S02-stage-2-label", "effect": "appear", "trigger": "with_previous", "duration": 0.01}
      ]
    }
  ]
}
```

Example PowerShell invocation, with paths adjusted to the active workspace:

```powershell
& './scripts/apply_motion.ps1' -InputPptx './work/deck/static.pptx' -Plan './work/deck/motion-plan.json' -OutputPptx './outputs/deck-animated-v01.pptx' -DryRun
& './scripts/apply_motion.ps1' -InputPptx './work/deck/static.pptx' -Plan './work/deck/motion-plan.json' -OutputPptx './outputs/deck-animated-v01.pptx'
```

Do not change machine execution policy or install PowerPoint automatically to enable this helper. A running-session refusal is a limitation of this conservative helper, not a reason to close the user's application. Use another available documented native workflow or preserve the static result and explain the limitation. Respect any higher-priority environment restrictions on Office automation.

The helper's success means that PowerPoint saved and parsed the native settings. It explicitly reports `playbackVerified: false`. Inspect slide-show playback through an available supported UI tool before claiming visual timing is correct. If unavailable, state that difference.

## More advanced motion

For Wipe, focus changes, exit/entrance choreography, or motion paths, use a documented native backend and test the exact feature before scaling it across the deck. Keep object mappings stable through export. Never add plausible-looking XML without schema-aware validation and player verification.

Morph requires matched objects on successive slides. [Microsoft's guidance](https://support.microsoft.com/en-us/powerpoint/morph-transition-tips-and-tricks) documents `!!`-prefixed matching names and a one-to-one match. It also notes that charts cross-fade rather than morph geometrically. Use Morph only when the target player and actual export path support it; the helper above does not. Count any duplicated states as actual slides.

## Honest fallback and export

If native animation cannot be implemented, do not describe an animation plan or browser animation as an animated PowerPoint. Deliver the correct static deck, retain the motion specification, and identify the unsupported feature. Do not silently add dozens of duplicate slides as a substitute when count is fixed.

For reading/printing and accessibility, preserve a static edition with the complete explanatory state. A PDF cannot contain native PowerPoint animation. Google Slides import may alter effects; check the actual imported document before claiming support. If video is requested, inspect the rendered timing and audio separately.

# Editable production packet — meaningful viewer control

Use with [the skill](../SKILL.md). A [domain pack](../../../domains/README.md) is optional when the full repository is available; otherwise fill the domain constraints from the user brief. Domain links in the filled example are optional context, not required dependencies. Specify what the viewer changes and what consequence appears. Editor controls and animated video do not prove viewer interaction; an MP4 fallback is linear.

## Interaction contract

- Audience and learning/decision objective: [fill].
- Source/content status and assumptions: [fill].
- Delivery layer: [web/LMS/player/prototype and actual capability].
- Viewer controls, available input methods and state persistence: [fill].
- Meaningful consequence and explanatory feedback: [fill].
- Fallback/transcript/captions/reduced-motion route: [fill].

## State and consequence map

| Viewer action | Starting state | State/result changed | Why this consequence matters | Feedback/retry | Keyboard/fallback behavior |
|---|---|---|---|---|---|
| [fill] | [fill] | [fill] | [fill] | [fill] | [fill] |

For simulations: [equation, units, bounds, deterministic source and uncertainty]. For branches: [destinations, skip/back/replay/resume behavior]. For learning: [practice versus assessment]. Visual identity: [actual content/meaning rather than decorative buttons]. Accessibility test scope: [actual evidence required].

## Filled example — LanternLab message check

Domain: [education](../../../domains/education.md). Fictional adult practice activity, no certification claim. Simulated message shows a mismatched sender address and a clearly fake destination string, never a live malicious link. Objective: inspect before clicking.

| Action | Consequence and explanation |
|---|---|
| “Inspect sender” | Reveal highlighted mismatch and explain that the address differs from the claimed sender |
| “Inspect destination” | Reveal the simulated destination in plain text; explain the mismatch without activating a link |
| “Click immediately” | Show a simulated feedback panel: “Pause first. Inspect the sender and destination.” Offer retry; do not punish or open a real URL |
| “Try again” | Reset the simulated choices and retain the activity instructions |

Controls are actual buttons, keyboard-operable, with visible focus and state feedback. Screen-reader announcement of changed feedback is tested when supported; it is not inferred from visual polish. No learner identity or score is collected. A linear narrated walkthrough plus transcript is the explicit fallback if viewer interaction cannot be delivered.

## Validation record

Exercise every branch/control, state reset, back/replay/resume and meaningful consequence. Inspect long feedback/narrow layout/zoom. Check keyboard, focus return, feedback announcements where in scope, captions and motion alternative. Technical clickability is insufficient if both branches say the same thing.

Implemented layer [fill/prototype/handoff]; actual control journey [evidence/not run]; accessibility checks [scope/not run]; fallback tested [evidence/not run]. Example above defines behavior, not a deployed activity.


## UI example choice when this brief includes a new interface

Offer three concrete same-content specimens with materially different structure/type/density/imagery for the user to choose. Preserve causal models, brand constraints and prior accepted choices; honor explicit opt-out or delegated selection. Record the actual preview and selected direction.

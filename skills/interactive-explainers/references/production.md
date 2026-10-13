# Interactive explainers: production rules

These rules apply to the selected task and supplied brief. Use judgment for reversible choices; preserve explicit user requirements.

## 1. Identify the causal model or decision

Identify the causal model or decision. Interaction must let the user compare, predict, choose, inspect or practice; buttons that merely reveal unrelated decoration do not make an explanation useful.

## 2. Define state transitions and feedback before visuals

Define state transitions and feedback before visuals. Specify initial/reset state, valid inputs, constraints, failure/recovery, and what changes on screen. Keep the model's assumptions and illustrative values visible when they affect interpretation.

## 3. Use a delivery layer that supports actual interaction: a web component/player, learning platform, or supported interactive authoring tool

Use a delivery layer that supports actual interaction: a web component/player, learning platform, or supported interactive authoring tool. An MP4 alone does not contain arbitrary clickable questions or branching controls.

## 4. Keep controls close to their effects and use clear labels/units

Keep controls close to their effects and use clear labels/units. Start with a useful default and provide reset or replay. Do not bury the main insight behind several setup actions.

## 5. Preserve a coherent illustration/design system while keeping navigation and input affordances familiar

Preserve a coherent illustration/design system while keeping navigation and input affordances familiar. Explain selections with text/status, not color alone.

## 6. Provide keyboard operation, visible focus, meaningful control labels and status announcements

Provide keyboard operation, visible focus, meaningful control labels and status announcements. Avoid hover-only critical information. Provide alternatives for drag/path gestures where applicable.

## 7. For branching video, define choices, target segments, pause/resume behavior, incorrect-answer feedback and re-entry

For branching video, define choices, target segments, pause/resume behavior, incorrect-answer feedback and re-entry. Verify every branch and keep captions/transcript available.

## 8. For a simulation, distinguish educational model from measured fact or prediction

For a simulation, distinguish educational model from measured fact or prediction. Validate the equations/data model and show limits. Attractive motion is not evidence of accuracy.

## 9. Exercise all reachable states, reset behavior, edge inputs, mobile layout and reduced-motion alternatives

Exercise all reachable states, reset behavior, edge inputs, mobile layout and reduced-motion alternatives. Check that controls do what their labels promise and update the explanation coherently.

## 10. Deliver the working artifact/source and its static/linear alternative where requested

Deliver the working artifact/source and its static/linear alternative where requested. State hosting/runtime dependencies and untested integrations without claiming a published live experience.

## Research references

These are further reading, not runtime dependencies or a license to copy upstream material. This file is original synthesis.

- [Viewer-interactive video capability](https://h5p.org/interactive-video)
- [Accessible interaction primitives](https://github.com/adobe/react-spectrum)

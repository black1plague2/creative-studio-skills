# App interfaces: production rules

These rules apply to the selected task and supplied brief. Use judgment for reversible choices; preserve explicit user requirements.

## 1. Start with tasks and information architecture

Start with tasks and information architecture. Identify entry, decision, action, feedback, recovery and next step. Design the journey, not just a sequence of attractive screenshots.

## 2. Inspect existing tokens and component patterns

Inspect existing tokens and component patterns. Establish or preserve a coherent system for typography, control size, spacing, borders, surfaces, accent and semantic states; record decisions for subsequent screens.

## 3. Specify relevant states per component/flow: default, hover, focus, selected, disabled, loading, empty, error and success

Specify relevant states per component/flow: default, hover, focus, selected, disabled, loading, empty, error and success. Do not invent meaningless states for static elements; do not omit failures for real actions.

## 4. Use established semantic/native controls or well-supported accessible primitives before custom interactions

Use established semantic/native controls or well-supported accessible primitives before custom interactions. Preserve keyboard behavior, labels, focus management and affordance. Styling a control does not excuse a broken action.

## 5. Design errors around recovery: what happened, what the user can do, and which fields/action need attention

Design errors around recovery: what happened, what the user can do, and which fields/action need attention. Do not rely on an unexplained disabled button or a transient toast for critical information.

## 6. Use density deliberately

Use density deliberately. A dashboard may need dense tables and restrained typography; onboarding may need a clearer illustration and fewer decisions. Familiarity can serve the user, so do not pursue novelty in standard controls without a reason.

## 7. Check long names, empty collections, unavailable images, slow/offline states, localization, zoom and narrow layouts

Check long names, empty collections, unavailable images, slow/offline states, localization, zoom and narrow layouts. Tables and sidebars need structural adaptation, not simply smaller fonts.

## 8. For native platforms, check safe areas, larger text, keyboard appearance, back behavior, touch/gesture alternatives and appropriate accessibility semantics

For native platforms, check safe areas, larger text, keyboard appearance, back behavior, touch/gesture alternatives and appropriate accessibility semantics. Web pixels and native points/dp are not interchangeable.

## 9. Motion should preserve spatial continuity and respond to input

Motion should preserve spatial continuity and respond to input. Prefer brief, interruptible feedback. Check reduced-motion behavior and real gestures; viewport emulation alone cannot validate physical touch.

## 10. Validate an actual primary journey, not just the happy-path screenshot

Validate an actual primary journey, not just the happy-path screenshot. Keep browser/component/accessibility checks distinct from visual critique. State whether the output is implemented, interactive prototype, or image-only concept.

## Research references

These are further reading, not runtime dependencies or a license to copy upstream material. This file is original synthesis.

- [Product craft and design memory](https://github.com/Dammyjay93/interface-design)
- [Accessible behavior primitives](https://github.com/adobe/react-spectrum)
- [Target size: correct AA standard](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)

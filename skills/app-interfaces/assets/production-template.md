# Editable production packet — task-focused app UI

Use with [the skill](../SKILL.md). A [domain pack](../../../domains/README.md) is optional when the full repository is available; otherwise fill the domain constraints from the user brief. Domain links in the filled example are optional context, not required dependencies. Specify behavior and recovery as concretely as palette and typography. A mockup is not functioning software.

## Task and platform

- Role, permission and primary task: [fill].
- Trigger → steps → successful outcome: [fill].
- Implemented/proposed/prototype boundary: [fill].
- Platform/stack/existing primitives and tokens: [fill].
- Real data/model/backend versus dummy local state: [fill].
- Source status, material questions and explicit assumptions: [fill].

## State specification

| Screen/component | Default and selected | Focus/keyboard | Loading/empty | Error and retained input | Success and next step |
|---|---|---|---|---|---|
| [fill] | [fill] | [fill] | [fill] | [fill] | [fill] |

Token roles: [text/surface/action/status; type; spacing; radius]. Navigation: [where user is and how to leave]. Data states: [unknown, stale, missing and long values]. Native behavior if relevant: [safe areas/larger text/keyboard/gestures]. Destructive actions if in scope: [consequence/recovery]. Do not invent backend success or permission grant.

## Filled example — QueueDesk assignment prototype

Domain: [SaaS](../../../domains/saas.md). Fictional coordinator assigns an owner to a synthetic ticket. No live customer service or integration exists. Primary action: “Assign owner.” Two selectable demo team members are clearly fictional; names are sample data.

Default: unassigned ticket; selected: chosen owner; focus: owner control and action have visible keyboard focus; loading: “Saving assignment…” with duplicate submission prevented; error: “Assignment wasn’t saved. Your selection is kept. Try again.” Success: show assigned owner after actual local simulated success. Empty: “No unassigned demo tickets.” Provide useful next action without claiming a real queue is clear.

Direction: task-focused density, one focal assignment region, reusable list/detail primitives, dark text on light neutral surfaces, restrained accent. Keep mock product state separate from public marketing. Test failed save/retained selection and retry, not only the happy-path screenshot.

## Evidence record

Deliverable type: [implemented/prototype/design/handoff]. Actual primary journey: [evidence or not run]. State coverage: [which states were exercised]. Narrow layout/zoom/long values: [actual result]. Keyboard/device/assistive checks: [actual scope; no inferred certification]. Findings: [severity/location/impact/repair/recheck]. Example here defines a prototype; it does not prove that one was built.


## UI example choice (when this task creates or redesigns UI)

Show three concrete same-content specimens before settling the final UI. Record option A/B/C, actual preview/reference, layout/type/density/imagery differences, task/brand fit, and the selected direction. Let the user choose; retain a prior selection for follow-ups and honor an explicit opt-out or request to choose for them. For visual-assets this applies only to UI mockups.

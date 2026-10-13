# Concrete UI directions before implementation

Open [the self-contained gallery](index.html) in a modern browser. It offers three original, real-content mini examples of the same fictional patient care portal. Choose with a button; a persistent visible status identifies the chosen direction. Selection is local to the gallery URL fragment (`#calm`, `#precision` or `#community`), so reloading preserves it. Clear selection is available. No server, framework, external font, external image or network request is required.

| Direction | Structure and expression | Practical emphasis |
| --- | --- | --- |
| Calm care | Supportive sidebar, paper/sage, serif appointment focal panel and chronological care rail | Personal continuity and comfortable scanning |
| Precision | Horizontal navigation, white/ink/cobalt, compact planner and aligned visit table | Scheduling, density and structured information |
| Warm community | Open composition, cream/terracotta, expressive serif greeting and personal task list | Welcome, tone and a smaller set of immediate tasks |

These examples are options to adapt to the live brief, **not mandatory themes**. For a different product or industry, make new content-bearing examples that fit its audience, domain, tasks and supplied references. Do not blindly apply a healthtech palette, care metaphor or appointment model to an unrelated interface. Distinguish the options through layout, type, density, composition and interaction priorities; recoloring one layout does not create meaningful options.

## How an AI should use this

1. Read the actual brief and relevant existing product material first.
2. Before final implementation, show at least three concrete UI examples with representative real content, outside-the-preview labels, and concise differences/tradeoffs. Use screenshots, rendered specimens or runnable mini examples available in the current host. An abstract moodboard or palette list alone does not satisfy this step.
3. Ask the user to choose an option or a specific mixture. Preserve their choice. If they explicitly opt out or already choose a supplied direction, follow that instruction instead of forcing a new approval loop.
4. Carry the chosen direction into the complete UI. Then test the real primary flow, state recovery, keyboard focus and responsive layout.

The previews here are intentionally visual, non-interactive UI specimens. The gallery’s choice buttons are the implemented interaction. A final interface must implement its own actions rather than shipping preview controls as functional UI. Choice labels and comparison notes stay outside the specimens so the intended product composition remains visible.

The separately delivered Morrow Care healthtech demo was accepted by the user and remains unchanged. This gallery does not modify it or require redesigning already approved work.

## Content and originality

All three options use fictional Alex Morgan, fictional Dr. Maya Chen, the same 15 October 2026 follow-up, and administrative visit-summary content. No medical advice, health measurements, real patient information, real service claim or actual clinician contact is included. Layout, copy, CSS and visual marks are original examples, not copied upstream templates.

## Practical checks

- Choose each direction: only one option should have `aria-pressed="true"`, a visible selected button label and a selected border.
- Verify the status text describes the same choice; reload the `#precision` or other selected fragment and confirm it restores correctly.
- Clear selection: all buttons become unselected, status recovers and keyboard focus moves to the first choice.
- Use Tab and Enter/Space to select; keyboard focus has a visible outline and the status is announced through a polite live region.
- Inspect desktop, 768px, 390px and 320px widths. All content should remain readable without horizontal overflow. Reduced motion removes press transforms.
- The preview controls are deliberately plain text/span specimens and are not keyboard stops; the functional gallery controls are semantic buttons.

Executed during creation: HTML ID uniqueness, exactly three semantic choice buttons, JavaScript syntax and absence of external asset links passed. A Node VM behavioral harness also passed restored selection, switching options, exclusive selected state, clear-selection focus and invalid-fragment recovery. The harness uses a modeled DOM; it does not establish visual layout or real screen-reader behavior. Browser inspection and repository-wide check outcomes are recorded by the integrating agent after execution.

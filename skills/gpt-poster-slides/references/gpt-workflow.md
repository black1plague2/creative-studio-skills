# GPT: source to complete poster slides

This is the only provider-specific production workflow in the library. Other AIs can plan or prepare its handoff; actual poster generation uses GPT image generation unless the user explicitly changes that requirement.

## Capability check

Inspect the host's actual image-generation tool and file capabilities. In an image-enabled GPT conversation, use its available native image tool. In an API workflow already authorized by the user, use current official GPT image documentation and a configured credential route; never ask the user to paste a secret into chat. Do not silently purchase credits, change model/provider, or invent a function/size parameter.

If generation is unavailable, produce a clearly labeled handoff: resolved brief, verified source ledger, deck plan, exact-copy list, style specification, reference roles, per-slide prompts, requested output sizes and QA criteria. State that images and final packaging remain. A prompt-only result is not a PPT.

## Read and extract

Read all relevant source content and inspect visual references. Identify what is factual, supplied but unverified, hypothetical, and illustrative. Preserve required caveats and real figures. Input may be a PRD, PDF, PPT, transcript, notes or an idea. Ask only the material questions in intake.md that these inputs do not answer.

## Plan the deck

Record audience, purpose, count, language, density, aspect and outputs. For each slide, specify role, message, exact required copy, illustration mechanism, technical relationships, and source locations. Build a coherent sequence. A reading-first deck can contain dense infographic plates; a spoken pitch generally needs larger, shorter copy. Do not force one fixed density on both.

## Lock the visual system

Define a topic-specific palette, type hierarchy, illustration medium, recurring motifs, character/object identity and composition grammar. Use supplied references to understand these choices, not to copy their labels or reuse personal content. Maintain one dominant direction. Test the direction on both a cover and representative content slide if it is unresolved.

## Generate

Save the final prompt for each slide before calling the tool. Generate one complete slide image at a time or use a supported batch interface for independent prompts. Request landscape 16:9 explicitly; 1920×1080, 2048×1152 or another exact 16:9 canvas can be a target only when the interface supports it. Inspect actual returned dimensions instead of promising them from prompt text alone.

Use exact text in quotes and distinguish headline, stage labels, annotations and footer. Keep text concise enough to verify. Pass an approved cover or reference image when supported and state which traits to preserve. A reference is not an edit target unless an edit is actually requested.

Exact copy preserves words, names, numbers, units, punctuation, qualifications and significant identifiers. Keep the source string in the copy/transcript record. Ordinary display spacing and line wrapping can adapt to composition unless the user requires exact typesetting; meaningful spacing in code, identifiers or aligned evidence must survive. A visual stage label can separate its numeral and word graphically without changing the wording.

## Review and iterate

Inspect every generated slide at full size. Verify spelling, required text, numbers, units, caveats, arrows, object relationships, anatomical/object artifacts, contrast and framing. Compare the set as a contact sheet. Repair with supported GPT regeneration/editing; preserve unchanged traits. Simplify or split a dense slide rather than accepting unreadable labels. Stop when substantive checks pass; do not force needless regeneration just to satisfy a style preference.

## Package and deliver

Create the ordered manifest and mark reviewed images only after actual inspection. Run the optional helpers, reopen outputs, and compare to the approved images. Deliver image files plus requested PDF/PPTX. Keep a transcript/exact-copy record because the final PPTX text is part of the image. Do not claim editable text, implemented UI, or evidence accuracy solely because a poster looks polished.

The local helpers accept native dimension rounding within one pixel, disclose it, and place the entire image proportionately on an exact 16:9 page. Meaningfully wrong ratios fail. If an exact PNG pixel canvas is a contractual requirement, obtain a supported generation/export of that canvas rather than stretching.

Current tool/model behavior should be checked against [official GPT image documentation](https://developers.openai.com/api/docs/guides/image-generation). This file does not pin a model name or assume every host exposes the same controls.

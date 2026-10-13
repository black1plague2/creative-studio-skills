# Natural voiceover: production rules

These rules apply to the selected task and supplied brief. Use judgment for reversible choices; preserve explicit user requirements.

## 1. Keep narration meaning exact while adapting written prose to speech: shorter clauses, ordinary vocabulary, concrete verbs and varied rhythm

Keep narration meaning exact while adapting written prose to speech: shorter clauses, ordinary vocabulary, concrete verbs and varied rhythm. On-screen labels need not be read verbatim if that creates repetition.

## 2. Choose the narrator to fit the subject

Choose the narrator to fit the subject. Natural delivery is not a named preset, and a synthetic voice is not automatically inferior or adequate. Audition the actual difficult sentence from this script.

## 3. For human recording, provide conversational direction, a quiet recording setup, pronunciation notes, pauses and pickup points

For human recording, provide conversational direction, a quiet recording setup, pronunciation notes, pauses and pickup points. Preserve intentional expression; do not over-process away the voice's character.

## 4. For synthesis, use the available provider/model's documented controls

For synthesis, use the available provider/model's documented controls. Pause markup, pronunciation dictionaries, style tags and speed settings differ. Read current primary documentation before making API-specific assumptions.

## 5. Maintain voice/model/recording conditions across scenes

Maintain voice/model/recording conditions across scenes. If generating segments, provide contextual stitching where supported and listen to boundary joins. Independently generated sentences often have inconsistent rhythm.

## 6. Build a pronunciation ledger for names, brands, acronyms, code terms, numbers and units

Build a pronunciation ledger for names, brands, acronyms, code terms, numbers and units. Verify important pronunciations in audio, not only in spelling or phonetic markup.

## 7. Budget from measured output

Budget from measured output. If too long, remove unnecessary wording or beats; do not force an unnaturally fast voice to fit a fixed slot. Keep a pause where the viewer needs to understand a change.

## 8. Listen without the picture, then with the picture

Listen without the picture, then with the picture. Check meaning, emphasis, cadence, breath/pauses, unwanted words/repetition, clipped endings, accent appropriateness and joins. A waveform or transcript cannot establish perceived naturalness.

## 9. Normalize/mix to the declared delivery target and keep narration audible over music

Normalize/mix to the declared delivery target and keep narration audible over music. Check clipping and audible noise/artifacts on representative devices; do not call one LUFS value universally correct.

## 10. If direct listening is unavailable, say the naturalness review is unrun and provide audio for the user to audition

If direct listening is unavailable, say the naturalness review is unrun and provide audio for the user to audition. Do not mark the voice approved or claim a human/AI origin you cannot establish.

## Research references

These are further reading, not runtime dependencies or a license to copy upstream material. This file is original synthesis.

- [Model-dependent speech controls](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices)
- [Local voice candidate](https://github.com/hexgrad/kokoro)
- [Local expressive voice candidate](https://github.com/resemble-ai/chatterbox)

# Reusable artifact templates and production records

Use the smallest record useful to this task. These are templates, not forms the user must complete before the agent can act.

- [Creative brief](creative-brief.md): source-derived answers and material open questions.
- [Source ledger](source-ledger.csv): content/claim provenance and qualification.
- [Artifact QA record](qa-record.md): observed defects and actual rechecks.
- [Production handoff](handoff.md): outputs, source, capabilities, and remaining work.
- [Cross-artifact review matrix](review-matrix.md): source, audience, craft, operation/audio and final-file evidence kept distinct.

## Artifact templates

Each template lives inside its skill folder so it can be copied with that skill. Use a [domain pack](../domains/README.md) optionally when the full repository is available, or fill domain constraints directly from a user's brief. Each asset includes editable production fields, a filled fictional example and actual-review requirements.

| Artifact | Template |
|---|---|
| Multi-artifact brief | [Creative director](../skills/creative-director/assets/production-template.md) |
| Generated 16:9 deck | [GPT poster slides](../skills/gpt-poster-slides/assets/production-template.md) |
| Poster / infographic | [Poster infographics](../skills/poster-infographics/assets/production-template.md) |
| Illustrations / image set | [Visual assets](../skills/visual-assets/assets/production-template.md) |
| Identity system | [Brand identity](../skills/brand-identity/assets/production-template.md) |
| Website | [Website frontends](../skills/website-frontends/assets/production-template.md) |
| App / dashboard / component | [App interfaces](../skills/app-interfaces/assets/production-template.md) |
| Reading-first PDF | [Editorial PDF](../skills/editorial-pdf/assets/production-template.md) |
| Editable Word | [Word documents](../skills/word-documents/assets/production-template.md) |
| Narrated video | [Explainer video](../skills/explainer-video/assets/production-template.md) |
| Narration / voice | [Natural voiceover](../skills/natural-voiceover/assets/production-template.md) |
| Viewer interaction | [Interactive explainers](../skills/interactive-explainers/assets/production-template.md) |
| Exact data story | [Data storytelling](../skills/data-storytelling/assets/production-template.md) |
| Campaign variants | [Social campaigns](../skills/social-campaigns/assets/production-template.md) |
| Creative text / UX copy | [Creative copy](../skills/creative-copy/assets/production-template.md) |

For new UI or visual redesign, show three concrete examples for the user's choice before settling the final UI. Use [the UI choice policy](../docs/ui-choice-policy.md) and [chooser example](../examples/ui-directions/README.md). Preserve an accepted direction for follow-ups; these templates do not impose an unrelated redesign on a bug fix.

The agent fills what the source establishes and asks only material missing questions. A reversible design choice can be an explicit assumption. Do not publish filled records containing private user material merely because the skill repo is public.

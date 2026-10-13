> **Research archive, not overriding production instructions.** This is the complete supplied narrative report, archived after the repository was created. Its research-phase status statements and alternative/editable-slide recommendations are historical. The current user contract requires complete GPT-generated 16:9 poster slides, including typography; that contract and `skills/gpt-poster-slides/SKILL.md` take precedence over older suggestions to generate illustration and text separately. The single local reference-brief link was adapted to an original public text-only interpretation. No user reference PDF/PPTX/video assets are included.

# Creative skills repository: research and proposed production rules

Research date: **13 October 2026**. Prepared for your personal creative-skills repository.

**Updated using your supplied examples:** your presentation default is now a complete image per slide, packaged as a PDF and optionally an image-based PPTX. The references support strong topic-specific illustration, both sparse and dense compositions, and designed architecture/user-flow graphics. Earlier editable-PPTX recommendations below are optional production/alternate-output routes. The detailed observations and revised contract are in [creative-direction-interpretation.md](creative-direction-interpretation.md). The supplied video is a 91-second illustrated product explainer; narration naturalness still needs a direct listening evaluation.

The strongest approach is a small set of task-specific skills that share source fidelity, reference research, deliberate visual decisions, rendered review, and an editable handoff. Keep alternative styles and production engines available. Combining every discovered rule verbatim would introduce contradictions and duplicate workflows.

## Coverage and evidence

This research inspected material from **58 distinct GitHub repositories**, with a broad pass over READMEs/catalogs and a focused pass over selected skill files, audit references, examples, and license files. Additional primary sources include MIT Communication Lab, Michael Alley’s assertion-evidence tutorial, Duarte, Matthew Butterick, Apple, Material Design, W3C, H5P, Slidev, Frame.io, and ElevenLabs documentation.

This is a bounded survey, not an exhaustive search of GitHub. Repository popularity was not used as proof of output quality. Engines, reusable skills, creator examples, and discovery directories are identified separately in the source registry.

**What was verified:** public source availability, specific written rules, selected workflow details, declared dependencies, example links, and selected license notices. **What was not tested:** repository scripts, rendered outputs from these workflows, voice comparisons, paid services, installation behavior, or cross-agent reliability. Some files were inspected through relevant excerpts rather than a complete code audit. Examples are evidence that a workflow has artifacts, not an independent quality rating.

A repository owner’s identity and public history do not establish that every instruction was manually written. For your request for realistic human methods, give particular weight to documented creator practice and concrete artifacts: [MIT’s annotated poster resources](https://github.com/MIT-BECL/Poster_Resources), [3Blue1Brown’s video source and interactive workflow](https://github.com/3b1b/videos), and [Duarte’s presentation case study](https://www.duarte.com/approach/case-studies/reimagining-event-presentations-to-tell-a-visionary-story/). These are stronger evidence of a working process than a generic claim that a skill produces professional work.

The GitHub API rate limit interrupted part of the metadata pass; raw public files remained accessible. Missing license metadata is recorded as unresolved, not interpreted as permission. Renamed repositories and historical paths were distinguished from current files. No GitHub repository was created or published during this research phase.

## The sources I would prioritize

| Task | Preferred starting sources | Why they fit your request |
|---|---|---|
| Visually composed slide images | Baoyu/K-Dense image workflows; Frontend Slides; assertion-evidence; JetBrains/dachent QA | Topic-specific composition, a complete image per slide, and exact export checks |
| Posters and illustrated summaries | MIT-BECL; Baoyu infographic; K-Dense posters | Real poster examples, explicit visual composition, and physical-output checks |
| PDFs and designed reports | OpenAI PDF; WeasyPrint or Typst; Butterick | Rendered-page review plus typography and reproducible typesetting |
| Editable Word documents | JetBrains doc; python-docx; narrow lessons from grapeot | Structure-aware editing and before/after layout checks |
| Website front ends | Refero research method; Impeccable; targeted frontend guidance; Vercel review | Evidence for the visual direction, critique, and actual browser verification |
| App UI | Interface Design; Impeccable product mode; React Aria/Radix; UI Skills; Emil | Consistent systems, complete states, familiar controls, and responsive interaction |
| Short narrated video | Remotion; konradre explainer/QC; creator editing practice | Narration-led timing, a small pilot, source-based editing, and final-file checks |
| Natural narration | Human recording when available; ElevenLabs or Kokoro/Chatterbox after audition | Delivery and listening review matter more than a voice preset name |
| Clickable/branching video | H5P or a deliberately built web player | Viewer decisions need an interactive delivery layer |

These selections are a fit assessment from the inspected materials. They are not benchmark results.

## Presentations: the closest match to your “full poster” requirement

Your supplied examples establish that each delivered slide should be a complete image with a deliberately composed visual identity. The PDFs include both open compositions and dense illustrated architecture/user-flow panels. Preserve purposeful technical diagrams as part of that identity; avoid automatically turning every paragraph into generic connected text boxes. The underlying production source can remain editable even when the delivered page is flattened.

[Michael Alley’s tutorial](https://www.craftscicom.org/ae_tutorial.html) starts by writing messages as complete sentences, builds slides around visual evidence, and places secondary detail in notes. That is a useful human communication model for your skill. [Duarte’s documented process](https://www.duarte.com/approach/case-studies/reimagining-event-presentations-to-tell-a-visionary-story/) connects discovery, narrative, a visual toolkit, presenter collaboration, and production review.

[Frontend Slides](https://github.com/zarazhangrui/frontend-slides/blob/main/SKILL.md) adds a practical way to choose aesthetics: three slide previews using the actual content. It distinguishes speaker-led and reading-first presentations and checks the fixed slide stage for clipping and overlap. [JetBrains’ slides skill](https://github.com/JetBrains/skills/blob/main/slides/SKILL.md) contributes editable native objects, render/montage tools, overflow checks, and font-substitution inspection. [dachent’s rubric](https://github.com/dachent/skills/blob/main/pptx-win/references/visual-qa-rubric.md) prioritizes blockers, then hierarchy/density, then polish; it advises reducing density before shrinking text.

There are two useful image approaches. [Baoyu’s deck skill](https://github.com/JimLiu/baoyu-skills/blob/main/skills/baoyu-slide-deck/SKILL.md) generates complete slide images from saved prompts and explicitly targets reading/sharing. [K-Dense’s scientific-slide skill](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-slides/SKILL.md) distinguishes conceptual image slides from exact results: preserve original quantitative figures, and use editable text/PowerPoint or Beamer where fidelity matters. Its PowerPoint branch generates visuals and places text separately.

**Proposed rules for your presentation skill — my synthesis:**

1. Extract the argument and verify claims before choosing layouts.
2. Decide whether this is a spoken presentation, a reading deck, or a physical poster.
3. Show two or three materially different real-content visual directions when direction is open.
4. Give each slide one primary takeaway and a clear focal point.
5. Choose imagery by meaning: a real screenshot for a product claim, photography for context, illustration for a concept, or a verified chart for a quantitative result.
6. Use a relationship diagram only when the relationship is what the audience needs to understand. Do not automatically translate every paragraph into boxes and arrows.
7. Keep verified copy, figures, data, and production source separately. Provide native editable objects as an alternate output when requested; package the approved visual as a complete slide image by default.
8. Generate illustration separately from exact slide text when possible. Inspect any text inside generated images manually.
9. Vary composition while preserving typography, palette, crop treatment, spacing, and annotation style.
10. Move excess explanation into speaker notes, additional slides, or an appendix.
11. Render every final slide; inspect individual slides and the contact sheet for both local defects and deck rhythm.
12. Deliver the complete slide images and image-based PDF/PPTX requested, with source/transcript or alternate editable versions where needed.

Suggested failure checks: missing evidence; fake data; unreadable labels; malformed charts; clipped text; accidental overlap; inconsistent type; distorted crops; repeated filler icons; missing notes; and an export that looks materially different from the reviewed source.

**Illustrative composition:** for a slide about a product launch, use a prominent product image/screenshot, a sentence stating the user benefit, and one verified supporting fact. An architecture diagram belongs on a separate explanation of how the system works. This is a proposed design treatment, not an example taken from an upstream deck.

## Posters, PDF reports, and Word documents

Posters need their own workflow. [MIT Communication Lab’s critique of #betterposter](https://mitcommlab.mit.edu/be/2023/09/27/toward-an-evenbetterposter-improving-the-betterposter-template/) supports a large, understandable main message but warns against giving it so much space that evidence becomes tiny. It recommends adapting rough layouts to audience, context, and content. [MIT-BECL’s resources](https://github.com/MIT-BECL/Poster_Resources) include annotated examples and PowerPoint/Illustrator templates.

For an actual printed poster, use final physical dimensions and effective image resolution, not just on-screen appearance. [K-Dense’s PPTX poster skill](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/pptx-posters/SKILL.md) checks physical geometry, placed-image DPI, fonts, provenance, accessibility review, and print/export proof. Its specialized scientific sign-off process is broader than an ordinary creative-poster task needs.

[Anthropic’s canvas-design skill](https://github.com/anthropics/skills/blob/main/skills/canvas-design/SKILL.md) is an additional static-art reference: state an aesthetic direction, then express it through form, color, composition, and sparse typography in a PNG/PDF. Its emphasis fits a highly visual poster, but its art-object framing and repeated craftsmanship language are not a measurable audit or a suitable universal rule for content-rich reports.

For PDFs, [OpenAI’s PDF skill](https://github.com/openai/skills/blob/main/skills/.curated/pdf/SKILL.md) explicitly separates text extraction from layout fidelity and requires page rendering and inspection. [WeasyPrint](https://github.com/Kozea/WeasyPrint) provides HTML/CSS print rendering; [Typst](https://github.com/typst/typst) provides a typeset source workflow. [pdfme](https://github.com/pdfme/pdfme) is useful for repeatable visual templates. They supply different authoring mechanisms, not different guarantees of editorial taste.

[Butterick’s typography guidance](https://practicaltypography.com/typography-in-ten-minutes.html) begins with body-text quality and its font size, line spacing, and line length. That is a better foundation for a long report than decorating its cover and neglecting the interior.

For Word, [JetBrains’ doc workflow](https://github.com/JetBrains/skills/blob/main/doc/SKILL.md) uses structured edits and a render–inspect loop. [grapeot’s form-editing guidance](https://github.com/grapeot/docx-skill/blob/main/docs/skill.md) highlights a specific failure: replacing underscores with an equal number of characters does not preserve visible width in a proportional font. Its CLI is described as a placeholder, so it is a narrow workflow reference rather than a ready production dependency.

**Proposed document rules — my synthesis:** choose a page grid and hierarchy appropriate to the audience; preserve exact source data and figure captions; use semantic headings/styles; check table widths, repeated headers, page breaks, orphan headings, footnotes, numbering, and cross-references; inspect every rendered page; verify accessible structure separately when required. Keep editable source and the final PDF/DOCX together. For an edited document, compare the affected pages before and after.

Treat scanned PDFs as a separate intake route requiring OCR and verification. [pdfplumber](https://github.com/jsvine/pdfplumber) explicitly works best on machine-generated PDFs; a clean text dump does not establish a faithful reconstruction.

## Website front ends: research, visual decisions, and working code

[Refero’s skill](https://github.com/referodesign/refero_skill/blob/master/skills/refero-design/SKILL.md) has an unusually useful research discipline: choose a primary reference, preserve its signature traits, give supporting references limited roles, and record why decisions were made. Its method discourages averaging several references into a bland compromise. Live library access has a separate account/paid requirement.

[Impeccable’s technical audit](https://github.com/pbakaus/impeccable/blob/main/skill/reference/audit.md) separates measurable implementation checks from aesthetic critique. It examines accessibility, performance, theming, responsive design, and implementation integrity, with severity, location, user impact, and a fix. [Vercel’s review skill](https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md) contributes traceable file/line findings against fetched guidelines. The [actual guideline file](https://github.com/vercel-labs/web-interface-guidelines/blob/main/command.md) covers forms, focus, media, overflowing content, navigation state, localization, and motion; distinguish its house copy/style conventions from standards.

**Proposed front-end rules — my synthesis:** begin with actual subject matter, audience, product facts, and the site’s main action. Research relevant real examples; choose a clear visual direction and asset strategy. Make typography, layout, imagery, and copy express that direction. Build with the existing stack and design system when present. Test real navigation/forms, narrow screens, keyboard focus, image loading, long copy, error states, and reduced motion. Inspect browser screenshots and perform the main user journey.

Avoid invented customers, endorsements, statistics, or screenshots that imply a product feature exists when it does not. Use truthful product evidence. A dramatic hero alone does not make the remaining page considered or usable.

Use [Playwright](https://github.com/microsoft/playwright) for browser interaction/screenshot checks and [axe-core](https://github.com/dequelabs/axe-core) for an automated accessibility supplement. Manual review remains necessary. Exact screenshot matching against a copyrighted reference is not the goal; identify principles and create an original result for the brief.

## App UI: consistent task flows and complete states

[Interface Design](https://github.com/Dammyjay93/interface-design/blob/main/.claude/skills/interface-design/SKILL.md) is specifically scoped to product interfaces. Useful ideas include a deliberate focal point and density, explicit tokens, reuse of primitives, visible component states, and durable design memory. [Impeccable’s product guidance](https://github.com/pbakaus/impeccable/blob/main/skill/reference/operate.md) allows familiar product patterns and restrained typography where those help users work. That context differs from an expressive campaign page.

[React Aria/Stately](https://github.com/adobe/react-spectrum) and [Radix](https://github.com/radix-ui/primitives) can supply established interaction behavior. [UI Skills’ accessibility module](https://github.com/ibelick/ui-skills/blob/main/skills/fixing-accessibility/SKILL.md) prioritizes accessible names, keyboard access, focus/dialogs, semantics, and form errors. [Emil Kowalski’s design-engineering guidance](https://github.com/emilkowalski/skills/blob/main/skills/emil-design-eng/SKILL.md) treats motion as a decision, considers interruption/gesture continuity, and recommends slow-motion and physical-device review.

**Proposed app-UI rules — my synthesis:** design the primary task and navigation before decorating screens. Specify default, selected, focused, disabled, loading, empty, error, and success states where relevant. Make errors identify a recovery action. Keep component vocabulary and tokens consistent across screens. Check long names, missing data, narrow windows, localization, and zoom. For native apps, verify platform conventions, safe areas, larger text, keyboard appearance, and actual gesture behavior.

[Apple’s motion guidance](https://developer.apple.com/design/human-interface-guidelines/motion) emphasizes purposeful, brief feedback and optional motion. [Material’s foundations](https://m3.material.io/foundations/) connect tokens, layout, content, accessibility, and interaction states. Native rules should remain in a platform-specific reference rather than being mixed indiscriminately into web CSS guidance.

## Video: short, precise, visual, and naturally narrated

The closest workflow match is a source-led explainer pipeline. [konradre’s explainer skill](https://github.com/konradre/video-production-skills/blob/main/skills/explainer-video/SKILL.md) uses a fact ledger, spoken anchor phrases, a storyboard, a shared style layer, a styled pilot, and rendered-frame review. It times scenes from measured narration and edits the script rather than forcing the voice speed to fit. Its checks examine readable time, scene joins, frozen/empty imagery, final audio, and declared export properties. These are useful production ideas; the exact visual quotas and numeric thresholds are that repository’s conventions.

[Remotion’s voiceover guide](https://github.com/remotion-dev/skills/blob/main/skills/remotion-best-practices/remotion-markup/voiceover.md) measures audio duration to set composition length. [Maartenlouis’ integration skill](https://github.com/Maartenlouis/elevenlabs-remotion-skill/blob/main/SKILL.md) adds scene regeneration and request stitching. Both are integration methods; neither establishes that the resulting voice sounds natural.

For concrete creator practice, [3Blue1Brown’s README](https://github.com/3b1b/videos) documents previewing and rerunning scene fragments through checkpoints before rendering. [Frame.io’s editing article](https://blog.frame.io/2023/04/05/insider-tips-final-cut-pro-precision-editor/) explains refining J/L cuts, which offset audio and picture cuts. Such techniques can support continuity rather than giving every narration sentence an identical transition.

**Proposed video rules — my synthesis:**

1. Extract source claims, select one clear message, and choose audience, aspect ratio, runtime, language, and delivery format.
2. Rewrite source prose into a spoken script. Remove administrative introductions and repeated explanations.
3. Map each beat to an actual visual action: demonstrate, compare, reveal, zoom, annotate, or show a concrete example.
4. Prefer provided footage/screenshots and meaningful illustration; avoid a slideshow where only headings move.
5. Audition the narrator using the script’s hardest sentence before producing the whole narration.
6. Measure the audio, then build the scene timing and caption timing around it.
7. Produce a brief representative pilot to test pace, legibility, imagery, and voice together.
8. Keep style and narrator consistent; preserve pauses and continuity at sentence joins.
9. Use music and sound effects to support comprehension; verify narration remains clear on the intended devices.
10. Review the full export, captions, transitions, first/last frames, visible text, audio stream, dimensions, runtime, and target-specific loudness.
11. Deliver editable project/source, MP4, caption file/transcript, and source/asset attribution where required.

For your first short-explainer skill, test a **45–90-second planning range** as appropriate to the content, using the supplied 91-second example to guide composition and continuity. This is a starting brief, not an industry rule or a strict cap. Actual narration duration decides how much content belongs. Keep a human recording route available when the speaker’s own voice is the desired result.

### Natural voice requires a listening gate

[ElevenLabs’ current documentation](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices) distinguishes controls by model. Some models use SSML breaks; newer v3/v4 guidance uses audio tags/punctuation instead. Do not copy an older voice script’s controls blindly into a different model. Test names, acronyms, numbers, units, accent, emotional tone, and pause behavior.

[Kokoro](https://github.com/hexgrad/kokoro) and [Chatterbox](https://github.com/resemble-ai/chatterbox) are candidates for a local voice branch. Their published quality claims are not results from this survey. Listen to your intended language and speaking style before choosing. [Fish Speech’s current license](https://github.com/fishaudio/fish-speech/blob/main/LICENSE) needs separate consideration for commercial use.

Proposed acceptance test: listen without looking at the screen; verify the message is understandable, delivery does not sound like a list of unrelated lines, important terms are pronounced correctly, and the voice has no unwanted words, repetition, clipped endings, or jarring joins. Then review audio and picture together. Normalize the final mix to the chosen delivery target; a single loudness setting is not universal across every platform.

### “Interactive video” has two different meanings

An animation can be lively without allowing viewer input. A clickable video needs a web or learning-platform layer. [H5P Interactive Video](https://h5p.org/interactive-video) supports questions, popups, links, bookmarks, and adaptive navigation. A Remotion preview/Studio may be interactive for the editor, while the resulting MP4 is linear.

For learning content, consider H5P. For a product demonstration, a custom web player can combine a video with clickable steps or controls. The skill should identify the intended viewer interaction before selecting a format, and label the MP4 fallback appropriately.

## Audit architecture for your own repository

The following is a proposed original structure, not copied upstream instructions.

| Review pass | Question | Evidence to keep |
|---|---|---|
| Source fidelity | Are claims, figures, names, and units correct? | Source ledger and extracted-content check |
| Audience and message | Can the intended audience understand and act? | Brief, story/flow outline, representative example |
| Visual craft | Does hierarchy, imagery, rhythm, and typography serve this content? | Rendered pages/screens/frames and specific critique |
| Interaction and accessibility | Can people operate/read/listen to the result in the intended environment? | Relevant keyboard/device/state/media checks |
| Technical delivery | Does the final exported artifact open and behave correctly? | Final-file checks and target-viewer inspection |

Use a compact finding format: **severity → location or timecode → observed defect → user impact → proposed fix → recheck result**. Distinguish a confirmed defect, a design judgment, and an unrun check. A reviewer should be able to see what failed. Do not let a high average score hide a blocker.

Examples of blockers: false chart value; unreadable key slide; document clipping; primary app action failing; missing video narration. Major issues include ambiguous flow, distracting visual competition, or poor speech/image synchronization. Minor findings are local polish defects. Use these severities proportionally to the task.

## Rules I would correct or keep contextual

| Discovered rule pattern | Treatment in your repository |
|---|---|
| “Never use Inter/system fonts” versus “default to them” | Font choice depends on brand, readability, and product context. Avoid automatic defaults rather than banning a family everywhere. |
| “No gradients/cards/serifs” | Use as critique prompts. They are legitimate when they serve hierarchy and the brief. |
| “Every slide needs an icon/diagram” | Require meaningful visual communication; do not add decoration to satisfy a quota. |
| “44×44 is the WCAG minimum” | Correct the standard label; keep a separate comfortable-touch house target if desired. |
| “All web PPTX exports are images” | Check the chosen exporter/version; some offer editable reconstruction with limits. |
| “TTS preset sounds human” | Require an audition and final listening review. |
| “A passing geometry check means the slide looks correct” | Font fallback, glyphs, wrapping, and image quality still need rendered review. |
| “More rules/styles/lines means better output” | Require evidence from relevant examples and actual tasks. |
| “Ship only after a universal numeric score” | Use task-specific blockers and observable evidence; avoid artificial certification. |

For the touch-size correction, [WCAG 2.2 AA SC 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) uses 24×24 CSS pixels with defined exceptions; [SC 2.5.5 at AAA](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html) uses 44×44 with its exceptions. Native platform sizing and a design team’s comfort targets are distinct concerns.

[Slidev’s current exporting documentation](https://sli.dev/guide/exporting) distinguishes default image PPTX export from editable reconstruction. Unsupported features remain images, some slides fall back, fonts may substitute, and text can rewrap. Export options should be assessed individually.

## Proposed repository blueprint

```text
creative-skills/
  README.md
  LICENSE
  SOURCES.md
  skills/
    visual-presentations/
      SKILL.md
      references/              # speaker/reading modes, image use, PPTX QA
      scripts/                 # reusable render and integrity checks
      assets/                  # your licensed motifs/templates
    posters-and-infographics/
    editorial-pdf/
    word-documents/
    website-frontends/
    app-interfaces/
    short-explainer-video/
    natural-voiceover/
    interactive-video/
    data-visualization/
  examples/                    # original input, source, final output, QA notes
```

The directory tree shows the intended boundaries. Do not create empty scaffolds for every possible resource. A small skill can be just a precise SKILL.md; add helpers, references, and assets only where they materially improve repeated work. Keep every installed skill self-contained, or document real shared dependencies explicitly.

Your `SOURCES.md` should record source URL, inspected file, pinned upstream commit, imported portion, license, attribution, modifications, and last review date. Link restricted material as research references rather than redistributing it. Do not apply your own repository license to third-party material indiscriminately.

The Office files in [Anthropic’s public repository](https://github.com/anthropics/skills/blob/main/skills/pptx/LICENSE.txt) have specific restrictions including copying, derivatives, and distribution. A public URL is not permission to put those files into your repo. [Remotion’s engine license](https://github.com/remotion-dev/remotion/blob/main/LICENSE.md) is custom, and [3Blue1Brown’s video source](https://github.com/3b1b/videos) has different terms from its animation engine. Treat skills, engines, model weights, fonts, sample content, and visual assets separately.

Start validation with a small portfolio: a visual deck from a document, a designed PDF/report, a multi-state app flow, a short narrated explainer, and a clickable learning example if needed. Compare the final artifacts against your preferences and record concrete corrections. That validates the skills more usefully than a growing instruction list.

## Remaining uncertainty

The survey establishes promising source material and written review practices. It does not establish that any single agent, image model, renderer, or voice provider can consistently meet your quality bar. The next implementation phase should create original skill instructions, reuse only clearly licensed helpers where appropriate, and run representative artifact evaluations. Your preferred visual examples, narration language/accent, installed Office tools, and willingness to use paid voice/image services will guide that phase.


## Complete repository inventory

Each entry is a source finding, not an execution endorsement. Repositories are grouped once by their primary category; the CSV and JSON preserve additional task categories, inspection depth, audit structure, limitations, recommendations, and license notes.

### Presentations

| Repository | What is useful | Limit / disposition |
|---|---|---|
| [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills) | Separate file integrity, content completeness, and rendered visual review; frontend guidance ties design to the subject. | Office skills have restrictive file-level licenses. Their aesthetic rules also differ from product-UI guidance. **Reference only for Office; assess frontend license separately.** |
| [JetBrains/skills](https://github.com/JetBrains/skills/blob/main/slides/SKILL.md) | Editable PPTX plus authoring JS; montage, overflow, and font-substitution helpers; DOCX render loop. | Slides metadata credits OpenAI; this is an adaptation, not an independent original workflow. **Strong technical candidate.** |
| [dachent/skills](https://github.com/dachent/skills/blob/main/pptx-win/references/visual-qa-rubric.md) | Define deck purpose and visual concept; use fewer stronger objects; inspect actual PowerPoint exports. | PowerPoint COM requires a working desktop Office installation; static density checks do not prove text fit. **Strong Windows candidate.** |
| [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides/blob/main/SKILL.md) | Three real-content style previews; distinguish speaker-led from reading-first decks; maintain fixed slide geometry. | HTML-first. Browser delivery and editable PowerPoint have different capabilities. Font bans are house style. **Strong art-direction candidate.** |
| [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer/blob/main/plugins/visual-explainer/SKILL.md) | Figure-led HTML; content-specific SVG, small multiples, tables, charts, and scene-based explanations. | Its technical-diagram emphasis is not the default for your poster-like presentation style. **Optional for technical explanations.** |
| [nexu-io/open-design](https://github.com/nexu-io/open-design/blob/main/skills/pptx-html-fidelity-audit/SKILL.md) | Compare source HTML with exported PPTX shapes and per-run typography. | Geometry misses glyph rendering and font fallback; add screenshot review. **Use focused export-audit ideas.** |
| [slidevjs/slidev](https://sli.dev/guide/exporting) | Browser slides with developer-friendly authoring and several export routes. | Default PPTX export uses slide images. Current docs also offer editable PPTX with per-element rasterization/fallback. **Optional interactive-deck engine.** |
| [marp-team/marp](https://github.com/marp-team/marp) | Markdown plus themes and export tooling provides a reproducible slide source. | Fast authoring does not establish art direction; distinguish tools and output semantics. **Optional simpler-deck engine.** |
| [hakimel/reveal.js](https://github.com/hakimel/reveal.js) | Web presentation framework with examples and authoring documentation. | It is an engine, not an editorial skill or native PPTX design system. **Optional HTML engine.** |
| [gitbrent/PptxGenJS](https://github.com/gitbrent/PptxGenJS) | Create native PowerPoint objects, text, charts, and images from JavaScript. | A library cannot decide whether a visual communicates the point. **Core editable-PPTX dependency.** |
| [touying-typ/touying](https://github.com/touying-typ/touying) | Typst themes, overlays, notes, and presentation source. | More natural for technical/typeset talks than general visual marketing decks. **Optional technical branch.** |
| [andreasKroepelin/polylux](https://github.com/andreasKroepelin/polylux) | Minimal source-driven slides, overlays, templates, and presenter support. | PDF/source editability differs from PowerPoint-object editability. **Optional technical branch.** |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-slides/SKILL.md) | Choose image slides for concepts; preserve original quantitative figures; use separate text for editable PPTX; poster guidance checks physical output. | Scientific workflow includes rigorous approval/security gates that should not become universal creative defaults. **Strong specialized reference.** |
| [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills/blob/main/skills/baoyu-slide-deck/SKILL.md) | Outline and style instructions before individual slide images; infographic layout and style are separate choices. | Slide-deck skill targets reading/sharing; full-slide images limit editable text and require accuracy checks. **Strong optional illustrated branch.** |

### Posters

| Repository | What is useful | Limit / disposition |
|---|---|---|
| [MIT-BECL/Poster_Resources](https://github.com/MIT-BECL/Poster_Resources) | Named contributors; PowerPoint/Illustrator templates, annotated examples, and master-slide guidance. | Scientific posters are not equivalent to short speaker-led slides; main/templates licenses differ. **Strong human example source.** |

### PDF

| Repository | What is useful | Limit / disposition |
|---|---|---|
| [openai/skills](https://github.com/openai/skills/blob/main/skills/.curated/pdf/SKILL.md) | PDF workflow distinguishes extraction from layout review; historical slides source contains rendering and layout helpers. | Current slides/doc raw paths returned 404; historical slides were inspected at a specific commit. **Use current PDF; historical slides are a reference.** |
| [typst/typst](https://github.com/typst/typst) | Structured, reproducible typesetting with font discovery and source-based compilation. | Layout quality and source accuracy still require editorial decisions. **Strong PDF engine option.** |
| [quarto-dev/quarto-cli](https://github.com/quarto-dev/quarto-cli) | Scientific/technical publishing across documents and presentations. | Its defaults do not ensure a distinctive visual report. **Optional technical publishing branch.** |
| [Kozea/WeasyPrint](https://github.com/Kozea/WeasyPrint) | Create print-oriented PDFs from HTML/CSS. | It is a print renderer, not a browser-app or creative-planning skill. **Strong editorial PDF engine.** |
| [pymupdf/PyMuPDF](https://github.com/pymupdf/PyMuPDF) | Read/manipulate/render PDFs; useful as an inspection or extraction component. | README presents AGPL/commercial licensing options; do not assume permissive vendoring. **Optional dependency after license selection.** |
| [jsvine/pdfplumber](https://github.com/jsvine/pdfplumber) | Character/geometry inspection, table extraction, and visual debugging. | Works best on machine-generated PDFs; extraction is not OCR or proof of faithful layout. **Strong source-inspection dependency.** |
| [pdfme/pdfme](https://github.com/pdfme/pdfme) | Visual template editor, JSON templates, browser/Node generation, and CLI validation. | Good for repeatable structured PDFs; narrative editing and art direction are separate. **Optional repeatable-template branch.** |

### Documents

| Repository | What is useful | Limit / disposition |
|---|---|---|
| [grapeot/docx-skill](https://github.com/grapeot/docx-skill/blob/main/docs/skill.md) | Inspect paragraphs/runs and compare rendered before/after; equal character counts do not preserve visual width. | The file explicitly describes a scaffold and placeholder CLI. It is not a finished general Word editor. **Use narrow lessons; do not depend on placeholder CLI.** |
| [python-openxml/python-docx](https://github.com/python-openxml/python-docx) | Create and update Word document structures. | It does not provide Word layout rendering or a complete editorial workflow. **Core Word dependency.** |

### Frontend

| Repository | What is useful | Limit / disposition |
|---|---|---|
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable/blob/main/skill/reference/audit.md) | Separate technical audit, design critique, product context, and final polish; product mode prioritizes familiar task behavior. | A self-scored 20-point result is not accessibility certification; arbitrary visual bans are contextual. **Strong critique/audit backbone.** |
| [ibelick/ui-skills](https://github.com/ibelick/ui-skills/blob/main/skills/fixing-accessibility/SKILL.md) | Baseline UI, accessibility, and motion-performance skills; empty states should offer a next action. | Strict Tailwind/font/motion preferences should remain stack/context-specific. **Strong focused audit modules.** |
| [emilkowalski/skills](https://github.com/emilkowalski/skills/blob/main/skills/emil-design-eng/SKILL.md) | Decide whether motion is needed; retain gesture continuity; origin-aware popovers; review in slow motion/on devices. | Some absolute performance/motion statements are simplifications; verify target engine and product use. **Strong motion/craft reference.** |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/ui-ux-pro-max/SKILL.md) | Detect actual stack; generate and persist a design system; page overrides; prioritize interaction and accessibility. | Large preset coverage is not evidence that a specific output is good. Avoid unexamined preset selection. **Useful searchable reference layer.** |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md) | Web review fetches current guidelines and reports file/line findings; React guidance targets performance and composition. | Guideline pointers can change; this is not a complete art-direction system. **Strong implementation review supplement.** |
| [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines/blob/main/command.md) | Concrete checks for forms, focus, media, content overflow, navigation state, motion, localization, and copy. | Contains Vercel house conventions alongside accessibility advice; universalize only source-verified requirements. **Strong detailed implementation checklist.** |
| [referodesign/refero_skill](https://github.com/referodesign/refero_skill/blob/master/skills/refero-design/SKILL.md) | Lock one primary reference; assign supporting references bounded roles; record evidence for design decisions. | Live reference library requires account/paid access; do not copy screenshots as your product assets. **Strong research method.** |
| [yuwen-lu/unslop-ui](https://github.com/yuwen-lu/unslop-ui/blob/main/SKILL.md) | Restraint in color, icons, containers, gradients, and animation. | Explicitly accepts Inter/system fonts while other sources ban them; use as critique prompts, not global bans. **Small optional critique module.** |
| [iuliandita/skills](https://github.com/iuliandita/skills/blob/main/skills/frontend-design/SKILL.md) | Rendered verification, real UI states, and honest reporting of unrun checks; shared evidence-oriented audit format. | Collection evaluation scores describe specific runs and are not a general quality guarantee. **Useful reporting/maintenance reference.** |
| [AkyRayy/Frontend-Design-SKILLS-for-AI](https://github.com/AkyRayy/Frontend-Design-SKILLS-for-AI/blob/main/SKILL.md) | Task-specific identity, editorial/UI patterns, typography, imagery, anti-patterns, and pre-ship checklist. | Length and stylistic richness do not establish actual production quality; some preview assets are SVG compositions. **Optional deeper design reference.** |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | Reusable components and examples for product implementation. | Using default components alone can create a recognizable template look. **Optional implementation primitive.** |
| [radix-ui/primitives](https://github.com/radix-ui/primitives) | Headless low-level UI components; customize styling around established behaviors. | Primitives do not make the final composed app automatically accessible. **Strong behavior primitive.** |
| [tailwindlabs/headlessui](https://github.com/tailwindlabs/headlessui) | Unstyled components aimed at accessible interfaces. | Stack fit and final design still need judgment. **Optional behavior primitive.** |
| [adobe/react-spectrum](https://github.com/adobe/react-spectrum) | React Aria/Stately separate behavior and state from visual design; multi-input and internationalization support. | Choose React Aria for custom identity; Spectrum carries Adobe visual conventions. **Strong accessible behavior option.** |
| [storybookjs/storybook](https://github.com/storybookjs/storybook) | Develop and document component states in isolation. | Screenshots of components alone do not prove a usable complete journey. **Strong state-review dependency.** |
| [microsoft/playwright](https://github.com/microsoft/playwright) | Real browser engines support interaction, screenshot, and cross-browser checks. | Viewport emulation alone does not prove physical touch or assistive-technology behavior. **Core browser-verification dependency.** |
| [dequelabs/axe-core](https://github.com/dequelabs/axe-core) | Automated rules for HTML accessibility and multiple WCAG versions/levels. | Automated results do not cover every accessibility issue. **Core automated-a11y supplement.** |

### App UI

| Repository | What is useful | Limit / disposition |
|---|---|---|
| [Dammyjay93/interface-design](https://github.com/Dammyjay93/interface-design/blob/main/.claude/skills/interface-design/SKILL.md) | One focal point, intentional density and tokens, existing primitives, visible state previews, persistent design memory. | Explicitly excludes marketing sites. Some standards shorthand needs correction before reuse. **Strong app-UI backbone.** |

### Video

| Repository | What is useful | Limit / disposition |
|---|---|---|
| [remotion-dev/skills](https://github.com/remotion-dev/skills/blob/main/skills/remotion-best-practices/remotion-markup/voiceover.md) | Creation, markup, audio, captions, preview, render, and multimedia guidance; duration can follow measured narration. | Current router prefers preview unless export is explicit; Studio editing interactivity is not viewer interaction. **Strong video implementation backbone.** |
| [remotion-dev/remotion](https://github.com/remotion-dev/remotion/blob/main/LICENSE.md) | Programmatic videos and browser preview/player infrastructure. | Custom engine license; do not describe all uses as unconditionally free. **Core candidate after license fit.** |
| [konradre/video-production-skills](https://github.com/konradre/video-production-skills/blob/main/skills/explainer-video/SKILL.md) | Source facts, narration anchors, storyboard, shared style layer, pilot, frame inspection, final-file checks. | Bash/WSL/render-host assumptions and numerous dependencies; metrics do not prove taste. **Strong editorial/QC ideas; adapt selectively.** |
| [Serennity007/awesome-video-creation](https://github.com/Serennity007/awesome-video-creation/blob/main/skills/audio/voiceover-production.md) | Script, storyboard, filming, edit, voiceover, and publishing templates. | Claims of proven workflows were not independently validated; prices/advice can age. **Supplementary checklist reference.** |
| [Maartenlouis/elevenlabs-remotion-skill](https://github.com/Maartenlouis/elevenlabs-remotion-skill/blob/main/SKILL.md) | Narrator presets, scene regeneration, request stitching, and audio-duration metadata. | A preset labeled natural is not a listening test; API/model compatibility needs checking. **Useful voice integration reference.** |
| [ManimCommunity/manim](https://github.com/ManimCommunity/manim) | Programmatic explanatory/math animation with a maintained community ecosystem. | More suited to mathematical/technical explainers than general live-action storytelling. **Optional technical animation engine.** |
| [Zulko/moviepy](https://github.com/Zulko/moviepy) | Python-based compositing and editing automation. | It supplies editing mechanics, not writing, direction, or natural narration. **Optional batch-editing engine.** |
| [hexgrad/kokoro](https://github.com/hexgrad/kokoro) | Compact local narration candidate with published voices and examples. | Author quality comparisons are claims; no blind listening evaluation was run here. **Strong local voice candidate.** |
| [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech/blob/main/LICENSE) | Alternative speech-generation system with multilingual/expressive focus. | Current Fish Audio Research License distinguishes research/noncommercial and commercial uses. **Optional after license and audio evaluation.** |
| [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox) | Voice-generation family with multilingual and expressive narration options. | Model/vendor quality claims are not comparative results from this research. **Useful local voice candidate.** |
| [3b1b/videos](https://github.com/3b1b/videos) | Published 3Blue1Brown scene source and documented checkpoint-based interactive iteration. | Uses the 3b1b Manim variant; video source/content is CC BY-NC-SA, unlike the MIT engine. **Strong human workflow reference.** |
| [3b1b/manim](https://github.com/3b1b/manim) | Precise explanatory animation and interactive workflow used by 3Blue1Brown. | Different APIs/workflow from Manim Community; avoid mixing their instructions. **Optional creator-workflow engine.** |

### Interactive video

| Repository | What is useful | Limit / disposition |
|---|---|---|
| [H5P/h5p-interactive-video](https://h5p.org/interactive-video) | Add questions, popups, links, bookmarks, and adaptive video navigation. | Requires a web/LMS delivery layer; the MP4 alone does not carry these interactions. **Strong truly-interactive option.** |

### Data visualization

| Repository | What is useful | Limit / disposition |
|---|---|---|
| [d3/d3](https://github.com/d3/d3) | Custom data-driven SVG/HTML visualizations and interaction. | Custom chart flexibility adds engineering cost; not an art-direction skill. **Optional advanced chart layer.** |
| [observablehq/plot](https://github.com/observablehq/plot) | Declarative charts and exploratory visualization. | A chart engine cannot decide which evidence your story needs. **Strong simpler chart option.** |

### Discovery

| Repository | What is useful | Limit / disposition |
|---|---|---|
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | Large cross-domain index for finding upstream skills. | A listing is not evidence of quality, originality, or safe execution. **Discovery only.** |

## License observations for reuse

These are observed notices, not a file-by-file clearance of every repository. Preserve attribution and inspect the exact pinned files and bundled assets before importing them.

| Repository | Observed status / next check |
|---|---|
| [anthropics/skills](https://github.com/anthropics/skills) | Mixed; pptx/docx/pdf LICENSE.txt imposes restrictions; frontend-design Apache-2.0 license file inspected |
| [openai/skills](https://github.com/openai/skills) | PDF Apache-2.0 license file; inspect other skills individually |
| [JetBrains/skills](https://github.com/JetBrains/skills) | Slides frontmatter declares Apache-2.0; inspect bundled file notices |
| [dachent/skills](https://github.com/dachent/skills) | MIT repository metadata |
| [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | MIT repository metadata |
| [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | MIT |
| [nexu-io/open-design](https://github.com/nexu-io/open-design) | Apache-2.0 repository metadata; check individual assets |
| [slidevjs/slidev](https://github.com/slidevjs/slidev) | MIT repository metadata |
| [marp-team/marp](https://github.com/marp-team/marp) | MIT repository metadata |
| [hakimel/reveal.js](https://github.com/hakimel/reveal.js) | MIT repository metadata |
| [gitbrent/PptxGenJS](https://github.com/gitbrent/PptxGenJS) | MIT repository metadata |
| [touying-typ/touying](https://github.com/touying-typ/touying) | MIT repository metadata |
| [andreasKroepelin/polylux](https://github.com/andreasKroepelin/polylux) | MIT repository metadata |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | MIT LICENSE.md inspected; check dependencies/assets separately |
| [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | MIT LICENSE inspected |
| [MIT-BECL/Poster_Resources](https://github.com/MIT-BECL/Poster_Resources) | Separate License-main and License-Templates; verify each |
| [typst/typst](https://github.com/typst/typst) | Apache-2.0 repository metadata |
| [quarto-dev/quarto-cli](https://github.com/quarto-dev/quarto-cli) | GitHub metadata NOASSERTION; inspect LICENSE and dependencies |
| [grapeot/docx-skill](https://github.com/grapeot/docx-skill) | License not established in inspected paths |
| [Kozea/WeasyPrint](https://github.com/Kozea/WeasyPrint) | BSD-3-Clause repository metadata |
| [python-openxml/python-docx](https://github.com/python-openxml/python-docx) | MIT repository metadata |
| [pymupdf/PyMuPDF](https://github.com/pymupdf/PyMuPDF) | AGPL-3.0 metadata; README describes commercial option |
| [jsvine/pdfplumber](https://github.com/jsvine/pdfplumber) | MIT repository metadata |
| [pdfme/pdfme](https://github.com/pdfme/pdfme) | MIT repository metadata and README |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Apache-2.0 repository metadata |
| [Dammyjay93/interface-design](https://github.com/Dammyjay93/interface-design) | MIT repository metadata |
| [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | MIT repository metadata |
| [emilkowalski/skills](https://github.com/emilkowalski/skills) | MIT LICENSE inspected; old /skill URL redirects |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | MIT LICENSE inspected |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | Root LICENSE path not found; verify notices before copying |
| [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) | Not cleared; inspect exact file/repository license |
| [referodesign/refero_skill](https://github.com/referodesign/refero_skill) | MIT LICENSE inspected; library content has separate access/rights |
| [yuwen-lu/unslop-ui](https://github.com/yuwen-lu/unslop-ui) | MIT LICENSE inspected |
| [iuliandita/skills](https://github.com/iuliandita/skills) | MIT LICENSE inspected |
| [AkyRayy/Frontend-Design-SKILLS-for-AI](https://github.com/AkyRayy/Frontend-Design-SKILLS-for-AI) | MIT LICENSE inspected |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | README states MIT |
| [radix-ui/primitives](https://github.com/radix-ui/primitives) | README states MIT |
| [tailwindlabs/headlessui](https://github.com/tailwindlabs/headlessui) | README states MIT |
| [adobe/react-spectrum](https://github.com/adobe/react-spectrum) | Repository page identifies Apache-2.0 |
| [storybookjs/storybook](https://github.com/storybookjs/storybook) | Verify package/file notices before copying |
| [microsoft/playwright](https://github.com/microsoft/playwright) | Verify package/file license before vendoring |
| [dequelabs/axe-core](https://github.com/dequelabs/axe-core) | Verify LICENSE and rules/package notices |
| [remotion-dev/skills](https://github.com/remotion-dev/skills) | No license file established in inspected paths; engine has separate terms |
| [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | Custom Remotion License |
| [konradre/video-production-skills](https://github.com/konradre/video-production-skills) | MIT LICENSE inspected; external software/services separate |
| [Serennity007/awesome-video-creation](https://github.com/Serennity007/awesome-video-creation) | MIT LICENSE inspected |
| [Maartenlouis/elevenlabs-remotion-skill](https://github.com/Maartenlouis/elevenlabs-remotion-skill) | MIT LICENSE inspected |
| [ManimCommunity/manim](https://github.com/ManimCommunity/manim) | Verify current LICENSE; separate from 3b1b video assets |
| [Zulko/moviepy](https://github.com/Zulko/moviepy) | README states MIT |
| [hexgrad/kokoro](https://github.com/hexgrad/kokoro) | Apache-2.0 repository license; model card describes Apache weights |
| [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | Custom Fish Audio Research License; commercial use requires separate license |
| [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox) | MIT LICENSE inspected; review model assets separately |
| [H5P/h5p-interactive-video](https://github.com/H5P/h5p-interactive-video) | Verify code/content licenses separately; official demo page has content attribution terms |
| [3b1b/videos](https://github.com/3b1b/videos) | README identifies CC BY-NC-SA 4.0 |
| [3b1b/manim](https://github.com/3b1b/manim) | MIT LICENSE.md inspected |
| [d3/d3](https://github.com/d3/d3) | ISC LICENSE inspected |
| [observablehq/plot](https://github.com/observablehq/plot) | ISC LICENSE inspected |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | Check upstream licenses individually |

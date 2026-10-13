# Optional engines and production routes

The 58-source survey includes tools/components as well as rules. Incorporating a tool means documenting where it can help and its limitations; it does not mean installing all of them or making every AI depend on them.

## Choose from the requested output

| Output | Optional route | Useful condition | Boundary / check |
|---|---|---|---|
| Complete 16:9 poster slides | GPT image generation; local image PDF/PPTX packaging | Default presentation contract | Generate entire poster with GPT; verify copy and evidence; native rounding and export checks are separate |
| Alternate HTML/technical deck | Slidev, reveal.js, Marp, Touying, Polylux | User explicitly wants browser interaction, mathematical typesetting or a different route | Not a silent replacement for GPT posters; inspect exporter/version and exact output semantics |
| Alternate editable PowerPoint | PptxGenJS or a compatible authoring engine | User explicitly requests native objects/editable evidence | Render actual output, check fonts, charts, relationships and editability; not default poster generation |
| Editorial PDF | Typst, WeasyPrint, ReportLab, Quarto | Typeset prose, HTML/CSS print layout, deterministic documents or research publishing | Use appropriate semantic source; inspect pages, tables, pagination, fonts and figures |
| Repeatable structured PDF | pdfme | Stable visual templates and JSON input | Template validation does not prove editorial taste or input truth |
| PDF intake / inspection | pdfplumber, PyMuPDF, pypdf/Poppler or compatible tools | Text/table extraction, geometry, rendering and quick checks | Scans need OCR; extraction is not layout fidelity; PyMuPDF has separate licensing choices |
| Word documents | python-docx, Office-compatible tools, supported OOXML/revision tooling | Structured editing, real styles, existing forms | Preserve runs/sections; render before/after; do not claim revision semantics a route lacks |
| Product UI behavior | React Aria/Stately, Radix, Headless UI, shadcn components | Supported stack and existing patterns | Composition still needs labels, states, focus and actual journey testing |
| UI verification | Browser tools/Playwright, Storybook, axe-core | State stories, real browser interactions, screenshots and automated a11y | Components and automation do not cover all journeys, physical devices or assistive technologies |
| Illustrated/technical motion | Remotion, Manim variants, MoviePy, timeline editors | Reproducible 2D scenes, exact explanatory animation or compositing | Check APIs/variant compatibility; actual narration and playback review required; engine licenses differ |
| Narration | Human recording, hosted TTS, local Kokoro/Chatterbox/Fish Speech where appropriate | Actual language, voice, privacy and license fit | Audition/listen; model controls differ; commercial use/weights may have separate terms |
| Viewer interaction | H5P or custom accessible web player | Questions, hotspots, branches, simulations | MP4 is linear; verify choices, reset/re-entry and keyboard/caption behavior |
| Data visuals | Observable Plot, D3, deterministic plotting tools | Faithful chart encoding and interactive exploration | Verify transforms/denominators/uncertainty; generated imagery is not measured data |

## Match tools to the source

Searchable PDF, scanned/OCR PDF and hybrid visual PDF require distinct intake. Existing Word forms may use paragraphs/tabs/underscores rather than real fields. HTML-to-PPTX conversion needs a discrepancy ledger comparing actual shapes/text/fonts to the reviewed source. Technical fonts and browser effects may substitute or rasterize. An output extension alone does not establish editability or fidelity.

## Decision record

Record requested contract, available tool, why this route fits, dependencies/rights, exact version/doc source where behavior is unstable, and required final inspection. Never silently choose a different provider for GPT posters or a paid route outside authorization. A missing tool can produce an honest handoff; it cannot justify fictitious output.

Relevant source-specific strengths and limitations remain in [the registry](../research/sources.csv) and [all-source coverage](../research/source-coverage.md). Read only the primary documentation needed for the route selected.

# Ordered slide manifest

Paths are relative to the manifest directory. Each image must remain inside that directory tree; absolute paths and traversal outside it are rejected. Do not use remote URLs. A manifest permits any intended slide order; packaging never sorts it behind your back.

```json
{
  "schema_version": 1,
  "title": "Example concept deck",
  "aspect_ratio": "16:9",
  "canvas_color": "#FFFFFF",
  "slides": [
    {
      "id": "cover",
      "image": "slides/01-cover.png",
      "expected_text": ["Exact title", "Exact subtitle"],
      "reviewed": false,
      "review_notes": "Review pending"
    }
  ]
}
```

Required fields: schema_version=1, non-empty title, aspect_ratio=16:9, and non-empty slides. Slide IDs and image paths are unique. Each slide requires expected_text as a list of strings; use an empty list only for an intentionally text-free poster. reviewed must be a Boolean; final packaging requires true. The optional canvas_color is a six-digit hex color used around proportionately contained artwork. Review notes describe the actual inspection.

The helper writes a PDF, PPTX, exact-copy transcript, and packaging-report JSON. Format selection uses `--formats pdf pptx` (the default); PDF-only or PPTX-only is supported. `--output-stem` selects a safe basename. Outputs refuse overwriting unless `--overwrite` is passed. `--allow-unreviewed` produces DRAFT-prefixed outputs and marks the report accordingly.

The packaging report records inspected input dimensions/rounding, output order and generated output filenames. It does not reopen or render the exports. Perform final-file checks separately and record their actual results. A text list or “reviewed: true” is not OCR validation or independent evidence of correctness.

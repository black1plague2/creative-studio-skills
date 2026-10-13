# Final poster and export checks

## Source and visual review

Check each image against its approved copy list and source ledger. Read every letter and numeric label. Verify arrows, stage order, grouping, object continuity and technical topology. Check illustration errors, unintended crop, crowded captions, hierarchy and contrast. Inspect dense content at intended viewing size, not only zoomed in.

Inspect the whole deck as a contact sheet for repeated generic layout, inconsistent characters/palette/strokes, unexplained density changes and narrative rhythm. Fix the specific defect at generation/editing source, then recheck affected images.

## Mechanical helpers

`validate_images.py` checks loadability, dimensions, 16:9 with at most one-pixel native rounding, and optional minimum dimensions. It cannot judge copy or design. `contact_sheet.py` makes a labeled review sheet; labels are separate from final slides. `package_slides.py` uses explicit manifest order and creates exact 16:9 PDF pages and PPTX slides. Each PPTX slide contains one proportionately placed image, no duplicated visible native copy.

Wrong aspect ratio, missing files, duplicate IDs/images, unreviewed manifest entries, and unsafe manifest path traversal fail before packaging. Draft packaging requires `--allow-unreviewed` and uses a DRAFT output prefix. All requested output collisions fail unless `--overwrite` is explicit. No helper uploads content or calls a paid API.

## Review the final files

Reopen the PDF/PPTX and check page/slide count, order, full-frame artwork, proportions and readability. Compare rendered output to the source image. If native generation rounded the dimensions by less than a pixel, the fixed 16:9 container may have a negligible letterbox; that is disclosed rather than fixed by stretching. Obtain an exact-size generation/export if exact PNG dimensions are required.

The transcript and prompt files are useful source/verification records. An image-only PPTX does not provide editable semantic slide text. Provide accessibility alternatives requested by the user and do not claim screen-reader accessibility from visual inspection alone.

## Acceptance record

Record slide ID, file/dimensions, exact-copy result, source/relationship result, design/continuity result, and exported-file recheck. A Boolean in a manifest records a review decision; it does not independently prove the review occurred. Report a missing tool or unrun check honestly.

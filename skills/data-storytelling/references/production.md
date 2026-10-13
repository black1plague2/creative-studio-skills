# Data storytelling: production rules

These rules apply to the selected task and supplied brief. Use judgment for reversible choices; preserve explicit user requirements.

## 1. Inspect source schema, types, units, dates, missingness, duplicates and provenance before plotting

Inspect source schema, types, units, dates, missingness, duplicates and provenance before plotting. Source data is not whatever number best supports the proposed story.

## 2. Name the actual comparison/question

Name the actual comparison/question. A time trend, distribution, ranking, composition and relationship require different encodings. Choose the simplest visual that faithfully answers it.

## 3. Keep calculations reproducible and distinguish counts, percentages, percentage points, rates and totals

Keep calculations reproducible and distinguish counts, percentages, percentage points, rates and totals. Define denominator, aggregation and time window. Check sampled results against source records.

## 4. Preserve uncertainty and limitations where they affect the claim

Preserve uncertainty and limitations where they affect the claim. Do not imply causality from a visual correlation or turn an illustrative simulation into a measured result.

## 5. Use honest scales, visible units and meaningful labels

Use honest scales, visible units and meaningful labels. A truncated axis needs a justified/contextual treatment; pie/area/3D effects must not distort comparisons. Annotate what matters without making the chart unreadable.

## 6. Design color by role and category consistency

Design color by role and category consistency. Do not rely on hue alone for important distinctions. Check label readability at the final page/screen/slide size.

## 7. Use deterministic plotting for final quantitative evidence

Use deterministic plotting for final quantitative evidence. Image generation may explore conceptual layout, but cannot be trusted to preserve exact plotted values or relationships without verification.

## 8. For a GPT poster that must carry an exact chart, explain the conflict and obtain an explicit deterministic-evidence exception or a separately supplied faithful chart

For a GPT poster that must carry an exact chart, explain the conflict and obtain an explicit deterministic-evidence exception or a separately supplied faithful chart. Do not let poster styling redraw the evidence.

## 9. For interactive charts, make filters/tooltips/state changes accessible and show when the denominator or range changes

For interactive charts, make filters/tooltips/state changes accessible and show when the denominator or range changes. Validate every displayed statistic after interaction.

## 10. Deliver chart/data/calculation source, final visuals and concise source notes

Deliver chart/data/calculation source, final visuals and concise source notes. Remove private row-level data from public examples; use clearly labeled synthetic data when demonstrating.

## Research references

These are further reading, not runtime dependencies or a license to copy upstream material. This file is original synthesis.

- [Declarative chart engine](https://github.com/observablehq/plot)
- [Custom chart engine](https://github.com/d3/d3)

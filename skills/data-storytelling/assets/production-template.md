# Editable production packet — faithful visual evidence

Use with [the skill](../SKILL.md). A [domain pack](../../../domains/README.md) is optional when the full repository is available; otherwise fill the domain constraints from the user brief. Domain links in the filled example are optional context, not required dependencies. Data meaning and reproducibility precede style. Do not use a generative image plot as faithful quantitative evidence by default.

## Evidence contract

- Audience/question and decision: [fill].
- Dataset/source/version/access rights: [fill].
- Actual/synthetic/estimated status, units and time period: [fill].
- Sampling/denominator/baseline/missingness/uncertainty: [fill].
- Required calculations and transformations: [fill].
- Allowed claim and conclusions not supported: [fill].
- Requested chart/table/interactive/report formats and actual renderer: [fill].

## Encoding and calculation record

| Field/calculation | Definition/source | Unit/precision | Transformation | Check |
|---|---|---|---|---|
| [fill] | [fill] | [fill] | [fill] | [fill] |

Chart choice and why: [comparison/trend/distribution/relationship]. Axes/baseline/range: [fill]. Labels, caption and uncertainty encoding: [fill]. Color roles: [meaningful categories, accessible differentiation beyond color where needed]. Companion table/source code: [fill]. Interactive state if relevant: [filters/tooltips and denominator change].

## Filled example — SunHarbor synthetic readings

Domain: [sustainability and energy](../../../domains/sustainability-energy.md). Fictional example dataset, not measured solar production:

| Sample day | Energy (kWh) |
|---|---:|
| Monday | 12 |
| Tuesday | 15 |
| Wednesday | 9 |

Checked exercise arithmetic: 12 + 15 + 9 = **36 kWh**. Caption: “Synthetic three-day example; no real production or impact claim.” Encoding: three equally wide vertical bars, energy axis starts at zero, clear day labels, values 12/15/9 on bars, unit kWh. An original deterministic chart and table preserve those quantities. No annual extrapolation, carbon conversion, cost savings or claim of typical performance is supported.

Message: “The sample readings vary by day.” Avoid “Tuesday proves the system is more efficient”: the dataset contains energy amounts only, not input/resource efficiency. A GPT presentation may illustrate this story, but exact data is separately preserved/verified and any deterministic-chart exception is explicit.

## Validation and delivery

Recalculate from source, inspect actual chart scales/labels/category order/rounding, preserve missingness and uncertainty, test interaction if present and compare exported figure to reviewed source. Deliver source table/calculations, chart code where available, figure and truthful narrative.

Actual calculation verification [evidence/pending]; rendered chart inspection [evidence/not run]; uncertainty/source limits [fill]; output checks [fill]. Example arithmetic above is defined exercise math; no chart has been rendered or visually accepted by this template.

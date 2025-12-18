# Effects Table Template

!!! abstract "Structured B-R Data Presentation"

    The Effects Table presents key benefits and risks in a standardized format for direct comparison.

[Download Effects Table Template :material-download:](https://github.com/nexvigilant/nv-BR-toolkit/raw/main/templates/Effects_Table_Template.md){ .md-button .md-button--primary }

---

## What is an Effects Table?

The **Effects Table** is the workhorse of benefit-risk communication:

- Used by EMA in assessment reports
- Increasingly adopted by FDA
- Provides structured, comparable data
- Shows both absolute and relative measures
- Includes confidence intervals for transparency

---

## Table Structure

| Outcome | Importance | Treatment | Comparator | Absolute<br/>Difference | Relative<br/>Measure | 95% CI | Favors |
|---------|------------|-----------|------------|------------------------|---------------------|--------|--------|
| **BENEFITS** | | | | | | | |
| [Endpoint 1] | Critical | ___% | ___% | +___% | RR ___ | [___, ___] | T/C |
| [Endpoint 2] | Important | | | | | | |
| **RISKS** | | | | | | | |
| [Risk 1] | Critical | ___% | ___% | +___% | RR ___ | [___, ___] | T/C |
| [Risk 2] | Important | | | | | | |

---

## Column Guide

| Column | Purpose | Guidance |
|--------|---------|----------|
| **Outcome** | Name of endpoint | Use patient-relevant terms |
| **Importance** | Decision weight | Critical / Important / Moderate / Minor |
| **Treatment** | Result in treatment arm | Include denominator |
| **Comparator** | Result in control arm | Same metric as treatment |
| **Absolute Difference** | Treatment minus Comparator | Consistent sign convention |
| **Relative Measure** | RR, OR, or HR | Specify which measure |
| **95% CI** | Confidence interval | For relative measure |
| **Favors** | Direction of effect | T = Treatment, C = Comparator |

---

## Importance Ratings

| Rating | Definition | Examples |
|--------|------------|----------|
| **Critical** | Primary decision drivers | Mortality, major morbidity, primary efficacy |
| **Important** | Meaningful patient impact | Key secondary endpoints, serious AEs |
| **Moderate** | Contributory outcomes | Symptom measures, moderate AEs |
| **Minor** | Limited decision impact | Mild AEs, laboratory findings |

---

## Metric Selection

| Measure | When to Use | Interpretation |
|---------|-------------|----------------|
| **Relative Risk (RR)** | Common events (>10%) | RR=2 → 2x as likely |
| **Odds Ratio (OR)** | Rare events, case-control | Approximates RR when rare |
| **Hazard Ratio (HR)** | Time-to-event outcomes | Instantaneous risk ratio |
| **NNT/NNH** | Patient communication | Number needed to treat/harm |

---

## NNT/NNH Calculation

```
NNT = 1 / Absolute Risk Reduction
NNH = 1 / Absolute Risk Increase
```

**Example:**
- ACR20: ARR = 27% → NNT = 1/0.27 = **4**
  - *"Treat 4 patients for 1 additional responder"*
- Serious Infection: ARI = 1.4% → NNH = 1/0.014 = **71**
  - *"71 patients treated for 1 additional serious infection"*

---

## Quality Checklist

Before finalizing your Effects Table:

- [ ] All critical outcomes included (benefits AND risks)
- [ ] Consistent timepoints used
- [ ] Both absolute and relative measures provided
- [ ] 95% confidence intervals included
- [ ] Importance ratings applied consistently
- [ ] Same population for all outcomes
- [ ] Outcomes ordered by importance
- [ ] Clear data source identified

---

## Common Mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| Mixing timepoints | Confuses interpretation | Note timepoints clearly |
| Only p-values | Hides effect size | Include estimate + CI |
| Missing CI | Obscures uncertainty | Always include 95% CI |
| Cherry-picking | Bias, regulatory concern | Include all key outcomes |
| Too many outcomes | Overwhelming | Focus on 8-12 most important |

---

## Template Features

The downloadable template includes:

- **Primary Effects Table** — Standard format
- **Extended Effects Table** — With NNT/NNH, timepoints, data source
- **Worked Example** — Anti-inflammatory agent
- **Quality Checklist** — Pre-submission verification
- **Conversion Formulas** — NNT/NNH, RR calculations
- **Excel Implementation Notes** — Formatting and formula guidance

---

## Related Resources

| Resource | Description |
|----------|-------------|
| [BRAD Template](brad.md) | Document structure using Effects Table |
| [Value Tree Template](value-tree.md) | Outcome identification |
| [Module 4: Assessment Templates](../modules/04-assessment-templates.md) | Detailed usage guidance |
| [Module 5: Visualization Tools](../modules/05-visualization-tools.md) | Visualizing Effects Table data |

---

**NexVigilant** | *Empowerment Through Vigilance*

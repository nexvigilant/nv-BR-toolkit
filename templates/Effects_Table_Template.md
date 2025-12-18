# Effects Table Template

**Product:** [Product Name]
**Indication:** [Indication]
**Comparator:** [Comparator]
**Data Cut-off:** [Date]
**Version:** [Version]

---

## EDUCATIONAL USE ONLY

This template is provided for educational purposes as part of the NexVigilant Benefit-Risk Intelligence Toolkit. It should NOT be used for regulatory submissions without appropriate internal review and validation.

---

## Effects Table Structure

The Effects Table presents key benefits and risks in a standardized format that enables:
- Direct comparison between treatment and comparator
- Both absolute and relative measures
- Uncertainty quantification via confidence intervals
- Importance ranking of outcomes

---

## Primary Effects Table

| Outcome | Importance | Treatment<br/>(N=___) | Comparator<br/>(N=___) | Absolute<br/>Difference | Relative<br/>Measure | 95% CI | Favors |
|---------|------------|----------------------|------------------------|------------------------|---------------------|--------|--------|
| **BENEFITS** | | | | | | | |
| [Primary efficacy endpoint] | Critical | ___% | ___% | +___% | RR ___ | [___, ___] | [T/C] |
| [Secondary efficacy 1] | Important | ___% | ___% | +___% | RR ___ | [___, ___] | |
| [Secondary efficacy 2] | Important | | | | | | |
| [Quality of Life] | Important | | | | | | |
| [Patient-reported outcome] | Moderate | | | | | | |
| **RISKS** | | | | | | | |
| [Serious AE 1] | Critical | ___% | ___% | +___% | RR ___ | [___, ___] | [T/C] |
| [Serious AE 2] | Important | ___% | ___% | +___% | RR ___ | [___, ___] | |
| [Common AE 1] | Moderate | ___% | ___% | +___% | RR ___ | [___, ___] | |
| [Common AE 2] | Minor | ___% | ___% | +___% | RR ___ | [___, ___] | |
| [Discontinuation due to AE] | Important | ___% | ___% | +___% | RR ___ | [___, ___] | |

---

## Guidance on Completing the Effects Table

### Column Definitions

| Column | Definition | Guidance |
|--------|------------|----------|
| **Outcome** | Name of benefit or risk endpoint | Use clear, patient-relevant terms where possible |
| **Importance** | Relative importance to decision | Critical / Important / Moderate / Minor |
| **Treatment** | Result in treatment arm | Include absolute value and denominator |
| **Comparator** | Result in comparator arm | Use same metric as treatment |
| **Absolute Difference** | Treatment minus Comparator | Use consistent sign convention (+/- from treatment perspective) |
| **Relative Measure** | Relative risk, odds ratio, or hazard ratio | Specify which measure (RR, OR, HR) |
| **95% CI** | Confidence interval | For relative measure |
| **Favors** | Which arm does result favor? | T = Treatment, C = Comparator, = = Neither |

### Importance Rating Criteria

| Rating | Definition | Examples |
|--------|------------|----------|
| **Critical** | Outcomes that are primary drivers of the B-R decision | Mortality, major morbidity, primary efficacy |
| **Important** | Outcomes with meaningful impact on patients or decision | Key secondary endpoints, serious AEs |
| **Moderate** | Outcomes that contribute but are not decisive | Symptom measures, moderate AEs |
| **Minor** | Outcomes with limited decision impact | Mild AEs, laboratory findings |

### Relative Measure Selection

| Measure | When to Use | Interpretation |
|---------|-------------|----------------|
| **Relative Risk (RR)** | Common events (>10%) | RR=2 means 2x as likely in treatment arm |
| **Odds Ratio (OR)** | Rare events, case-control | Approximates RR when event is rare |
| **Hazard Ratio (HR)** | Time-to-event outcomes | Instantaneous risk ratio |
| **Rate Ratio** | Exposure-adjusted incidence | When exposure time differs |

---

## Extended Effects Table (Optional)

Use this extended format when additional context is needed:

| Outcome | Importance | Treatment | Comparator | Difference | [95% CI] | NNT/NNH | Timepoint | Data Source | Notes |
|---------|------------|-----------|------------|------------|----------|---------|-----------|-------------|-------|
| | | | | | | | | | |

### Additional Columns

| Column | Purpose |
|--------|---------|
| **NNT/NNH** | Number Needed to Treat/Harm for absolute risk interpretation |
| **Timepoint** | When outcome was assessed (e.g., Week 24, Month 12) |
| **Data Source** | Study identifier (e.g., Study 301, pooled Phase 3) |
| **Notes** | Important caveats or context |

---

## Worked Example: Anti-Inflammatory Agent

| Outcome | Importance | Treatment<br/>(N=500) | Placebo<br/>(N=500) | Absolute<br/>Difference | Relative<br/>Measure | 95% CI | Favors |
|---------|------------|----------------------|---------------------|------------------------|---------------------|--------|--------|
| **BENEFITS** | | | | | | | |
| ACR20 Response (W24) | Critical | 62% | 35% | +27% | RR 1.77 | [1.50, 2.10] | T |
| DAS28 Remission (W52) | Important | 28% | 8% | +20% | RR 3.50 | [2.30, 5.30] | T |
| HAQ-DI Improvement | Important | 58% | 32% | +26% | RR 1.81 | [1.52, 2.16] | T |
| Patient Global Assessment | Moderate | -2.1 | -0.8 | -1.3 | SMD -0.45 | [-0.58, -0.32] | T |
| **RISKS** | | | | | | | |
| Serious Infection | Critical | 3.2% | 1.8% | +1.4% | RR 1.78 | [1.10, 2.90] | C |
| Hepatic AE (ALT >3x ULN) | Important | 2.1% | 1.2% | +0.9% | RR 1.75 | [0.90, 3.40] | = |
| Injection Site Reaction | Moderate | 8.4% | 2.1% | +6.3% | RR 4.00 | [2.60, 6.20] | C |
| Any SAE | Important | 8.2% | 6.4% | +1.8% | RR 1.28 | [0.94, 1.74] | = |
| Discontinuation due to AE | Important | 5.6% | 3.8% | +1.8% | RR 1.47 | [0.98, 2.21] | = |

---

## Quality Checklist

Before finalizing your Effects Table, verify:

- [ ] All critical outcomes included (benefits AND risks)
- [ ] Consistent timepoints used (or differences noted)
- [ ] Both absolute and relative measures provided
- [ ] 95% confidence intervals included for all estimates
- [ ] Importance ratings applied consistently
- [ ] Same population/denominator used for all outcomes
- [ ] Outcomes ordered by importance within category
- [ ] Clear data source identified
- [ ] No cherry-picking of favorable outcomes

---

## Common Mistakes to Avoid

| Mistake | Why It's a Problem | Correct Approach |
|---------|-------------------|------------------|
| Mixing timepoints | Confuses interpretation | Note timepoints, use consistent where possible |
| Only p-values | Hides effect size | Always include effect estimate + CI |
| Missing CI | Obscures uncertainty | Include 95% CI for all estimates |
| Excluding unfavorable outcomes | Bias, regulatory concern | Include all pre-specified key outcomes |
| Inconsistent direction | Confusing | Align all measures so "better" is consistent |
| Too many outcomes | Overwhelming | Focus on 8-12 most important outcomes |

---

## Conversion Formulas

### NNT/NNH Calculation

```
NNT = 1 / Absolute Risk Reduction (ARR)
NNH = 1 / Absolute Risk Increase (ARI)

Example:
- ACR20: ARR = 27%, NNT = 1/0.27 = 3.7 ≈ 4
  "Treat 4 patients for 1 additional ACR20 responder"

- Serious Infection: ARI = 1.4%, NNH = 1/0.014 = 71
  "71 patients treated for 1 additional serious infection"
```

### Relative Risk from Absolute Values

```
RR = (Treatment Event Rate) / (Comparator Event Rate)

Example:
- ACR20: RR = 62% / 35% = 1.77
  "Treatment patients are 77% more likely to respond"
```

---

## Excel Implementation Notes

When implementing in Excel:

1. **Formatting**: Use conditional formatting to color-code "Favors" column
2. **Formulas**:
   - Absolute Difference: `=Treatment - Comparator`
   - Relative Risk: `=Treatment / Comparator`
   - NNT: `=1/ABS(Treatment - Comparator)`
3. **Validation**: Use data validation for Importance dropdown
4. **CI Display**: Consider `CONCATENATE` to format CI nicely: `[1.50, 2.10]`

---

## References

- EMA Benefit-Risk Methodology Project Work Package 3
- FDA Benefit-Risk Assessment Framework
- CIOMS Working Group XII Report
- NexVigilant B-R Intelligence Toolkit

---

**NexVigilant** | *Empowerment Through Vigilance*

This template is part of the [Benefit-Risk Intelligence Toolkit](https://github.com/nexvigilant/nv-BR-toolkit).

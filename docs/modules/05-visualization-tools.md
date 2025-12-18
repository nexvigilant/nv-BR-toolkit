# Module 5: Visualization Tools

!!! abstract "Time: 2 hours"

    Master the visual communication of benefit-risk data. Create forest plots, heatmaps, tornado diagrams, and MCDA visualizations that effectively convey complex B-R information to diverse stakeholders.

## Learning Objectives

After completing this module, you will be able to:

- [x] Create forest plots for B-R data presentation
- [x] Build B-R heatmaps for quick visual comparison
- [x] Construct tornado diagrams for sensitivity analysis
- [x] Develop MCDA visualizations with weighted scores
- [x] Select appropriate visualizations for different audiences

## Materials

| File | Description |
|------|-------------|
| `Forest_Plot_Generator.xlsx` | Generate forest plots for B-R data |
| `Heatmap_Builder.xlsx` | Create B-R heatmaps |
| `MCDA_Decision_Model.xlsx` | MCDA visualization tool |
| `Tornado_Plot_Template.xlsx` | Sensitivity analysis tornado diagrams |

---

## Why Visualization Matters

!!! quote "Data Visualization Principle"

    "A picture is worth a thousand data points—but only if it tells the right story."

Effective B-R visualization:

- **Simplifies complexity** — Distills multi-dimensional data
- **Enables comparison** — Treatment vs comparator at a glance
- **Highlights uncertainty** — Communicates confidence intervals
- **Supports decisions** — Provides actionable insights

---

## Visualization 1: Forest Plots

### What is a Forest Plot?

A **Forest Plot** displays effect estimates and confidence intervals for multiple outcomes, enabling visual comparison of benefits and risks.

### Forest Plot Anatomy

```
Outcome              Favors Control  |  Favors Treatment
                                    ●|
Primary Efficacy                         ●━━━━━━━━|
Remission                                    ●━━━━━━━━━━|
Physical Function                         ●━━━━━|
Serious Infection         |━━━━━●
Hepatic Events            |━━●
Injection Site       |━━━●
                     ─────┴─────┴─────┴─────┴─────┴─────
                     0.5   1.0   1.5   2.0   2.5   3.0
                              Relative Risk
```

### Interpreting Forest Plots

| Element | Meaning |
|---------|---------|
| **Point estimate (●)** | Best estimate of effect |
| **Horizontal line (━)** | Confidence interval (uncertainty) |
| **Vertical line (\|)** | Line of no effect (RR=1) |
| **Position relative to line** | Direction of effect |
| **Width of CI** | Precision of estimate |

### Forest Plot Best Practices

!!! success "Effective Forest Plots"

    - **Separate benefits and risks** — Use different colors or sections
    - **Consistent scale** — Log scale for relative measures
    - **Include all outcomes** — Don't cherry-pick favorable results
    - **Show heterogeneity** — Include I² for pooled estimates

!!! danger "Common Mistakes"

    - Mixing absolute and relative measures
    - Inconsistent outcome direction (higher = better vs lower = better)
    - Missing confidence intervals
    - Cluttered with too many outcomes

### Creating a Forest Plot

#### Step 1: Prepare Data

| Outcome | RR | Lower CI | Upper CI | Favors |
|---------|----|---------:|----------|--------|
| ACR20 Response | 1.77 | 1.50 | 2.10 | Treatment |
| Remission | 3.50 | 2.30 | 5.30 | Treatment |
| Serious Infection | 1.78 | 1.10 | 2.90 | Control |
| Hepatic AE | 1.75 | 0.90 | 3.40 | Control |

#### Step 2: Plot Structure

```python
# Conceptual Python code for forest plot
import matplotlib.pyplot as plt

outcomes = ['ACR20', 'Remission', 'Serious Infection', 'Hepatic AE']
rr = [1.77, 3.50, 1.78, 1.75]
ci_low = [1.50, 2.30, 1.10, 0.90]
ci_high = [2.10, 5.30, 2.90, 3.40]
colors = ['green', 'green', 'red', 'red']

# Plot horizontal error bars
plt.errorbar(rr, outcomes, xerr=[rr-ci_low, ci_high-rr],
             fmt='o', color=colors)
plt.axvline(x=1, color='black', linestyle='--')
plt.xlabel('Relative Risk')
```

---

## Visualization 2: B-R Heatmaps

### What is a B-R Heatmap?

A **Heatmap** uses color intensity to represent the magnitude of benefits and risks, enabling quick visual comparison across multiple dimensions.

### Heatmap Structure

```
                   BENEFIT              RISK
                 ┌─────────────┐   ┌─────────────┐
                 │ Low │ High  │   │ Low │ High  │
     ┌───────────┼─────┼───────┼───┼─────┼───────┤
     │ Drug A    │ 🟡  │ 🟢    │   │ 🟢  │ 🟡    │
     │ Drug B    │ 🟢  │ 🟡    │   │ 🟡  │ 🔴    │
     │ Drug C    │ 🟡  │ 🟢    │   │ 🟢  │ 🟢    │
     │ Placebo   │ 🔴  │ 🔴    │   │ 🟢  │ 🟢    │
     └───────────┴─────┴───────┴───┴─────┴───────┘

     🟢 Favorable  🟡 Moderate  🔴 Unfavorable
```

### Heatmap Applications

| Use Case | Row Dimension | Column Dimension |
|----------|---------------|------------------|
| Treatment comparison | Treatments | Outcomes |
| Subgroup analysis | Subgroups | Outcomes |
| Lifecycle tracking | Time periods | Outcomes |
| Multi-indication | Indications | Outcomes |

### Color Coding Conventions

| For Benefits | For Risks |
|--------------|-----------|
| 🟢 Green = High benefit | 🟢 Green = Low risk |
| 🟡 Yellow = Moderate | 🟡 Yellow = Moderate |
| 🔴 Red = Low/No benefit | 🔴 Red = High risk |

!!! warning "Colorblind Accessibility"

    Consider using patterns or shapes alongside colors, or use colorblind-friendly palettes (e.g., viridis).

---

## Visualization 3: Tornado Diagrams

### What is a Tornado Diagram?

A **Tornado Diagram** shows how uncertainty in individual parameters affects the overall result, identifying key drivers of the B-R conclusion.

### Tornado Diagram Anatomy

```
Parameter Impact on Net Benefit Score

                    ← Worse    |    Better →
                               |
Efficacy Estimate    ████████████████|████████████████
Serious Infection        ████████|████████
Time Horizon                 ████|████
Discount Rate                 ███|███
Hepatic AE Risk               ██|██
Injection Site                 █|█
                    ──────────────┼──────────────
                    -0.3  -0.2  -0.1   0   0.1  0.2  0.3
                              Change in Net Benefit
```

### Interpreting Tornado Diagrams

- **Bar length** — Sensitivity of result to parameter uncertainty
- **Bar position** — Direction of impact (left = worse, right = better)
- **Bar order** — Most influential parameters at top
- **Base case** — Vertical line represents central estimate

### Building a Tornado Diagram

#### Step 1: Identify Parameters

| Parameter | Base Case | Low | High |
|-----------|-----------|-----|------|
| Efficacy (ACR20) | 62% | 55% | 69% |
| Serious Infection | 3.2% | 2.1% | 4.3% |
| Time Horizon | 52 weeks | 24 weeks | 104 weeks |
| Discount Rate | 3% | 0% | 6% |

#### Step 2: Calculate Impact

| Parameter | Net Benefit (Low) | Net Benefit (High) | Range |
|-----------|-------------------|--------------------| ------|
| Efficacy | 0.15 | 0.35 | 0.20 |
| Serious Infection | 0.28 | 0.22 | 0.06 |
| Time Horizon | 0.22 | 0.28 | 0.06 |
| Discount Rate | 0.26 | 0.24 | 0.02 |

### When to Use Tornado Diagrams

!!! tip "Tornado Diagram Use Cases"

    - **Regulatory discussions** — Demonstrate robustness of conclusions
    - **Internal decision-making** — Identify data gaps to address
    - **Stakeholder communication** — Explain key uncertainties
    - **Sensitivity analysis** — Document one-way sensitivity results

---

## Visualization 4: MCDA Visualizations

### MCDA Overview

**Multi-Criteria Decision Analysis (MCDA)** combines multiple outcomes with explicit weights to produce an overall score.

### MCDA Visualization Types

#### 1. Weighted Score Bar Chart

```
                    Treatment Score by Criterion

Efficacy        ████████████████████░░░░░░░░░░  Weight: 40%
Safety          ██████████████░░░░░░░░░░░░░░░░  Weight: 30%
Tolerability    ████████████████████████░░░░░░  Weight: 15%
Convenience     ██████████████████████████████  Weight: 15%
                ├────────────────────────────────┤
                0%        50%       100%

Overall Score: 72.5 / 100
```

#### 2. Stacked Value Contribution

```
Treatment Comparison (Weighted Scores)

Drug A:    [====Efficacy====][=Safety=][Tol][Conv]  72.5
Drug B:    [===Efficacy===][==Safety==][Tol][Conv]  68.3
Placebo:   [Eff][====Safety====][=Tol=][==Conv==]   45.2
           ├───────────────────────────────────────┤
           0              50            100
```

#### 3. Radar/Spider Chart

```
                    Efficacy
                       ▲
                       │
                 ●─────●─────●
                /│           │\
               / │           │ \
     Safety   ●  │     ●     │  ●  Tolerability
               \ │           │ /
                \│           │/
                 ●─────●─────●
                       │
                       ▼
                   Convenience

     ── Drug A    ●● Drug B    ○○ Placebo
```

### MCDA Weighting Methods

| Method | Description | Best For |
|--------|-------------|----------|
| **Equal Weights** | All criteria weighted equally | Initial exploration |
| **Expert Elicitation** | Weights from clinical experts | Internal decisions |
| **Swing Weighting** | Based on criterion range importance | Regulatory submissions |
| **Patient Preferences** | Weights from patient studies | Patient-centered decisions |

### MCDA Worked Example

#### Step 1: Define Criteria and Weights

| Criterion | Weight | Rationale |
|-----------|--------|-----------|
| Efficacy | 40% | Primary driver of use |
| Serious Safety | 30% | Critical for acceptance |
| Tolerability | 15% | Impacts adherence |
| Convenience | 15% | Differentiator |

#### Step 2: Score Each Treatment

| Criterion | Drug A | Drug B | Placebo |
|-----------|--------|--------|---------|
| Efficacy | 85 | 70 | 20 |
| Serious Safety | 60 | 75 | 95 |
| Tolerability | 70 | 80 | 90 |
| Convenience | 90 | 50 | 80 |

#### Step 3: Calculate Weighted Scores

**Drug A:** (85×0.40) + (60×0.30) + (70×0.15) + (90×0.15) = **76.0**

**Drug B:** (70×0.40) + (75×0.30) + (80×0.15) + (50×0.15) = **70.0**

**Placebo:** (20×0.40) + (95×0.30) + (90×0.15) + (80×0.15) = **62.0**

---

## Visualization Selection Guide

### Audience-Based Selection

| Audience | Recommended Visualizations |
|----------|---------------------------|
| **Regulators** | Forest plots, Effects tables, Tornado diagrams |
| **HTA Bodies** | MCDA charts, NNT/NNH visualizations |
| **Clinicians** | Forest plots, Heatmaps |
| **Patients** | Icon arrays, Simple bar charts, Infographics |
| **Executives** | Heatmaps, Summary dashboards |

### Purpose-Based Selection

| Purpose | Best Visualization |
|---------|-------------------|
| Compare treatment effects | Forest plot |
| Show overall B-R balance | Stacked bar, Heatmap |
| Explore uncertainty | Tornado diagram |
| Integrate multiple criteria | MCDA spider chart |
| Communicate absolute risk | Icon array, NNT pictogram |

---

## Interactive: Python Visualization

Launch the visualization tutorial in Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nexvigilant/nv-BR-toolkit/blob/main/notebooks/DOOR_Analysis_Tutorial.ipynb)

### Quick Code: Forest Plot

```python
import matplotlib.pyplot as plt
import numpy as np

# Data
outcomes = ['ACR20', 'Remission', 'Ser. Infection', 'Hepatic AE']
rr = np.array([1.77, 3.50, 1.78, 1.75])
ci_low = np.array([1.50, 2.30, 1.10, 0.90])
ci_high = np.array([2.10, 5.30, 2.90, 3.40])
colors = ['#2ecc71', '#2ecc71', '#e74c3c', '#e74c3c']

# Create plot
fig, ax = plt.subplots(figsize=(10, 5))
y_pos = np.arange(len(outcomes))

# Plot error bars
for i, (y, x, lo, hi, c) in enumerate(zip(y_pos, rr, ci_low, ci_high, colors)):
    ax.plot([lo, hi], [y, y], color=c, linewidth=2)
    ax.plot(x, y, 'o', color=c, markersize=10)

# Reference line
ax.axvline(x=1, color='black', linestyle='--', alpha=0.5)

# Labels
ax.set_yticks(y_pos)
ax.set_yticklabels(outcomes)
ax.set_xlabel('Relative Risk (log scale)')
ax.set_xscale('log')
ax.set_title('Benefit-Risk Forest Plot')

plt.tight_layout()
plt.show()
```

---

## Key Takeaways

!!! success "Visualization Principles"

    1. **Match visualization to audience** — Regulators need detail; executives need summary
    2. **Always show uncertainty** — Confidence intervals are not optional
    3. **Maintain consistency** — Same scales, colors, and conventions across figures
    4. **Tell a story** — Visualizations should support the B-R narrative

---

## Further Resources

| Resource | Description |
|----------|-------------|
| [Module 6: Case Studies](06-case-studies.md) | See visualizations in context |
| [DOOR Analysis Tutorial](../interactive/door-analysis.md) | Interactive visualization |
| [Glossary: Forest Plot](../reference/glossary.md#f) | Definition |
| [Glossary: Tornado Diagram](../reference/glossary.md#t) | Definition |

---

!!! warning "Educational Disclaimer"

    This module is provided for **educational purposes only**. Visualization approaches should be validated with your regulatory affairs and statistics teams before use in submissions.

---

[Continue to Module 6: Case Studies →](06-case-studies.md){ .md-button .md-button--primary }

---

**NexVigilant** | *Empowerment Through Vigilance*

# MCDA Walkthrough Tutorial

!!! abstract "Interactive Learning"

    This hands-on Jupyter notebook walks you through Multi-Criteria Decision Analysis (MCDA) step by step.

## Launch the Tutorial

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nexvigilant/nv-BR-toolkit/blob/main/notebooks/MCDA_Walkthrough_Tutorial.ipynb)

---

## What You'll Learn

| Topic | Description |
|-------|-------------|
| **Criteria Definition** | How to identify and structure decision criteria |
| **Swing Weighting** | Systematic approach to elicit stakeholder preferences |
| **Performance Scoring** | Converting raw data to 0-100 scores |
| **Weighted Aggregation** | Calculating composite benefit-risk scores |
| **Sensitivity Analysis** | Testing robustness of conclusions |
| **Visualization** | Creating stakeholder-ready charts |

---

## Prerequisites

- Basic Python knowledge (helpful but not required)
- Understanding of benefit-risk concepts from [Module 2: Foundation](../modules/02-foundation.md)
- Familiarity with effects tables from [Module 4: Assessment Templates](../modules/04-assessment-templates.md)

---

## Tutorial Overview

### Part 1: Framework Setup

Define the decision criteria based on the Value Tree approach:

```python
criteria = {
    'Overall Survival': {'category': 'Benefit', 'direction': 'higher_better'},
    'Progression-Free Survival': {'category': 'Benefit', 'direction': 'higher_better'},
    'Tumor Response': {'category': 'Benefit', 'direction': 'higher_better'},
    'Grade 3-4 AEs': {'category': 'Risk', 'direction': 'lower_better'},
    'Quality of Life': {'category': 'Benefit', 'direction': 'higher_better'}
}
```

### Part 2: Weight Elicitation

Use swing weighting to derive stakeholder preferences:

```python
swing_points = {
    'Overall Survival': 100,           # Anchor - most important
    'Progression-Free Survival': 55,   # 55% as important as OS
    'Tumor Response': 30,              # Surrogate, less weight
    'Grade 3-4 AEs': 70,               # Safety is critical
    'Quality of Life': 45              # Patient-centric
}
```

### Part 3: Scoring and Calculation

Transform clinical data to scores and calculate weighted totals:

| Treatment | Weighted Score | Interpretation |
|-----------|---------------|----------------|
| NEXONC | 74.8 | Preferred option |
| Standard Chemo | 48.3 | Moderate B-R |
| Best Supportive Care | 45.2 | Limited efficacy |

### Part 4: Sensitivity Analysis

Test how conclusions change with different weight scenarios:

- **Efficacy-Focused**: Prioritize survival endpoints
- **Safety-Focused**: Prioritize adverse event avoidance
- **Patient-Centric**: Balance QoL with efficacy

---

## Key Visualizations

The notebook generates several publication-ready visualizations:

1. **Stacked Bar Chart**: Shows contribution of each criterion to total score
2. **Radar/Spider Chart**: Compares treatments across all criteria
3. **Sensitivity Plot**: Shows how total scores change with varying weights
4. **Scenario Comparison**: Side-by-side comparison across weight scenarios

---

## MCDA vs DOOR: When to Use Each

| Factor | MCDA | DOOR |
|--------|------|------|
| **Best for** | Multiple stakeholder perspectives | Composite endpoints with hierarchy |
| **Weights** | Explicit, stakeholder-derived | Implicit in outcome ranking |
| **Output** | Composite score (0-100) | Win ratio, net benefit |
| **Transparency** | High (weights visible) | High (pairwise comparisons) |
| **Complexity** | Moderate-High | Moderate |

!!! tip "Complementary Methods"

    MCDA and DOOR can be used together! DOOR for composite endpoints, MCDA for overall B-R integration.

---

## Related Resources

| Resource | Description |
|----------|-------------|
| [DOOR Analysis Tutorial](door-analysis.md) | Companion DOOR methodology notebook |
| [Module 5: Visualization Tools](../modules/05-visualization-tools.md) | MCDA visualization guidance |
| [Module 6: Case Studies](../modules/06-case-studies.md) | Complete MCDA worked example |
| [MCDA Template](../templates/effects-table.md) | Excel-based MCDA tool |

---

**NexVigilant** | *Empowerment Through Vigilance*

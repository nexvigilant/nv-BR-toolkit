# DOOR Analysis

!!! abstract "Interactive Learning Module"

    **Time:** 45-60 minutes | **Level:** Intermediate | **Prerequisites:** Module 2 Foundation

## What is DOOR?

**DOOR (Desirability of Outcome Ranking)** is a method for analyzing composite endpoints that respects clinical hierarchies. Unlike traditional approaches that assign arbitrary numerical weights, DOOR preserves the clinical judgment that "death is always worse than hospitalization."

### The Core Principle

!!! quote "Fundamental Axiom"

    A patient in a "better" outcome category is **ALWAYS** preferred to a patient in a "worse" category—regardless of any other factors.

This simple principle enables powerful, interpretable analysis without requiring stakeholders to agree on numerical weights.

---

## When to Use DOOR

<div class="grid" markdown>

:material-check-circle:{ .lg .middle } **Ideal Scenarios**
:
    - Composite endpoints with meaningful clinical hierarchy
    - When numerical weights would be controversial or arbitrary
    - When interpretability for non-statisticians is important
    - Regulatory submissions requiring transparent methodology

:material-close-circle:{ .lg .middle } **Not Recommended**
:
    - Continuous outcomes without natural categories
    - When within-category differences matter significantly
    - Very large trials (computationally intensive)
    - When outcomes are truly equivalent in importance

</div>

---

## Interactive Tutorial

### Launch in Google Colab

The complete hands-on tutorial with executable Python code:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nexvigilant/nv-BR-toolkit/blob/main/notebooks/DOOR_Analysis_Tutorial.ipynb)

!!! tip "What You'll Build"

    In this notebook, you will:

    1. **Define** an 8-level outcome hierarchy for a cardiovascular trial
    2. **Generate** simulated trial data (1,000 patients)
    3. **Perform** pairwise comparisons across all patient pairs
    4. **Calculate** win ratio, net benefit, and p-values
    5. **Visualize** outcome distributions with publication-ready charts
    6. **Interpret** results in a benefit-risk context

---

## Case Scenario: Anticoagulant Trial

### Clinical Context

You're analyzing data from a hypothetical Phase III trial comparing a novel anticoagulant (Drug A) to placebo in patients at high risk for thromboembolic events.

**Primary composite endpoint:** Major adverse cardiovascular events (MACE) plus bleeding events

### Step 1: Define the Outcome Hierarchy

The clinical team must first establish the hierarchy. This requires **explicit clinical judgment**:

```python
outcome_hierarchy = [
    "Alive, no CV event, no bleed",           # Rank 1 - Best
    "Alive, no CV event, minor bleed",        # Rank 2
    "Alive, minor CV event, no bleed",        # Rank 3
    "Alive, major CV event recovered",        # Rank 4
    "Alive, no CV event, major bleed",        # Rank 5
    "Alive, major CV event + major bleed",    # Rank 6
    "CV death",                               # Rank 7
    "Non-CV death"                            # Rank 8 - Worst
]
```

!!! question "Discussion Point"

    **Why is "major bleed" ranked worse than "minor CV event"?**

    This reflects the clinical reality that major bleeding events (GI hemorrhage, intracranial bleeding) can be life-threatening and often require intervention. However, this hierarchy could vary based on:

    - Patient population characteristics
    - Specific definitions of "minor" and "major"
    - Stakeholder input (patients may rank events differently than clinicians)

    **Key insight:** The hierarchy itself becomes a documented part of the analysis, making the clinical judgment explicit and auditable.

### Step 2: Pairwise Comparison Logic

DOOR compares **every** treatment patient against **every** control patient:

| Comparison Result | Interpretation |
|-------------------|----------------|
| Treatment rank < Control rank | **Treatment wins** (lower rank = better outcome) |
| Treatment rank > Control rank | **Control wins** |
| Treatment rank = Control rank | **Tie** |

With 500 patients per arm, this means **250,000 pairwise comparisons**.

### Step 3: Key Metrics

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| **Win Ratio** | Treatment wins ÷ Control wins | >1 favors treatment |
| **Net Benefit** | P(trt better) - P(ctrl better) | Range: -1 to +1 |
| **p-value** | Mann-Whitney U test | Statistical significance |

### Example Results

From the simulated tutorial data:

```
Win Ratio:     1.42
Net Benefit:   +11.8%
p-value:       < 0.001
```

**Interpretation:** In 11.8% more pairwise comparisons, the treatment patient had a better outcome than the control patient. The win ratio of 1.42 indicates that for every control "win," treatment achieves 1.42 wins.

---

## Visualization Examples

### Outcome Distribution Chart

The stacked bar chart shows the proportion of patients in each outcome category:

```
Drug A:   [====Green====][Yel][Ora][===Red===]
Placebo:  [==Green==][Yel][=Orange=][====Red====]
```

**Visual pattern:** Treatment arm shows more green (favorable outcomes) and less red (severe outcomes).

### Win Ratio Forest Plot

```
        |
   1.42 |     ●━━━━━━━━━|
        |               |
   1.00 |───────────────|─── (no difference)
        |               |
        |_______________|
```

---

## Quick Reference: Python Implementation

```python
from door_analysis import DOORAnalysis, create_example_data

# Step 1: Load data and define hierarchy
data, hierarchy = create_example_data()

# Step 2: Initialize analyzer
door = DOORAnalysis(outcome_hierarchy=hierarchy)

# Step 3: Assign outcome ranks
data = door.assign_outcomes(data, outcome_column='outcome')

# Step 4: Run comparison
results = door.compare_treatments(
    data,
    treatment_col='treatment',
    treatment_arm='Drug A',
    control_arm='Placebo'
)

# Step 5: Generate report
print(door.generate_report())
```

---

## Key Takeaways

!!! success "What Makes DOOR Powerful"

    1. **Transparency** — Clinical judgments are explicit in the hierarchy
    2. **Interpretability** — Win ratio is intuitive for non-statisticians
    3. **No arbitrary weights** — Ordinal comparison, not numerical scoring
    4. **Stakeholder alignment** — Forces upfront discussion of outcome priorities

!!! warning "Limitations to Consider"

    1. Requires consensus on hierarchy (can be contentious)
    2. Computationally intensive for very large N
    3. Doesn't capture within-category nuance
    4. Sensitivity analysis needed for borderline rankings

---

## Further Learning

| Resource | Description |
|----------|-------------|
| [CIOMS WG XII Report](../reference/cioms-wg-xii.md) | Framework context for DOOR |
| [Module 6: Case Studies](../modules/06-case-studies.md) | Additional worked examples |
| [Effects Tables](../modules/04-assessment-templates.md) | Complementary presentation method |

---

[Launch the Interactive Notebook :material-rocket-launch:](https://colab.research.google.com/github/nexvigilant/nv-BR-toolkit/blob/main/notebooks/DOOR_Analysis_Tutorial.ipynb){ .md-button .md-button--primary }
[Back to Modules](../modules/01-leadership-briefing.md){ .md-button }

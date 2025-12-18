# DOOR Analysis

## What is DOOR?

**DOOR (Desirability of Outcome Ranking)** is a method for analyzing composite endpoints that respects clinical hierarchies.

## Key Principle

> A patient in a "better" category is ALWAYS preferred to a patient in a "worse" category.

## When to Use DOOR

✅ Composite endpoints with meaningful hierarchy
✅ When you don't want arbitrary numerical weights
✅ When interpretability is important

## Quick Start

### Python

```python
from door_analysis import DOORAnalysis, create_example_data

# Create example data
data, hierarchy = create_example_data()

# Run analysis
door = DOORAnalysis(outcome_hierarchy=hierarchy)
data = door.assign_outcomes(data, outcome_column='outcome')
results = door.compare_treatments(data, 'treatment', 'Drug A', 'Placebo')

print(door.generate_report())
```

### Interactive

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nexvigilant/nv-BR-toolkit/blob/main/notebooks/DOOR_Analysis_Tutorial.ipynb)

## Key Metrics

| Metric | Interpretation |
|--------|---------------|
| **Win Ratio** | Treatment wins / Control wins. >1 favors treatment |
| **Net Benefit** | P(trt better) - P(ctrl better). Range: -1 to +1 |
| **p-value** | Statistical significance (Mann-Whitney U) |

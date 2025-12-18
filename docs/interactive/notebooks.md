# Jupyter Notebooks

!!! abstract "Hands-On Learning"

    Interactive notebooks for learning benefit-risk methodologies with Python.

---

## Available Notebooks

| Notebook | Method | Topics |
|----------|--------|--------|
| [DOOR Analysis Tutorial](#door-analysis-tutorial) | DOOR | Outcome hierarchies, pairwise comparisons, win ratios |
| [MCDA Walkthrough](#mcda-walkthrough) | MCDA | Criteria weighting, scoring, sensitivity analysis |

---

## DOOR Analysis Tutorial

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nexvigilant/nv-BR-toolkit/blob/main/notebooks/DOOR_Analysis_Tutorial.ipynb)

**Desirability of Outcome Ranking** for composite endpoints:

- Define outcome hierarchies based on clinical importance
- Perform pairwise comparisons between treatment arms
- Calculate win ratios and net benefit
- Visualize outcome distributions
- Conduct sensitivity analysis on hierarchy

[Learn more about DOOR →](door-analysis.md)

---

## MCDA Walkthrough

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nexvigilant/nv-BR-toolkit/blob/main/notebooks/MCDA_Walkthrough_Tutorial.ipynb)

**Multi-Criteria Decision Analysis** for explicit value integration:

- Define and structure decision criteria
- Apply swing weighting methodology
- Score treatment options on 0-100 scale
- Calculate weighted preference scores
- Perform multi-scenario sensitivity analysis
- Create stakeholder-ready visualizations

[Learn more about MCDA →](mcda-walkthrough.md)

---

## Method Comparison

| Feature | DOOR | MCDA |
|---------|------|------|
| **Best for** | Composite endpoints with hierarchy | Multiple stakeholder perspectives |
| **Weights** | Implicit (in hierarchy) | Explicit (stakeholder-derived) |
| **Output** | Win ratio, net benefit | Composite score (0-100) |
| **Stakeholder input** | Hierarchy validation | Weight elicitation |
| **Sensitivity** | Hierarchy variations | Weight variations |

!!! tip "Complementary Methods"

    DOOR and MCDA can be used together:

    - **DOOR** for composite endpoint analysis
    - **MCDA** for overall benefit-risk integration

---

## Running Locally

### Quick Start

```bash
# Clone the repository
git clone https://github.com/nexvigilant/nv-BR-toolkit.git
cd nv-BR-toolkit

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook notebooks/
```

### Using Google Colab

No installation required! Click the "Open in Colab" badge above to run notebooks directly in your browser.

---

## Requirements

| Package | Version | Purpose |
|---------|---------|---------|
| Python | 3.10+ | Runtime |
| pandas | 2.0+ | Data manipulation |
| numpy | 1.24+ | Numerical operations |
| scipy | 1.10+ | Statistical tests |
| matplotlib | 3.7+ | Visualization |
| Jupyter | 1.0+ | Notebook interface |

---

## Related Resources

| Resource | Description |
|----------|-------------|
| [Module 5: Visualization Tools](../modules/05-visualization-tools.md) | Visualization guidance |
| [Module 6: Case Studies](../modules/06-case-studies.md) | Complete worked examples |
| [Templates](../templates/index.md) | Downloadable assessment templates |

---

**NexVigilant** | *Empowerment Through Vigilance*

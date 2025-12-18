# NexVigilant Benefit-Risk Intelligence Toolkit

[![Educational Use](https://img.shields.io/badge/Use-Educational%20Only-blue.svg)](https://github.com/nexvigilant/nv-BR-toolkit)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![CIOMS WG XII](https://img.shields.io/badge/Based%20On-CIOMS%20WG%20XII-green.svg)](https://cioms.ch)

A comprehensive educational toolkit for learning benefit-risk assessment methodologies in pharmaceutical development and pharmacovigilance.

---

## IMPORTANT DISCLAIMER

> **This toolkit is provided strictly for EDUCATIONAL and INSTRUCTIONAL purposes only.**
>
> - **DO NOT** use this toolkit as a substitute for internal operating procedures
> - **DO NOT** use these materials to inform regulatory decision-making
> - **DO NOT** rely on these templates for actual regulatory submissions
> - **DO NOT** use this code in production environments without proper validation
>
> This toolkit is designed to support learning and understanding of benefit-risk concepts. Any real-world application requires:
> - Validated systems and processes
> - Qualified personnel
> - Appropriate regulatory oversight
> - Organization-specific SOPs and governance
>
> **NexVigilant provides this toolkit "as is" without warranty of any kind. Users assume all risk associated with its use.**

---

## Overview

The Benefit-Risk (B-R) Intelligence Toolkit provides practical resources for understanding modern benefit-risk assessment frameworks, with emphasis on:

- **CIOMS Working Group XII** methodology and recommendations
- **Structured Benefit-Risk Framework (SBRF)** principles
- **Multi-Criteria Decision Analysis (MCDA)** techniques
- **DOOR Analysis** (Desirability of Outcome Ranking)
- **Effects Tables** and **Value Trees** construction
- **Quantitative visualization** methods for B-R communication

## Toolkit Structure

```
nv-BR-toolkit/
├── 01_Leadership_Briefing/          # Executive summary materials
│   └── CIOMS_WG_XII_Executive_Summary.pptx
│
├── 02_Foundation_Module/            # Core concepts and terminology
│   ├── BR_Glossary.docx             # Key B-R terminology
│   ├── Lifecycle_BR_Maturity_Model.docx
│   └── SBRF_Quick_Reference_Guide.docx
│
├── 03_Decision_Support_Module/      # Decision frameworks
│   ├── Patient_Preference_Study_Selector.docx
│   ├── Quantitative_Analysis_Decision_Tree.docx
│   └── RMM_Selection_Framework.docx
│
├── 04_Assessment_Templates/         # Working templates
│   ├── BRAD_Template.docx           # Benefit-Risk Action Document
│   ├── Effects_Table_Template.xlsx
│   └── Value_Tree_Builder.xlsx
│
├── 05_Visualization_Tools/          # Analysis & visualization
│   ├── Forest_Plot_Generator.xlsx
│   ├── Heatmap_Builder.xlsx
│   ├── MCDA_Decision_Model.xlsx
│   └── Tornado_Plot_Template.xlsx
│
├── 06_Case_Study_Workbooks/         # Hands-on learning
│   ├── door_analysis.py             # Python DOOR implementation
│   ├── DOOR_Analysis_Template.xlsx
│   ├── MCDA_Calculation_Walkthrough.xlsx
│   ├── MCDA_Tutorial.docx
│   └── Vaccine_BRA_Worked_Example.docx
│
├── 07_Competency_Assessment/        # Self-assessment tools
│   └── BR_Self_Assessment_Quiz.docx
│
└── 08_Regulatory_Reference/         # Regulatory landscape
    └── Regulatory_Landscape_Comparison.docx
```

## Learning Objectives

After working through this toolkit, learners will be able to:

1. **Describe** the key principles of the CIOMS WG XII benefit-risk framework
2. **Apply** structured B-R assessment methodology to example scenarios
3. **Construct** effects tables and value trees for benefit-risk communication
4. **Calculate** and interpret MCDA-based quantitative B-R assessments
5. **Generate** visualizations (forest plots, tornado diagrams) for B-R data
6. **Perform** DOOR analysis for composite endpoint evaluation
7. **Compare** regulatory approaches to B-R assessment across regions

## Technical Requirements

### Python Code (DOOR Analysis)

The `door_analysis.py` script requires:

```bash
pip install pandas numpy scipy matplotlib
```

**Usage:**
```python
from door_analysis import DOORAnalysis

# Define outcome hierarchy (most to least desirable)
hierarchy = [
    "Alive, no event",
    "Alive, minor event",
    "Alive, major event",
    "Death"
]

# Initialize and run analysis
door = DOORAnalysis(outcome_hierarchy=hierarchy)
data = door.assign_outcomes(patient_data, outcome_column='outcome')
results = door.compare_treatments(data, 'treatment', 'Drug A', 'Placebo')
print(door.generate_report())
```

### Excel Templates

Templates are designed for **Microsoft Excel 2016+** or compatible software. Some advanced features (data validation, conditional formatting) may have limited functionality in other spreadsheet applications.

## Key Methodologies Covered

### CIOMS Working Group XII

The Council for International Organizations of Medical Sciences (CIOMS) Working Group XII published comprehensive guidance on benefit-risk assessment. This toolkit operationalizes key concepts from their report.

### Structured Benefit-Risk Framework (SBRF)

A systematic 6-step process for B-R assessment:
1. Decision context
2. Identify outcomes
3. Identify data sources
4. Assess outcome importance
5. Assess outcome probability
6. Integrate benefit-risk

### Multi-Criteria Decision Analysis (MCDA)

Quantitative methodology that:
- Assigns weights to outcomes based on stakeholder values
- Scores treatments on each outcome
- Calculates weighted aggregate scores
- Enables transparent trade-off analysis

### DOOR Analysis

Composite endpoint analysis that:
- Ranks patient outcomes hierarchically
- Preserves clinical ordering without assuming numerical equivalence
- Uses win ratio and net benefit metrics
- Applies non-parametric statistical testing

## Recommended Learning Path

| Stage | Module | Time Estimate |
|-------|--------|---------------|
| 1 | Leadership Briefing | 30 min |
| 2 | Foundation Module | 2 hours |
| 3 | Decision Support | 1.5 hours |
| 4 | Assessment Templates | 2 hours |
| 5 | Case Study Workbooks | 4 hours |
| 6 | Visualization Tools | 2 hours |
| 7 | Competency Assessment | 30 min |
| 8 | Regulatory Reference | 1 hour |

## Regulatory Context

This toolkit references frameworks from multiple regulatory authorities:

- **FDA** - Benefit-Risk Framework (BRF)
- **EMA** - Benefit-Risk Methodology Project (BRIM)
- **Health Canada** - Notice of Compliance with conditions
- **PMDA** - Risk Management Plan guidance
- **TGA** - Risk Management oversight

**Note:** Regulatory requirements change frequently. Always consult current guidance documents for actual submissions.

## Contributing

We welcome contributions that enhance the educational value of this toolkit:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add educational improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

**Contribution Guidelines:**
- Maintain the educational focus
- Do not add proprietary or confidential content
- Ensure all examples use hypothetical/simulated data
- Include clear learning objectives for new content

## License

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

**You are free to:**
- Share — copy and redistribute the material
- Adapt — remix, transform, and build upon the material

**Under the following terms:**
- **Attribution** — Give appropriate credit to NexVigilant
- **NonCommercial** — Not for commercial purposes
- **ShareAlike** — Distribute contributions under the same license

## Acknowledgments

This toolkit was developed with reference to:

- CIOMS Working Group XII Report
- FDA Benefit-Risk Framework
- EMA Benefit-Risk Methodology Project
- Published literature on MCDA and B-R assessment
- Expert contributions from pharmaceutical industry professionals

## Contact

**NexVigilant**
*Empowerment Through Vigilance*

- Website: [nexvigilant.com](https://www.nexvigilant.com)
- Email: education@nexvigilant.com

---

**Last Updated:** December 2024
**Version:** 1.0

*For questions about this toolkit or NexVigilant's educational offerings, please contact us at the email above.*

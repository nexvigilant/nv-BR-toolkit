# Value Tree Template

**Product:** [Product Name]
**Indication:** [Indication]
**Version:** [Version]
**Date:** [Date]

---

## EDUCATIONAL USE ONLY

This template is provided for educational purposes as part of the NexVigilant Benefit-Risk Intelligence Toolkit. It should NOT be used for regulatory submissions without appropriate internal review and validation.

---

## Purpose of the Value Tree

A **Value Tree** (also called an objectives hierarchy) provides:

1. **Comprehensive identification** of all relevant benefit and risk factors
2. **Hierarchical structure** showing relationships between outcomes
3. **Foundation for MCDA** by defining criteria to be weighted and scored
4. **Stakeholder alignment** through visual consensus-building

---

## Value Tree Construction Principles

| Principle | Definition | Example |
|-----------|------------|---------|
| **Completeness** | All relevant outcomes included | Include efficacy, safety, QoL, convenience |
| **Non-redundancy** | No double-counting | Don't include both "SAEs" and "Hospitalizations" if overlap |
| **Measurability** | Each endpoint can be quantified | Avoid vague concepts like "patient well-being" |
| **Preference Independence** | Preferences on one criterion don't depend on another | Can evaluate "efficacy" independently of "safety" |

---

## Generic Value Tree Structure

```
PRODUCT BENEFIT-RISK ASSESSMENT
│
├── BENEFITS
│   │
│   ├── EFFICACY
│   │   ├── [Primary endpoint]
│   │   ├── [Key secondary endpoint 1]
│   │   ├── [Key secondary endpoint 2]
│   │   └── [Durability of response]
│   │
│   ├── PATIENT-RELEVANT OUTCOMES
│   │   ├── [Symptom improvement]
│   │   ├── [Quality of life]
│   │   ├── [Physical function]
│   │   └── [Patient satisfaction]
│   │
│   └── CONVENIENCE / ADHERENCE
│       ├── [Dosing frequency]
│       ├── [Route of administration]
│       └── [Treatment burden]
│
└── RISKS
    │
    ├── IDENTIFIED RISKS
    │   ├── [Serious adverse event 1]
    │   ├── [Serious adverse event 2]
    │   ├── [Common adverse event 1]
    │   └── [Common adverse event 2]
    │
    ├── POTENTIAL RISKS
    │   ├── [Class effect concern]
    │   ├── [Mechanism-based concern]
    │   └── [Non-clinical signal]
    │
    ├── MISSING INFORMATION
    │   ├── [Long-term safety]
    │   ├── [Special population data]
    │   └── [Drug interaction data]
    │
    └── TOLERABILITY / BURDEN
        ├── [Treatment discontinuation]
        ├── [Quality of life impact]
        └── [Monitoring requirements]
```

---

## Value Tree Worksheet

Use this worksheet to build your Value Tree systematically.

### Step 1: Define Top-Level Categories

| Category | Include? | Rationale |
|----------|----------|-----------|
| **Benefits** | [ ] Yes | |
| **Risks** | [ ] Yes | |
| **Uncertainties** | [ ] Yes / [ ] No | Consider if highlighting unknowns adds value |

### Step 2: Define Benefit Subcategories

| Subcategory | Include? | Specific Outcomes to Include |
|-------------|----------|------------------------------|
| **Efficacy** | [ ] Yes | |
| **Patient-Reported Outcomes** | [ ] Yes / [ ] No | |
| **Quality of Life** | [ ] Yes / [ ] No | |
| **Physical Function** | [ ] Yes / [ ] No | |
| **Survival** | [ ] Yes / [ ] No | |
| **Convenience** | [ ] Yes / [ ] No | |
| **Durability** | [ ] Yes / [ ] No | |

### Step 3: Define Risk Subcategories

| Subcategory | Include? | Specific Outcomes to Include |
|-------------|----------|------------------------------|
| **Identified Risks (Serious)** | [ ] Yes | |
| **Identified Risks (Non-serious)** | [ ] Yes | |
| **Potential Risks** | [ ] Yes / [ ] No | |
| **Missing Information** | [ ] Yes / [ ] No | |
| **Tolerability** | [ ] Yes / [ ] No | |
| **Treatment Burden** | [ ] Yes / [ ] No | |

### Step 4: List Specific Outcomes

#### Benefits

| # | Outcome | Subcategory | Metric | Data Source | Notes |
|---|---------|-------------|--------|-------------|-------|
| B1 | | Efficacy | | | |
| B2 | | Efficacy | | | |
| B3 | | PRO/QoL | | | |
| B4 | | Function | | | |
| B5 | | Convenience | | | |

#### Risks

| # | Outcome | Subcategory | Metric | Data Source | Notes |
|---|---------|-------------|--------|-------------|-------|
| R1 | | Serious AE | | | |
| R2 | | Serious AE | | | |
| R3 | | Common AE | | | |
| R4 | | Common AE | | | |
| R5 | | Tolerability | | | |

---

## Validation Checklist

Before finalizing your Value Tree, validate against these criteria:

### Completeness Check

| Question | Yes/No | Action if No |
|----------|--------|--------------|
| Are all primary endpoints included? | | Add missing endpoints |
| Are key secondary endpoints included? | | Review protocol, add relevant |
| Are all serious risks included? | | Review safety database |
| Are patient-relevant outcomes represented? | | Consider PRO/QoL measures |
| Are regulatory-requested outcomes included? | | Review agency guidance |

### Non-Redundancy Check

| Potential Overlap | Resolution |
|-------------------|------------|
| [Outcome A] vs [Outcome B] | [Keep X, remove Y because...] |
| | |

### Measurability Check

| Outcome | Metric Available? | If No, Alternative |
|---------|-------------------|-------------------|
| | [ ] Yes / [ ] No | |
| | [ ] Yes / [ ] No | |

### Preference Independence Check

| Outcome Pair | Independent? | If No, Resolution |
|--------------|--------------|-------------------|
| [A] and [B] | [ ] Yes / [ ] No | |
| | | |

---

## Therapeutic Area Examples

### Example 1: Rheumatoid Arthritis (Biologic)

```
BIOLOGIC FOR RA
├── BENEFITS
│   ├── Efficacy
│   │   ├── ACR20/50/70 Response
│   │   ├── DAS28 Remission
│   │   └── Radiographic Non-Progression
│   ├── Function
│   │   ├── HAQ-DI Improvement
│   │   └── SF-36 Physical Component
│   └── Convenience
│       └── Dosing Frequency (monthly vs weekly)
│
└── RISKS
    ├── Infections
    │   ├── Serious Infections
    │   ├── Opportunistic Infections
    │   └── Herpes Zoster
    ├── Malignancy
    │   └── Lymphoma
    ├── Other Serious
    │   ├── Cardiovascular Events
    │   └── Hepatotoxicity
    └── Tolerability
        ├── Injection Site Reactions
        └── Infusion Reactions
```

### Example 2: Oncology (Immuno-Oncology)

```
PD-1 INHIBITOR FOR NSCLC
├── BENEFITS
│   ├── Survival
│   │   ├── Overall Survival
│   │   └── Progression-Free Survival
│   ├── Tumor Response
│   │   ├── Objective Response Rate
│   │   └── Duration of Response
│   └── Quality of Life
│       └── Maintained/Improved QoL
│
└── RISKS
    ├── Immune-Related AEs
    │   ├── Pneumonitis
    │   ├── Colitis
    │   ├── Hepatitis
    │   ├── Endocrinopathies
    │   └── Nephritis
    ├── Other Serious
    │   ├── Infusion Reactions
    │   └── Severe Skin Reactions
    └── Tolerability
        ├── Fatigue
        ├── Nausea
        └── Treatment Discontinuation
```

### Example 3: Vaccine

```
VACCINE FOR INFECTIOUS DISEASE
├── BENEFITS
│   ├── Prevention
│   │   ├── Symptomatic Infection
│   │   ├── Severe Disease
│   │   └── Death
│   ├── Immunogenicity
│   │   ├── Seroconversion Rate
│   │   └── Antibody Titers
│   └── Societal
│       └── Reduced Transmission
│
└── RISKS
    ├── Reactogenicity
    │   ├── Local (Injection Site)
    │   └── Systemic (Fever, Fatigue)
    ├── Serious AEs
    │   ├── Anaphylaxis
    │   ├── Myocarditis/Pericarditis
    │   └── Guillain-Barré Syndrome
    └── Missing Information
        ├── Long-term Safety
        └── Durability of Protection
```

---

## Converting Value Tree to MCDA Criteria

Once your Value Tree is complete, select **leaf nodes** as MCDA criteria:

| Value Tree Node | MCDA Criterion? | Weight Assignment Method |
|-----------------|-----------------|-------------------------|
| [Leaf outcome 1] | [ ] Yes | [Swing / DCE / Expert] |
| [Leaf outcome 2] | [ ] Yes | |
| [Leaf outcome 3] | [ ] No (aggregate parent) | |

**Note:** Only include outcomes that can be measured and scored. Aggregate categories (like "Efficacy" or "Safety") are not directly used as MCDA criteria—their leaf nodes are.

---

## Stakeholder Validation

Document stakeholder input on the Value Tree:

| Stakeholder | Role | Feedback | Changes Made |
|-------------|------|----------|--------------|
| [Name] | Clinical Lead | | |
| [Name] | Safety Lead | | |
| [Name] | Regulatory Lead | | |
| [Name] | Patient Representative | | |

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | | | Initial draft |
| 1.0 | | | Final after stakeholder review |

---

## References

- Marsh K, et al. "Multiple Criteria Decision Analysis for Health Care Decision Making" Value Health 2014
- CIOMS Working Group XII Report
- FDA Benefit-Risk Assessment Framework
- EMA Benefit-Risk Methodology Project

---

**NexVigilant** | *Empowerment Through Vigilance*

This template is part of the [Benefit-Risk Intelligence Toolkit](https://github.com/nexvigilant/nv-BR-toolkit).

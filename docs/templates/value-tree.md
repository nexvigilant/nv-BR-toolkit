# Value Tree Template

!!! abstract "Hierarchical Outcome Identification"

    The Value Tree ensures comprehensive, structured identification of all relevant benefit and risk factors.

[Download Value Tree Template :material-download:](https://github.com/nexvigilant/nv-BR-toolkit/raw/main/templates/Value_Tree_Template.md){ .md-button .md-button--primary }

---

## What is a Value Tree?

A **Value Tree** (also called an objectives hierarchy) provides:

- **Comprehensive identification** of all relevant outcomes
- **Hierarchical structure** showing relationships
- **Foundation for MCDA** by defining criteria
- **Stakeholder alignment** through visual consensus

---

## Generic Structure

```
PRODUCT BENEFIT-RISK ASSESSMENT
│
├── BENEFITS
│   ├── EFFICACY
│   │   ├── [Primary endpoint]
│   │   ├── [Secondary endpoint]
│   │   └── [Durability of response]
│   │
│   ├── PATIENT-RELEVANT OUTCOMES
│   │   ├── [Symptom improvement]
│   │   ├── [Quality of life]
│   │   └── [Physical function]
│   │
│   └── CONVENIENCE
│       ├── [Dosing frequency]
│       └── [Route of administration]
│
└── RISKS
    ├── IDENTIFIED RISKS
    │   ├── [Serious AE 1]
    │   ├── [Serious AE 2]
    │   └── [Common AEs]
    │
    ├── POTENTIAL RISKS
    │   └── [Class/mechanism concerns]
    │
    ├── MISSING INFORMATION
    │   └── [Long-term safety]
    │
    └── TOLERABILITY
        └── [Treatment discontinuation]
```

---

## Construction Principles

| Principle | Definition | Check |
|-----------|------------|-------|
| **Completeness** | All relevant outcomes included | Are all endpoints covered? |
| **Non-redundancy** | No double-counting | Any overlapping outcomes? |
| **Measurability** | Each can be quantified | Can we score each outcome? |
| **Preference Independence** | Can evaluate independently | Do preferences on one depend on another? |

---

## Construction Steps

### Step 1: Define Categories

| Category | Include? |
|----------|----------|
| Benefits | Yes |
| Risks | Yes |
| Uncertainties | Consider |

### Step 2: Define Subcategories

**Benefits:**
- Efficacy
- Patient-Reported Outcomes
- Quality of Life
- Convenience

**Risks:**
- Identified Risks (Serious)
- Identified Risks (Non-serious)
- Potential Risks
- Missing Information
- Tolerability

### Step 3: Populate Specific Outcomes

For each subcategory, identify:

- What outcomes are **measured in trials**?
- What outcomes **matter to patients**?
- What outcomes are **requested by regulators**?

### Step 4: Validate with Stakeholders

- Clinical team: All relevant outcomes?
- Regulatory: Agency expectations met?
- Patients: Patient-relevant outcomes represented?

---

## Therapeutic Area Examples

### Rheumatoid Arthritis

```
BIOLOGIC FOR RA
├── BENEFITS
│   ├── Efficacy
│   │   ├── ACR20/50/70 Response
│   │   ├── DAS28 Remission
│   │   └── Radiographic Non-Progression
│   ├── Function
│   │   └── HAQ-DI Improvement
│   └── Convenience
│       └── Dosing Frequency
│
└── RISKS
    ├── Infections
    │   ├── Serious Infections
    │   └── Herpes Zoster
    ├── Malignancy
    │   └── Lymphoma
    └── Tolerability
        └── Injection Site Reactions
```

### Oncology (Immuno-Oncology)

```
PD-1 INHIBITOR FOR NSCLC
├── BENEFITS
│   ├── Survival
│   │   ├── Overall Survival
│   │   └── Progression-Free Survival
│   ├── Tumor Response
│   │   └── Objective Response Rate
│   └── Quality of Life
│       └── Maintained/Improved QoL
│
└── RISKS
    ├── Immune-Related AEs
    │   ├── Pneumonitis
    │   ├── Colitis
    │   └── Endocrinopathies
    └── Tolerability
        └── Treatment Discontinuation
```

### Vaccine

```
VACCINE FOR INFECTIOUS DISEASE
├── BENEFITS
│   ├── Prevention
│   │   ├── Symptomatic Infection
│   │   ├── Severe Disease
│   │   └── Death
│   └── Immunogenicity
│       └── Seroconversion Rate
│
└── RISKS
    ├── Reactogenicity
    │   ├── Local Reactions
    │   └── Systemic Reactions
    ├── Serious AEs
    │   ├── Anaphylaxis
    │   └── Myocarditis
    └── Missing Information
        └── Long-term Safety
```

---

## Converting to MCDA

Select **leaf nodes** (endpoints at the bottom of the tree) as MCDA criteria:

| Value Tree Node | MCDA Criterion? |
|-----------------|-----------------|
| Overall Survival | Yes ✓ |
| Survival (parent) | No (use leaf nodes) |
| Serious Infections | Yes ✓ |

Only include outcomes that can be measured and scored.

---

## Template Features

The downloadable template includes:

- **Generic Structure** — Adaptable framework
- **Step-by-Step Worksheet** — Guided construction
- **Validation Checklist** — Quality verification
- **Therapeutic Area Examples** — RA, Oncology, Vaccine
- **MCDA Conversion Guide** — From Value Tree to weighted criteria
- **Stakeholder Validation Section** — Document input and changes

---

## Related Resources

| Resource | Description |
|----------|-------------|
| [BRAD Template](brad.md) | Document using Value Tree |
| [Effects Table Template](effects-table.md) | Quantify Value Tree outcomes |
| [Module 4: Assessment Templates](../modules/04-assessment-templates.md) | Detailed usage guidance |
| [MCDA Walkthrough](../interactive/mcda-walkthrough.md) | Apply Value Tree in MCDA |

---

**NexVigilant** | *Empowerment Through Vigilance*

# Module 6: Case Studies

!!! abstract "Time: 4 hours"

    Apply everything you've learned through comprehensive worked examples. These case studies demonstrate end-to-end B-R assessment for realistic pharmaceutical scenarios.

## Learning Objectives

After completing this module, you will be able to:

- [x] Apply SBRF to complete B-R assessments
- [x] Conduct DOOR analysis on composite endpoints
- [x] Perform MCDA with explicit weighting
- [x] Communicate B-R conclusions to different audiences

## Materials

| File | Description |
|------|-------------|
| `door_analysis.py` | Python DOOR implementation |
| `DOOR_Analysis_Template.xlsx` | Excel-based DOOR analysis |
| `MCDA_Calculation_Walkthrough.xlsx` | Step-by-step MCDA |
| `MCDA_Tutorial.docx` | MCDA concepts and guidance |
| `Vaccine_BRA_Worked_Example.docx` | Complete vaccine B-R example |

## Interactive Option

Launch the DOOR Analysis tutorial in Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nexvigilant/nv-BR-toolkit/blob/main/notebooks/DOOR_Analysis_Tutorial.ipynb)

---

## Case Study 1: Novel Anticoagulant (DOOR Analysis)

### Clinical Context

**Product:** NEXCOAG (novel Factor Xa inhibitor)
**Indication:** Prevention of stroke in non-valvular atrial fibrillation
**Comparator:** Warfarin (standard of care)
**Trial:** 15,000 patients, 2-year follow-up, event-driven

### Step 1: Define Outcome Hierarchy

The clinical team establishes the hierarchy based on severity and patient impact:

```
OUTCOME HIERARCHY (Most to Least Desirable)
═══════════════════════════════════════════
Rank 1: 🟢 Alive, no stroke, no major bleed
Rank 2: 🟢 Alive, no stroke, minor bleed only
Rank 3: 🟡 Alive, TIA only, no bleed
Rank 4: 🟡 Alive, non-disabling stroke, recovered
Rank 5: 🟠 Alive, major bleed, recovered
Rank 6: 🟠 Alive, disabling stroke
Rank 7: 🔴 Hemorrhagic stroke
Rank 8: 🔴 Ischemic stroke death
Rank 9: 🔴 Major bleed death
Rank 10: 🔴 Other CV death
```

!!! question "Discussion Point"

    **Why is hemorrhagic stroke ranked worse than disabling ischemic stroke?**

    The clinical team determined that hemorrhagic strokes in anticoagulated patients carry higher mortality and worse functional outcomes. However, this ranking could be debated—some might argue disabling stroke has worse long-term impact. This illustrates why **documenting the hierarchy rationale** is essential.

### Step 2: Outcome Distribution

| Outcome | NEXCOAG (n=7,500) | Warfarin (n=7,500) |
|---------|-------------------|-------------------|
| Alive, no event | 6,450 (86.0%) | 6,150 (82.0%) |
| Minor bleed only | 525 (7.0%) | 600 (8.0%) |
| TIA only | 75 (1.0%) | 90 (1.2%) |
| Non-disabling stroke | 120 (1.6%) | 180 (2.4%) |
| Major bleed, recovered | 150 (2.0%) | 225 (3.0%) |
| Disabling stroke | 60 (0.8%) | 90 (1.2%) |
| Hemorrhagic stroke | 30 (0.4%) | 45 (0.6%) |
| Ischemic stroke death | 45 (0.6%) | 75 (1.0%) |
| Major bleed death | 30 (0.4%) | 30 (0.4%) |
| Other CV death | 15 (0.2%) | 15 (0.2%) |

### Step 3: DOOR Analysis Results

```
╔═══════════════════════════════════════════════════════════════╗
║                    DOOR ANALYSIS RESULTS                      ║
╠═══════════════════════════════════════════════════════════════╣
║  Total Pairwise Comparisons:    56,250,000                    ║
║                                                               ║
║  NEXCOAG Wins:                  32,062,500 (57.0%)            ║
║  Warfarin Wins:                 21,937,500 (39.0%)            ║
║  Ties:                           2,250,000 (4.0%)             ║
║                                                               ║
║  ┌─────────────────────────────────────────────────────────┐  ║
║  │  WIN RATIO:     1.46                                    │  ║
║  │  NET BENEFIT:   +18.0%                                  │  ║
║  │  p-value:       < 0.0001                                │  ║
║  └─────────────────────────────────────────────────────────┘  ║
╚═══════════════════════════════════════════════════════════════╝
```

### Step 4: Interpretation

!!! success "DOOR Analysis Conclusion"

    **NEXCOAG demonstrates a favorable benefit-risk profile compared to warfarin:**

    - Win Ratio of 1.46 indicates that in pairwise comparisons, NEXCOAG patients achieve better outcomes 46% more often than warfarin patients
    - Net benefit of +18% means NEXCOAG is favored in 18% more comparisons
    - Results are highly statistically significant (p < 0.0001)

    **Key drivers of advantage:**
    - Fewer disabling strokes
    - Fewer major bleeds
    - More patients remaining event-free

### Step 5: Sensitivity Analysis

| Scenario | Win Ratio | Interpretation |
|----------|-----------|----------------|
| Base case | 1.46 | Robust NEXCOAG advantage |
| Remove minor bleeds | 1.52 | Advantage strengthens |
| Swap Ranks 5-6 | 1.44 | Minimal impact |
| Exclude TIA | 1.45 | Stable result |
| Worst-case hierarchy | 1.38 | Still favors NEXCOAG |

**Conclusion:** Results are robust across plausible alternative hierarchies.

---

## Case Study 2: Oncology Agent (MCDA)

### Clinical Context

**Product:** NEXONC (novel PD-1 inhibitor + chemotherapy)
**Indication:** First-line advanced NSCLC
**Comparator:** Chemotherapy alone
**Trial:** 600 patients, median follow-up 18 months

### Step 1: Define Criteria and Weights

Working with oncologists, patients, and regulators, the team establishes:

| Criterion | Weight | Justification |
|-----------|--------|---------------|
| Overall Survival | 35% | Ultimate efficacy measure |
| Progression-Free Survival | 20% | Clinically meaningful delay |
| Tumor Response | 10% | Surrogate for benefit |
| Serious Adverse Events | 20% | Critical safety |
| Quality of Life | 15% | Patient-centric |
| **Total** | **100%** | |

### Step 2: Evidence Summary (Effects Table)

| Outcome | NEXONC | Chemo | Difference | Rating |
|---------|--------|-------|------------|--------|
| **BENEFITS** | | | | |
| Median OS | 22.0 mo | 14.0 mo | +8.0 mo | +++ |
| 2-year OS | 48% | 28% | +20% | +++ |
| Median PFS | 10.5 mo | 5.5 mo | +5.0 mo | ++ |
| ORR | 52% | 28% | +24% | ++ |
| **RISKS** | | | | |
| Grade 3-4 AEs | 58% | 52% | +6% | - |
| Immune-related AEs | 28% | 2% | +26% | -- |
| Treatment discontinuation | 18% | 12% | +6% | - |
| **QoL** | | | | |
| Maintained/improved | 62% | 48% | +14% | ++ |

### Step 3: Performance Scoring

Convert evidence to 0-100 scores based on clinical relevance:

| Criterion | NEXONC Score | Chemo Score | Scoring Rationale |
|-----------|--------------|-------------|-------------------|
| OS | 85 | 45 | Based on survival curves |
| PFS | 80 | 40 | Based on HR and median |
| Response | 75 | 40 | Based on ORR difference |
| Safety | 55 | 65 | Grade 3-4 + irAEs |
| QoL | 70 | 50 | Based on maintained QoL |

### Step 4: Weighted Score Calculation

```
NEXONC Weighted Score:
═══════════════════════════════════════════════════
OS:       85 × 0.35 = 29.75
PFS:      80 × 0.20 = 16.00
Response: 75 × 0.10 =  7.50
Safety:   55 × 0.20 = 11.00
QoL:      70 × 0.15 = 10.50
─────────────────────────────────
TOTAL:                74.75 / 100
═══════════════════════════════════════════════════

Chemotherapy Weighted Score:
═══════════════════════════════════════════════════
OS:       45 × 0.35 = 15.75
PFS:      40 × 0.20 =  8.00
Response: 40 × 0.10 =  4.00
Safety:   65 × 0.20 = 13.00
QoL:      50 × 0.15 =  7.50
─────────────────────────────────
TOTAL:                48.25 / 100
═══════════════════════════════════════════════════
```

### Step 5: Visualization

```
MCDA Score Comparison
═════════════════════════════════════════════════════════════

NEXONC:     ████████████████████████████████████████░░░░░░  74.8
            │    OS    │  PFS │Resp│  Safety │ QoL │

Chemo:      ████████████████████████░░░░░░░░░░░░░░░░░░░░░░  48.3
            │  OS │ PFS│Resp│ Safety │QoL│

            ├────────────────────────────────────────────────┤
            0              50             100

Difference: +26.5 points in favor of NEXONC
```

### Step 6: Sensitivity Analysis

| Weight Scenario | NEXONC | Chemo | Difference |
|-----------------|--------|-------|------------|
| Base case | 74.8 | 48.3 | +26.5 |
| Safety prioritized (40%) | 68.5 | 52.5 | +16.0 |
| Equal weights | 73.0 | 48.0 | +25.0 |
| Patient-derived weights | 76.2 | 46.8 | +29.4 |

**Conclusion:** NEXONC maintains a favorable B-R balance across all plausible weight scenarios.

---

## Case Study 3: Vaccine (Complete SBRF Assessment)

### Clinical Context

**Product:** NEXVAX (mRNA vaccine for emerging pathogen)
**Indication:** Prevention of infection in adults ≥18 years
**Comparator:** Placebo
**Trial:** 40,000 participants, 6-month efficacy follow-up

### SBRF Step 1: Decision Context

| Element | Value |
|---------|-------|
| **Decision** | Initial EUA/approval for adult population |
| **Population** | Adults ≥18 years, healthy or stable comorbidities |
| **Comparator** | Placebo (no approved vaccine available) |
| **Unmet need** | High (pandemic, significant morbidity/mortality) |
| **Regulatory context** | Emergency Use Authorization pathway |

### SBRF Step 2: Identify Outcomes

**Value Tree:**

```
NEXVAX Benefit-Risk
├── BENEFITS
│   ├── Prevention
│   │   ├── Symptomatic infection
│   │   ├── Severe disease
│   │   └── Death
│   └── Societal
│       ├── Reduced transmission
│       └── Healthcare capacity
│
└── RISKS
    ├── Reactogenicity
    │   ├── Local (injection site)
    │   └── Systemic (fever, fatigue)
    ├── Adverse Events
    │   ├── Allergic reactions
    │   ├── Myocarditis/pericarditis
    │   └── Other serious AEs
    └── Unknown
        └── Long-term effects
```

### SBRF Step 3: Data Sources

| Source | Endpoints | Limitations |
|--------|-----------|-------------|
| Phase 3 RCT | Efficacy, common AEs | Limited follow-up |
| Phase 1/2 trials | Immunogenicity, safety | Small N |
| Platform experience | Class effects | Different antigen |
| Post-auth surveillance | Rare AEs | Reporting bias |

### SBRF Step 4: Outcome Importance

| Outcome | Importance | Rationale |
|---------|------------|-----------|
| Prevention of death | Critical | Most severe outcome |
| Prevention of severe disease | Critical | Primary benefit |
| Prevention of symptomatic infection | Important | Main efficacy endpoint |
| Myocarditis/pericarditis | Critical | Serious safety signal |
| Anaphylaxis | Important | Rare but manageable |
| Reactogenicity | Moderate | Expected, self-limiting |

### SBRF Step 5: Quantify Outcomes

**Effects Table:**

| Outcome | NEXVAX | Placebo | VE/Difference | 95% CI |
|---------|--------|---------|---------------|--------|
| **BENEFITS** | | | | |
| Symptomatic infection | 0.4% | 2.5% | 84% VE | 76-90% |
| Severe disease | 0.02% | 0.3% | 93% VE | 82-98% |
| COVID death | 0.01% | 0.08% | 88% VE | 65-96% |
| **RISKS** | | | | |
| Local reactogenicity | 84% | 19% | +65% | 63-67% |
| Systemic reactogenicity | 62% | 24% | +38% | 36-40% |
| Anaphylaxis | 0.005% | 0% | +0.005% | - |
| Myocarditis (young males) | 0.002% | 0% | +0.002% | - |
| Serious AEs | 0.4% | 0.4% | 0% | -0.1-0.1% |

### SBRF Step 6: Integrate B-R

!!! example "NEXVAX Benefit-Risk Summary"

    **For adults ≥18 years** at risk of pathogen exposure, **NEXVAX** provides:

    **BENEFITS:**
    - 84% reduction in symptomatic infection
    - 93% reduction in severe disease
    - 88% reduction in death
    - Societal benefit through reduced transmission

    **RISKS:**
    - Common reactogenicity (expected, self-limiting)
    - Rare anaphylaxis (~1 in 20,000, manageable with monitoring)
    - Very rare myocarditis (~1 in 50,000, primarily young males, mostly resolved)
    - No signal for other serious AEs above background

    **CONCLUSION:** Benefits substantially outweigh risks for the proposed population. Enhanced monitoring recommended for anaphylaxis (15-30 min observation) and myocarditis (young male awareness).

### Risk Communication Examples

**For Regulators (Technical):**

> "Vaccine efficacy against severe disease was 93.3% (95% CI: 82.4-97.8%), with an NNT of ~300 to prevent one severe case over 6 months. The excess risk of myocarditis in males 18-29 was 1.9 per 100,000 doses (95% CI: 1.2-2.8), with most cases resolving within 7 days."

**For Healthcare Providers:**

> "NEXVAX prevents about 9 out of 10 severe cases. The main side effects are sore arm and feeling tired for a day or two. There's a small risk of heart inflammation in younger men (~1 in 50,000), so counsel patients to seek care if they have chest pain after vaccination."

**For Patients:**

> "This vaccine is very effective at preventing serious illness. Most people feel tired and have a sore arm for a day or two—this means your immune system is working. Serious side effects are rare, and the benefits far outweigh the risks for most people."

---

## Key Takeaways

!!! success "Case Study Lessons"

    1. **DOOR** excels when outcomes have a natural hierarchy and you want to avoid arbitrary weights
    2. **MCDA** is powerful when stakeholders have different value perspectives that need explicit integration
    3. **SBRF** provides comprehensive structure for regulatory-grade assessments
    4. **Communication** must be tailored to audience—same data, different framing

---

## Practice Exercise

!!! question "Apply Your Learning"

    Select one of the case studies and:

    1. **Modify the hierarchy or weights** — How does this change conclusions?
    2. **Identify a key assumption** — What would invalidate the analysis?
    3. **Draft communication** — Write a 2-sentence summary for a patient audience

---

## Further Resources

| Resource | Description |
|----------|-------------|
| [Module 7: Competency Assessment](07-competency-assessment.md) | Test your knowledge |
| [DOOR Analysis Tutorial](../interactive/door-analysis.md) | Hands-on practice |
| [Glossary](../reference/glossary.md) | Term definitions |

---

!!! warning "Educational Disclaimer"

    This module is provided for **educational purposes only**. All case studies use hypothetical products (NEXCOAG, NEXONC, NEXVAX) for illustration. Do not apply these analyses to actual regulatory decisions without proper validation.

---

[Continue to Module 7: Competency Assessment →](07-competency-assessment.md){ .md-button .md-button--primary }

---

**NexVigilant** | *Empowerment Through Vigilance*

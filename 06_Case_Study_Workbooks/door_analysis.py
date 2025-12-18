#!/usr/bin/env python3
"""
DOOR (Desirability of Outcome Ranking) Analysis Implementation
NexVigilant Benefit-Risk Intelligence Toolkit

Based on CIOMS WG XII methodology for composite endpoint analysis
that respects patient-relevant outcome hierarchies.

DOOR ranks patient outcomes from most desirable to least desirable,
then compares the distribution of outcomes between treatment groups.

Author: NexVigilant Capability Engineering
Version: 1.0
"""

import pandas as pd
import numpy as np
from scipy import stats
from collections import Counter
import matplotlib.pyplot as plt


class DOORAnalysis:
    """
    Implements Desirability of Outcome Ranking (DOOR) methodology.
    
    DOOR creates a hierarchical ranking of composite outcomes where
    each patient is assigned to exactly one outcome category, and
    categories are ordered from most to least desirable.
    
    Key Principle: A patient in a "better" category is ALWAYS preferred
    to a patient in a "worse" category, regardless of specific within-
    category performance.
    """
    
    def __init__(self, outcome_hierarchy: list):
        """
        Initialize DOOR analysis with outcome hierarchy.
        
        Args:
            outcome_hierarchy: List of outcome categories from MOST desirable
                              (index 0) to LEAST desirable (last index).
                              
        Example:
            hierarchy = [
                "Alive, no stroke, no major bleed",       # Rank 1 (Best)
                "Alive, no stroke, minor bleed only",     # Rank 2
                "Alive, minor stroke, no major bleed",    # Rank 3
                "Alive, major stroke, no major bleed",    # Rank 4
                "Alive, no stroke, major bleed",          # Rank 5
                "Alive, major stroke, major bleed",       # Rank 6
                "Death from any cause"                    # Rank 7 (Worst)
            ]
        """
        self.outcome_hierarchy = outcome_hierarchy
        self.n_categories = len(outcome_hierarchy)
        # Create rank mapping (1 = best, higher = worse)
        self.rank_map = {outcome: rank + 1 
                         for rank, outcome in enumerate(outcome_hierarchy)}
        self.results = None
        
    def assign_outcomes(self, patient_data: pd.DataFrame, 
                        outcome_column: str) -> pd.DataFrame:
        """
        Assign each patient to their DOOR outcome category.
        
        Args:
            patient_data: DataFrame with patient-level data
            outcome_column: Name of column containing outcome category
            
        Returns:
            DataFrame with added 'door_rank' column
        """
        data = patient_data.copy()
        
        # Validate all outcomes are in hierarchy
        unique_outcomes = data[outcome_column].unique()
        invalid = set(unique_outcomes) - set(self.outcome_hierarchy)
        if invalid:
            raise ValueError(f"Unknown outcomes: {invalid}")
            
        # Assign ranks
        data['door_rank'] = data[outcome_column].map(self.rank_map)
        data['door_category'] = data[outcome_column]
        
        return data
    
    def compare_treatments(self, data: pd.DataFrame, 
                          treatment_column: str,
                          treatment_arm: str,
                          control_arm: str) -> dict:
        """
        Perform pairwise comparison of treatment vs control using DOOR.
        
        For each pair of patients (one from each arm), determine which
        patient has the more desirable outcome. The treatment "wins" if
        the treatment patient has a lower (better) DOOR rank.
        
        Args:
            data: DataFrame with door_rank assigned
            treatment_column: Column name for treatment assignment
            treatment_arm: Value indicating treatment group
            control_arm: Value indicating control group
            
        Returns:
            Dictionary with comparison results and statistics
        """
        # Split by treatment
        trt = data[data[treatment_column] == treatment_arm]['door_rank'].values
        ctrl = data[data[treatment_column] == control_arm]['door_rank'].values
        
        # Perform all pairwise comparisons
        n_trt = len(trt)
        n_ctrl = len(ctrl)
        n_pairs = n_trt * n_ctrl
        
        trt_wins = 0  # Treatment patient has better (lower) rank
        ctrl_wins = 0  # Control patient has better (lower) rank
        ties = 0  # Same rank
        
        for t in trt:
            for c in ctrl:
                if t < c:
                    trt_wins += 1
                elif t > c:
                    ctrl_wins += 1
                else:
                    ties += 1
        
        # Calculate statistics
        p_trt_better = trt_wins / n_pairs
        p_ctrl_better = ctrl_wins / n_pairs
        p_tie = ties / n_pairs
        
        # Win ratio (treatment wins / control wins)
        win_ratio = trt_wins / ctrl_wins if ctrl_wins > 0 else float('inf')
        
        # Net benefit (P(trt better) - P(ctrl better))
        net_benefit = p_trt_better - p_ctrl_better
        
        # Mann-Whitney U test for statistical significance
        u_stat, p_value = stats.mannwhitneyu(trt, ctrl, alternative='less')
        
        # Store results
        self.results = {
            'n_treatment': n_trt,
            'n_control': n_ctrl,
            'n_pairs': n_pairs,
            'treatment_wins': trt_wins,
            'control_wins': ctrl_wins,
            'ties': ties,
            'p_treatment_better': p_trt_better,
            'p_control_better': p_ctrl_better,
            'p_tie': p_tie,
            'win_ratio': win_ratio,
            'net_benefit': net_benefit,
            'mann_whitney_u': u_stat,
            'p_value': p_value
        }
        
        return self.results
    
    def get_outcome_distribution(self, data: pd.DataFrame,
                                 treatment_column: str) -> pd.DataFrame:
        """
        Get distribution of outcomes by treatment group.
        
        Returns:
            DataFrame with counts and percentages per category per group
        """
        # Calculate distribution
        dist = data.groupby([treatment_column, 'door_category']).size()
        dist = dist.unstack(fill_value=0)
        
        # Reorder columns by hierarchy
        dist = dist[[c for c in self.outcome_hierarchy if c in dist.columns]]
        
        # Add percentages
        totals = dist.sum(axis=1)
        pct = dist.div(totals, axis=0) * 100
        pct.columns = [f"{c} (%)" for c in pct.columns]
        
        # Combine
        result = pd.concat([dist, pct], axis=1)
        
        return result
    
    def plot_stacked_bar(self, data: pd.DataFrame,
                         treatment_column: str,
                         title: str = "DOOR Outcome Distribution",
                         figsize: tuple = (10, 6)) -> plt.Figure:
        """
        Create stacked bar chart of outcome distributions.
        """
        # Get distribution
        dist = data.groupby([treatment_column, 'door_category']).size()
        dist = dist.unstack(fill_value=0)
        dist = dist[[c for c in self.outcome_hierarchy if c in dist.columns]]
        
        # Convert to percentages
        pct = dist.div(dist.sum(axis=1), axis=0) * 100
        
        # Create plot
        fig, ax = plt.subplots(figsize=figsize)
        
        # Color gradient from green (best) to red (worst)
        n_cats = len(pct.columns)
        colors = plt.cm.RdYlGn_r(np.linspace(0.1, 0.9, n_cats))
        
        # Plot stacked bars
        bottom = np.zeros(len(pct))
        for i, (col, color) in enumerate(zip(pct.columns, colors)):
            ax.barh(pct.index, pct[col], left=bottom, label=col, color=color)
            bottom += pct[col].values
        
        ax.set_xlabel('Percentage of Patients')
        ax.set_title(title)
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.set_xlim(0, 100)
        
        plt.tight_layout()
        return fig
    
    def generate_report(self) -> str:
        """
        Generate text report of DOOR analysis results.
        """
        if self.results is None:
            return "No analysis results available. Run compare_treatments() first."
        
        r = self.results
        
        report = f"""
╔══════════════════════════════════════════════════════════════════════╗
║                    DOOR ANALYSIS RESULTS                              ║
║            Desirability of Outcome Ranking                            ║
╚══════════════════════════════════════════════════════════════════════╝

SAMPLE SIZES
─────────────────────────────────────────────────────────────
  Treatment arm:     {r['n_treatment']:,} patients
  Control arm:       {r['n_control']:,} patients
  Total comparisons: {r['n_pairs']:,} pairs

PAIRWISE COMPARISON RESULTS
─────────────────────────────────────────────────────────────
  Treatment patient has better outcome:  {r['treatment_wins']:,} pairs ({r['p_treatment_better']:.1%})
  Control patient has better outcome:    {r['control_wins']:,} pairs ({r['p_control_better']:.1%})
  Tied outcomes:                         {r['ties']:,} pairs ({r['p_tie']:.1%})

KEY METRICS
─────────────────────────────────────────────────────────────
  Win Ratio (Treatment/Control):         {r['win_ratio']:.2f}
  Net Benefit (P_trt - P_ctrl):          {r['net_benefit']:.3f} ({r['net_benefit']*100:.1f}%)
  Mann-Whitney U statistic:              {r['mann_whitney_u']:.0f}
  p-value (one-sided):                   {r['p_value']:.4f}

INTERPRETATION
─────────────────────────────────────────────────────────────
"""
        
        # Interpretation
        if r['win_ratio'] > 1.0:
            report += f"""
  • Treatment demonstrates FAVORABLE benefit-risk profile
  • For every pair where control "wins", treatment "wins" {r['win_ratio']:.2f} times
  • Treatment patients more likely to have desirable outcomes
"""
        elif r['win_ratio'] < 1.0:
            report += f"""
  • Control demonstrates more favorable outcomes
  • Win ratio < 1.0 suggests treatment may not improve outcomes
"""
        else:
            report += """
  • Treatments appear equivalent on DOOR ranking
"""
        
        if r['p_value'] < 0.05:
            report += f"  • Result is statistically significant (p = {r['p_value']:.4f})\n"
        else:
            report += f"  • Result is NOT statistically significant (p = {r['p_value']:.4f})\n"
        
        report += """
─────────────────────────────────────────────────────────────
Note: DOOR preserves the clinical ordering of outcomes without
assuming numerical equivalence between categories. A patient
in category 2 is always better than category 3, but we don't
assume the "distance" between them equals other category gaps.
─────────────────────────────────────────────────────────────
"""
        return report


def create_example_data():
    """
    Create example dataset for DOOR analysis demonstration.
    Simulates a cardiovascular trial comparing Drug A vs Placebo.
    """
    np.random.seed(42)
    
    # Define outcome hierarchy for CV trial
    outcomes = [
        "Alive, no CV event, no bleed",
        "Alive, no CV event, minor bleed",
        "Alive, minor CV event, no bleed",
        "Alive, major CV event recovered",
        "Alive, no CV event, major bleed",
        "Alive, major CV event + major bleed",
        "CV death",
        "Non-CV death"
    ]
    
    # Simulate treatment arm (better outcomes)
    n_treatment = 500
    treatment_probs = [0.45, 0.15, 0.12, 0.10, 0.08, 0.05, 0.03, 0.02]
    treatment_outcomes = np.random.choice(
        outcomes, size=n_treatment, p=treatment_probs
    )
    
    # Simulate control arm (worse outcomes)
    n_control = 500
    control_probs = [0.35, 0.12, 0.10, 0.12, 0.10, 0.08, 0.08, 0.05]
    control_outcomes = np.random.choice(
        outcomes, size=n_control, p=control_probs
    )
    
    # Create DataFrame
    treatment_data = pd.DataFrame({
        'patient_id': [f'T{i:04d}' for i in range(n_treatment)],
        'treatment': 'Drug A',
        'outcome': treatment_outcomes
    })
    
    control_data = pd.DataFrame({
        'patient_id': [f'C{i:04d}' for i in range(n_control)],
        'treatment': 'Placebo',
        'outcome': control_outcomes
    })
    
    data = pd.concat([treatment_data, control_data], ignore_index=True)
    
    return data, outcomes


def main():
    """
    Demonstrate DOOR analysis with example data.
    """
    print("=" * 70)
    print("DOOR ANALYSIS DEMONSTRATION")
    print("NexVigilant Benefit-Risk Intelligence Toolkit")
    print("=" * 70)
    print()
    
    # Create example data
    print("Creating simulated trial data...")
    data, hierarchy = create_example_data()
    print(f"  {len(data)} patients randomized")
    print()
    
    # Display hierarchy
    print("OUTCOME HIERARCHY (Most → Least Desirable):")
    print("-" * 50)
    for i, outcome in enumerate(hierarchy, 1):
        print(f"  Rank {i}: {outcome}")
    print()
    
    # Initialize DOOR analysis
    door = DOORAnalysis(outcome_hierarchy=hierarchy)
    
    # Assign outcomes
    data = door.assign_outcomes(data, outcome_column='outcome')
    
    # Get distribution
    print("OUTCOME DISTRIBUTION BY ARM:")
    print("-" * 50)
    dist = door.get_outcome_distribution(data, treatment_column='treatment')
    print(dist.to_string())
    print()
    
    # Compare treatments
    results = door.compare_treatments(
        data,
        treatment_column='treatment',
        treatment_arm='Drug A',
        control_arm='Placebo'
    )
    
    # Print report
    print(door.generate_report())
    
    # Save visualization
    fig = door.plot_stacked_bar(
        data, 
        treatment_column='treatment',
        title='DOOR Outcome Distribution: Drug A vs Placebo'
    )
    fig.savefig('door_analysis_plot.png', 
                dpi=150, bbox_inches='tight')
    print("Visualization saved to: door_analysis_plot.png")
    print()
    
    # Export results to CSV
    results_df = pd.DataFrame([results])
    results_df.to_csv('door_results.csv', index=False)
    print("Results exported to: door_results.csv")
    
    return door, data, results


if __name__ == "__main__":
    door, data, results = main()

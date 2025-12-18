#!/usr/bin/env python3
"""
NexVigilant Benefit-Risk Assessment Scaffolding Tool

Generates a new benefit-risk assessment directory from templates.

Usage:
    python scaffold_assessment.py --name "MyDrug-Indication" --type brad
    python scaffold_assessment.py --name "JAK-Inhibitor-RA" --type mcda
    python scaffold_assessment.py --name "Vaccine-COVID" --type full

Template Types:
    brad   - BRAD document only
    mcda   - MCDA worksheet with Value Tree
    full   - Complete assessment (BRAD + Effects Table + Value Tree + MCDA)

Educational Use Only:
    This tool is provided by NexVigilant for educational and learning purposes.
    Do not use generated scaffolds for regulatory submissions without proper
    validation by qualified regulatory professionals.

NexVigilant | Empowerment Through Vigilance
"""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path
import shutil


# Template paths relative to repository root
TEMPLATE_DIR = Path(__file__).parent.parent / "templates"
ASSESSMENTS_DIR = Path(__file__).parent.parent / "assessments"


def sanitize_name(name: str) -> str:
    """Convert name to directory-safe format."""
    return name.lower().replace(" ", "-").replace("_", "-")


def get_template_content(template_name: str) -> str:
    """Read template content from templates directory."""
    template_path = TEMPLATE_DIR / f"{template_name}_Template.md"
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")
    return template_path.read_text(encoding="utf-8")


def personalize_template(content: str, project_name: str, author: str) -> str:
    """Replace placeholders in template with project-specific values."""
    replacements = {
        "[Product Name]": project_name,
        "[PRODUCT]": project_name.upper().replace("-", "_"),
        "[Indication]": "To be specified",
        "[Author Name]": author,
        "[Date]": datetime.now().strftime("%Y-%m-%d"),
        "[Version]": "1.0",
    }

    for placeholder, value in replacements.items():
        content = content.replace(placeholder, value)

    return content


def create_assessment_structure(name: str, assessment_type: str, author: str) -> Path:
    """
    Create the assessment directory structure based on type.

    Returns the path to the created assessment directory.
    """
    safe_name = sanitize_name(name)
    assessment_path = ASSESSMENTS_DIR / safe_name

    # Create main directory
    assessment_path.mkdir(parents=True, exist_ok=True)

    # Create subdirectories
    (assessment_path / "data").mkdir(exist_ok=True)
    (assessment_path / "outputs").mkdir(exist_ok=True)
    (assessment_path / "references").mkdir(exist_ok=True)

    # Determine which templates to include
    templates_to_create = []

    if assessment_type == "brad":
        templates_to_create = ["BRAD"]
    elif assessment_type == "mcda":
        templates_to_create = ["Value_Tree", "Effects_Table"]
    elif assessment_type == "full":
        templates_to_create = ["BRAD", "Effects_Table", "Value_Tree"]
    else:
        raise ValueError(f"Unknown assessment type: {assessment_type}")

    # Create each template file
    for template in templates_to_create:
        try:
            content = get_template_content(template)
            personalized = personalize_template(content, name, author)

            output_name = f"{safe_name}_{template.lower()}.md"
            output_path = assessment_path / output_name
            output_path.write_text(personalized, encoding="utf-8")
            print(f"  Created: {output_name}")
        except FileNotFoundError as e:
            print(f"  Warning: {e}")

    # Create README for the assessment
    readme_content = f"""# {name} Benefit-Risk Assessment

**Created**: {datetime.now().strftime("%Y-%m-%d")}
**Author**: {author}
**Type**: {assessment_type.upper()}

---

## Overview

This directory contains the benefit-risk assessment materials for {name}.

## Directory Structure

```
{safe_name}/
├── data/              # Raw data files (CSVs, datasets)
├── outputs/           # Generated outputs (figures, reports)
├── references/        # Supporting documents, literature
└── *.md               # Assessment documents
```

## Getting Started

1. Review the generated template files
2. Populate the `data/` directory with your clinical trial data
3. Complete each section of the BRAD or MCDA documents
4. Generate visualizations using the toolkit notebooks

## Educational Disclaimer

This assessment scaffold was generated using the NexVigilant Benefit-Risk
Intelligence Toolkit for **educational purposes only**.

It should NOT be used for regulatory submissions without:
- Internal review and validation
- Alignment with company SOPs
- Regulatory affairs approval
- Quality assurance sign-off

---

**NexVigilant** | *Empowerment Through Vigilance*
"""

    readme_path = assessment_path / "README.md"
    readme_path.write_text(readme_content, encoding="utf-8")
    print(f"  Created: README.md")

    return assessment_path


def list_available_templates():
    """List all available templates."""
    print("\nAvailable Templates:")
    print("-" * 40)

    if not TEMPLATE_DIR.exists():
        print("  No templates directory found.")
        return

    for template_file in sorted(TEMPLATE_DIR.glob("*_Template.md")):
        name = template_file.stem.replace("_Template", "")
        print(f"  - {name}")

    print("\nAssessment Types:")
    print("-" * 40)
    print("  brad  - BRAD document only")
    print("  mcda  - MCDA worksheet with Value Tree and Effects Table")
    print("  full  - Complete assessment (all templates)")


def main():
    parser = argparse.ArgumentParser(
        description="Scaffold a new Benefit-Risk Assessment from templates",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python scaffold_assessment.py --name "JAK-Inhibitor-RA" --type full
    python scaffold_assessment.py --name "COVID-Vaccine" --type brad --author "Jane Doe"
    python scaffold_assessment.py --list

Educational Use Only - NexVigilant | Empowerment Through Vigilance
        """
    )

    parser.add_argument(
        "--name", "-n",
        help="Name of the assessment (e.g., 'JAK-Inhibitor-RA')"
    )

    parser.add_argument(
        "--type", "-t",
        choices=["brad", "mcda", "full"],
        default="full",
        help="Type of assessment scaffold (default: full)"
    )

    parser.add_argument(
        "--author", "-a",
        default="NexVigilant User",
        help="Author name for document headers"
    )

    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="List available templates"
    )

    parser.add_argument(
        "--output-dir", "-o",
        type=Path,
        help="Custom output directory (default: assessments/)"
    )

    args = parser.parse_args()

    if args.list:
        list_available_templates()
        return 0

    if not args.name:
        parser.error("--name is required. Use --list to see available templates.")

    # Override assessments directory if specified
    global ASSESSMENTS_DIR
    if args.output_dir:
        ASSESSMENTS_DIR = args.output_dir

    print(f"\nNexVigilant B-R Assessment Scaffold")
    print("=" * 50)
    print(f"Assessment: {args.name}")
    print(f"Type: {args.type.upper()}")
    print(f"Author: {args.author}")
    print("-" * 50)

    try:
        assessment_path = create_assessment_structure(
            args.name,
            args.type,
            args.author
        )
        print("-" * 50)
        print(f"\nSuccess! Assessment created at:")
        print(f"  {assessment_path}")
        print("\nNext steps:")
        print("  1. cd", assessment_path)
        print("  2. Review and complete the generated templates")
        print("  3. Add your data to the data/ directory")
        print("  4. Use toolkit notebooks for analysis")
        print("\nEducational Use Only - Not for regulatory submissions")
        return 0

    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

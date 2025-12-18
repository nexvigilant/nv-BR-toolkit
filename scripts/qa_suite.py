#!/usr/bin/env python3
"""
NexVigilant B-R Toolkit Quality Assurance Suite

Comprehensive testing for documentation, notebooks, templates, and content integrity.

Usage:
    python qa_suite.py                    # Run all checks
    python qa_suite.py --check links      # Run specific check
    python qa_suite.py --verbose          # Detailed output
    python qa_suite.py --fix              # Auto-fix where possible

Checks:
    1. links       - Validate internal/external links
    2. notebooks   - Validate notebook structure and execution
    3. templates   - Check template completeness
    4. branding    - Verify NexVigilant branding consistency
    5. disclaimers - Check educational disclaimers present
    6. glossary    - Verify glossary term coverage
    7. structure   - Validate module structure
    8. references  - Cross-reference validation

Educational Use Only:
    NexVigilant | Empowerment Through Vigilance
"""

import argparse
import io
import json
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from collections import defaultdict

# Handle Windows console encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Cross-platform symbols (ASCII fallback for Windows)
SYMBOLS = {
    'pass': '[PASS]' if sys.platform == 'win32' else '✅ PASS',
    'fail': '[FAIL]' if sys.platform == 'win32' else '❌ FAIL',
    'warn': '[WARN]' if sys.platform == 'win32' else '⚠️ WARN',
    'tip': '[TIP]' if sys.platform == 'win32' else '💡',
}


# Configuration
REPO_ROOT = Path(__file__).parent.parent
DOCS_DIR = REPO_ROOT / "docs"
NOTEBOOKS_DIR = REPO_ROOT / "notebooks"
TEMPLATES_DIR = REPO_ROOT / "templates"
MODULES_DIR = DOCS_DIR / "modules"


@dataclass
class CheckResult:
    """Result of a single check."""
    name: str
    passed: bool
    message: str
    details: List[str] = field(default_factory=list)
    fixable: bool = False


@dataclass
class QAReport:
    """Overall QA report."""
    results: List[CheckResult] = field(default_factory=list)

    @property
    def passed(self) -> int:
        return sum(1 for r in self.results if r.passed)

    @property
    def failed(self) -> int:
        return sum(1 for r in self.results if not r.passed)

    @property
    def total(self) -> int:
        return len(self.results)

    @property
    def success_rate(self) -> float:
        return (self.passed / self.total * 100) if self.total > 0 else 0


# =============================================================================
# CHECK FUNCTIONS
# =============================================================================

def check_internal_links(verbose: bool = False) -> CheckResult:
    """Check all internal markdown links are valid."""
    issues = []
    checked = 0

    # Regex for markdown links: [text](path)
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

    for md_file in DOCS_DIR.rglob("*.md"):
        content = md_file.read_text(encoding='utf-8')

        for match in link_pattern.finditer(content):
            link_text, link_path = match.groups()

            # Skip external links and anchors
            if link_path.startswith(('http://', 'https://', '#', 'mailto:')):
                continue

            # Handle relative paths
            checked += 1

            # Remove anchor from path
            clean_path = link_path.split('#')[0]
            if not clean_path:
                continue

            # Resolve relative path
            if clean_path.startswith('/'):
                target = DOCS_DIR / clean_path.lstrip('/')
            else:
                target = md_file.parent / clean_path

            # Check if target exists
            if not target.exists():
                issues.append(f"{md_file.name}: broken link '{link_path}'")

    return CheckResult(
        name="Internal Links",
        passed=len(issues) == 0,
        message=f"Checked {checked} links, {len(issues)} broken",
        details=issues[:20]  # Limit details
    )


def check_external_links(verbose: bool = False) -> CheckResult:
    """Check external links are properly formatted (doesn't verify reachability)."""
    issues = []
    external_links = set()

    link_pattern = re.compile(r'\[([^\]]+)\]\((https?://[^)]+)\)')

    for md_file in DOCS_DIR.rglob("*.md"):
        content = md_file.read_text(encoding='utf-8')

        for match in link_pattern.finditer(content):
            link_text, url = match.groups()
            external_links.add(url)

            # Check for common issues
            if ' ' in url and '%20' not in url:
                issues.append(f"{md_file.name}: unescaped space in URL '{url[:50]}...'")

            if url.endswith('.'):
                issues.append(f"{md_file.name}: URL ends with period '{url[:50]}...'")

    return CheckResult(
        name="External Links Format",
        passed=len(issues) == 0,
        message=f"Found {len(external_links)} unique external links, {len(issues)} format issues",
        details=issues
    )


def check_notebook_structure(verbose: bool = False) -> CheckResult:
    """Validate Jupyter notebook structure."""
    issues = []
    notebooks = list(NOTEBOOKS_DIR.glob("*.ipynb"))

    for nb_path in notebooks:
        try:
            with open(nb_path, 'r', encoding='utf-8') as f:
                nb = json.load(f)

            # Check required keys
            if 'cells' not in nb:
                issues.append(f"{nb_path.name}: missing 'cells' key")
                continue

            if nb.get('nbformat', 0) < 4:
                issues.append(f"{nb_path.name}: outdated notebook format")

            # Check cell structure
            code_cells = 0
            markdown_cells = 0

            for i, cell in enumerate(nb['cells']):
                cell_type = cell.get('cell_type', '')

                if cell_type == 'code':
                    code_cells += 1
                    # Check for outputs (should be cleared for version control)
                    if cell.get('outputs') and len(cell['outputs']) > 0:
                        if verbose:
                            issues.append(f"{nb_path.name}: cell {i} has uncleaned outputs")
                elif cell_type == 'markdown':
                    markdown_cells += 1

            # Warn if no code cells
            if code_cells == 0:
                issues.append(f"{nb_path.name}: no code cells found")

            # Warn if no markdown cells
            if markdown_cells == 0:
                issues.append(f"{nb_path.name}: no markdown cells (documentation)")

        except json.JSONDecodeError as e:
            issues.append(f"{nb_path.name}: invalid JSON - {e}")
        except Exception as e:
            issues.append(f"{nb_path.name}: error - {e}")

    return CheckResult(
        name="Notebook Structure",
        passed=len(issues) == 0,
        message=f"Validated {len(notebooks)} notebooks, {len(issues)} issues",
        details=issues
    )


def check_template_completeness(verbose: bool = False) -> CheckResult:
    """Check all templates have required sections."""
    issues = []
    templates = list(TEMPLATES_DIR.glob("*.md"))

    required_sections = [
        "Educational",  # Must mention educational use
        "NexVigilant",  # Branding
    ]

    for template in templates:
        content = template.read_text(encoding='utf-8')
        content_lower = content.lower()

        for section in required_sections:
            if section.lower() not in content_lower:
                issues.append(f"{template.name}: missing '{section}' reference")

    return CheckResult(
        name="Template Completeness",
        passed=len(issues) == 0,
        message=f"Checked {len(templates)} templates, {len(issues)} missing elements",
        details=issues
    )


def check_branding_consistency(verbose: bool = False) -> CheckResult:
    """Verify NexVigilant branding is consistent across all files."""
    issues = []

    required_branding = "NexVigilant"
    tagline = "Empowerment Through Vigilance"

    for md_file in DOCS_DIR.rglob("*.md"):
        content = md_file.read_text(encoding='utf-8')

        # Check for NexVigilant mention
        if required_branding not in content:
            issues.append(f"{md_file.name}: missing NexVigilant branding")

    # Check modules specifically for tagline
    for module in MODULES_DIR.glob("*.md"):
        content = module.read_text(encoding='utf-8')
        if tagline not in content:
            issues.append(f"{module.name}: missing tagline")

    return CheckResult(
        name="Branding Consistency",
        passed=len(issues) == 0,
        message=f"Checked branding, {len(issues)} files missing",
        details=issues,
        fixable=True
    )


def check_educational_disclaimers(verbose: bool = False) -> CheckResult:
    """Verify educational disclaimers are present in all modules."""
    issues = []

    disclaimer_patterns = [
        r"educational\s+purposes?\s+only",
        r"educational\s+use\s+only",
        r"educational\s+disclaimer",
        r"for\s+learning\s+purposes"
    ]

    for module in MODULES_DIR.glob("*.md"):
        content = module.read_text(encoding='utf-8')

        has_disclaimer = any(
            re.search(pattern, content, re.IGNORECASE) for pattern in disclaimer_patterns
        )

        if not has_disclaimer:
            issues.append(f"{module.name}: missing educational disclaimer")

    # Also check templates
    for template in TEMPLATES_DIR.glob("*.md"):
        content = template.read_text(encoding='utf-8')

        has_disclaimer = any(
            re.search(pattern, content, re.IGNORECASE) for pattern in disclaimer_patterns
        )

        if not has_disclaimer:
            issues.append(f"templates/{template.name}: missing educational disclaimer")

    return CheckResult(
        name="Educational Disclaimers",
        passed=len(issues) == 0,
        message=f"Checked disclaimers, {len(issues)} missing",
        details=issues,
        fixable=True
    )


def check_glossary_coverage(verbose: bool = False) -> CheckResult:
    """Check that key terms in modules are defined in glossary."""
    issues = []

    glossary_path = DOCS_DIR / "reference" / "glossary.md"
    if not glossary_path.exists():
        return CheckResult(
            name="Glossary Coverage",
            passed=False,
            message="Glossary file not found",
            details=["reference/glossary.md does not exist"]
        )

    glossary_content = glossary_path.read_text(encoding='utf-8')

    # Key terms that should be in glossary
    key_terms = [
        "BRAD", "Effects Table", "Value Tree", "DOOR", "MCDA",
        "NNT", "NNH", "CIOMS", "SBRF", "RMP", "REMS",
        "Win Ratio", "ICH", "PrOACT-URL"
    ]

    for term in key_terms:
        # Check if term appears in glossary (case-insensitive)
        if term.lower() not in glossary_content.lower():
            issues.append(f"Term not in glossary: {term}")

    return CheckResult(
        name="Glossary Coverage",
        passed=len(issues) == 0,
        message=f"Checked {len(key_terms)} key terms, {len(issues)} missing",
        details=issues
    )


def check_module_structure(verbose: bool = False) -> CheckResult:
    """Validate all modules have consistent structure."""
    issues = []

    required_elements = [
        ("Learning Objectives", r"[Ll]earning [Oo]bjectives"),
        ("Key Takeaways", r"[Kk]ey [Tt]akeaways"),
        ("Navigation", r"\[.*→.*\]\(.*\.md\)"),  # Navigation links
    ]

    expected_modules = [
        "01-leadership-briefing.md",
        "02-foundation.md",
        "03-decision-support.md",
        "04-assessment-templates.md",
        "05-visualization-tools.md",
        "06-case-studies.md",
        "07-competency-assessment.md",
        "08-regulatory-reference.md",
    ]

    # Check all expected modules exist
    for module_name in expected_modules:
        module_path = MODULES_DIR / module_name
        if not module_path.exists():
            issues.append(f"Missing module: {module_name}")
            continue

        content = module_path.read_text(encoding='utf-8')

        for element_name, pattern in required_elements:
            if not re.search(pattern, content):
                issues.append(f"{module_name}: missing {element_name}")

    return CheckResult(
        name="Module Structure",
        passed=len(issues) == 0,
        message=f"Validated {len(expected_modules)} modules, {len(issues)} issues",
        details=issues
    )


def check_cross_references(verbose: bool = False) -> CheckResult:
    """Validate cross-references between modules are accurate."""
    issues = []

    # Find all module references
    module_ref_pattern = re.compile(r'\[.*?\]\((\.\./)?(modules/)?(\d{2}-[a-z-]+\.md)\)')

    for md_file in DOCS_DIR.rglob("*.md"):
        content = md_file.read_text(encoding='utf-8')

        for match in module_ref_pattern.finditer(content):
            ref_module = match.group(3)

            # Check if referenced module exists
            target = MODULES_DIR / ref_module
            if not target.exists():
                issues.append(f"{md_file.name}: references non-existent module '{ref_module}'")

    return CheckResult(
        name="Cross References",
        passed=len(issues) == 0,
        message=f"Validated cross-references, {len(issues)} broken",
        details=issues
    )


def check_mkdocs_config(verbose: bool = False) -> CheckResult:
    """Validate mkdocs.yml configuration."""
    issues = []

    mkdocs_path = REPO_ROOT / "mkdocs.yml"
    if not mkdocs_path.exists():
        return CheckResult(
            name="MkDocs Config",
            passed=False,
            message="mkdocs.yml not found",
            details=["mkdocs.yml does not exist in repository root"]
        )

    content = mkdocs_path.read_text(encoding='utf-8')

    # Check for required configurations
    required_configs = [
        ("site_name", r"site_name:"),
        ("theme", r"theme:"),
        ("nav", r"nav:"),
        ("plugins", r"plugins:"),
    ]

    for config_name, pattern in required_configs:
        if not re.search(pattern, content):
            issues.append(f"Missing configuration: {config_name}")

    # Check all nav items point to existing files
    nav_pattern = re.compile(r":\s+([a-z-/]+\.md)")
    for match in nav_pattern.finditer(content):
        nav_file = match.group(1)
        target = DOCS_DIR / nav_file
        if not target.exists():
            issues.append(f"Nav points to missing file: {nav_file}")

    return CheckResult(
        name="MkDocs Config",
        passed=len(issues) == 0,
        message=f"Validated mkdocs.yml, {len(issues)} issues",
        details=issues
    )


# =============================================================================
# MAIN RUNNER
# =============================================================================

ALL_CHECKS = {
    "links": [check_internal_links, check_external_links],
    "notebooks": [check_notebook_structure],
    "templates": [check_template_completeness],
    "branding": [check_branding_consistency],
    "disclaimers": [check_educational_disclaimers],
    "glossary": [check_glossary_coverage],
    "structure": [check_module_structure, check_mkdocs_config],
    "references": [check_cross_references],
}


def run_checks(
    checks: Optional[List[str]] = None,
    verbose: bool = False
) -> QAReport:
    """Run specified checks and return report."""
    report = QAReport()

    if checks is None:
        checks = list(ALL_CHECKS.keys())

    for check_name in checks:
        if check_name not in ALL_CHECKS:
            print(f"Unknown check: {check_name}")
            continue

        for check_func in ALL_CHECKS[check_name]:
            result = check_func(verbose=verbose)
            report.results.append(result)

    return report


def print_report(report: QAReport, verbose: bool = False):
    """Print formatted report."""
    print("\n" + "=" * 60)
    print("NEXVIGILANT B-R TOOLKIT QA REPORT")
    print("=" * 60)

    for result in report.results:
        status = SYMBOLS['pass'] if result.passed else SYMBOLS['fail']
        print(f"\n{status} | {result.name}")
        print(f"       {result.message}")

        if not result.passed and result.details:
            for detail in result.details[:10]:  # Limit details shown
                print(f"       - {detail}")

            if len(result.details) > 10:
                print(f"       ... and {len(result.details) - 10} more")

            if result.fixable:
                print(f"       {SYMBOLS['tip']} This issue may be auto-fixable with --fix")

    print("\n" + "-" * 60)
    print(f"SUMMARY: {report.passed}/{report.total} checks passed ({report.success_rate:.1f}%)")

    if report.failed > 0:
        print(f"         {report.failed} checks need attention")

    print("-" * 60)
    print("Educational Use Only - NexVigilant | Empowerment Through Vigilance")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="NexVigilant B-R Toolkit Quality Assurance Suite",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Available checks:
    links       - Internal and external link validation
    notebooks   - Jupyter notebook structure validation
    templates   - Template completeness checks
    branding    - NexVigilant branding consistency
    disclaimers - Educational disclaimer presence
    glossary    - Glossary term coverage
    structure   - Module structure validation
    references  - Cross-reference validation

Examples:
    python qa_suite.py                    # Run all checks
    python qa_suite.py --check links      # Run only link checks
    python qa_suite.py --check structure --verbose

Educational Use Only - NexVigilant | Empowerment Through Vigilance
        """
    )

    parser.add_argument(
        '--check', '-c',
        action='append',
        dest='checks',
        choices=list(ALL_CHECKS.keys()),
        help="Run specific check(s) only"
    )

    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help="Show detailed output"
    )

    parser.add_argument(
        '--json',
        action='store_true',
        help="Output results as JSON"
    )

    parser.add_argument(
        '--fail-fast',
        action='store_true',
        help="Stop on first failure"
    )

    args = parser.parse_args()

    print("NexVigilant B-R Toolkit QA Suite")
    print("-" * 40)

    report = run_checks(
        checks=args.checks,
        verbose=args.verbose
    )

    if args.json:
        # JSON output for CI integration
        output = {
            "passed": report.passed,
            "failed": report.failed,
            "total": report.total,
            "success_rate": report.success_rate,
            "results": [
                {
                    "name": r.name,
                    "passed": r.passed,
                    "message": r.message,
                    "details": r.details
                }
                for r in report.results
            ]
        }
        print(json.dumps(output, indent=2))
    else:
        print_report(report, verbose=args.verbose)

    # Exit code for CI
    sys.exit(0 if report.failed == 0 else 1)


if __name__ == "__main__":
    main()

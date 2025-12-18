#!/usr/bin/env python3
"""
NexVigilant Notebook Validation Tool

Validates Jupyter notebooks by:
1. Checking notebook structure (valid JSON, cells, kernelspec)
2. Optionally executing notebooks to verify code runs without errors
3. Reporting any issues found

Usage:
    python validate_notebooks.py                      # Validate all notebooks
    python validate_notebooks.py --execute            # Validate and execute
    python validate_notebooks.py notebooks/DOOR*.ipynb  # Specific notebooks
    python validate_notebooks.py --timeout 120       # Custom timeout per notebook

Educational Use Only:
    This tool is provided by NexVigilant for educational and learning purposes.

NexVigilant | Empowerment Through Vigilance
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple, Optional
import tempfile


# Default notebook directory relative to script location
NOTEBOOKS_DIR = Path(__file__).parent.parent / "notebooks"


class NotebookValidationError(Exception):
    """Custom exception for notebook validation errors."""
    pass


def validate_notebook_structure(notebook_path: Path) -> List[str]:
    """
    Validate notebook JSON structure.

    Returns a list of issues found (empty if valid).
    """
    issues = []

    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
    except json.JSONDecodeError as e:
        issues.append(f"Invalid JSON: {e}")
        return issues
    except Exception as e:
        issues.append(f"Cannot read file: {e}")
        return issues

    # Check required keys
    required_keys = ['cells', 'metadata', 'nbformat', 'nbformat_minor']
    for key in required_keys:
        if key not in notebook:
            issues.append(f"Missing required key: {key}")

    # Check nbformat version
    if notebook.get('nbformat', 0) < 4:
        issues.append(f"Old notebook format: nbformat {notebook.get('nbformat')}")

    # Check cells
    cells = notebook.get('cells', [])
    if not cells:
        issues.append("No cells in notebook")
    else:
        for i, cell in enumerate(cells):
            if 'cell_type' not in cell:
                issues.append(f"Cell {i}: missing cell_type")
            if 'source' not in cell:
                issues.append(f"Cell {i}: missing source")

            cell_type = cell.get('cell_type', '')
            if cell_type not in ['markdown', 'code', 'raw']:
                issues.append(f"Cell {i}: invalid cell_type '{cell_type}'")

    # Check kernelspec
    metadata = notebook.get('metadata', {})
    kernelspec = metadata.get('kernelspec', {})
    if not kernelspec:
        issues.append("Missing kernelspec in metadata")
    elif 'name' not in kernelspec:
        issues.append("kernelspec missing 'name'")

    return issues


def count_cells_by_type(notebook_path: Path) -> dict:
    """Count cells by type in a notebook."""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
    except:
        return {}

    counts = {'markdown': 0, 'code': 0, 'raw': 0}
    for cell in notebook.get('cells', []):
        cell_type = cell.get('cell_type', 'unknown')
        if cell_type in counts:
            counts[cell_type] += 1

    return counts


def execute_notebook(
    notebook_path: Path,
    timeout: int = 300,
    kernel: str = 'python3'
) -> Tuple[bool, Optional[str]]:
    """
    Execute a notebook and return (success, error_message).

    Requires nbconvert to be installed.
    """
    try:
        # Create temp directory for output
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / notebook_path.name

            # Execute notebook using nbconvert
            result = subprocess.run(
                [
                    sys.executable, '-m', 'nbconvert',
                    '--to', 'notebook',
                    '--execute',
                    '--ExecutePreprocessor.timeout=' + str(timeout),
                    '--ExecutePreprocessor.kernel_name=' + kernel,
                    '--output', str(output_path),
                    str(notebook_path)
                ],
                capture_output=True,
                text=True,
                timeout=timeout + 30  # Extra buffer for nbconvert overhead
            )

            if result.returncode != 0:
                # Extract useful error info
                error_msg = result.stderr.strip() or result.stdout.strip()
                # Truncate long errors
                if len(error_msg) > 500:
                    error_msg = error_msg[:500] + "... (truncated)"
                return False, error_msg

            return True, None

    except subprocess.TimeoutExpired:
        return False, f"Execution timed out after {timeout}s"
    except FileNotFoundError:
        return False, "nbconvert not found. Install with: pip install nbconvert"
    except Exception as e:
        return False, str(e)


def validate_notebooks(
    notebook_paths: List[Path],
    execute: bool = False,
    timeout: int = 300,
    verbose: bool = False
) -> dict:
    """
    Validate a list of notebooks.

    Returns a summary dict with results.
    """
    results = {
        'total': len(notebook_paths),
        'valid': 0,
        'executed': 0,
        'failed': 0,
        'details': []
    }

    for nb_path in notebook_paths:
        detail = {
            'path': str(nb_path),
            'name': nb_path.name,
            'structure_valid': False,
            'structure_issues': [],
            'execution_attempted': False,
            'execution_passed': False,
            'execution_error': None,
            'cell_counts': {}
        }

        print(f"\nValidating: {nb_path.name}")
        print("-" * 50)

        # Structure validation
        issues = validate_notebook_structure(nb_path)
        detail['structure_issues'] = issues
        detail['cell_counts'] = count_cells_by_type(nb_path)

        if issues:
            print(f"  Structure: FAILED")
            for issue in issues:
                print(f"    - {issue}")
            results['failed'] += 1
        else:
            print(f"  Structure: OK")
            detail['structure_valid'] = True
            results['valid'] += 1

            if verbose:
                counts = detail['cell_counts']
                print(f"    Cells: {counts.get('code', 0)} code, "
                      f"{counts.get('markdown', 0)} markdown")

        # Execution (only if structure is valid)
        if execute and detail['structure_valid']:
            print(f"  Executing (timeout: {timeout}s)...")
            detail['execution_attempted'] = True

            success, error = execute_notebook(nb_path, timeout)

            if success:
                print(f"  Execution: PASSED")
                detail['execution_passed'] = True
                results['executed'] += 1
            else:
                print(f"  Execution: FAILED")
                print(f"    Error: {error}")
                detail['execution_error'] = error
                results['failed'] += 1
                results['valid'] -= 1  # Demote from valid if execution fails

        results['details'].append(detail)

    return results


def find_notebooks(directory: Path, pattern: str = "*.ipynb") -> List[Path]:
    """Find all notebooks in a directory matching a pattern."""
    notebooks = list(directory.glob(pattern))
    # Sort by name for consistent ordering
    return sorted(notebooks)


def print_summary(results: dict):
    """Print validation summary."""
    print("\n" + "=" * 50)
    print("VALIDATION SUMMARY")
    print("=" * 50)

    print(f"\nTotal notebooks: {results['total']}")
    print(f"Structure valid: {results['valid']}")

    if any(d['execution_attempted'] for d in results['details']):
        print(f"Execution passed: {results['executed']}")

    print(f"Failed: {results['failed']}")

    if results['failed'] > 0:
        print("\nFailed notebooks:")
        for detail in results['details']:
            if detail['structure_issues'] or (
                detail['execution_attempted'] and not detail['execution_passed']
            ):
                print(f"  - {detail['name']}")


def main():
    parser = argparse.ArgumentParser(
        description="Validate Jupyter notebooks for structure and execution",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python validate_notebooks.py                   # Validate all notebooks
    python validate_notebooks.py --execute         # Validate + execute
    python validate_notebooks.py notebooks/*.ipynb # Specific files
    python validate_notebooks.py --verbose         # Show cell counts

Educational Use Only - NexVigilant | Empowerment Through Vigilance
        """
    )

    parser.add_argument(
        'notebooks',
        nargs='*',
        type=Path,
        help="Specific notebook files to validate (default: all in notebooks/)"
    )

    parser.add_argument(
        '--execute', '-e',
        action='store_true',
        help="Execute notebooks to verify code runs"
    )

    parser.add_argument(
        '--timeout', '-t',
        type=int,
        default=300,
        help="Timeout per notebook in seconds (default: 300)"
    )

    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help="Show detailed information"
    )

    parser.add_argument(
        '--dir', '-d',
        type=Path,
        default=NOTEBOOKS_DIR,
        help="Directory containing notebooks (default: notebooks/)"
    )

    args = parser.parse_args()

    print("NexVigilant Notebook Validator")
    print("=" * 50)

    # Determine which notebooks to validate
    if args.notebooks:
        notebook_paths = args.notebooks
    else:
        if not args.dir.exists():
            print(f"Notebooks directory not found: {args.dir}")
            return 1
        notebook_paths = find_notebooks(args.dir)

    if not notebook_paths:
        print("No notebooks found to validate.")
        return 1

    print(f"Found {len(notebook_paths)} notebook(s)")
    if args.execute:
        print(f"Execution: ENABLED (timeout: {args.timeout}s)")
    else:
        print("Execution: DISABLED (structure check only)")

    # Run validation
    results = validate_notebooks(
        notebook_paths,
        execute=args.execute,
        timeout=args.timeout,
        verbose=args.verbose
    )

    # Print summary
    print_summary(results)

    # Return exit code
    if results['failed'] > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

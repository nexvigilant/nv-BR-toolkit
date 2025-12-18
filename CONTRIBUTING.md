# Contributing to the Benefit-Risk Intelligence Toolkit

Thank you for your interest in contributing to the NexVigilant Benefit-Risk Intelligence Toolkit!

## Important Notices

### Educational Purpose Only

This toolkit is designed exclusively for **educational and instructional purposes**. All contributions must align with this mission.

**Contributions must NOT:**
- Contain proprietary or confidential content
- Include real patient data or actual regulatory submissions
- Provide advice that could be used for regulatory decision-making
- Replace the need for professional judgment or internal SOPs

### What We Welcome

We welcome contributions that:

1. **Enhance Educational Value**
   - Improve clarity of explanations
   - Add helpful examples with hypothetical data
   - Create new exercises or case studies
   - Translate concepts for different audiences

2. **Improve Technical Quality**
   - Fix bugs in code examples
   - Improve code documentation
   - Add unit tests
   - Enhance visualization tools

3. **Expand Coverage**
   - Add new B-R methodologies (with references)
   - Include additional regulatory perspectives
   - Create supplementary learning materials
   - Develop interactive exercises

4. **Fix Issues**
   - Correct factual errors
   - Update outdated references
   - Improve accessibility
   - Fix formatting problems

## How to Contribute

### Reporting Issues

1. Check existing issues to avoid duplicates
2. Use a clear, descriptive title
3. Provide:
   - Description of the issue
   - Steps to reproduce (if applicable)
   - Expected vs actual behavior
   - Relevant file/module references

### Submitting Changes

1. **Fork the repository**

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-improvement
   ```

3. **Make your changes**
   - Follow existing code style
   - Include appropriate documentation
   - Use hypothetical data only
   - Add references for new concepts

4. **Test your changes**
   - Verify code runs without errors
   - Check Excel templates open correctly
   - Ensure documentation renders properly

5. **Commit with clear messages**
   ```bash
   git commit -m "Add: brief description of change"
   ```

   Use prefixes:
   - `Add:` for new features/content
   - `Fix:` for bug fixes
   - `Update:` for improvements to existing content
   - `Docs:` for documentation changes

6. **Push and create a Pull Request**
   ```bash
   git push origin feature/your-improvement
   ```
   Then open a PR against the `main` branch.

### Pull Request Guidelines

Your PR should include:

- [ ] Clear description of changes
- [ ] Rationale for the addition/change
- [ ] Confirmation that content is original or properly attributed
- [ ] Statement that no confidential/proprietary content is included
- [ ] Verification that examples use hypothetical data only

## Code Standards

### Python Code

- Follow PEP 8 style guidelines
- Include docstrings for all functions/classes
- Use type hints where appropriate
- Add inline comments for complex logic
- Include example usage in docstrings

```python
def calculate_win_ratio(treatment_wins: int, control_wins: int) -> float:
    """
    Calculate the win ratio for DOOR analysis.

    Args:
        treatment_wins: Number of pairwise comparisons where treatment wins
        control_wins: Number of pairwise comparisons where control wins

    Returns:
        Win ratio (treatment wins / control wins)

    Example:
        >>> calculate_win_ratio(150, 100)
        1.5
    """
    if control_wins == 0:
        return float('inf')
    return treatment_wins / control_wins
```

### Documentation

- Use clear, professional language
- Define technical terms on first use
- Include references for methodological claims
- Use consistent formatting

### Excel Templates

- Include instructions on first sheet or within cells
- Use data validation where appropriate
- Protect formulas from accidental editing
- Include example data that can be cleared

## Attribution

- All external content must be properly attributed
- Include references to source publications
- Credit original authors/organizations
- Use CC-compatible content only

## Questions?

If you have questions about contributing:

1. Check the README and existing documentation
2. Review closed issues for similar questions
3. Open a new issue with the "question" label
4. Contact: education@nexvigilant.com

## Code of Conduct

Contributors are expected to:

- Be respectful and professional
- Focus on educational improvement
- Provide constructive feedback
- Support fellow contributors
- Maintain the toolkit's educational mission

---

Thank you for helping make benefit-risk assessment education more accessible!

**NexVigilant**
*Empowerment Through Vigilance*

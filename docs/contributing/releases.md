# Release Process

This document describes the release workflow for the NexVigilant B-R Intelligence Toolkit.

---

## Semantic Versioning

We follow [Semantic Versioning](https://semver.org/) (SemVer):

- **MAJOR** (`X.0.0`): Breaking changes or major overhauls
- **MINOR** (`0.X.0`): New features, modules, or significant enhancements
- **PATCH** (`0.0.X`): Bug fixes, documentation updates, minor improvements

### Version Examples

| Version | Reason |
|---------|--------|
| `v1.0.0` | Initial stable release |
| `v1.1.0` | Added new module or major feature |
| `v1.1.1` | Fixed broken links or typos |
| `v2.0.0` | Complete curriculum restructure |

---

## Creating a Release

### Prerequisites

1. All changes committed and pushed to `main` branch
2. QA suite passes (automated via GitHub Actions)
3. Documentation is up to date

### Step 1: Update Changelog (Optional)

If you maintain a manual changelog, update `CHANGELOG.md`:

```markdown
## [1.2.0] - 2025-12-18

### Added
- New visualization tutorials
- Interactive knowledge checks

### Changed
- Updated regulatory references

### Fixed
- Broken links in Module 3
```

### Step 2: Create and Push Tag

```bash
# Ensure you're on main branch with latest changes
git checkout main
git pull origin main

# Create annotated tag
git tag -a v1.2.0 -m "Release v1.2.0: Added visualization tutorials"

# Push the tag to trigger release workflow
git push origin v1.2.0
```

### Step 3: Automated Release

Once the tag is pushed, GitHub Actions automatically:

1. Generates changelog from commits since last tag
2. Creates release notes with installation instructions
3. Bundles templates and notebooks as release assets
4. Creates the GitHub Release

### Step 4: Verify Release

1. Go to [Releases](https://github.com/nexvigilant/nv-BR-toolkit/releases)
2. Verify release notes are accurate
3. Test download links work
4. Announce release (optional)

---

## Pre-Release Versions

For testing or preview releases, use pre-release suffixes:

```bash
# Alpha release
git tag -a v1.3.0-alpha.1 -m "Alpha: New MCDA features"

# Beta release
git tag -a v1.3.0-beta.1 -m "Beta: Testing new module"

# Release candidate
git tag -a v1.3.0-rc.1 -m "RC1: Final testing"
```

Pre-releases are automatically marked as such in GitHub.

---

## Hotfix Releases

For urgent fixes to released versions:

```bash
# Create hotfix branch from release tag
git checkout -b hotfix/1.2.1 v1.2.0

# Make fixes
git add .
git commit -m "fix: corrected regulatory citation"

# Merge to main
git checkout main
git merge hotfix/1.2.1

# Tag and release
git tag -a v1.2.1 -m "Hotfix: Corrected regulatory citation"
git push origin main --tags
```

---

## Release Checklist

Before creating a release:

- [ ] All QA checks pass (`npm run qa` or GitHub Actions)
- [ ] Documentation reviewed and updated
- [ ] No broken internal links
- [ ] All notebooks execute without errors
- [ ] Templates are current and complete
- [ ] Educational disclaimers present in all modules
- [ ] NexVigilant branding consistent

---

## Rollback Procedure

If a release needs to be reverted:

```bash
# Delete the tag locally and remotely
git tag -d v1.2.0
git push origin :refs/tags/v1.2.0

# Delete the GitHub Release through the web UI
# Then fix issues and create new release
```

---

## Automated Workflows

### QA Suite (`.github/workflows/qa.yml`)

Runs on every push and PR:

- Link validation
- Notebook structure checks
- Branding consistency
- Educational disclaimers
- Template completeness

### Release (`.github/workflows/release.yml`)

Triggered by version tags (`v*.*.*`):

- Generates changelog
- Creates GitHub Release
- Bundles assets

### Notebook Tests (`.github/workflows/notebook-tests.yml`)

Validates Jupyter notebooks:

- Structure validation
- Execution testing (optional)
- Dependency checks

---

## Questions?

Open a [Discussion](https://github.com/nexvigilant/nv-BR-toolkit/discussions) for release-related questions.

---

!!! info "Educational Disclaimer"
    This release process documentation is provided for **educational purposes** to demonstrate software release best practices. Adapt as needed for your organization's requirements.

---

*NexVigilant — Empowerment Through Vigilance*

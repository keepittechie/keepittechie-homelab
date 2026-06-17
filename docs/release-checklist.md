# Release Checklist

Use this checklist for future documentation releases. A release should mark a meaningful public documentation milestone, not every small typo fix.

## Before Opening The Release PR

- [ ] Update `CHANGELOG.md`.
- [ ] Update or create release notes under `docs/releases/`.
- [ ] Confirm README version and release links are current.
- [ ] Confirm the documentation index links to the release docs.
- [ ] Confirm examples are sanitized.
- [ ] Confirm screenshots are absent or reviewed with the screenshot policy.

## Local Checks

- [ ] Run `python3 scripts/check_markdown_links.py`.
- [ ] Run `python3 scripts/check_diagrams.py`.
- [ ] Run `python3 scripts/public_safety_scan.py`.
- [ ] Run `git diff --check`.
- [ ] Confirm Mermaid diagrams render on GitHub.
- [ ] Confirm important README links work.

## Pull Request

- [ ] Open a release-focused pull request.
- [ ] Confirm GitHub Actions pass.
- [ ] Review the diff for unexpected binary files.
- [ ] Confirm no private configs, screenshots, credentials, or raw exports were added.
- [ ] Squash merge after review.

## After Merge

- [ ] Tag the release after merge.
- [ ] Create GitHub release notes from the public-safe release draft.
- [ ] Do not attach archives that include private configs, screenshots, logs, or exports.

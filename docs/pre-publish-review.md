# Pre-Publish Review Checklist

Use this checklist before publishing, merging, or sharing updates from the public homelab repo.

## Safety Review

- [ ] Run `python3 scripts/public_safety_scan.py`.
- [ ] Run secret-pattern scan.
- [ ] Run private domain scan.
- [ ] Run private IP scan.
- [ ] Review screenshots with the [Screenshot Policy](screenshots-policy.md).
- [ ] Review visual assets with the [Visual Assets Guide](visual-assets-guide.md).
- [ ] Check images at full size before commit.
- [ ] Confirm browser UI is cropped or blurred if needed.
- [ ] Confirm no screenshots were added without review.
- [ ] Review config snippets for secrets.
- [ ] Confirm files under `examples/` use sanitized placeholders only.
- [ ] Confirm no private `.env` files are tracked.
- [ ] Confirm no raw firewall/router/NAS exports are tracked.

## Documentation Review

- [ ] Run `python3 scripts/check_markdown_links.py`.
- [ ] Run `python3 scripts/check_diagrams.py`.
- [ ] Run `git diff --check`.
- [ ] README links work.
- [ ] Service matrix is current.
- [ ] Roadmap reflects current status.
- [ ] Documentation index is updated.
- [ ] New docs are linked from the right index page.
- [ ] Glossary terms were reviewed for new beginner-facing terms.
- [ ] Service page structure remains consistent.
- [ ] Diagrams are sanitized.
- [ ] License section is present.
- [ ] Public-facing language review is complete.
- [ ] Viewer-facing navigation links to the [Viewer Guide](viewer-guide.md) and examples.

## GitHub Review

- [ ] GitHub Actions pass.
- [ ] Docs Quality workflow passes.
- [ ] Pull request diff reviewed.
- [ ] Pull request checklist is complete.
- [ ] No unexpected binary files were added.

## Release Readiness

- [ ] `CHANGELOG.md` is updated.
- [ ] Release notes are updated under `docs/releases/`.
- [ ] Docs quality scripts pass.
- [ ] Public-safety scan passes.
- [ ] README version and release links are current.
- [ ] Release checklist is reviewed for release-focused PRs.

Related docs:

- [GitHub Repo Settings Guide](github-repo-settings.md)
- [Release Checklist](release-checklist.md)
- [Screenshot Policy](screenshots-policy.md)
- [Visual Assets Guide](visual-assets-guide.md)
- [Assets Index](../assets/README.md)
- [Contributing Guide](../CONTRIBUTING.md)

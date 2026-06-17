# Pre-Publish Review Checklist

Use this checklist before publishing, merging, or sharing updates from the public homelab repo.

## Safety Review

- [ ] Run secret-pattern scan.
- [ ] Run private domain scan.
- [ ] Run private IP scan.
- [ ] Review screenshots with the [Screenshot Policy](screenshots-policy.md).
- [ ] Review config snippets for secrets.
- [ ] Confirm files under `examples/` use sanitized placeholders only.
- [ ] Confirm no private `.env` files are tracked.
- [ ] Confirm no raw firewall/router/NAS exports are tracked.

## Documentation Review

- [ ] README links work.
- [ ] Service matrix is current.
- [ ] Roadmap reflects current status.
- [ ] Diagrams are sanitized.
- [ ] License section is present.
- [ ] Public-facing language review is complete.
- [ ] Viewer-facing navigation links to the [Viewer Guide](viewer-guide.md) and examples.

## GitHub Review

- [ ] GitHub Actions pass.
- [ ] Pull request diff reviewed.
- [ ] Pull request checklist is complete.
- [ ] No unexpected binary files were added.

Related docs:

- [GitHub Repo Settings Guide](github-repo-settings.md)
- [Screenshot Policy](screenshots-policy.md)
- [Contributing Guide](../CONTRIBUTING.md)

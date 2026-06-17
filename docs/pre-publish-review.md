# Pre-Publish Review Checklist

Use this checklist before publishing, merging, or sharing updates from the public homelab repo.

## Safety Review

- [ ] Run secret-pattern scan.
- [ ] Run private domain scan.
- [ ] Run private IP scan.
- [ ] Review screenshots for sensitive data.
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

## GitHub Review

- [ ] GitHub Actions pass.
- [ ] Pull request diff reviewed.
- [ ] No unexpected binary files were added.

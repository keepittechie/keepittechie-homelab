# Repo Maintenance Checklist

Use this checklist for ongoing repo maintenance. For a final review before publishing or merging, use the [Pre-Publish Review Checklist](pre-publish-review.md).

## Before Each Commit

- [ ] Review `git status`.
- [ ] Review the diff for every changed file.
- [ ] Run the grep-based secret scan.
- [ ] Confirm `.env.example` still contains placeholders only.
- [ ] Confirm private configs are not staged.
- [ ] Confirm raw firewall, router, switch, NAS, and app exports are not staged.

## Documentation Updates

- [ ] Update the service matrix when services move, change roles, or change exposure level.
- [ ] Update the roadmap when phases are completed or new public docs are planned.
- [ ] Update diagrams when the architecture changes.
- [ ] Confirm links still point to existing files.
- [ ] Update learning paths when guides change.

## Public Safety Review

- [ ] Replace live domains with `home.example.com`.
- [ ] Replace detailed live network data with `10.10.0.0/24` examples.
- [ ] Remove screenshots that show credentials, account IDs, private records, or public IPs.
- [ ] Keep personal app examples fake and sanitized.
- [ ] Keep Cloudflare Tunnel credentials and route internals out of Git.

## GitHub Checks

- [ ] Review GitHub Actions results.
- [ ] Fix secret scan failures before merging.
- [ ] Confirm documentation-only changes do not accidentally add generated archives or exports.

## Periodic Review

- [ ] Revisit service README files after major lab changes.
- [ ] Add restore test evidence for critical services as it becomes available.
- [ ] Prune stale placeholders that no longer help viewers.
- [ ] Keep the repo focused on teaching architecture and operations, not dumping private configs.

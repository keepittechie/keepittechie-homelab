# GitHub Repo Settings Guide

This page documents recommended public GitHub settings for the KeepItTechie homelab repo. It is a guide only; it does not change any GitHub settings.

## Suggested Description

```text
Public-safe documentation, diagrams, and sanitized examples for the KeepItTechie homelab.
```

## Suggested Website Link

Use a public-safe link such as a channel page, project landing page, or published documentation page.

Do not use a private dashboard, internal service URL, live homelab URL, or admin endpoint as the repo website link.

## Suggested Topics

```text
homelab
self-hosted
linux
proxmox
pfsense
pihole
nginx
grafana
prometheus
zfs
nas
local-ai
open-source
documentation
```

## Branch Protection

Recommended settings for the default branch:

- Require pull requests before merging.
- Require the basic secret scan workflow to pass.
- Require review for changes that add examples, diagrams, screenshots, or security guidance.
- Prevent force pushes to the default branch.
- Keep direct pushes limited to trusted maintainers.

## Merge Preference

Squash merge is a good default for this repo because most changes are documentation-focused. It keeps the public history readable while preserving the pull request discussion.

Suggested commit style:

```text
docs: add public-safe monitoring diagram
docs: polish viewer navigation
docs: add sanitized reverse proxy example
```

## GitHub Actions Checks

The basic secret scan should remain enabled for pull requests and pushes. It is intentionally simple and may catch false positives, but that is useful for a public repo where safety matters more than convenience.

When a false positive appears, prefer changing the example wording or placeholder path before weakening the scan.

## Public Repo Safety Note

The repo should document architecture, teaching patterns, and sanitized examples. It should not contain live service URLs, exact private host addresses, private screenshots, credentials, raw exports, or private operational runbooks.

Related docs:

- [Pre-Publish Review Checklist](pre-publish-review.md)
- [Screenshot Policy](screenshots-policy.md)
- [Contributing Guide](../CONTRIBUTING.md)

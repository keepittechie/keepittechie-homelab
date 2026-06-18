# Visual Assets Guide

This page explains how visual assets should be planned, reviewed, and added to the public KeepItTechie homelab repo.

## Why Visuals Matter

Visuals help readers understand the lab faster. A clear diagram, demo dashboard, flow chart, or service layout can make a concept easier to follow than a long paragraph.

The tradeoff is risk. Images can leak private details that are easy to miss in a quick review, such as browser bookmarks, internal URLs, usernames, terminal paths, dashboard labels, app data, or API details. Treat every image like a config snippet: review it before publishing.

## Safe Visual Types

| Visual Type | Why It Is Safer |
|---|---|
| Mermaid diagrams | Render from sanitized Markdown and are easy to review in text form |
| Sanitized diagrams exported as PNG/SVG | Useful for sharing when all labels use public-safe examples |
| Fake/demo dashboard screenshots | Teach layout and signal types without live infrastructure |
| Cropped screenshots with no private data | Keep attention on one public-safe concept |
| Mockups made from sanitized examples | Good for planned dashboards, thumbnails, or service maps |
| Social preview images that do not show real configs | Useful for sharing the repo without leaking lab details |
| Terminal screenshots using fake paths and fake hostnames | Safer than live terminal captures when teaching commands |

## Risky Visual Types

| Visual Type | Why It Is Risky |
|---|---|
| Real Grafana dashboards | Can expose hostnames, URLs, service names, and operational state |
| pfSense firewall pages | Can reveal rules, networks, aliases, and edge policy |
| Pi-hole admin pages | Can expose local DNS records, query logs, and clients |
| Proxmox VM lists | Can reveal hostnames, VM roles, IDs, and resource layout |
| Cloudflare Tunnel pages | Can expose routes, tunnel details, and account context |
| Nextcloud file views | Can expose real files, users, and folders |
| FinanceHQ or CareerFill pages | Can expose financial or career data |
| Browser windows with bookmarks or logged-in user data | Can expose accounts, apps, and browsing context |
| Terminals showing real paths, usernames, hostnames, or tokens | Can reveal private system details in plain text |

## Screenshot Review Checklist

- [ ] No real public IPs
- [ ] No exact private host IPs
- [ ] No private domains
- [ ] No usernames or email addresses
- [ ] No tokens, API keys, or secrets
- [ ] No Cloudflare tunnel IDs
- [ ] No private cert paths
- [ ] No browser bookmarks or history
- [ ] No financial or career data
- [ ] No private files or documents
- [ ] No private chat logs or AI prompts
- [ ] No database names if sensitive
- [ ] No raw firewall/router/NAS exports
- [ ] Image reviewed at full size before commit

## Sanitized Demo Dashboard Ideas

Future visuals can use fake data to teach the pattern without exposing the live lab:

- Fake Grafana overview dashboard.
- Fake service status dashboard.
- Fake backup status dashboard.
- Fake DNS flow mockup.
- Fake local AI request flow.
- Fake reverse proxy route map.
- Fake storage layout diagram.

## Thumbnail and Social Preview Ideas

Potential public-safe thumbnail or social preview concepts:

- KeepItTechie Homelab Map.
- DNS to Proxy to Apps.
- Backups Are Not Real Until Restore Works.
- Local AI on Linux.
- Do Not Expose Everything.

These should use recreated graphics, sanitized labels, and simple visual metaphors instead of screenshots from live tools.

## File Naming and Location

Planned visual assets should live under `assets/`:

```text
assets/
  README.md
  diagrams/
  screenshots/
  thumbnails/
  mockups/
```

Recommended file naming:

```text
assets/diagrams/homelab-overview-public-safe.png
assets/screenshots/grafana-demo-overview.png
assets/thumbnails/local-ai-on-linux.png
assets/mockups/reverse-proxy-route-map.png
```

Use names that describe the visual and make the public-safe intent obvious. Avoid names that include private hostnames, private app names, dates tied to incidents, or sensitive workflows.

## What Should Never Be Added

- Raw screenshots from sensitive dashboards.
- Unreviewed terminal screenshots.
- Unredacted browser screenshots.
- Exports containing secrets.
- Real app data.
- Private documents.
- Real prompts or chat history.
- Anything that bypasses the screenshot policy.

## Related Docs

- [Screenshot Policy](screenshots-policy.md)
- [Pre-Publish Review](pre-publish-review.md)
- [Diagram Index](../diagrams/README.md)
- [Current Setup](current-setup.md)
- [Service Catalog](service-catalog.md)
- [Assets Index](../assets/README.md)

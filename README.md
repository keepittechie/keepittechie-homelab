# KeepItTechie Homelab

![Docs](https://img.shields.io/badge/docs-public--safe-blue)
![Version](https://img.shields.io/badge/docs-v0.1.0-blue)
![License](https://img.shields.io/badge/license-CC%20BY%204.0-green)
![Homelab](https://img.shields.io/badge/homelab-linux%20%7C%20self--hosted-lightgrey)

This repo is the public-safe tour map for the KeepItTechie homelab. It shows how the lab is put together, why each layer exists, and what viewers can learn from running real Linux and open source services at home.

Think of it as a teaching repo, not a config dump. The docs explain the patterns behind pfSense, Pi-hole, Proxmox, storage, backups, monitoring, media workflows, local AI, dashboards, and automation without exposing private infrastructure details.

Current documentation baseline: [v0.1.0](docs/releases/v0.1.0.md). See the [changelog](CHANGELOG.md) for release history.

## Start Here

| Start With | Link | Why |
|---|---|---|
| Tour the lab | [Current Setup](docs/current-setup.md) | See what is running and why it exists |
| Build in stages | [Build Your Own Homelab](docs/build-your-own.md) | Start small and add one layer at a time |
| Follow a path | [Viewer Guide](docs/viewer-guide.md) | Choose the best route through the repo |
| Find everything | [Documentation Index](docs/docs-index.md) | Browse every major guide by topic |
| Learn the terms | [Glossary](docs/glossary.md) | Look up homelab vocabulary as you read |
| See the map | [Diagrams](diagrams/README.md) | Follow sanitized architecture and service flows |
| Study examples | [Sanitized Examples](examples/README.md) | Learn safe config patterns without private values |
| Browse services | [Service Catalog](docs/service-catalog.md) | Pick a service and learn what it does |
| Compare services | [Service Matrix](docs/service-matrix.md) | Compare access level, host role, and backup priority |
| Big picture | [Homelab Overview](docs/overview.md) | Understand the purpose and layout |
| Core stack | [Core Infrastructure](docs/core-infrastructure.md) | Read the first deep dives in order |
| Storage and monitoring | [Storage and Monitoring](docs/storage-monitoring.md) | Understand storage, backups, restore proof, and visibility |
| Apps and AI | [Apps and AI](docs/apps-and-ai.md) | Explore local AI, media, dashboards, docs, personal apps, and automation |
| Security | [Security Notes](docs/security-notes.md) | Learn what stays private |

## Homelab Areas

The lab is easier to understand when it is broken into roles instead of treated like one big stack.

| Area | Main Docs | Service Docs |
|---|---|---|
| Network | [Core Infrastructure](docs/core-infrastructure.md), [Network Design](docs/network.md) | [pfSense](services/pfsense/README.md), [Pi-hole](services/pihole/README.md), [Reverse Proxy](services/reverse-proxy/README.md), [Cloudflare Tunnel](services/cloudflare-tunnel/README.md) |
| Virtualization | [Core Infrastructure](docs/core-infrastructure.md), [Hardware](docs/hardware.md), [Public-Safe Inventory](docs/inventory-public.md), [Service Matrix](docs/service-matrix.md) | [Proxmox](services/proxmox/README.md) |
| Storage and backups | [Storage and Monitoring](docs/storage-monitoring.md), [Storage and Backups](docs/storage-and-backups.md) | [Synology](services/synology/README.md), [ZFS Storage](services/zfs-storage/README.md), [Proxmox Backup Server](services/proxmox-backup-server/README.md) |
| Observability | [Storage and Monitoring](docs/storage-monitoring.md), [Service Matrix](docs/service-matrix.md) | [Monitoring](services/monitoring/README.md) |
| Media | [Apps and AI](docs/apps-and-ai.md), [Service Matrix](docs/service-matrix.md) | [Media Stack](services/media-stack/README.md) |
| Local AI | [Apps and AI](docs/apps-and-ai.md), [Content Map](docs/content-map.md) | [Local AI](services/local-ai/README.md) |
| Documentation and dashboard | [Apps and AI](docs/apps-and-ai.md), [Diagrams](diagrams/README.md) | [Wiki.js](services/wiki/README.md), [Glance Dashboard](services/glance/README.md) |
| Personal apps | [Apps and AI](docs/apps-and-ai.md), [Security Notes](docs/security-notes.md) | [FinanceHQ](services/financehq/README.md), [CareerFill](services/careerfill/README.md) |
| Automation | [Apps and AI](docs/apps-and-ai.md), [Maintenance Checklist](docs/maintenance-checklist.md) | [AWX / Ansible](services/automation-awx/README.md) |

## Sanitized Examples

The [examples directory](examples/README.md) contains public-safe templates for common homelab patterns:

- [NGINX reverse proxy](examples/nginx/README.md)
- [Docker Compose apps](examples/docker-compose/README.md)
- [Prometheus scrape config](examples/prometheus/README.md)
- [Pi-hole local DNS records](examples/pihole/README.md)
- [Cloudflare Tunnel config shape](examples/cloudflare-tunnel/README.md)
- [Environment file placeholders](examples/env/README.md)

These examples are teaching templates, not production config dumps. Replace placeholder values only in private config, and never commit real credentials.

## Current Architecture

The sanitized high-level architecture is documented here:

- [Mermaid homelab overview](diagrams/homelab-overview.md)
- [Diagram index](diagrams/README.md)

At a high level, the flow is:

```text
Internet
  -> Cloudflare Tunnel / VPN
  -> pfSense
  -> LAN / VLANs
  -> Pi-hole DNS
  -> Proxmox workloads
  -> Storage, monitoring, media, local AI, personal apps, and automation
```

All names and networks in public examples use sanitized values such as `home.example.com` and `10.10.0.0/24`.

## Diagrams

| Diagram | Use It To Understand |
|---|---|
| [Homelab Overview](diagrams/homelab-overview.md) | The full sanitized architecture |
| [DNS Flow](diagrams/dns-flow.md) | pfSense DHCP, Pi-hole, local records, and upstream DNS |
| [Backup Flow](diagrams/backup-flow.md) | VM backups, app data, ZFS snapshots, and restore testing |
| [Reverse Proxy Flow](diagrams/reverse-proxy-flow.md) | Internal HTTPS and selected public access |
| [Local AI Flow](diagrams/local-ai-flow.md) | Open WebUI, local API endpoint, llama.cpp, model storage, and GPU runtime |
| [Monitoring Flow](diagrams/monitoring-flow.md) | Exporters, Prometheus, Loki, Grafana, alerts, and review loops |

## What This Repo Is / Is Not

| This Repo Is | This Repo Is Not |
|---|---|
| A public learning resource for KeepItTechie viewers | A dump of private production configs |
| A sanitized architecture guide | A live DNS zone or firewall export |
| A companion to homelab videos | A credential store |
| A rebuild and documentation aid | A full backup of the lab |
| A place for safe examples | A place for real secrets, keys, or private data |

Short version: this repo teaches the lab design. It is not a live backup, inventory export, credential store, or screenshot dump.

## How To Use This Repo

1. Tour the [current setup](docs/current-setup.md).
2. Use [Build Your Own Homelab](docs/build-your-own.md) if you want to build something similar in stages.
3. Open the [diagram index](diagrams/README.md) to see the flows visually.
4. Browse the [service catalog](docs/service-catalog.md) or [service matrix](docs/service-matrix.md).
5. Read the service README for the part of the lab you want to understand.
6. Compare the docs with the [sanitized examples](examples/README.md).
7. Check [Security Notes](docs/security-notes.md) before adapting any pattern in a public repo.

For a beginner-friendly walkthrough, use the [Viewer Guide](docs/viewer-guide.md). For deeper navigation, use the [Documentation Index](docs/docs-index.md) and [Glossary](docs/glossary.md).

## YouTube Companion Series

This repo is designed to support KeepItTechie videos. The companion plan is here:

- [YouTube Companion Series](docs/youtube-series.md)
- [Content Map](docs/content-map.md)

Planned topics include the full homelab tour, pfSense, Pi-hole, Proxmox, Proxmox Backup Server, Synology vs ZFS, reverse proxying, Cloudflare Tunnel, Grafana monitoring, local AI, dashboards, AWX, and local-first personal apps.

## Security First

This repo should never contain:

- Real passwords or recovery codes
- API keys, service account credentials, or tunnel credentials
- SSH private keys, VPN keys, or backup encryption keys
- Private certificates or certificate authority keys
- Full pfSense, switch, NAS, or app exports with secrets
- Real public IP addresses
- Raw `.env` files
- Financial data, job application data, private messages, or personal records

Use `.env.example`, sanitized YAML, diagrams, and Markdown explanations instead. A good public doc should explain the pattern without leaking the real system.

Screenshots need the same review as config snippets. See the [Screenshot Policy](docs/screenshots-policy.md) before adding images.

## Quality Checks

Pull requests run lightweight documentation checks for Markdown links, diagram structure, public-safety patterns, and whitespace. The same checks can be run locally from [scripts/README.md](scripts/README.md).

## Repo Layout

| Path | Purpose |
|---|---|
| `docs/` | Main viewer-facing documentation |
| `services/` | Per-service breakdowns |
| `diagrams/` | Public-safe architecture diagrams and placeholders |
| `examples/` | Sanitized configuration examples and templates |
| `inventory/sanitized/` | Safe example inventory |
| `inventory/private.example/` | Pattern for private inventory that should stay untracked |
| `scripts/` | Lightweight documentation quality and public-safety checks |
| `templates/` | Reusable documentation templates |

## Contributing

This is mainly a public documentation repo for the KeepItTechie homelab, but typo fixes, diagram improvements, sanitized examples, and beginner-friendly documentation improvements are welcome.

- [Contributing guide](CONTRIBUTING.md)
- [Pull request template](.github/pull_request_template.md)
- [Issue templates](.github/ISSUE_TEMPLATE/)
- [GitHub repo settings guide](docs/github-repo-settings.md)
- [Release checklist](docs/release-checklist.md)

## License

This homelab documentation is licensed under the [Creative Commons Attribution 4.0 International License](LICENSE).

You are free to share and adapt the material as long as you give appropriate credit to Joshua Lacy / KeepItTechie.

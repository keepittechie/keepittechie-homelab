# Documentation Index

Use this page when the README is too high-level and a more complete map of the repo is useful.

## Start Here

| Page | Purpose |
|---|---|
| [Viewer Guide](viewer-guide.md) | Beginner-friendly path through the repo |
| [Current Setup](current-setup.md) | Public-safe tour of what is running and why |
| [Build Your Own Homelab](build-your-own.md) | Staged path for building a beginner-friendly lab |
| [Homelab Overview](overview.md) | Big-picture design and service roles |
| [Hardware](hardware.md) | Public-safe hardware roles and learning value |
| [Public-Safe Inventory](inventory-public.md) | Sanitized role-based inventory view |
| [Service Catalog](service-catalog.md) | Friendly service list grouped by category |
| [Glossary](glossary.md) | Short definitions for common homelab terms |
| [Service Matrix](service-matrix.md) | Service-by-service comparison |
| [How To Read Service Pages](how-to-read-service-pages.md) | Explains the standard service README sections |

## Architecture and Diagrams

| Page | Purpose |
|---|---|
| [Diagram Index](../diagrams/README.md) | Public-safe Mermaid diagrams |
| [Visual Assets Guide](visual-assets-guide.md) | Planning and review guide for future public-safe visuals |
| [Assets Index](../assets/README.md) | Placeholder folder map for future reviewed assets |
| [Homelab Overview Diagram](../diagrams/homelab-overview.md) | High-level architecture flow |
| [DNS Flow](../diagrams/dns-flow.md) | Internal DNS and Pi-hole flow |
| [Backup Flow](../diagrams/backup-flow.md) | Backup and restore test flow |
| [Reverse Proxy Flow](../diagrams/reverse-proxy-flow.md) | Internal HTTPS and selected public access |
| [Local AI Flow](../diagrams/local-ai-flow.md) | Local AI request path |
| [Monitoring Flow](../diagrams/monitoring-flow.md) | Metrics, logs, dashboards, and review loop |

## Core Infrastructure

| Page | Purpose |
|---|---|
| [Core Infrastructure](core-infrastructure.md) | Firewall, DNS, virtualization, backups, proxying, and tunnel overview |
| [Network Design](network.md) | DNS, segmentation, firewall principles, and troubleshooting |
| [pfSense](../services/pfsense/README.md) | Firewall and routing deep dive |
| [Pi-hole](../services/pihole/README.md) | DNS and filtering deep dive |
| [Proxmox](../services/proxmox/README.md) | Virtualization deep dive |
| [Reverse Proxy](../services/reverse-proxy/README.md) | Internal HTTPS routing deep dive |
| [Cloudflare Tunnel](../services/cloudflare-tunnel/README.md) | Selected public access deep dive |

## Storage, Backups, and Monitoring

| Page | Purpose |
|---|---|
| [Storage and Monitoring](storage-monitoring.md) | Reading path for storage, backup, and visibility topics |
| [Storage and Backups](storage-and-backups.md) | Backup model, NAS shares, ZFS snapshots, and restore test evidence |
| [Synology NAS](../services/synology/README.md) | Shared storage deep dive |
| [ZFS Storage](../services/zfs-storage/README.md) | Linux ZFS learning deep dive |
| [Proxmox Backup Server](../services/proxmox-backup-server/README.md) | VM backup target deep dive |
| [Monitoring](../services/monitoring/README.md) | Grafana, Prometheus, Loki, and exporters deep dive |

## Apps, Media, and Local AI

| Page | Purpose |
|---|---|
| [Apps and AI](apps-and-ai.md) | Reading path for apps, media, dashboards, docs, local AI, and automation |
| [Local AI](../services/local-ai/README.md) | GPU, local endpoint, llama.cpp, and Open WebUI deep dive |
| [Media Stack](../services/media-stack/README.md) | Plex and media automation overview |
| [Wiki.js](../services/wiki/README.md) | Documentation hub overview |
| [Nextcloud](../services/nextcloud/README.md) | Private cloud overview |
| [Glance / Homepage Dashboard](../services/glance/README.md) | Dashboard and link grouping overview |
| [FinanceHQ](../services/financehq/README.md) | Local-first finance app boundary |
| [CareerFill](../services/careerfill/README.md) | Local-first career workflow boundary |
| [AWX / Ansible](../services/automation-awx/README.md) | Automation controller overview |

## Examples and Templates

| Page | Purpose |
|---|---|
| [Sanitized Examples](../examples/README.md) | Public-safe example index |
| [NGINX Example](../examples/nginx/README.md) | Reverse proxy server block pattern |
| [Docker Compose Examples](../examples/docker-compose/README.md) | App and dashboard compose patterns |
| [Prometheus Example](../examples/prometheus/README.md) | Metrics scrape pattern |
| [Pi-hole DNS Example](../examples/pihole/README.md) | Local DNS record format |
| [Cloudflare Tunnel Example](../examples/cloudflare-tunnel/README.md) | Tunnel config shape without credentials |
| [Env Example](../examples/env/README.md) | Placeholder environment file pattern |
| [Service Template](../templates/service-template.md) | Reusable service README structure |

## Safety and Contribution

| Page | Purpose |
|---|---|
| [Security Notes](security-notes.md) | What stays private and how examples are sanitized |
| [Pre-Publish Review](pre-publish-review.md) | Checklist before publishing or merging |
| [Screenshot Policy](screenshots-policy.md) | Screenshot review rules |
| [Visual Assets Guide](visual-assets-guide.md) | Visual review rules and asset planning |
| [Contributing](../CONTRIBUTING.md) | Contribution guidance |
| [GitHub Repo Settings](github-repo-settings.md) | Suggested public repo settings |

## Release and Maintenance

| Page | Purpose |
|---|---|
| [Changelog](../CHANGELOG.md) | Release history for public documentation milestones |
| [v0.1.0 Release Notes](releases/v0.1.0.md) | First public documentation baseline |
| [Release Checklist](release-checklist.md) | Checklist for future documentation releases |
| [Pre-Publish Review](pre-publish-review.md) | Public-safe review before publishing or merging |
| [Local Quality Scripts](../scripts/README.md) | How to run documentation quality checks locally |

## Planning and Roadmap

| Page | Purpose |
|---|---|
| [Documentation Roadmap](roadmap.md) | Completed phases and future work |
| [Maintenance Checklist](maintenance-checklist.md) | Ongoing repo maintenance checklist |
| [YouTube Companion Series](youtube-series.md) | Video topic plan tied to repo docs |
| [Episode Companion Pages](episodes/README.md) | Viewer-facing pages tied to KeepItTechie videos |
| [Full Homelab Tour Companion](episodes/full-homelab-tour.md) | First episode guide for the broad lab tour |
| [Homelab DNS and Pi-hole Companion](episodes/dns-pihole.md) | Episode guide for local DNS, filtering, and service names |
| [Proxmox VM Layout Companion](episodes/proxmox-vm-layout.md) | Episode guide for virtualization and VM organization |
| [Homelab Backups and Restore Testing Companion](episodes/backups-restore.md) | Episode guide for backup strategy, PBS, and restore verification |
| [Homelab Monitoring with Grafana and Prometheus Companion](episodes/monitoring-grafana.md) | Episode guide covering metrics, logs, uptime checks, and dashboards |
| [Homelab Reverse Proxy and Internal HTTPS Companion](episodes/reverse-proxy.md) | Episode guide covering reverse proxying, TLS, and selected public access |
| [Local AI on Linux Companion](episodes/local-ai.md) | Episode guide covering local AI services, endpoints, and privacy boundaries |
| [Content Map](content-map.md) | Repo-to-content mapping |

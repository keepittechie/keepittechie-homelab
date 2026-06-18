# Content Map

This page maps the repo by learning topic. It is meant to help readers connect a homelab area to the docs, diagrams, guides, and sanitized examples that explain it.

For guided reading paths, see [Learning Paths](learning-paths.md).

## Topic Map

| Topic | Reader Takeaway | Start Here |
|---|---|---|
| Full homelab overview | How the major pieces fit together without getting lost in tools | [Current Setup](current-setup.md), [Full Homelab Tour Guide](guides/full-homelab-tour.md) |
| pfSense firewall design | Basic routing, DHCP, firewall policy, and safe exposure boundaries | [Network Design](network.md), [pfSense](../services/pfsense/README.md) |
| Pi-hole DNS pair | Local DNS, redundancy, filtering, and service names | [Homelab DNS and Pi-hole](guides/dns-pihole.md), [Pi-hole](../services/pihole/README.md) |
| Proxmox virtualization | Why VMs make a homelab easier to test, group, and rebuild | [Proxmox VM Layout](guides/proxmox-vm-layout.md), [Proxmox](../services/proxmox/README.md) |
| Proxmox Backup Server | Backups, retention concepts, and restore tests that actually matter | [Backups and Restore Testing](guides/backups-restore.md), [PBS](../services/proxmox-backup-server/README.md) |
| Synology and ZFS storage | Appliance NAS workflows and Linux storage learning | [Storage and Backups](storage-and-backups.md), [Storage and Monitoring](storage-monitoring.md) |
| NGINX reverse proxy | Clean internal URLs, TLS concepts, and routing to backend apps | [Reverse Proxy Guide](guides/reverse-proxy.md), [Reverse Proxy](../services/reverse-proxy/README.md) |
| Cloudflare Tunnel | Selected public access without publishing every internal service | [Cloudflare Tunnel](../services/cloudflare-tunnel/README.md), [Security Notes](security-notes.md) |
| Monitoring stack | Grafana, Prometheus, logs, exporters, and uptime checks | [Monitoring Guide](guides/monitoring-grafana.md), [Monitoring](../services/monitoring/README.md) |
| Media stack | Plex, Servarr-style automation, Tautulli, and Tdarr as a multi-app workflow | [Media Stack](../services/media-stack/README.md), [Apps and AI](apps-and-ai.md) |
| Local AI | Running AI locally with a GPU server concept, Open WebUI, and private endpoints | [Local AI Guide](guides/local-ai.md), [Local AI Stack](../services/local-ai/README.md) |
| Wiki.js | Building a documentation habit while keeping private notes private | [Wiki.js](../services/wiki/README.md), [Docs Index](docs-index.md) |
| Glance dashboard | Creating a simple daily control surface without exposing admin links | [Glance](../services/glance/README.md), [Apps and AI](apps-and-ai.md) |
| FinanceHQ | Local-first personal app patterns with demo data only | [FinanceHQ](../services/financehq/README.md), [Security Notes](security-notes.md) |
| CareerFill | Career workflow app patterns without publishing job or resume data | [CareerFill](../services/careerfill/README.md), [Security Notes](security-notes.md) |
| AWX / Ansible | Turning repeatable admin work into safe automation patterns | [AWX / Ansible](../services/automation-awx/README.md), [Sanitized Inventory](../inventory/sanitized/hosts.example.yml) |

## How to Use This Map

- Start with the topic that matches the current question.
- Open the guide first if one exists.
- Use service docs to understand purpose, placement, network behavior, backups, and security notes.
- Use diagrams to see the flow visually.
- Use sanitized examples only as templates, not production config.

## Public-Safe Boundaries

This map intentionally avoids exact host IPs, live internal domains, raw exports, credentials, screenshots, serial numbers, MAC addresses, financial data, and career data.

## Related Docs

- [Learning Paths](learning-paths.md)
- [Current Setup](current-setup.md)
- [Build Your Own Homelab](build-your-own.md)
- [Service Catalog](service-catalog.md)
- [Service Matrix](service-matrix.md)
- [Sanitized Examples](../examples/README.md)

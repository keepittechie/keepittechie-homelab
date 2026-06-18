# Build Your Own Homelab

This page gives viewers a beginner-friendly path for building a homelab inspired by the KeepItTechie setup. The goal is not to clone the lab exactly. The goal is to understand the layers and build something useful one step at a time.

## Before You Start

A homelab does not need to be expensive or complicated. One spare machine, an old desktop, a mini PC, or a laptop can teach the same core ideas that show up in larger labs.

Start with the hardware already available when possible. The first win is not a perfect rack. The first win is a small service that runs, survives a reboot, has notes, and can be rebuilt.

Use this repo as a guide to understand patterns, not as a checklist to copy line for line. Start small, document what changes, and keep private data and credentials out of GitHub.

Good first rules:

- Build one layer at a time.
- Keep notes while learning.
- Use sanitized names such as `home.example.com` in public docs.
- Avoid publishing exact host IPs, private domains, credentials, raw exports, or screenshots with sensitive data.
- Add backups before adding too much complexity.
- Test restore steps before depending on a service.

## Stage 1: Start With One Machine

Start with a single Linux machine and learn the basics before adding more services. This can be a spare desktop, a laptop, a mini PC, or a VM.

Focus on:

- Installing and updating a Linux server.
- Connecting over SSH.
- Creating normal admin users.
- Learning basic firewall behavior.
- Running one simple Docker Compose app.
- Keeping config and data paths organized.

This stage teaches the foundation that every later service depends on. If SSH, updates, users, storage paths, and firewall behavior are confusing, the bigger lab will be confusing too.

Related docs:

- [Glossary](glossary.md)
- [Docker Compose Examples](../examples/docker-compose/README.md)

## Stage 2: Learn Basic Networking

Networking is easier when the basic pieces are clear. Learn how a LAN works, what an IP address represents, how DHCP assigns addresses, what the gateway does, and how DNS turns names into destinations.

Focus on:

- LAN addressing.
- DHCP leases.
- Default gateway.
- DNS resolution.
- Basic troubleshooting with `ping`, `dig`, and `traceroute`.

This stage matters because every service becomes harder to troubleshoot when the network layer is unclear. A little networking knowledge saves a lot of guessing later.

Related docs:

- [Network Design](network.md)
- [DNS Flow Diagram](../diagrams/dns-flow.md)

## Stage 3: Add Local DNS

After the network basics make sense, add local DNS with Pi-hole or a similar DNS service. Local DNS lets viewers use service names such as `grafana.home.example.com` instead of remembering raw IP addresses.

Focus on:

- Primary and secondary DNS concepts.
- Local service names.
- DNS records that point to internal services.
- Using DHCP to hand out the correct DNS servers.
- Keeping real DNS records private when publishing docs.

Related docs:

- [Pi-hole](../services/pihole/README.md)
- [Pi-hole DNS Example](../examples/pihole/README.md)

## Stage 4: Add Virtualization

Virtualization lets one physical machine run multiple isolated workloads. Proxmox is the platform documented in this repo, but the learning ideas apply to other virtualization platforms too.

Focus on:

- Creating VMs by role.
- Separating service identity from machine identity.
- Understanding snapshots versus backups.
- Testing changes in disposable VMs.
- Planning VM backup coverage early.

Service identity is the name users remember, such as `proxy.home.example.com`. Machine identity is the host or VM running the workload. Keeping those ideas separate makes services easier to move, rebuild, and document.

Related docs:

- [Proxmox](../services/proxmox/README.md)
- [Core Infrastructure](core-infrastructure.md)

## Stage 5: Add Storage

Storage becomes important once services start keeping real data. Start with simple shared folders, then learn deeper concepts such as NAS shares, SMB, NFS, app data, media libraries, and snapshots.

Focus on:

- NAS concepts.
- SMB and NFS share basics.
- App data layout.
- Media storage layout.
- ZFS pools, datasets, snapshots, and scrubs if deeper Linux storage learning is the goal.

The KeepItTechie setup documents both a Synology NAS and a Linux ZFS storage server because they teach different lessons. A NAS is useful for stable shared storage. ZFS is useful for learning how Linux storage works under the hood.

Related docs:

- [Storage and Monitoring](storage-monitoring.md)
- [Synology NAS](../services/synology/README.md)
- [ZFS Storage](../services/zfs-storage/README.md)

## Stage 6: Add Backups

Backups should arrive before the lab becomes complicated. A service that matters should have a backup plan, and that plan should include restore testing.

Focus on:

- Backup targets.
- Proxmox Backup Server concepts.
- App data backups.
- NAS backup targets.
- Restore test evidence.
- A simple 3-2-1 backup mindset.

A backup is only useful when the restore path works. Keep a short restore log so future troubleshooting is based on proof, not assumptions.

Related docs:

- [Storage and Backups](storage-and-backups.md)
- [Proxmox Backup Server](../services/proxmox-backup-server/README.md)
- [Backup Flow Diagram](../diagrams/backup-flow.md)

## Stage 7: Add Monitoring

Monitoring should start simple. Begin with uptime checks and basic host health, then add richer metrics, logs, dashboards, and alerts.

Focus on:

- Basic service checks.
- Linux host metrics.
- Container metrics.
- Grafana and Prometheus.
- Logs with Loki and Promtail.
- Alerts that point to real action instead of creating noise.

Monitoring is useful when it helps answer: what changed, what is unhealthy, and where should troubleshooting start?

Related docs:

- [Monitoring](../services/monitoring/README.md)
- [Monitoring Flow Diagram](../diagrams/monitoring-flow.md)

## Stage 8: Add a Reverse Proxy

A reverse proxy makes services easier to reach with friendly names and internal HTTPS. NGINX is the reverse proxy documented in this repo.

Focus on:

- Friendly URLs such as `proxy.home.example.com`.
- Internal HTTPS.
- Reverse proxy routes to backend apps.
- The difference between private access and selected public access.
- Cloudflare Tunnel only when a service truly needs controlled public access.

Not every dashboard should be public. Hypervisors, backup systems, admin dashboards, monitoring, and automation controllers should stay private unless there is a specific hardened access plan.

Related docs:

- [Reverse Proxy](../services/reverse-proxy/README.md)
- [Cloudflare Tunnel](../services/cloudflare-tunnel/README.md)
- [NGINX Example](../examples/nginx/README.md)
- [Cloudflare Tunnel Example](../examples/cloudflare-tunnel/README.md)
- [Reverse Proxy Flow Diagram](../diagrams/reverse-proxy-flow.md)

## Stage 9: Add Self-Hosted Apps

Once networking, storage, backups, and access are understood, add apps that solve real problems. Start with a dashboard or wiki, then add more data-heavy services such as Nextcloud.

Focus on:

- Nextcloud.
- Wiki.js.
- A dashboard such as Glance or Homepage.
- Personal apps with demo data in public docs.
- App data, database, and file backup needs.
- The difference between fake demo data and private records.

Personal apps can teach a lot, but real financial records, job application data, resumes, and private databases do not belong in a public repo.

Related docs:

- [Apps and AI](apps-and-ai.md)
- [Nextcloud](../services/nextcloud/README.md)
- [Wiki.js](../services/wiki/README.md)
- [Glance Dashboard](../services/glance/README.md)

## Stage 10: Add Local AI

Local AI is optional. It can be a great Linux learning project, but it should come after the basics are stable.

Focus on:

- Open WebUI.
- Simple local inference.
- OpenAI-compatible local API patterns.
- Model storage.
- GPU acceleration when available.
- Protecting AI endpoints from public access.

A GPU helps with many workloads, but it is not required to learn the architecture. Start with a simple local setup, then expand when the use case is clear.

Related docs:

- [Local AI](../services/local-ai/README.md)
- [Local AI Flow Diagram](../diagrams/local-ai-flow.md)

## Stage 11: Add Automation

Automation should make known tasks repeatable. Start with simple Ansible playbooks before adding a full AWX controller.

Focus on:

- Ansible inventory basics.
- Read-only playbooks.
- Safe update workflows.
- AWX job templates later.
- Credentials and private inventories that stay outside public Git.

Good automation starts with small, boring, repeatable tasks. Avoid automating a process that is not understood manually yet.

Related docs:

- [AWX / Ansible Automation](../services/automation-awx/README.md)
- [Sanitized Examples](../examples/README.md)

## Common Beginner Mistakes

- Buying too much hardware too early.
- Exposing admin dashboards to the internet.
- Skipping backups.
- Never testing restores.
- Relying on raw IP addresses instead of DNS names.
- Mixing important data with experiments.
- Committing `.env` files or credentials.
- Making monitoring too complex too early.
- Copying configs without understanding the purpose.

## Suggested Learning Order

| Step | Focus | Suggested Docs |
|---|---|---|
| 1 | Linux and one simple app | [Docker Compose Examples](../examples/docker-compose/README.md), [Glossary](glossary.md) |
| 2 | Networking basics | [Network Design](network.md), [DNS Flow Diagram](../diagrams/dns-flow.md) |
| 3 | Local DNS | [Pi-hole](../services/pihole/README.md), [Pi-hole DNS Example](../examples/pihole/README.md) |
| 4 | Virtualization | [Proxmox](../services/proxmox/README.md), [Core Infrastructure](core-infrastructure.md) |
| 5 | Storage | [Storage and Monitoring](storage-monitoring.md), [Synology NAS](../services/synology/README.md), [ZFS Storage](../services/zfs-storage/README.md) |
| 6 | Backups | [Storage and Backups](storage-and-backups.md), [Backup Flow Diagram](../diagrams/backup-flow.md) |
| 7 | Monitoring | [Monitoring](../services/monitoring/README.md), [Monitoring Flow Diagram](../diagrams/monitoring-flow.md) |
| 8 | Reverse proxying | [Reverse Proxy](../services/reverse-proxy/README.md), [NGINX Example](../examples/nginx/README.md) |
| 9 | Self-hosted apps | [Apps and AI](apps-and-ai.md), [Service Catalog](service-catalog.md) |
| 10 | Local AI | [Local AI](../services/local-ai/README.md), [Local AI Flow Diagram](../diagrams/local-ai-flow.md) |
| 11 | Automation | [AWX / Ansible Automation](../services/automation-awx/README.md), [Sanitized Examples](../examples/README.md) |

## Related Docs

- [Current Setup](current-setup.md)
- [Viewer Guide](viewer-guide.md)
- [Documentation Index](docs-index.md)
- [Glossary](glossary.md)
- [Service Catalog](service-catalog.md)
- [Pre-Publish Review](pre-publish-review.md)

# Replication Quickstart

This guide explains how to use this repo to build a similar homelab pattern safely.

It is meant to help readers understand what to build first, what can wait, and how to adapt the KeepItTechie homelab patterns without copying private details.

## What This Quickstart Is

This quickstart is a practical map for copying the architecture pattern safely:

- Start small.
- Build one layer at a time.
- Document decisions as the lab grows.
- Use sanitized examples in public docs.
- Keep private details out of GitHub.
- Learn why each layer exists before adding the next one.

The goal is not to recreate every KeepItTechie service. The goal is to learn the pattern well enough to build a lab that fits a real home environment.

## What This Quickstart Is Not

This quickstart is not:

- A live inventory.
- A copy/paste config pack.
- A production security guide.
- A replacement for understanding the tools.
- A place to publish real secrets or private network details.
- A raw export of firewall, NAS, cloud, or application configuration.

Use the repo docs to understand the design. Keep real implementation details in private notes.

## The Core Idea

The homelab pattern is layered:

```text
Network -> DNS -> Virtualization -> Storage -> Backups -> Monitoring -> Proxy -> Apps
```

Readers do not need every layer on day one. A small lab that has one Linux host, working DNS notes, one app, and a backup plan is already a useful learning environment.

## Minimum Starting Point

A beginner can start with:

- One Linux machine.
- One router or firewall.
- One DNS plan.
- One simple Docker app.
- One backup target.

| Need | Beginner Option | Later Upgrade |
|---|---|---|
| Compute | Old desktop / mini PC | Proxmox host |
| DNS | Router DNS / Pi-hole | Primary + secondary DNS |
| Storage | External drive | NAS / ZFS |
| Backups | Manual backup | PBS / NAS backup target |
| Apps | One Docker Compose app | App VM / dedicated app host |

## Phase 1: Name the Lab

Build:

- Pick a private naming pattern.
- Choose a sanitized public example domain such as `home.example.com`.
- Decide how services will be named.

Why it matters:

- Names make the lab easier to document, troubleshoot, and rebuild.
- A service name can stay stable even if the backend machine changes.

Document privately:

- Real internal domain.
- Real DNS records.
- Real hostnames.

Do not publish:

- Live DNS zones.
- Exact host addresses.
- Private service URLs.

Related docs:

- [Glossary](glossary.md)
- [Homelab DNS and Pi-hole](guides/dns-pihole.md)
- [Pi-hole DNS Example](../examples/pihole/README.md)

## Phase 2: Build the Network Foundation

Build:

- Basic LAN access.
- Router or firewall rules.
- DHCP settings.
- A simple segmentation plan if needed.

Why it matters:

- Every service depends on the network.
- Troubleshooting is easier when DHCP, gateway, DNS, and firewall behavior are understood.

Document privately:

- VLAN IDs.
- Firewall rules.
- DHCP scopes.
- Admin URLs.

Do not publish:

- Raw firewall exports.
- Full network maps.
- Real public IPs.
- Exact private host IPs.

Related docs:

- [Network Design](network.md)
- [Core Infrastructure](core-infrastructure.md)
- [pfSense](../services/pfsense/README.md)
- [DNS Flow Diagram](../diagrams/dns-flow.md)

## Phase 3: Add DNS

Build:

- One DNS service, such as Pi-hole.
- Local service names.
- A plan to add secondary DNS later.
- DHCP handoff so clients use the intended DNS servers.

Why it matters:

- DNS removes the need to memorize raw addresses.
- Internal service names make reverse proxy routing and documentation cleaner.

Document privately:

- Real DNS records.
- Upstream choices if sensitive.
- Resolver host details.

Do not publish:

- Pi-hole API tokens.
- Query logs.
- Admin screenshots.
- Full DNS exports.

Related docs:

- [Homelab DNS and Pi-hole](guides/dns-pihole.md)
- [Pi-hole](../services/pihole/README.md)
- [Pi-hole DNS Example](../examples/pihole/README.md)

## Phase 4: Add a Virtualization Layer

Build:

- A virtualization host, such as Proxmox.
- VMs grouped by role.
- A simple naming pattern for machines and services.

Why it matters:

- Virtualization separates workloads.
- Test systems can be rebuilt without disrupting every service.
- VM role planning makes backups easier to reason about.

Document privately:

- VM IDs.
- Exact specs.
- Host addresses.
- Storage mappings.

Do not publish:

- Raw Proxmox exports.
- Live screenshots.
- Exact VM inventory.

Related docs:

- [Proxmox VM Layout](guides/proxmox-vm-layout.md)
- [Proxmox](../services/proxmox/README.md)
- [Core Infrastructure](core-infrastructure.md)

## Phase 5: Add Storage

Build:

- A place to store app data.
- A place to store shared files.
- A basic media or file layout if those services are planned.
- A snapshot plan when the storage platform supports it.

Why it matters:

- Apps become harder to rebuild once they hold real data.
- Storage layout affects backups, permissions, and restore planning.

Document privately:

- Real storage paths.
- Share names if sensitive.
- Dataset names if sensitive.
- Disk or hardware identifiers.

Do not publish:

- NAS exports.
- Exact pool output.
- Disk serials.
- Private file paths.

Related docs:

- [Storage and Monitoring](storage-monitoring.md)
- [Storage and Backups](storage-and-backups.md)
- [Synology NAS](../services/synology/README.md)
- [ZFS Storage](../services/zfs-storage/README.md)

## Phase 6: Add Backups

Build:

- A backup target separate from the primary workload.
- VM backups if using virtualization.
- App-aware backups when apps store databases or mounted data.
- A restore test process.

Why it matters:

- Backups should protect learning time and real data.
- Restore testing proves the backup path works.

Document privately:

- Backup schedules.
- Restore test dates.
- Backup storage paths.
- Encryption key handling.

Do not publish:

- Backup keys.
- Raw backup job exports.
- Private restore logs.
- Screenshots with real workload names.

Related docs:

- [Homelab Backups and Restore Testing](guides/backups-restore.md)
- [Storage and Backups](storage-and-backups.md)
- [Proxmox Backup Server](../services/proxmox-backup-server/README.md)
- [Backup Flow Diagram](../diagrams/backup-flow.md)

## Phase 7: Add Monitoring

Build:

- Basic uptime checks.
- Host metrics.
- Container metrics if Docker is used.
- A simple dashboard that answers real questions.

Why it matters:

- Monitoring turns guessing into evidence.
- Start with useful checks before building complex dashboards.

Document privately:

- Real target lists.
- Alert routes.
- Notification endpoints.
- Log locations.

Do not publish:

- Alert webhook URLs.
- Raw logs.
- Dashboard screenshots with private hostnames.
- Prometheus configs copied from the live lab.

Related docs:

- [Homelab Monitoring with Grafana and Prometheus](guides/monitoring-grafana.md)
- [Monitoring](../services/monitoring/README.md)
- [Monitoring Flow Diagram](../diagrams/monitoring-flow.md)
- [Prometheus Example](../examples/prometheus/README.md)

## Phase 8: Add Reverse Proxy and Internal HTTPS

Build:

- A reverse proxy.
- Internal DNS names that point to the proxy.
- Internal HTTPS if useful.
- A decision table for what stays private.

Why it matters:

- Friendly service names are easier than ports and raw addresses.
- Internal HTTPS teaches TLS concepts without publishing every service.

Document privately:

- Real backend targets.
- Certificate locations.
- Access control details.
- Public routes.

Do not publish:

- Private certs.
- Cloudflare Tunnel credentials.
- Exact backend host addresses.
- Live NGINX or tunnel configs from the lab.

Related docs:

- [Homelab Reverse Proxy and Internal HTTPS](guides/reverse-proxy.md)
- [Reverse Proxy](../services/reverse-proxy/README.md)
- [Cloudflare Tunnel](../services/cloudflare-tunnel/README.md)
- [NGINX Example](../examples/nginx/README.md)
- [Cloudflare Tunnel Example](../examples/cloudflare-tunnel/README.md)

## Phase 9: Add Apps

Build:

- One useful app first.
- A dashboard or wiki.
- App data backups.
- Private notes for app-specific restore steps.

Why it matters:

- Apps are where the lab becomes useful.
- App data is often more important than the container or VM that runs it.

Document privately:

- App database paths.
- Private app URLs.
- User data.
- Import/export locations.

Do not publish:

- Financial data.
- Career data.
- User files.
- Private app databases.
- `.env` files.

Related docs:

- [Apps and AI](apps-and-ai.md)
- [Service Catalog](service-catalog.md)
- [Docker Compose Examples](../examples/docker-compose/README.md)
- [Env Example](../examples/env/README.md)

## Phase 10: Add Local AI Optional

Build:

- A simple local AI web UI or endpoint.
- Model storage.
- Monitoring for resource usage.
- Private prompts and private app integration notes.

Why it matters:

- Local AI is a useful Linux, GPU, API, and automation learning layer.
- It should be protected like any other internal service.

Document privately:

- Model paths.
- Private prompts.
- Uploaded documents.
- Vector databases.
- Endpoint credentials.

Do not publish:

- API keys.
- Chat logs.
- Private documents.
- Live endpoints.
- Raw app configs.

Related docs:

- [Local AI on Linux](guides/local-ai.md)
- [Local AI](../services/local-ai/README.md)
- [Local AI Flow Diagram](../diagrams/local-ai-flow.md)

## Example Build Order

| Order | Build | Why This Comes First |
|---|---|---|
| 1 | Basic Linux server | Learn SSH, updates, users |
| 2 | Local DNS | Stop memorizing IPs |
| 3 | Virtualization | Separate workloads |
| 4 | Backups | Protect work before adding complexity |
| 5 | Monitoring | See what is failing |
| 6 | Reverse proxy | Clean service access |
| 7 | Apps | Add useful services |
| 8 | Local AI | Optional advanced layer |

## What to Document Privately

- Real IP addresses.
- Real DNS records.
- Firewall rules.
- VLAN IDs.
- Admin URLs.
- Credentials location.
- Backup schedules.
- Restore test dates.
- Storage paths.
- App database paths.

## What Is Safe to Share Publicly

- Architecture diagrams.
- Sanitized examples.
- Service categories.
- Public-safe lessons learned.
- Generic config templates.
- Fake or demo DNS names.
- Fake or demo dashboards.
- Broad network examples such as `10.10.0.0/24`.

## Common Mistakes

- Buying too much hardware too early.
- Exposing admin tools publicly.
- Skipping backups.
- Confusing snapshots with backups.
- Copying configs blindly.
- Publishing real DNS records.
- Not documenting restore tests.
- Building monitoring that is too noisy.
- Mixing private data into public examples.

## Related Docs

- [Current Setup](current-setup.md)
- [Build Your Own Homelab](build-your-own.md)
- [Learning Paths](learning-paths.md)
- [Documentation Index](docs-index.md)
- [Homelab Guides](guides/README.md)
- [Service Catalog](service-catalog.md)
- [Service Matrix](service-matrix.md)
- [Glossary](glossary.md)
- [Sanitized Examples](../examples/README.md)
- [Diagrams](../diagrams/README.md)

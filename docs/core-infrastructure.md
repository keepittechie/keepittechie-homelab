# Core Infrastructure

This page is the beginner-friendly entry point for the services that make the rest of the KeepItTechie homelab work.

Core infrastructure means the services that provide network access, DNS, virtualization, backups, internal web routing, and controlled public exposure. If these pieces are unclear, every app on top of them becomes harder to explain and troubleshoot.

For visual references, start with the [homelab overview diagram](../diagrams/homelab-overview.md), then review the [DNS flow](../diagrams/dns-flow.md) and [reverse proxy flow](../diagrams/reverse-proxy-flow.md). For unfamiliar terms, use the [Glossary](glossary.md).

## Recommended Reading Order

| Step | Service | Why Start Here |
|---|---|---|
| 1 | [pfSense](../services/pfsense/README.md) | Understand routing, firewall policy, DHCP, and network boundaries |
| 2 | [Pi-hole](../services/pihole/README.md) | Understand internal DNS, local service names, and DNS filtering |
| 3 | [Proxmox](../services/proxmox/README.md) and [Proxmox VM Layout Guide](guides/proxmox-vm-layout.md) | Understand where the VMs and containers run |
| 4 | [Proxmox Backup Server](../services/proxmox-backup-server/README.md) | Understand how VM recovery is planned |
| 5 | [Reverse Proxy](../services/reverse-proxy/README.md) and [Reverse Proxy Guide](guides/reverse-proxy.md) | Understand internal HTTPS and service identities |
| 6 | [Cloudflare Tunnel](../services/cloudflare-tunnel/README.md) | Understand selected public access and why most admin tools stay private |

## Core Stack Summary

| Layer | Service | Public-Safe Example | Main Lesson |
|---|---|---|---|
| Edge firewall | pfSense | `firewall.home.example.com` | Keep network policy centralized |
| DNS | Pi-hole primary and secondary | `pihole1.home.example.com`, `pihole2.home.example.com` | Make services readable and keep DNS controlled |
| Virtualization | Proxmox | `proxmox.home.example.com` | Separate workloads by role |
| Backup target | Proxmox Backup Server | `pbs.home.example.com` | Backups need restore testing |
| Internal web routing | NGINX reverse proxy | `proxy.home.example.com` | Clean URLs do not replace access control |
| Public access | Cloudflare Tunnel | Sanitized public route examples only | Publish only selected services |

## How These Services Work Together

```text
Client
  |
Pi-hole DNS
  |
pfSense routing and firewall policy
  |
Proxmox workloads
  |
Reverse proxy, apps, storage, monitoring, and backups
```

When a user opens `grafana.home.example.com`, the basic path is:

1. The client asks Pi-hole for the name.
2. Pi-hole returns the internal route.
3. pfSense allows or denies the network path.
4. The reverse proxy routes web traffic to the backend.
5. Monitoring, backups, and documentation help keep the service maintainable.

## Public-Safe Documentation Boundary

Document:

- What each service does.
- Why it exists.
- How it fits into the lab.
- What should stay private.
- Sanitized examples viewers can reuse.

Do not document:

- Raw firewall exports.
- Real tunnel credentials.
- Live public routes unless intentionally public branding.
- Private certificates or keys.
- Full DNS zone exports.
- Backup datastore internals.

## Related Docs

- [Storage and Monitoring](storage-monitoring.md)
- [Apps and AI](apps-and-ai.md)
- [Homelab Reverse Proxy and Internal HTTPS Guide](guides/reverse-proxy.md)
- [Proxmox VM Layout Guide](guides/proxmox-vm-layout.md)
- [Glossary](glossary.md)
- [How To Read Service Pages](how-to-read-service-pages.md)
- [Public-Safe Diagrams](../diagrams/README.md)
- [Service Matrix](service-matrix.md)
- [Pre-Publish Review Checklist](pre-publish-review.md)

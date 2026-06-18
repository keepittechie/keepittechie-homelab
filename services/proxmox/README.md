# Proxmox

## Purpose

Proxmox is the virtualization layer for the homelab. It runs the VMs and containers that support DNS, reverse proxying, monitoring, media services, backups, local AI tooling, personal apps, and automation.

## Why This Matters

Virtualization turns a single physical server into a flexible learning platform. Instead of installing every service directly on one OS, Proxmox lets the lab separate workloads by role, test changes safely, back up whole systems, and rebuild services without starting from scratch.

It also teaches a core homelab lesson: the service identity users type is not always the same as the machine identity that runs it.

## Where It Fits in the Homelab

```text
Server hardware
  |
Proxmox VE
  |
VMs and containers
  |
DNS, proxy, apps, monitoring, media, AI, automation
```

Proxmox is the platform underneath most lab workloads. pfSense controls network policy, Pi-hole provides DNS, and Proxmox provides the compute layer.

## Host / Runtime

| Field | Value |
|---|---|
| Runtime | Proxmox VE on server hardware |
| Example DNS | `proxmox.home.example.com` |
| Public access | No |
| Backup target | Proxmox Backup Server |
| Admin access | Trusted LAN or VPN only |

## Network / DNS

Proxmox management should stay private. Guest VMs and service identities can use separate names:

```text
machine identity: pontus.home.example.com
service identity: pihole1.home.example.com

machine identity: zelus.home.example.com
service identity: proxy.home.example.com
```

This distinction helps readers understand why moving a service does not always require changing the service identity users remember.

## Key Responsibilities

- Host core infrastructure VMs.
- Provide VM snapshots and lifecycle controls.
- Integrate with Proxmox Backup Server.
- Keep workloads separated by role.
- Provide a practical place to test Linux, Docker, storage, and automation patterns.
- Support rebuilds and restore tests.

## Example Public-Safe Configuration

Sanitized VM role examples:

| VM / Host Example | Role | Service Alias Examples | Backup Priority |
|---|---|---|---|
| `pontus` | Primary DNS | `pihole1.home.example.com` | High |
| `priapus` | Secondary DNS | `pihole2.home.example.com` | High |
| `zelus` | Reverse proxy and automation | `proxy.home.example.com` | High |
| `heimdall` | Docker app host | `grafana.home.example.com` | Medium |
| `apollo` | Media services | `plex.home.example.com` | Medium |
| `hephaestus` | GPU and local AI workloads | `ai.home.example.com` | Medium |
| `chronos` | Backup target | `pbs.home.example.com` | Critical |

The names are examples for documentation. They should not be treated as a live inventory export.

## Backup and Restore Notes

- Back up important VMs to Proxmox Backup Server.
- Keep restore notes per service, not only per VM.
- Test restores into an isolated network where practical.
- Add app-aware backups for databases and stateful services.
- Document what is easy to rebuild versus what must be recoverable.

## Security Notes

- Keep the Proxmox UI private.
- Use strong admin authentication.
- Avoid broad VM-to-VM access unless required.
- Do not publish cluster credentials, API credentials, or full host exports.
- Be careful with screenshots that show VM IDs, storage paths, or private hostnames.

## Common Mistakes to Avoid

- Treating snapshots as a replacement for backups.
- Backing up VMs without testing restores.
- Running unrelated critical services in one overloaded VM.
- Using service identity and machine identity interchangeably.
- Publishing the full VM inventory when a sanitized role table is enough.

## What Readers Can Learn

- Why virtualization is useful in a homelab.
- How to design VM roles around service boundaries.
- How DNS aliases make services portable.
- How Proxmox and PBS work together for recovery.

## Future Improvements

- Add a sanitized Proxmox storage layout.
- Add a restore-test writeup.
- Add a VM naming convention page.

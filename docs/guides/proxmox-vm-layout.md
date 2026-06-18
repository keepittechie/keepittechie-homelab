# Proxmox VM Layout

This guide explains how Proxmox, virtualization, and VM role planning fit into a homelab.

## Guide Goal

This guide shows how Proxmox acts as the virtualization layer for the lab and why organizing VMs by role makes a homelab easier to understand, back up, and rebuild.

The guide helps readers see Proxmox as more than a place to create random VMs. It is the compute layer that supports DNS, app hosting, monitoring, media, documentation, automation, and other workloads.

## What Readers Will Learn

- What Proxmox does in a homelab.
- Why VMs are useful for learning and isolation.
- How services can be grouped by purpose.
- Why VM names are not always the same as service names.
- How backups fit into VM planning.
- Why snapshots help but do not replace backups.
- Why raw Proxmox exports and live inventory details should stay private.

## Why Virtualization Matters

Virtualization lets one physical host run many isolated workloads. Instead of installing every service directly on one operating system, a homelab can separate roles into VMs or containers.

This helps with:

- Safer testing.
- Cleaner rebuilds.
- Better service separation.
- Easier backup planning.
- Disposable lab experiments.
- Clearer documentation.

Snapshots are useful when testing changes, but they are not a full backup strategy. A snapshot usually depends on the same host or storage layer. A real backup plan needs a separate target and restore testing.

## Where Proxmox Fits

Proxmox sits under many of the service layers in the lab. It can run or support:

- DNS servers.
- Docker and app hosts.
- Monitoring services.
- Media services.
- Backup-related systems.
- Documentation services.
- Local AI support where appropriate.
- Automation tools.

In a public repo, the important thing is to explain the role of each workload without publishing live VM IDs, exact specs, exact host addresses, or private inventory.

## Grouping VMs by Role

Grouping VMs by role makes the lab easier to reason about. Readers do not need the live inventory to understand the design.

Useful role groups include:

- Network support.
- App hosting.
- Media.
- Monitoring.
- Storage and backup.
- Local AI.
- Automation.
- Documentation.

This kind of grouping also helps answer practical questions: what needs a backup, what can be rebuilt, what should stay private, and what depends on storage or DNS.

## Service Identity vs Machine Identity

Machine identity is the VM or host. Service identity is the name people use to reach the service.

For example:

```text
docker1.home.example.com
  -> dashboard.home.example.com
  -> wiki.home.example.com
  -> app.home.example.com
```

In that example, `docker1.home.example.com` is the machine identity. The dashboard, wiki, and app names are service identities. This keeps documentation clearer because a service can move later without changing the name readers or users remember.

## Backups and Restore Thinking

Every important VM needs a backup plan. The backup target should be separate from the VM host so one failure does not take out both the workload and the backup.

Proxmox Backup Server can be part of this pattern:

```text
Proxmox VM
  -> backup job
  -> pbs.home.example.com
  -> restore test evidence
```

The important lesson is not just "backup completed." The important lesson is whether the VM or service can be restored when needed.

## Public-Safe Examples

- Open the sanitized homelab overview diagram.
- Open the service catalog grouped by role.
- Use a sanitized VM role table.
- Explain how service names differ from VM names.
- Open the backup flow diagram.
- Review what not to publish: live VM IDs, exact host addresses, raw exports, screenshots, and private storage paths.

Do not include a live Proxmox dashboard unless it is heavily sanitized or recreated with demo data.

## Example VM Role Table

| VM / Host Role | Example Machine Identity | Example Services | Backup Priority | Notes |
|---|---|---|---|---|
| DNS VM | `dns1.home.example.com` | Pi-hole primary | High | Keeps local DNS available |
| Docker/App VM | `docker1.home.example.com` | Dashboard, wiki, apps | High | Runs several containerized services |
| Monitoring VM | `monitoring.home.example.com` | Grafana, Prometheus | Medium | Helps track lab health |
| Backup VM | `pbs.home.example.com` | Proxmox Backup Server | High | Stores VM backups |
| Local AI VM/Host | `ai.home.example.com` | Open WebUI, local API | Medium | Used for local AI experiments |

These are sanitized examples. They are not live VM names, VM IDs, host addresses, or an exported inventory.

## Common Mistakes

- Putting every service on one VM without a plan.
- Confusing snapshots with backups.
- Exposing the Proxmox UI publicly.
- Documenting exact VM IDs or host addresses in a public repo.
- Skipping backups for important VMs.
- Never testing restores.
- Giving every service a random name with no pattern.
- Overbuilding before learning the basics.

## What Is Intentionally Not Shown

- Proxmox UI screenshots.
- Live VM IDs.
- Exact VM specs.
- Exact host IPs.
- Private hostnames.
- Backup encryption keys.
- Raw Proxmox exports.
- Raw backup schedules if sensitive.
- Private storage paths.

## Commands and Examples

These commands are examples readers can adapt in their own lab:

```bash
# Show the VM list on a Proxmox host
qm list

# Show the container list if LXC is used
pct list

# Check backup jobs from the Proxmox UI or PBS UI.
# Do not publish screenshots unless sanitized.
```

Review command output before sharing it publicly. VM names, VM IDs, storage names, and notes can reveal more than expected.

## Next Steps

- Read the [Proxmox service doc](../../services/proxmox/README.md).
- Study the [Current Setup](../current-setup.md) page.
- Review the [Service Catalog](../service-catalog.md).
- Study the [backup flow](../../diagrams/backup-flow.md).
- Document VM roles privately.
- Add restore test evidence over time.

## Related Docs

- [Core Infrastructure](../core-infrastructure.md)
- [Current Setup](../current-setup.md)
- [Service Catalog](../service-catalog.md)
- [Service Matrix](../service-matrix.md)
- [Storage and Backups](../storage-and-backups.md)
- [Proxmox](../../services/proxmox/README.md)
- [Proxmox Backup Server](../../services/proxmox-backup-server/README.md)
- [Homelab Overview Diagram](../../diagrams/homelab-overview.md)
- [Backup Flow](../../diagrams/backup-flow.md)
- [Glossary](../glossary.md)
- [Pre-Publish Review](../pre-publish-review.md)

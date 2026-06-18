# Storage and Monitoring

This page is the beginner-friendly entry point for storage, backups, and monitoring in the KeepItTechie homelab.

Storage keeps services running and data available. Backups make recovery possible. Monitoring tells you when something is unhealthy before the outage becomes a mystery.

For visual references, see the [backup flow diagram](../diagrams/backup-flow.md), [monitoring flow diagram](../diagrams/monitoring-flow.md), and [Homelab Backups and Restore Testing companion](episodes/backups-restore.md). For unfamiliar terms such as dataset, snapshot, scrub, metrics, and logs, use the [Glossary](glossary.md).

## Recommended Reading Order

| Step | Topic | Link | Why Start Here |
|---|---|---|---|
| 1 | Storage and backup strategy | [Storage and Backups](storage-and-backups.md) | Understand the full recovery model first |
| 2 | Synology NAS | [Synology NAS](../services/synology/README.md) | Learn shared storage, media storage, and backup target concepts |
| 3 | ZFS Storage Server | [ZFS Storage Server](../services/zfs-storage/README.md) | Learn datasets, snapshots, scrubs, and Linux storage |
| 4 | Proxmox Backup Server | [Proxmox Backup Server](../services/proxmox-backup-server/README.md) | Understand VM backup and restore testing |
| 5 | Monitoring Stack | [Monitoring](../services/monitoring/README.md) | Learn how metrics, logs, and dashboards support operations |

## Stack Summary

| Layer | Service | Public-Safe Example | Main Lesson |
|---|---|---|---|
| Shared storage | Synology NAS | `nas.home.example.com` | NAS storage is useful, but it is not automatically a backup |
| Linux storage | ZFS Storage Server | `zfs.home.example.com` | Datasets, snapshots, and scrubs teach storage fundamentals |
| VM backups | Proxmox Backup Server | `pbs.home.example.com` | Backups need retention and restore testing |
| Dashboards | Grafana | `grafana.home.example.com` | Start with simple visibility |
| Metrics | Prometheus | `prometheus.home.example.com` | Metrics show trends and current health |
| Logs | Loki and Promtail | `loki.home.example.com` | Logs help explain what metrics cannot |

## How These Services Work Together

```text
Apps and VMs
  |
  +-- store files on NAS or ZFS where appropriate
  +-- back up VMs to Proxmox Backup Server
  +-- export metrics and logs to monitoring stack
  +-- document restore test evidence in public-safe notes
```

## Beginner Mental Model

| Question | Where To Look |
|---|---|
| Where do shared files and media live? | Synology NAS |
| Where can Linux storage concepts be learned deeply? | ZFS Storage Server |
| Where do VM backups go? | Proxmox Backup Server |
| How is storage growth monitored? | Grafana and exporters |
| How are backups proven to work? | Restore test evidence |

## Public-Safe Documentation Boundary

Document:

- Generic share and dataset purpose.
- Backup intent and restore process.
- Dashboard ideas and metric categories.
- Sanitized paths such as `/mnt/storage/media` and `/volume1/backups`.

Do not document:

- Raw NAS exports.
- Raw backup exports.
- Full ZFS pool status from live systems.
- Disk serial numbers.
- Real files, account names, or private share paths.
- Logs that contain private data.

## Related Docs

- [Core Infrastructure](core-infrastructure.md)
- [Apps and AI](apps-and-ai.md)
- [Homelab Backups and Restore Testing Companion](episodes/backups-restore.md)
- [Glossary](glossary.md)
- [How To Read Service Pages](how-to-read-service-pages.md)
- [Public-Safe Diagrams](../diagrams/README.md)
- [Service Matrix](service-matrix.md)
- [Pre-Publish Review Checklist](pre-publish-review.md)

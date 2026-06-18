# Homelab Backups and Restore Testing

This page is a public-safe companion guide for a KeepItTechie video about homelab backups, Proxmox Backup Server, and proving backups through restore testing.

## Episode Goal

This episode teaches how to think about backups in a homelab and why a restore test matters more than a "backup completed" message.

The focus is practical: protect important services, keep backup targets separate from the systems they protect, and document restore evidence without publishing private infrastructure details.

## What Viewers Will Learn

- Why backups should be planned before adding more services.
- Why snapshots are helpful but not enough by themselves.
- What Proxmox Backup Server does in a Proxmox-based lab.
- Why backup targets should be separate from the VM host.
- How NAS storage and ZFS snapshots can fit into a backup strategy.
- Why restore testing should be documented.
- What backup details should stay out of a public repo.

## Why Backups Matter

Homelabs break. Updates fail, disks fail, services get misconfigured, and important files can be deleted by mistake.

Backups protect more than data. They protect learning time. When a service can be restored, troubleshooting becomes less stressful and rebuilding becomes a planned exercise instead of a full restart.

Good documentation makes backups more useful. A backup file is only part of the story; the repo should also explain what is covered, what is not covered, and how restore testing is tracked.

## Snapshots vs Backups

Snapshots and backups solve related problems, but they are not the same thing.

| Concept | What It Means | Useful For | Limitation |
|---|---|---|---|
| Snapshot | A quick point-in-time state, often on the same platform or storage system | Updates, testing, rollback, accidental change recovery | May disappear with the host or storage system |
| Backup | A separate recovery copy intended to restore a workload or data set | Rebuilds, host failure, data recovery, disaster recovery practice | Must be tested to prove it works |

Snapshots are useful before risky changes. Backups are needed when the original system is unavailable or damaged.

## Where Proxmox Backup Server Fits

Proxmox Backup Server is the VM and container backup target in this style of lab. It stores backups outside the running VM workload and supports concepts such as deduplication, compression, retention, and restore workflows.

For beginners, the key thing to understand is that PBS is not just storage. It is part of the recovery path. It helps answer:

- Which VMs are backed up?
- How long are backups kept?
- Where would a restore happen?
- When was the last restore test?

PBS UI details, datastore names, encryption keys, and raw exports should remain private.

## Backup Targets and Storage

Backup storage should be separate from primary VM storage. If the same host or disk failure can destroy both the VM and the backup, the backup plan is weak.

Common storage roles in this repo:

- Proxmox Backup Server stores VM and container backups.
- A NAS can act as a backup target or secondary landing area.
- ZFS snapshots can protect datasets from accidental changes.
- App-aware exports may be needed when databases or mounted data are involved.

The 3-2-1 mindset is useful here: keep multiple copies, use more than one storage location or type, and keep at least one copy away from the original failure domain.

Public docs should use sanitized paths and service names only, such as `pbs.home.example.com`, `nas.home.example.com`, and `/mnt/storage/backups`.

## Restore Testing

A backup is trusted after a restore test, not just after a scheduled job finishes.

A simple restore test can look like this:

1. Pick a safe backup source.
2. Restore into an isolated test VM or test location.
3. Confirm the restored system boots.
4. Confirm the expected service starts.
5. Confirm the expected data exists.
6. Record the result with sanitized notes.

Do not publish screenshots or command output that reveals hostnames, paths, users, file names, databases, or app data from the live lab.

## Public-Safe Demo Ideas

- Show the [backup flow diagram](../../diagrams/backup-flow.md).
- Walk through a sanitized restore test evidence table.
- Explain the difference between a snapshot and a backup with a simple example.
- Show how a backup target should be separate from the VM host.
- Review what should not be published.
- Use the [pre-publish review checklist](../pre-publish-review.md) before sharing notes.

Avoid showing live PBS dashboards unless the view is sanitized or recreated with demo data.

## Example Backup Plan

This table is a teaching example. It does not represent the live backup schedule.

| Workload | Backup Method | Target | Frequency Example | Restore Priority | Notes |
|---|---|---|---|---|---|
| DNS VM | VM backup | PBS / NAS target | Weekly | High | DNS affects the whole lab |
| App VM | VM backup + app data backup | PBS / appdata backup | Weekly | High | Apps may need both VM and data restore |
| Monitoring VM | VM backup | PBS target | Weekly | Medium | Useful but not always critical |
| Personal app data | App/database backup | Separate storage | Daily or weekly | High | Use fake/demo data in public docs |

## Example Restore Test Evidence

Use a simple table to record proof that a restore path works. Keep the real details private if they reveal hostnames, paths, app data, or users.

| Date | Backup Source | Restore Target | Result | Notes |
|---|---|---|---|---|
| YYYY-MM-DD | Example VM backup | Isolated test VM | Pass / Fail | Sanitized notes only |

## Common Mistakes

- Confusing snapshots with backups.
- Keeping backups only on the same host.
- Never testing restores.
- Backing up VMs but not app data.
- Publishing backup paths or screenshots with sensitive information.
- Storing encryption keys with the backup.
- Not documenting what is covered.
- Making backup plans too complex to maintain.

## What Is Intentionally Not Shown

- Real backup schedules.
- Private datastore names.
- Backup encryption keys.
- Real restore screenshots.
- Exact NAS paths.
- Private app data.
- Backup job exports.
- Raw PBS or Proxmox configs.
- Financial or career app databases.

## Commands and Examples

These commands are safe examples that viewers can adapt in their own lab. Review command output before sharing it publicly because it can include hostnames, pool names, dataset names, and paths.

```bash
# List Proxmox VMs
qm list

# Check ZFS pool status in a viewer's own lab
zpool status

# List ZFS datasets in a viewer's own lab
zfs list
```

## After Watching

- Read the [Storage and Backups](../storage-and-backups.md) guide.
- Study the [backup flow diagram](../../diagrams/backup-flow.md).
- Review the [Proxmox Backup Server](../../services/proxmox-backup-server/README.md) service doc.
- Write a private backup inventory for important workloads.
- Schedule a restore test.
- Document restore test evidence safely.

## Related Docs

- [Storage and Backups](../storage-and-backups.md)
- [Storage and Monitoring](../storage-monitoring.md)
- [Current Setup](../current-setup.md)
- [Service Catalog](../service-catalog.md)
- [Proxmox Backup Server](../../services/proxmox-backup-server/README.md)
- [Proxmox](../../services/proxmox/README.md)
- [Synology NAS](../../services/synology/README.md)
- [ZFS Storage](../../services/zfs-storage/README.md)
- [Backup Flow Diagram](../../diagrams/backup-flow.md)
- [Pre-Publish Review](../pre-publish-review.md)
- [Glossary](../glossary.md)

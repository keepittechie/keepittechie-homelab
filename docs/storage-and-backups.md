# Storage and Backups

## Storage Layers

| Layer | Purpose |
|---|---|
| VM disks | Operating systems and app runtimes |
| Synology NAS | Shared storage and backup target |
| ZFS storage server | ZFS learning, datasets, redundancy |
| Proxmox Backup Server | Incremental VM backup management |

## Backup Principles

- Back up VMs regularly.
- Keep backups separate from the VM host.
- Test restore workflows.
- Document what is backed up and what is not.
- Keep encryption keys and credentials out of Git.

## Example Backup Schedule

| Backup | Frequency | Destination |
|---|---|---|
| Proxmox VMs | Weekly | Proxmox Backup Server |
| Critical app data | Daily or weekly | NAS / backup target |
| Git repos | Continuous | GitHub / local mirrors |
| Config exports | After major changes | Sanitized archive |

## Restore Checklist

1. Confirm backup exists.
2. Confirm target storage is available.
3. Restore into isolated test VM if possible.
4. Validate service health.
5. Update documentation if steps changed.

# Synology NAS

## Purpose

The Synology NAS provides shared storage for files, media, and selected backup targets. It is the stable appliance-style storage layer in the lab.

## Where It Fits

```text
Apps and clients
  |
SMB / NFS / app-specific access
  |
Synology NAS
```

The NAS is useful for day-to-day storage and media workflows, while the Rocky Linux ZFS server is better for Linux-first storage learning and experiments.

## Host / Runtime

| Field | Value |
|---|---|
| Runtime | Synology DSM |
| Example DNS | `nas.home.example.com` |
| Public access | No |
| Primary users | Media stack, clients, selected app backups |

## Key Dependencies

- pfSense network access
- Pi-hole DNS record
- SMB or NFS clients
- Snapshot and backup settings
- UPS or clean shutdown planning, if available

## Network / DNS

Example:

```text
nas.home.example.com -> 10.10.0.4
```

The admin UI should remain private. File services should be limited to the clients and servers that actually need them.

## Backup Notes

- Keep NAS configuration exports private.
- Use snapshots for fast rollback where appropriate.
- Replicate or back up important data outside the NAS when possible.
- Do not confuse RAID with backup.

## Security Notes

- Do not expose the DSM admin interface to the public internet.
- Use named accounts with only the permissions they need.
- Avoid publishing share names if they reveal private projects or people.
- Keep backup and sync credentials out of Git.

## What Viewers Can Learn

- When a NAS appliance makes sense in a homelab.
- How SMB/NFS shares support apps without becoming the whole backup strategy.
- Why snapshots are useful but not a full disaster recovery plan.
- How to separate media storage from app runtime storage.

## Future Improvements

- Add a sanitized share layout.
- Add a snapshot and restore example.
- Document which workloads use NAS storage.

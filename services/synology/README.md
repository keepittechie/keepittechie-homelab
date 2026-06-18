# Synology NAS

## Purpose

The Synology NAS provides shared storage for the homelab. It is used for file shares, media storage, selected backup targets, and appliance-style storage administration.

## Why This Matters

A NAS is one of the most practical additions to a homelab because it gives multiple systems a common place to store and retrieve data. It also gives readers a clear way to understand the difference between app runtime disks, shared files, media libraries, snapshots, and backups.

The NAS is not the same thing as Proxmox VM storage. VM storage runs operating systems and services. NAS storage is shared storage that apps and clients can mount or use as a backup destination.

## Where It Fits in the Homelab

```text
Clients, media apps, and backup jobs
  |
SMB / NFS / app-specific access
  |
nas.home.example.com
```

The NAS complements the ZFS storage server. Synology provides an appliance workflow, while the ZFS server provides a Linux-first storage learning platform.

## Host / Runtime

| Field | Value |
|---|---|
| Runtime | Synology DSM |
| Example DNS | `nas.home.example.com` |
| Public access | No |
| Primary users | Media stack, clients, selected backup jobs |
| Admin access | Trusted LAN or VPN only |

## Storage / Data Layout

Example public-safe share layout:

| Share | Purpose | Access Pattern | Backup Priority | Public Notes |
|---|---|---|---|---|
| `/volume1/media` | Media libraries | Read/write by media apps, read by clients | Medium | Do not publish real library names |
| `/volume1/backups` | Backup target | Write by backup jobs, admin read | High | Keep backup credentials private |
| `/volume1/appdata` | App support files | Limited service access | High | App data may need app-aware backups |
| `/volume1/public-demo` | Sanitized demo files | Read-only for examples | Low | Use fake files only |

This table is a teaching model, not a live share export.

## Network / DNS

Example:

```text
nas.home.example.com -> 10.10.0.x
```

SMB and NFS access should be limited to the clients and servers that need it. The Synology admin UI should stay private.

## Key Responsibilities

- Provide shared storage for clients and services.
- Store media libraries and selected backup targets.
- Support SMB and NFS access patterns.
- Provide snapshots where useful for quick rollback.
- Keep appliance configuration recoverable through private backups.
- Keep storage access separate from public web exposure.

## Example Public-Safe Configuration

Example storage usage map:

| Workload | Uses NAS? | Example Path | Notes |
|---|---|---|---|
| Plex | Yes | `/volume1/media` | Media files are separate from Plex metadata |
| Proxmox backup copy | Maybe | `/volume1/backups` | Depends on private backup design |
| App exports | Maybe | `/volume1/backups/app-exports` | Keep export contents private |
| Public docs examples | No live data | `/volume1/public-demo` | Use fake demo files only |

## Backup and Restore Notes

- Keep Synology configuration exports private.
- Use snapshots for rollback, but do not treat snapshots as complete off-device backups.
- Replicate or back up critical shares outside the NAS where possible.
- Document what is stored on NAS shares versus VM disks.
- Test restore of a file, a folder, and any app backup that depends on NAS storage.

## Security Notes

- Do not expose DSM administration to the public internet.
- Use named service accounts with least privilege.
- Keep SMB/NFS permissions narrow.
- Do not commit raw NAS exports.
- Avoid screenshots that reveal share names, user names, or private file paths.

## Common Mistakes to Avoid

- Treating RAID as a backup.
- Giving every app broad read/write access to every share.
- Storing app databases on network shares without understanding the app requirements.
- Publishing real share exports.
- Forgetting that NAS availability can affect media, backups, and apps at the same time.

## What Readers Can Learn

- How shared storage supports a homelab.
- Why NAS storage and VM storage solve different problems.
- How SMB and NFS fit into self-hosting.
- Why snapshots are useful but incomplete without backup strategy.
- How to document storage safely.

## Future Improvements

- Add a sanitized snapshot policy example.
- Add a restore test using fake demo files.
- Add a storage dependency table covering media and app services.

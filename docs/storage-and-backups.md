# Storage And Backups

Storage in the homelab has two jobs: support daily services and make recovery possible when something breaks. This page explains the public-safe architecture without publishing private shares, keys, or backup exports.

## Storage Layers

| Layer | Platform | Purpose |
|---|---|---|
| VM disks | Proxmox storage | Operating systems and app runtime data |
| Shared NAS storage | Synology NAS | Media, files, shared folders, and selected backup targets |
| Linux ZFS storage | Rocky Linux ZFS server | ZFS learning, datasets, snapshots, and Linux storage practice |
| VM backup datastore | Proxmox Backup Server | Deduplicated VM and container backups |
| Git repos | GitHub and local clones | Versioned documentation and application code |

## How Storage Fits Together

```text
Proxmox VMs
  |
  +-- Local VM disks for OS and app runtime
  +-- NAS mounts for shared files or media
  +-- ZFS datasets for Linux storage experiments
  +-- PBS backups for VM recovery
```

The main lesson: a NAS share is not automatically a backup, and a VM snapshot is not a complete recovery plan by itself.

## Backup Strategy

| Data Type | Example Source | Backup Target | Notes |
|---|---|---|---|
| VM and container disks | Proxmox guests | Proxmox Backup Server | Use retention and restore tests |
| App configuration | Docker app VMs | Git or private backup location | Sanitize before publishing examples |
| Databases | Wiki.js, personal apps, monitoring | App-aware dumps plus VM backups | Database consistency matters |
| Media metadata | Plex, Tautulli, Servarr | NAS or app backup path | Media files and metadata have different restore needs |
| Documentation | This repo and Wiki.js | Git plus app backup | Public docs and private runbooks stay separate |
| Storage datasets | ZFS server | Snapshots or replication target | Document dataset purpose and retention |

## Example Schedule

| Backup | Frequency | Destination | Restore Test |
|---|---|---|---|
| Core infrastructure VMs | Weekly or better | PBS | Restore into an isolated test VM |
| Critical app databases | Daily or weekly | Private backup location | Test import into a disposable container |
| Wiki and docs | After major edits | Git plus app backup | Confirm pages render |
| NAS configuration | After major changes | Private encrypted copy | Confirm export can be read |
| ZFS snapshots | Scheduled | Same pool or replication target | Confirm files can be rolled back |

## Restore Checklist

1. Identify whether the failure is app, VM, storage, DNS, or network related.
2. Confirm the backup exists and matches the service you need.
3. Restore into an isolated test target when possible.
4. Validate DNS, reverse proxy, database, storage mounts, and login flow.
5. Update the service README if the restore process changed.

## What Viewers Can Learn

- Why backups should be tested, not assumed.
- How PBS differs from a simple file copy.
- Why app-aware database backups matter.
- How NAS storage and ZFS storage solve different problems.
- How to document recovery steps before an outage.

## Public Repo Boundary

Do not publish backup encryption keys, NAS exports, private share names, raw database dumps, real user files, or screenshots showing private data.

# Storage And Backups

Storage in the homelab has two jobs: support daily services and make recovery possible when something breaks. This page explains the public-safe architecture without publishing private shares, keys, raw exports, or live backup details.

For the storage and monitoring reading path, see [Storage and Monitoring](storage-monitoring.md).

## Storage Layers

| Layer | Platform | Purpose | Public-Safe Example |
|---|---|---|---|
| VM disks | Proxmox storage | Operating systems and app runtime data | VM boot disks and service disks |
| Shared NAS storage | Synology NAS | Media, files, selected backup targets | `/volume1/media`, `/volume1/backups` |
| Linux ZFS storage | Rocky Linux ZFS server | Datasets, snapshots, Linux storage learning | `/mnt/storage/media`, `/mnt/storage/appdata` |
| VM backup datastore | Proxmox Backup Server | Deduplicated VM and container backups | `pbs.home.example.com` |
| Git repos | GitHub and local clones | Versioned docs and safe config examples | Public docs and private repos separated |

## How Storage Fits Together

```text
Proxmox VMs
  |
  +-- Local VM disks for OS and app runtime
  +-- NAS shares for media, files, and selected backup targets
  +-- ZFS datasets for Linux storage learning and selected workloads
  +-- PBS backups for VM and container recovery
```

The main lesson: a NAS share is not automatically a backup, a ZFS snapshot is not automatically off-host protection, and a VM snapshot is not a full restore plan.

## VM Backups

VM backups protect complete guests or containers. In this lab, Proxmox Backup Server is the preferred target for Proxmox workloads.

| Backup Type | Source | Target | Notes |
|---|---|---|---|
| Core infrastructure VM | DNS, proxy, automation, monitoring | PBS | Restore testing matters |
| App VM | Wiki, dashboard, personal apps | PBS plus app-aware backup | Databases may need separate dumps |
| Media automation VM | Servarr, request tools, transcode tools | PBS | Often easier to rebuild than core infra |
| Test VM | Lab experiments | PBS or no backup | Do not waste retention on throwaway systems |

## App Data Backups

App data needs its own thinking. A VM backup may not be enough if a database is mid-write, external storage is mounted separately, or app state lives outside the VM disk.

| App Data | Example Location | Backup Approach | Notes |
|---|---|---|---|
| Databases | `/mnt/storage/appdata` | App-aware export plus VM backup | Needed for consistent restore |
| Media metadata | `/mnt/storage/appdata` | App backup and config backup | Separate from media files |
| Uploaded files | `/mnt/storage/backups` or app storage | File backup plus app notes | Confirm what the app owns |
| Dashboard config | `/mnt/storage/appdata` | Git-safe export or private backup | Remove credentials before publishing examples |

## NAS Shares

NAS shares provide common storage for clients and services. They are useful for media and backup targets, but they should be documented carefully.

| Share | Purpose | Example Path | Public Boundary |
|---|---|---|---|
| Media | Media libraries | `/volume1/media` | Do not publish real library names |
| Backups | Backup landing area | `/volume1/backups` | Do not publish backup contents |
| App support | App-adjacent files | `/volume1/appdata` | Avoid real app data |
| Demo | Public-safe examples | `/volume1/public-demo` | Fake files only |

## ZFS Snapshots

ZFS snapshots are useful rollback points. They are fast and practical, but they remain tied to the storage system unless replicated or backed up elsewhere.

| Dataset | Example Snapshot | Use |
|---|---|---|
| `tank/appdata` | `tank/appdata@example-snapshot` | Roll back app support files |
| `tank/media` | `tank/media@example-snapshot` | Protect against accidental deletes |
| `tank/lab` | `tank/lab@example-snapshot` | Experiment safely |

## PBS Restore Testing

Backups should produce evidence. A restore test does not need to expose private data; it just needs to prove that the recovery path works.

1. Pick a safe VM or test target.
2. Restore from PBS into an isolated environment.
3. Confirm the service boots.
4. Confirm DNS, proxy, storage mounts, and login flow where applicable.
5. Record the result in sanitized notes.

## 3-2-1 Backup Mindset

The classic 3-2-1 idea is:

- Keep multiple copies of important data.
- Use more than one storage type or location.
- Keep at least one copy away from the original failure domain.

In a homelab, this does not have to be perfect on day one. The practical goal is to avoid having the only backup live on the same system that failed.

## Restore Test Evidence Template

| Date | Backup Source | Restore Target | Result | Notes |
|---|---|---|---|---|
| YYYY-MM-DD | Example VM backup | Test VM | Pass / Fail | Sanitized notes |

## Restore Documentation

Document these details for important services:

- What is backed up.
- Where the backup lives.
- How often it runs.
- What is not included.
- How to restore safely.
- How the last restore test went.

## What Not To Publish

Do not publish:

- Backup encryption keys.
- Raw NAS exports.
- Raw backup exports.
- Private share names if they reveal personal data.
- Full database dumps.
- Real user files.
- Screenshots showing private data.
- Exact disk serials or full pool status output.

## What Viewers Can Learn

- Why backups should be tested.
- How PBS, NAS storage, and ZFS snapshots solve different problems.
- Why app-aware backups matter.
- How to document restore evidence without exposing the live lab.
- How to think about storage as part of operations, not just capacity.

# ZFS Storage Server

## Purpose

The ZFS storage server is a Rocky Linux system used for Linux-first storage practice, resilient datasets, snapshots, scrubs, and storage experiments.

## Where It Fits

```text
Linux apps / lab clients
  |
NFS, SMB, or direct service mounts
  |
Rocky Linux ZFS server
```

This server complements the Synology NAS. The NAS provides appliance storage; the ZFS server provides hands-on Linux storage learning.

## Host / Runtime

| Field | Value |
|---|---|
| Example host | `bison` |
| Runtime | Rocky Linux with ZFS |
| Example DNS | `zfs.home.example.com` |
| Public access | No |
| Main use | Datasets, storage learning, lab shares |

## Key Dependencies

- ZFS packages and kernel compatibility
- Disk health monitoring
- Snapshot schedule
- Scrub schedule
- Network shares for approved clients

## Network / DNS

Example:

```text
zfs.home.example.com -> 10.10.0.5
```

Expose only the storage protocols needed by trusted clients. Keep management tools private.

## Backup Notes

- ZFS snapshots help with rollback, but they are not off-host backups.
- Replicate important datasets when possible.
- Keep pool layout and disk identifiers private in the public repo.
- Document dataset purpose and retention in sanitized form.

## Security Notes

- Restrict NFS/SMB access by client and purpose.
- Do not publish full pool layouts with disk serial numbers.
- Keep management interfaces private.
- Test restore or rollback before relying on a snapshot plan.

## What Viewers Can Learn

- How ZFS pools, datasets, snapshots, and scrubs fit together.
- Why Linux storage teaches different lessons than a NAS appliance.
- How to think about snapshots versus backups.
- How to document storage without exposing private data.

## Future Improvements

- Add a sanitized dataset naming example.
- Add scrub and snapshot command examples.
- Add a public-safe ZFS health checklist.

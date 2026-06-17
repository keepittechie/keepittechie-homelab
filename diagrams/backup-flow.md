# Backup Flow Diagram

This diagram shows the public-safe backup and restore model for virtual machines, app data, NAS storage, ZFS snapshots, and restore verification.

## Diagram

```mermaid
flowchart TD
    VMs[Proxmox VMs and Containers] --> PBS[Proxmox Backup Server<br/>pbs.home.example.com]
    Apps[Application Data<br/>/mnt/storage/appdata] --> AppBackup[App-Aware Backup Jobs]
    Media[Media and Files<br/>/mnt/storage/media] --> NAS[Synology NAS<br/>nas.home.example.com]
    ZFS[Linux ZFS Datasets] --> Snapshots[ZFS Snapshots]

    AppBackup --> NAS
    AppBackup --> PBS
    Snapshots --> SnapshotReview[Snapshot Review]
    NAS --> BackupTarget[NAS Backup Target<br/>/volume1/backups]
    PBS --> Retention[Retention Policy]

    Retention --> RestoreTest[Restore Test Workflow]
    BackupTarget --> RestoreTest
    SnapshotReview --> RestoreTest

    RestoreTest --> IsolatedRestore[Restore to Test Target]
    IsolatedRestore --> VerifyBoot[Verify Boot and Service Health]
    VerifyBoot --> Evidence[Restore Test Evidence<br/>sanitized notes]
```

## How to Read This

Backups are split by what they protect. Proxmox Backup Server protects VM and container recovery. NAS storage can hold files and selected backup targets. ZFS snapshots provide rollback points for datasets. App-aware jobs cover data that may not be consistent from a VM backup alone.

The important final step is restore verification. A backup is only useful if the restore path has been tested and documented.

## Public-Safe Notes

- Paths such as `/mnt/storage/appdata`, `/mnt/storage/media`, and `/volume1/backups` are generic examples.
- The diagram does not include real dataset names, backup encryption details, raw NAS exports, or backup logs.
- Restore evidence should be sanitized before it is added to the public repo.

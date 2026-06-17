# Hardware

## Overview

This page describes the KeepItTechie homelab hardware at a public-safe level. It focuses on hardware categories, roles, and learning value rather than exact serial numbers, MAC addresses, full drive details, or private management information.

The goal is to help viewers understand why different kinds of hardware exist in the lab and how those roles support the services documented in this repo.

| Hardware Area | Role | Why It Matters | Public-Safe Notes |
|---|---|---|---|
| Firewall / router | Network edge and policy point | Centralizes routing, DHCP, firewall rules, and segmentation | Document role and design, not raw exports |
| Proxmox virtualization host | VM and container platform | Runs core infrastructure and lab workloads | Keep management access private |
| Synology NAS | Shared storage appliance | Provides files, media storage, and selected backup targets | Do not publish share exports or user files |
| Linux ZFS storage server | Linux storage learning platform | Teaches pools, datasets, snapshots, scrubs, and storage operations | Avoid disk serials and full pool output |
| GPU / local AI server | AI and GPU-assisted workloads | Supports local AI, model serving, and selected media workflows | Keep endpoints and model paths private |
| Client / admin workstation | Trusted management client | Used to administer, test, document, and record content | Do not publish user paths or screenshots with private data |
| Managed switch / Wi-Fi access layer | Wired and wireless connectivity | Supports segmentation and client access | Keep detailed port maps and device identifiers private |

## Compute

The compute layer is centered on Proxmox and supporting Linux hosts. Proxmox provides the virtualization layer for VMs and containers. Smaller workloads can run as containers or app VMs, while heavier workloads such as media or local AI are kept separate by role.

Public-safe compute examples:

| Compute Role | Typical Workloads | Viewer Lesson |
|---|---|---|
| Proxmox host | DNS, proxy, monitoring, app VMs, automation | Virtualization helps separate services by role |
| Docker / app host | Wiki.js, dashboard, monitoring, personal apps | Containers are useful when app state and config are managed carefully |
| Media host or VM | Plex, Servarr-style apps, Tautulli, Tdarr | Media services depend on storage, permissions, and private dashboards |
| GPU / AI server | llama.cpp endpoint, Open WebUI, local model experiments | Local AI benefits from dedicated compute and protected access |
| Admin workstation | Management, testing, documentation, recording | Trusted clients should be treated differently from guest devices |

## Network

The network hardware supports routing, segmentation, DNS, and access control. pfSense is the main firewall and router. Pi-hole provides internal DNS and filtering. A managed switch or Wi-Fi access layer can support client access and network separation.

Public-safe network examples:

| Network Role | Purpose | Viewer Lesson |
|---|---|---|
| pfSense firewall/router | Routing, DHCP, firewall policy, VPN, segmentation | Network policy should have a clear control point |
| Pi-hole primary and secondary | Internal DNS and filtering | DNS redundancy keeps service names available |
| Managed switch | Wired connectivity and possible VLAN support | Segmentation starts with both design and hardware support |
| Wi-Fi access layer | Client connectivity | Wireless access should not replace firewall policy |

## Storage

Storage is split by job. The Synology NAS provides appliance-style shared storage. The Linux ZFS storage server provides hands-on Linux storage learning. Local VM disks support operating systems and app runtimes.

Public-safe storage examples:

| Storage Role | Purpose | Viewer Lesson |
|---|---|---|
| Synology NAS | Shared files, media libraries, selected backup targets | A NAS is useful, but it is not automatically a backup |
| Linux ZFS storage server | Datasets, snapshots, scrubs, Linux storage practice | ZFS adds data integrity concepts beyond a basic filesystem |
| Local VM disks | Guest operating systems and runtime data | App data placement affects backup and restore planning |

## Backup Hardware

Backup storage exists to make recovery possible, not just to create files called backups. Proxmox Backup Server handles VM and container backup workflows, while NAS or storage targets may support selected app and file backup patterns.

Public-safe backup examples:

| Backup Role | Purpose | Viewer Lesson |
|---|---|---|
| Proxmox Backup Server | VM and container backups | Backups should have retention and restore tests |
| NAS backup target | File and app backup landing area | A backup target should not be the only copy of important data |
| Test restore target | Safe place to validate recovery | Restore test evidence matters more than backup claims |

## Media and GPU Workloads

Media and GPU workloads are separated from core infrastructure where possible because they can be storage-heavy, compute-heavy, or both. Plex, Servarr-style automation, Tautulli, Tdarr, Open WebUI, and llama.cpp patterns all benefit from deliberate placement.

Public-safe workload examples:

| Workload Area | Hardware Need | Viewer Lesson |
|---|---|---|
| Plex and media services | Storage access and possible hardware acceleration | Media stacks need careful paths, permissions, and privacy |
| Tdarr / transcode jobs | CPU or GPU resources | Processing jobs should not starve core infrastructure |
| Local AI | GPU resources and model storage | AI endpoints should stay protected even when local |

## What Is Intentionally Not Listed

- Serial numbers.
- MAC addresses.
- Exact drive serials.
- Exact private host IPs.
- Real internal domains.
- Detailed switch port maps.
- Raw firewall, router, or NAS exports.
- Private storage paths that reveal personal data.
- Photos or screenshots showing labels, QR codes, or management screens.

## Related Docs

- [Current Setup](current-setup.md)
- [Public-Safe Inventory](inventory-public.md)
- [Service Catalog](service-catalog.md)
- [Service Matrix](service-matrix.md)
- [Core Infrastructure](core-infrastructure.md)
- [Storage and Monitoring](storage-monitoring.md)
- [Apps and AI](apps-and-ai.md)

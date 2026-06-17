# Homelab Overview

The KeepItTechie homelab is a practical Linux and self-hosting environment. It is used for learning, content creation, local services, automation, media, monitoring, storage, and local AI experiments.

The goal is not to make a perfect enterprise network at home. The goal is to build a lab that is understandable, repairable, teachable, and safe enough to expose only the services that truly need public access.

For the visual version of this page, see the [Mermaid homelab overview](../diagrams/homelab-overview.md). For the first service deep dives, start with [Core Infrastructure](core-infrastructure.md). For storage, backups, and visibility, read [Storage and Monitoring](storage-monitoring.md). For application, media, local AI, dashboard, documentation, and automation services, read [Apps and AI](apps-and-ai.md). For a quick service-by-service comparison, see the [service matrix](service-matrix.md).

## Design Goals

| Goal | How The Lab Supports It |
|---|---|
| Learn by running real services | Use real DNS, reverse proxying, backups, monitoring, and automation |
| Keep critical services local-first | Private apps stay behind LAN, VPN, or internal DNS |
| Make services easy to find | Use readable names such as `grafana.home.example.com` |
| Separate roles | Firewall, DNS, storage, virtualization, monitoring, and apps each have clear ownership |
| Teach from the lab | Keep notes simple enough to explain in videos and rebuild later |
| Stay public-safe | Publish architecture, not secrets or raw exports |

## High-Level Layout

```text
Internet
  |
Cloudflare Tunnel
  | selected public services only
  |
pfSense firewall
  |
Internal LAN / lab networks
  |
  +-- Proxmox virtualization
  |   +-- Pi-hole primary and secondary DNS
  |   +-- NGINX reverse proxy
  |   +-- Monitoring stack
  |   +-- Media stack
  |   +-- Wiki.js, Glance, and personal apps
  |   +-- Local AI workloads
  |
  +-- Synology NAS
  +-- Rocky Linux ZFS storage server
  +-- Proxmox Backup Server
  +-- Admin workstations and client devices
```

## Main Roles

| Role | Service / Platform | Why It Exists |
|---|---|---|
| Firewall and routing | pfSense | Controls traffic, DHCP, VLANs, VPN, and firewall policy |
| DNS | Pi-hole VMs | Provides ad blocking, local service names, and DNS visibility |
| Virtualization | Proxmox | Hosts VMs and lab workloads |
| Shared storage | Synology NAS | Provides stable NAS storage for files, media, and backup targets |
| Linux storage learning | Rocky Linux ZFS server | Gives hands-on ZFS practice outside the NAS appliance |
| VM backups | Proxmox Backup Server | Stores deduplicated VM and container backups |
| Internal routing | NGINX reverse proxy | Gives services clean HTTPS names |
| Selected public access | Cloudflare Tunnel | Publishes only approved services without broad inbound exposure |
| Observability | Grafana, Prometheus, Loki, exporters | Makes health, metrics, and logs visible |
| Media | Plex, Servarr stack, Tautulli, Tdarr | Handles media streaming, automation, analytics, and transcode workflows |
| Local AI | GPU server, llama.cpp-compatible endpoint, Open WebUI | Keeps AI experimentation private and Linux-first |
| Automation | AWX / Ansible | Centralizes repeatable admin tasks |
| Documentation | Wiki.js and this repo | Keeps public teaching docs separate from private runbooks |

## Hostname Pattern

The real lab uses memorable hostnames for machines and service aliases for workloads. Public docs use sanitized examples:

```text
pontus.home.example.com       # example primary Pi-hole VM
priapus.home.example.com      # example secondary Pi-hole VM
proxy.home.example.com        # example reverse proxy alias
grafana.home.example.com      # example service alias
ai.home.example.com           # example local AI endpoint alias
```

This keeps the idea visible without publishing the live DNS zone.

## Public vs Private Boundary

| Category | Default Exposure |
|---|---|
| Firewall, DNS, hypervisor, backup server | Private only |
| Monitoring dashboards | Private only |
| Automation controllers | Private only |
| Media front ends | Limited, only when intentionally configured |
| Wiki or portfolio-style content | Public or partial, depending on namespace |
| Personal apps | Private only unless explicitly hardened |

The simplest rule: admin tools stay private, viewer-facing or intentionally shared apps can be routed through controlled public access.

## Related Docs

- [Core Infrastructure](core-infrastructure.md)
- [Storage and Monitoring](storage-monitoring.md)
- [Apps and AI](apps-and-ai.md)
- [Service Matrix](service-matrix.md)
- [Documentation Roadmap](roadmap.md)
- [Maintenance Checklist](maintenance-checklist.md)
- [Pre-Publish Review Checklist](pre-publish-review.md)
- [YouTube Companion Series](youtube-series.md)

# Homelab Overview

The KeepItTechie homelab is built around practical Linux, self-hosting, automation, and infrastructure learning.

## High-Level Layout

```text
Internet
  |
Cloudflare / VPN
  |
pfSense Firewall
  |
LAN / VLANs
  |
+-- Proxmox Host
|   +-- Docker App VM
|   +-- Pi-hole VMs
|   +-- Reverse Proxy VM
|   +-- PBS VM
|   +-- Media VMs
|   +-- Local AI / GPU VM
|
+-- Synology NAS
+-- ZFS Storage Server
+-- Client Devices
```

## Major Infrastructure Roles

| Role | Purpose |
|---|---|
| Firewall | Routes traffic, handles VLANs, VPN access, and firewall policy |
| DNS | Internal name resolution and ad blocking |
| Virtualization | Hosts Linux VMs and application workloads |
| Storage | Media, backups, datasets, shared files |
| Monitoring | Health, metrics, logs, and alert visibility |
| Reverse Proxy | Internal HTTPS routing and selected public app access |
| Local AI | Private AI experimentation, local inference, agent tooling |
| Documentation | Wiki, dashboards, Git repos, runbooks |

## Naming Convention

The lab uses memorable hostnames for servers and service aliases for common workloads.

Example pattern:

```text
server-name.home.example.com     -> physical or virtual machine identity
service-name.home.example.com    -> service role identity
```

This keeps machine identity separate from service identity.

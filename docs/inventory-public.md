# Public-Safe Inventory

This page summarizes the homelab by role without publishing live host details.

It is a public-safe tour, not a live inventory dump. The goal is to show how the lab is organized so readers can learn the pattern and explore related docs.

## Inventory Philosophy

The repo documents roles, service identities, access levels, and learning value. It intentionally avoids exact host IPs, serial numbers, MAC addresses, real internal domains, private DNS records, raw exports, credentials, and private runtime config.

Public examples use sanitized names such as `home.example.com`, `proxy.home.example.com`, `grafana.home.example.com`, and `ai.home.example.com`.

## Infrastructure Roles

| Role | Example Service Identity | Category | Access Level | Notes |
|---|---|---|---|---|
| Firewall / Router | `firewall.home.example.com` | Network | Private | Edge routing, DHCP, firewall policy, and segmentation |
| Primary DNS | `pihole1.home.example.com` | DNS | Private LAN | Internal DNS, filtering, and local records |
| Secondary DNS | `pihole2.home.example.com` | DNS | Private LAN | DNS redundancy for maintenance or failure |
| Virtualization | `proxmox.home.example.com` | Compute | VPN Only | VM and container host platform |
| Reverse proxy | `proxy.home.example.com` | Access | Private LAN | Internal HTTPS and service routing |
| Selected public access | `public.example.com` | Edge access | Limited Public | Public access only for approved services |

## Application Roles

| Role | Example Service Identity | Category | Access Level | Notes |
|---|---|---|---|---|
| Dashboard | `dashboard.home.example.com` | Navigation | Private LAN | Groups internal links and status widgets |
| Wiki | `wiki.home.example.com` | Documentation | Limited Public | Public/private docs should be separated |
| Private cloud | `nextcloud.home.example.com` | Files | Limited Public | Requires careful backup and hardening |
| Personal finance app | `finance.home.example.com` | Personal app | Private LAN | Fake data only in public examples |
| Career workflow app | `career.home.example.com` | Personal app | Private LAN | Resume and job data stay private |
| Automation UI | `awx.home.example.com` | Automation | VPN Only | Inventories and credentials stay private |

## Storage and Backup Roles

| Role | Example Service Identity | Category | Access Level | Notes |
|---|---|---|---|---|
| NAS | `nas.home.example.com` | Storage | Private LAN | Shared files, media storage, and selected backup targets |
| ZFS storage | `zfs.home.example.com` | Storage | Private LAN | Linux datasets, snapshots, scrubs, and storage learning |
| Backup server | `pbs.home.example.com` | Backup | VPN Only | VM and container backup target |
| App data storage | `appdata.home.example.com` | Storage | Internal Only | Generic app state and data placement concept |

## Monitoring and Visibility Roles

| Role | Example Service Identity | Category | Access Level | Notes |
|---|---|---|---|---|
| Grafana | `grafana.home.example.com` | Monitoring | Private LAN | Metrics and log dashboards |
| Prometheus | `prometheus.home.example.com` | Metrics | Internal Only | Scrapes metrics from exporters |
| Loki | `loki.home.example.com` | Logs | Internal Only | Stores logs for troubleshooting |
| Blackbox checks | `blackbox.home.example.com` | Monitoring | Internal Only | Checks service availability from the outside |
| Exporters | `exporters.home.example.com` | Metrics | Internal Only | Expose host, container, and platform metrics |

## Learning Value

| Area | What Readers Can Learn |
|---|---|
| Network | How routing, DNS, firewall policy, and segmentation fit together |
| Virtualization | Why VMs and containers help organize a homelab |
| Storage | How NAS storage, ZFS, datasets, and snapshots solve different problems |
| Backups | Why restore test evidence matters |
| Monitoring | How metrics, logs, dashboards, and checks support operations |
| Apps | How to document useful services without exposing private data |

## What Is Not Included

- Exact host IPs.
- Serial numbers.
- MAC addresses.
- Real internal domains.
- Private DNS records.
- Raw firewall, router, NAS, or app exports.
- Credentials, tokens, API keys, or private certificates.
- Financial, career, or private app data.

## Related Docs

- [Hardware](hardware.md)
- [Current Setup](current-setup.md)
- [Service Catalog](service-catalog.md)
- [Service Matrix](service-matrix.md)
- [Sanitized Inventory Example](../inventory/sanitized/hosts.example.yml)
- [Security Notes](security-notes.md)

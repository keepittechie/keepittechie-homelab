# Service Catalog

This catalog groups the KeepItTechie homelab services by category in a viewer-friendly way.

It is a public-safe learning map, not a live service export. The repo intentionally avoids exact host IPs, serial numbers, MAC addresses, real internal domains, private DNS records, raw exports, credentials, and private runtime config.

## Network and Access

### pfSense

- **Purpose:** Firewall, routing, DHCP, VPN, and segmentation.
- **Access:** Private / VPN only.
- **Learn more:** [pfSense](../services/pfsense/README.md)

### Pi-hole

- **Purpose:** Internal DNS, local records, and DNS filtering with primary and secondary resolvers.
- **Access:** Private LAN.
- **Learn more:** [Pi-hole](../services/pihole/README.md)

### NGINX Reverse Proxy

- **Purpose:** Internal HTTPS routing using service identities such as `proxy.home.example.com`.
- **Access:** Private LAN, with selected routes reviewed separately.
- **Learn more:** [Reverse Proxy](../services/reverse-proxy/README.md)

### Cloudflare Tunnel

- **Purpose:** Selected public access without opening broad inbound firewall ports.
- **Access:** Limited Public for approved services only.
- **Learn more:** [Cloudflare Tunnel](../services/cloudflare-tunnel/README.md)

## Virtualization and Backups

### Proxmox

- **Purpose:** VM and container platform for the lab.
- **Access:** VPN only.
- **Learn more:** [Proxmox](../services/proxmox/README.md)

### Proxmox Backup Server

- **Purpose:** VM and container backup target with retention and restore test planning.
- **Access:** VPN only.
- **Learn more:** [Proxmox Backup Server](../services/proxmox-backup-server/README.md)

## Storage

### Synology NAS

- **Purpose:** Shared files, media storage, and selected backup targets.
- **Access:** Private LAN.
- **Learn more:** [Synology NAS](../services/synology/README.md)

### Linux ZFS Storage

- **Purpose:** Linux storage learning with pools, datasets, snapshots, and scrubs.
- **Access:** Private LAN.
- **Learn more:** [ZFS Storage](../services/zfs-storage/README.md)

## Monitoring

### Grafana, Prometheus, Loki, and Exporters

- **Purpose:** Metrics, logs, dashboards, service checks, and operational visibility.
- **Access:** Private LAN / internal only.
- **Learn more:** [Monitoring](../services/monitoring/README.md)

## Media

### Media Stack

- **Purpose:** Plex, Servarr-style automation, Tautulli, and Tdarr workflows.
- **Access:** Private LAN by default, with limited public access only when reviewed.
- **Learn more:** [Media Stack](../services/media-stack/README.md)

## Local AI

### Local AI Stack

- **Purpose:** GPU server concept, llama.cpp OpenAI-compatible endpoint, and Open WebUI.
- **Access:** Private LAN / internal only.
- **Learn more:** [Local AI](../services/local-ai/README.md)

## Personal Apps

### FinanceHQ

- **Purpose:** Local-first personal finance app.
- **Access:** Private LAN.
- **Learn more:** [FinanceHQ](../services/financehq/README.md)

### CareerFill

- **Purpose:** Local-first career and job workflow app.
- **Access:** Private LAN.
- **Learn more:** [CareerFill](../services/careerfill/README.md)

## Documentation and Automation

### Wiki.js

- **Purpose:** Documentation hub for public and private knowledge boundaries.
- **Access:** Limited Public depending on namespace.
- **Learn more:** [Wiki.js](../services/wiki/README.md)

### Glance / Homepage Dashboard

- **Purpose:** Internal dashboard for service links and status views.
- **Access:** Private LAN.
- **Learn more:** [Glance / Homepage Dashboard](../services/glance/README.md)

### AWX / Ansible

- **Purpose:** Web automation controller and repeatable admin workflows.
- **Access:** VPN only.
- **Learn more:** [AWX / Ansible Automation](../services/automation-awx/README.md)

## Related Docs

- [Current Setup](current-setup.md)
- [Public-Safe Inventory](inventory-public.md)
- [Service Matrix](service-matrix.md)
- [How To Read Service Pages](how-to-read-service-pages.md)
- [Sanitized Examples](../examples/README.md)

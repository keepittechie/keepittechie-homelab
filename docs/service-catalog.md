# Service Catalog

This catalog groups the KeepItTechie homelab services by category. Use it when a quick answer is enough: what does this service do, why is it in the lab, and where is the deeper doc?

It is a public-safe learning map, not a live service export. The repo intentionally avoids exact host IPs, serial numbers, MAC addresses, real internal domains, private DNS records, raw exports, credentials, and private runtime config.

## Network and Access

### pfSense

- **Purpose:** Firewall, routing, DHCP, VPN, and segmentation.
- **Why it matters:** This is the control point that keeps admin services private and gives the rest of the lab a clean network foundation.
- **Access:** Private / VPN only.
- **Learn more:** [pfSense](../services/pfsense/README.md)

### Pi-hole

- **Purpose:** Internal DNS, local records, and DNS filtering with primary and secondary resolvers.
- **Why it matters:** Viewers can learn why names such as `grafana.home.example.com` are easier to manage than raw addresses.
- **Access:** Private LAN.
- **Learn more:** [Pi-hole](../services/pihole/README.md)

### NGINX Reverse Proxy

- **Purpose:** Internal HTTPS routing using service identities such as `proxy.home.example.com`.
- **Why it matters:** This is the pattern that gives apps friendly names while keeping private dashboards off the public internet.
- **Access:** Private LAN, with selected routes reviewed separately.
- **Learn more:** [Reverse Proxy](../services/reverse-proxy/README.md)

### Cloudflare Tunnel

- **Purpose:** Selected public access without opening broad inbound firewall ports.
- **Why it matters:** It shows how public access can be intentional instead of turning every service into an internet-facing app.
- **Access:** Limited Public for approved services only.
- **Learn more:** [Cloudflare Tunnel](../services/cloudflare-tunnel/README.md)

## Virtualization and Backups

### Proxmox

- **Purpose:** VM and container platform for the lab.
- **Why it matters:** Proxmox makes it easier to isolate workloads, test changes, back up systems, and rebuild services.
- **Access:** VPN only.
- **Learn more:** [Proxmox](../services/proxmox/README.md)

### Proxmox Backup Server

- **Purpose:** VM and container backup target with retention and restore test planning.
- **Why it matters:** It connects backup theory to a real restore path, which is what actually matters during recovery.
- **Access:** VPN only.
- **Learn more:** [Proxmox Backup Server](../services/proxmox-backup-server/README.md)

## Storage

### Synology NAS

- **Purpose:** Shared files, media storage, and selected backup targets.
- **Why it matters:** A NAS teaches shared storage, permissions, snapshots, and the difference between storage and backup.
- **Access:** Private LAN.
- **Learn more:** [Synology NAS](../services/synology/README.md)

### Linux ZFS Storage

- **Purpose:** Linux storage learning with pools, datasets, snapshots, and scrubs.
- **Why it matters:** ZFS is a good way to learn storage concepts that are usually hidden behind appliance interfaces.
- **Access:** Private LAN.
- **Learn more:** [ZFS Storage](../services/zfs-storage/README.md)

## Monitoring

### Grafana, Prometheus, Loki, and Exporters

- **Purpose:** Metrics, logs, dashboards, service checks, and operational visibility.
- **Why it matters:** Monitoring helps answer what changed, what broke, and where troubleshooting should start.
- **Access:** Private LAN / internal only.
- **Learn more:** [Monitoring](../services/monitoring/README.md)

## Media

### Media Stack

- **Purpose:** Plex, Servarr-style automation, Tautulli, and Tdarr workflows.
- **Why it matters:** The media stack is a practical example of multiple apps depending on storage, DNS, permissions, and private dashboards.
- **Access:** Private LAN by default, with limited public access only when reviewed.
- **Learn more:** [Media Stack](../services/media-stack/README.md)

## Local AI

### Local AI Stack

- **Purpose:** GPU server concept, llama.cpp OpenAI-compatible endpoint, and Open WebUI.
- **Why it matters:** This shows how local-first AI can run inside a Linux homelab without exposing prompts or compute resources publicly.
- **Access:** Private LAN / internal only.
- **Learn more:** [Local AI](../services/local-ai/README.md)

## Personal Apps

### FinanceHQ

- **Purpose:** Local-first personal finance app.
- **Why it matters:** It demonstrates how to document architecture and backup thinking without publishing real financial records.
- **Access:** Private LAN.
- **Learn more:** [FinanceHQ](../services/financehq/README.md)

### CareerFill

- **Purpose:** Local-first career and job workflow app.
- **Why it matters:** It shows how personal workflow apps can be discussed publicly while resumes, applications, and messages stay private.
- **Access:** Private LAN.
- **Learn more:** [CareerFill](../services/careerfill/README.md)

## Documentation and Automation

### Wiki.js

- **Purpose:** Documentation hub for public and private knowledge boundaries.
- **Why it matters:** A wiki helps separate public teaching docs from private runbooks and operational notes.
- **Access:** Limited Public depending on namespace.
- **Learn more:** [Wiki.js](../services/wiki/README.md)

### Glance / Homepage Dashboard

- **Purpose:** Internal dashboard for service links and status views.
- **Why it matters:** A dashboard makes daily navigation easier, but it can also reveal too much if exposed publicly.
- **Access:** Private LAN.
- **Learn more:** [Glance / Homepage Dashboard](../services/glance/README.md)

### AWX / Ansible

- **Purpose:** Web automation controller and repeatable admin workflows.
- **Why it matters:** Automation turns repeated admin tasks into documented jobs, but real credentials and inventories must stay private.
- **Access:** VPN only.
- **Learn more:** [AWX / Ansible Automation](../services/automation-awx/README.md)

## Related Docs

- [Current Setup](current-setup.md)
- [Public-Safe Inventory](inventory-public.md)
- [Service Matrix](service-matrix.md)
- [How To Read Service Pages](how-to-read-service-pages.md)
- [Sanitized Examples](../examples/README.md)

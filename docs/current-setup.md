# Current Setup

This page gives a high-level tour of the KeepItTechie homelab as documented in this repo. It is written like a walkthrough: what each part does, why it exists, and what viewers can take into their own lab.

## How to Read This Page

This is a public-safe overview, not a live inventory dump. It explains the shape of the lab without publishing the details that should stay private.

Exact host IPs, private domains, credentials, private certificates, tunnel identifiers, raw config exports, and sensitive app data are intentionally left out. Public examples use sanitized values such as `home.example.com`, `10.10.0.0/24`, `proxy.home.example.com`, `grafana.home.example.com`, and `ai.home.example.com`.

## Network

The tour starts at the network edge. pfSense is the firewall and router, so it is the part of the lab that decides how traffic moves between the internet, trusted devices, lab services, and lower-trust networks.

Pi-hole provides the internal DNS layer. The lab uses a primary and secondary DNS pattern so clients can keep resolving names during maintenance or failure of one resolver. For beginners, the key thing to understand is that DNS turns a service name such as `grafana.home.example.com` into the place that service lives.

The public docs use `10.10.0.0/24` as an example network and describe VLAN or segmentation concepts without publishing the real network map.

This section teaches how routing, firewall policy, DHCP, DNS, and segmentation work together instead of treating them as separate topics.

Related docs:

- [Homelab DNS and Pi-hole Guide](guides/dns-pihole.md)
- [Network Design](network.md)
- [Core Infrastructure](core-infrastructure.md)
- [DNS Flow Diagram](../diagrams/dns-flow.md)
- [pfSense](../services/pfsense/README.md)
- [Pi-hole](../services/pihole/README.md)

## Virtualization

Once the network is in place, Proxmox becomes the compute layer. It runs VMs and containers grouped by purpose: DNS, reverse proxying, monitoring, media services, automation, documentation, local AI, and personal apps.

The docs separate service identity from machine identity. A service identity is the name users remember, such as `proxy.home.example.com`. A machine identity is the VM or host that runs the service. This makes it easier to move or rebuild a service without changing how people reach it.

This is where viewers can see why virtualization is useful in a homelab: isolation, snapshots, backup integration, testing, and cleaner rebuilds.

Related docs:

- [Proxmox VM Layout Guide](guides/proxmox-vm-layout.md)
- [Proxmox](../services/proxmox/README.md)
- [Core Infrastructure](core-infrastructure.md)

## Storage

Storage is split across a Synology NAS and a Linux ZFS storage server. The NAS handles shared files, media libraries, and selected backup targets. The ZFS server is the hands-on Linux storage learning box, where pools, datasets, snapshots, scrubs, and storage operations are easier to study directly.

The docs explain media storage, app data, backup storage, and snapshot concepts without publishing private share names, disk serials, raw NAS exports, or full pool output.

The reason this matters is simple: shared storage, snapshots, and backups solve different problems.

Related docs:

- [Storage and Monitoring](storage-monitoring.md)
- [Storage and Backups](storage-and-backups.md)
- [Synology NAS](../services/synology/README.md)
- [ZFS Storage](../services/zfs-storage/README.md)

## Backups

Proxmox Backup Server is the VM and container backup target. It is the part of the lab that turns virtual machines from "easy to create" into "possible to recover."

The backup docs focus on recoverability, not just backup creation. Restore test evidence matters because a backup is only useful if the restore path works.

Viewers can learn how VM backups, app-aware backups, NAS targets, ZFS snapshots, and restore testing fit together without pretending that one tool solves every recovery problem.

Related docs:

- [Homelab Backups and Restore Testing Guide](guides/backups-restore.md)
- [Proxmox Backup Server](../services/proxmox-backup-server/README.md)
- [Backup Flow Diagram](../diagrams/backup-flow.md)
- [Storage and Backups](storage-and-backups.md)

## Monitoring

Monitoring is built around Grafana, Prometheus, exporters, Loki, and Promtail. Node Exporter shows Linux host metrics. cAdvisor shows container metrics. Blackbox Exporter checks service availability. Loki and Promtail collect logs.

Monitoring is treated as visibility, not decoration. The goal is to answer three practical questions: what is healthy, what changed, and where should troubleshooting start?

Viewers can learn the difference between metrics, logs, dashboards, and service checks.

Related docs:

- [Homelab Monitoring with Grafana and Prometheus Guide](guides/monitoring-grafana.md)
- [Monitoring](../services/monitoring/README.md)
- [Monitoring Flow Diagram](../diagrams/monitoring-flow.md)

## Reverse Proxy and Remote Access

NGINX provides internal HTTPS routing through the reverse proxy. Internal DNS points service identities such as `grafana.home.example.com` at the proxy, and the proxy sends traffic to the correct backend app.

Cloudflare Tunnel is documented as a selected public access path only. It is not a reason to publish every dashboard. Admin tools, monitoring, backup systems, hypervisors, and automation controllers should stay private unless there is a specific hardened access plan.

Viewers can learn the difference between internal reverse proxy access, VPN-style access, and selected public access.

Related docs:

- [Homelab Reverse Proxy and Internal HTTPS Guide](guides/reverse-proxy.md)
- [Reverse Proxy](../services/reverse-proxy/README.md)
- [Cloudflare Tunnel](../services/cloudflare-tunnel/README.md)
- [Reverse Proxy Flow Diagram](../diagrams/reverse-proxy-flow.md)
- [NGINX Example](../examples/nginx/README.md)
- [Cloudflare Tunnel Example](../examples/cloudflare-tunnel/README.md)

## Media

The media stack includes Plex, Servarr-style automation, Tautulli, and Tdarr. Plex handles playback, Servarr-style apps organize the workflow, Tautulli adds Plex visibility, and Tdarr supports transcode automation.

Media services depend heavily on storage, metadata, and app state. Automation dashboards should stay private because they can expose libraries, paths, queues, and account details.

Viewers can learn how multi-app workflows depend on DNS, storage, permissions, backups, and private dashboards.

Related docs:

- [Media Stack](../services/media-stack/README.md)

## Local AI

The local AI stack uses a GPU server concept, a llama.cpp OpenAI-compatible endpoint, and Open WebUI. This keeps AI experimentation local-first and makes it easier to learn how Linux, GPUs, models, APIs, and private app integrations fit together.

AI endpoints should stay protected. A local endpoint can still expose private prompts, app context, model behavior, or compute resources if it is published carelessly.

Viewers can learn how a local AI service can support private experimentation without depending on a hosted API for every request.

Related docs:

- [Local AI on Linux Guide](guides/local-ai.md)
- [Local AI](../services/local-ai/README.md)
- [Local AI Flow Diagram](../diagrams/local-ai-flow.md)

## Personal Apps

FinanceHQ and CareerFill are local-first personal apps. The repo documents their architecture and lessons without publishing private financial records, job applications, recruiter messages, resumes, or private databases.

Public examples should use demo or fake data only.

Viewers can learn how personal apps can be documented safely: publish architecture, boundaries, backup thinking, and lessons learned, not private records.

Related docs:

- [FinanceHQ](../services/financehq/README.md)
- [CareerFill](../services/careerfill/README.md)

## Documentation

Documentation lives in this repo and in Wiki.js. The public repo focuses on viewer-friendly architecture, service summaries, diagrams, glossary entries, examples, and safety boundaries. Wiki.js can support deeper internal notes, but public and private documentation should stay separated.

Viewers can learn how to turn a real homelab into a teachable system without dumping private notes into GitHub.

Related docs:

- [Wiki.js](../services/wiki/README.md)
- [Documentation Index](docs-index.md)
- [Glossary](glossary.md)
- [Sanitized Examples](../examples/README.md)
- [Diagrams](../diagrams/README.md)

## Automation

AWX and Ansible provide the automation layer. Inventories, playbooks, credentials, and job templates can make admin tasks repeatable, but real inventory and credentials must stay private.

The repo should teach safe automation patterns using sanitized examples and role-based explanations.

Viewers can learn how automation improves repeatability while still requiring careful boundaries around credentials and inventories.

Related docs:

- [AWX / Ansible Automation](../services/automation-awx/README.md)

## What Is Intentionally Not Included

- Exact host IPs.
- Real internal domains.
- Secrets.
- Tokens.
- Credentials.
- Private certificates.
- Tunnel identifiers.
- Raw firewall exports.
- Raw NAS exports.
- Screenshots with sensitive data.
- Financial or career data.
- Private app databases.

## Where to Go Next

1. [Viewer Guide](viewer-guide.md)
2. [Full Homelab Tour Guide](guides/full-homelab-tour.md)
3. [Build Your Own Homelab](build-your-own.md)
4. [Glossary](glossary.md)
5. [Hardware](hardware.md)
6. [Public-Safe Inventory](inventory-public.md)
7. [Service Catalog](service-catalog.md)
8. [Diagrams](../diagrams/README.md)
9. [Service Matrix](service-matrix.md)
10. [Core Infrastructure](core-infrastructure.md)
11. [Storage and Monitoring](storage-monitoring.md)
12. [Apps and AI](apps-and-ai.md)
13. [Sanitized Examples](../examples/README.md)

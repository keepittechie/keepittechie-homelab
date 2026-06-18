# Full Homelab Tour

This page is a public-safe companion guide for a KeepItTechie homelab tour video.

## Episode Goal

The goal of this episode is to introduce the major layers of the KeepItTechie homelab without turning the tour into a private inventory dump.

A full tour can show how the network, DNS, virtualization, storage, backups, monitoring, reverse proxy, media services, local AI, documentation, automation, and personal apps fit together. For beginners, the key takeaway is that a homelab becomes easier to understand when every service has a role.

## What Viewers Will Learn

- Why a homelab is useful for learning Linux, networking, storage, automation, and self-hosting.
- How services are grouped by role instead of treated as one giant stack.
- Why DNS matters once more than a few services exist.
- Why backups should come before adding too much complexity.
- Why not every service should be exposed publicly.
- How diagrams and sanitized examples help viewers learn safely.
- How this repo separates public teaching docs from private config.

## Lab Areas Covered

| Area | What It Does | Related Docs |
|---|---|---|
| Network | Routes traffic, applies firewall policy, and separates trusted from lower-trust networks | [Network Design](../network.md), [Core Infrastructure](../core-infrastructure.md) |
| DNS | Gives services readable names and keeps local resolution controlled | [Pi-hole](../../services/pihole/README.md), [DNS Flow](../../diagrams/dns-flow.md) |
| Proxmox / Virtualization | Runs VMs and containers grouped by purpose | [Proxmox](../../services/proxmox/README.md), [Core Infrastructure](../core-infrastructure.md) |
| Storage | Provides shared files, app data storage, media storage, and ZFS learning space | [Storage and Monitoring](../storage-monitoring.md), [Storage and Backups](../storage-and-backups.md) |
| Backups | Makes recovery possible through VM backups, app data backups, and restore testing | [Proxmox Backup Server](../../services/proxmox-backup-server/README.md), [Backup Flow](../../diagrams/backup-flow.md) |
| Monitoring | Shows host health, container health, logs, service checks, and trends | [Monitoring](../../services/monitoring/README.md), [Monitoring Flow](../../diagrams/monitoring-flow.md) |
| Reverse Proxy / Remote Access | Provides internal HTTPS and selected public access boundaries | [Reverse Proxy](../../services/reverse-proxy/README.md), [Cloudflare Tunnel](../../services/cloudflare-tunnel/README.md) |
| Media | Runs Plex and media automation workflows backed by storage | [Media Stack](../../services/media-stack/README.md) |
| Local AI | Runs local-first AI tooling with a GPU server concept and Open WebUI | [Local AI](../../services/local-ai/README.md), [Local AI Flow](../../diagrams/local-ai-flow.md) |
| Personal Apps | Documents local-first app patterns without publishing private records | [FinanceHQ](../../services/financehq/README.md), [CareerFill](../../services/careerfill/README.md) |
| Documentation | Keeps public teaching docs separate from private runbooks | [Wiki.js](../../services/wiki/README.md), [Documentation Index](../docs-index.md) |
| Automation | Uses AWX and Ansible concepts to make admin tasks repeatable | [AWX / Ansible](../../services/automation-awx/README.md) |

## Suggested Video Flow

1. A tour video can start with what this repo is and is not: a public-safe learning map, not a private config dump.
2. Viewers can follow the high-level diagram to see the whole lab before opening individual service docs.
3. The network and DNS section can explain pfSense, Pi-hole, service names, and why internal DNS matters.
4. The virtualization section can show how Proxmox groups workloads by role.
5. The storage and backups section can explain NAS storage, ZFS learning, Proxmox Backup Server, and restore testing.
6. The monitoring section can explain Grafana, Prometheus, exporters, Loki, logs, and service checks.
7. The apps and media section can show how user-facing apps depend on storage, DNS, proxying, and backups.
8. The local AI section can explain Open WebUI, a local OpenAI-compatible endpoint, and why AI endpoints stay protected.
9. The automation and documentation section can connect AWX, Ansible, Wiki.js, and this repo.
10. The close can point viewers to the build-your-own path so they can start small instead of copying the whole lab.

## Repo Files to Follow Along

- [README](../../README.md)
- [Current Setup](../current-setup.md)
- [Build Your Own Homelab](../build-your-own.md)
- [Viewer Guide](../viewer-guide.md)
- [Documentation Index](../docs-index.md)
- [Service Catalog](../service-catalog.md)
- [Service Matrix](../service-matrix.md)
- [Diagrams](../../diagrams/README.md)
- [Sanitized Examples](../../examples/README.md)

## Public-Safe Demo Ideas

- Walk through the Mermaid homelab overview diagram.
- Open the sanitized DNS flow and explain how service names replace raw addresses.
- Use the service catalog to show services grouped by role.
- Open the sanitized NGINX example and explain the reverse proxy pattern.
- Open the Docker Compose template and point out placeholder values.
- Show how to read a service README: purpose, placement, network, backup, and security notes.
- Show examples of what not to publish, such as raw firewall exports, private dashboards, and live config.

Avoid live dashboards unless the view is sanitized or uses fake demo data.

## What Is Intentionally Not Shown

- Exact host IPs.
- Real internal domains.
- Credential values, API keys, or access tokens.
- Private certificates.
- Tunnel identifiers.
- Raw firewall exports.
- Raw NAS exports.
- Live admin dashboards.
- Financial or career app data.
- Private databases.
- Real user files.

## Commands and Examples

Viewers can clone the public repo and run the lightweight docs checks locally:

```bash
git clone https://github.com/keepittechie/keepittechie-homelab.git
cd keepittechie-homelab

python3 scripts/check_markdown_links.py
python3 scripts/check_diagrams.py
python3 scripts/public_safety_scan.py
```

These commands check documentation links, diagram structure, and obvious public-safety issues. They do not replace manual review.

## After Watching

- Read the [Current Setup](../current-setup.md) page.
- Follow the [Build Your Own Homelab](../build-your-own.md) learning path.
- Study the [diagrams](../../diagrams/README.md).
- Pick one service area from the [Service Catalog](../service-catalog.md).
- Adapt [sanitized examples](../../examples/README.md) in a private lab.
- Document your own lab safely with placeholders and public-safe notes.

## Related Docs

- [Current Setup](../current-setup.md)
- [Build Your Own Homelab](../build-your-own.md)
- [Viewer Guide](../viewer-guide.md)
- [Glossary](../glossary.md)
- [Screenshot Policy](../screenshots-policy.md)
- [Pre-Publish Review](../pre-publish-review.md)

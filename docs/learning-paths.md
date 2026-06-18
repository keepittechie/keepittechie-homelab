# Learning Paths

This page groups the repo into practical paths readers can follow.

The KeepItTechie homelab has a lot of moving parts, but readers do not need to learn everything at once. Pick the path that matches the current goal, read the public-safe docs, and adapt the patterns in a private lab.

## Start Here

Use this path to understand the repo before jumping into individual services.

1. [Current Setup](current-setup.md)
2. [Viewer Guide](viewer-guide.md)
3. [Documentation Index](docs-index.md)
4. [Glossary](glossary.md)
5. [Homelab Guides](guides/README.md)

## Build a Basic Homelab

This path is for readers starting from a small machine, mini PC, old desktop, or spare laptop.

- Read [Build Your Own Homelab](build-your-own.md).
- Review [How to Read Service Pages](how-to-read-service-pages.md).
- Start with one Linux host and one simple app.
- Add DNS, backups, and monitoring before adding too many services.
- Keep private credentials and real config outside public GitHub repos.

## Learn Networking and DNS

This path explains how the lab routes traffic, hands out network settings, and gives services readable names.

- [Network Design](network.md)
- [Core Infrastructure](core-infrastructure.md)
- [Homelab DNS and Pi-hole](guides/dns-pihole.md)
- [DNS Flow Diagram](../diagrams/dns-flow.md)
- [pfSense](../services/pfsense/README.md)
- [Pi-hole](../services/pihole/README.md)

## Learn Virtualization

This path explains how Proxmox supports the VM and container layout.

- [Proxmox VM Layout](guides/proxmox-vm-layout.md)
- [Proxmox](../services/proxmox/README.md)
- [Core Infrastructure](core-infrastructure.md)
- [Service Catalog](service-catalog.md)
- [Service Matrix](service-matrix.md)

## Learn Backups and Restore Testing

This path focuses on recovery, not just backup jobs.

- [Homelab Backups and Restore Testing](guides/backups-restore.md)
- [Storage and Backups](storage-and-backups.md)
- [Storage and Monitoring](storage-monitoring.md)
- [Backup Flow Diagram](../diagrams/backup-flow.md)
- [Proxmox Backup Server](../services/proxmox-backup-server/README.md)
- [Synology NAS](../services/synology/README.md)
- [ZFS Storage](../services/zfs-storage/README.md)

## Learn Monitoring

This path explains how the lab checks hosts, containers, services, metrics, and logs.

- [Homelab Monitoring with Grafana and Prometheus](guides/monitoring-grafana.md)
- [Monitoring](../services/monitoring/README.md)
- [Monitoring Flow Diagram](../diagrams/monitoring-flow.md)
- [Prometheus Example](../examples/prometheus/README.md)
- [Screenshots Policy](screenshots-policy.md)

## Learn Reverse Proxy and Internal HTTPS

This path explains clean service names, internal HTTPS, and the difference between private access and selected public access.

- [Homelab Reverse Proxy and Internal HTTPS](guides/reverse-proxy.md)
- [Reverse Proxy](../services/reverse-proxy/README.md)
- [Cloudflare Tunnel](../services/cloudflare-tunnel/README.md)
- [Reverse Proxy Flow Diagram](../diagrams/reverse-proxy-flow.md)
- [NGINX Example](../examples/nginx/README.md)
- [Cloudflare Tunnel Example](../examples/cloudflare-tunnel/README.md)

## Learn Local AI

This path explains how local AI fits into a Linux homelab without exposing private prompts, documents, endpoints, or model paths.

- [Local AI on Linux](guides/local-ai.md)
- [Apps and AI](apps-and-ai.md)
- [Local AI Stack](../services/local-ai/README.md)
- [Local AI Flow Diagram](../diagrams/local-ai-flow.md)
- [Build Your Own Homelab](build-your-own.md)

## Related Docs

- [Current Setup](current-setup.md)
- [Build Your Own Homelab](build-your-own.md)
- [Homelab Guides](guides/README.md)
- [Documentation Index](docs-index.md)
- [Service Catalog](service-catalog.md)
- [Sanitized Examples](../examples/README.md)
- [Pre-Publish Review](pre-publish-review.md)

# Viewer Guide

This guide explains how viewers can use the KeepItTechie homelab repo as a learning resource.

## Recommended Path

1. Start with the [Homelab Overview](overview.md).
2. Tour the [Current Setup](current-setup.md).
3. Read [Build Your Own Homelab](build-your-own.md) to see a staged learning path.
4. Review [Hardware](hardware.md) for hardware roles.
5. Browse the [Service Catalog](service-catalog.md).
6. Open the [diagram index](../diagrams/README.md).
7. Read the [service matrix](service-matrix.md) to understand what runs where.
8. Keep the [Glossary](glossary.md) open for unfamiliar terms.
9. Review [How To Read Service Pages](how-to-read-service-pages.md).
10. Pick one service area to study.
11. Compare the service README with the matching [sanitized examples](../examples/README.md).
12. Use the [Security Notes](security-notes.md) before adapting any pattern.
13. Build safely in a lab before using a pattern for important services.

## Good First Topics

| Topic | Start Here | Why |
|---|---|---|
| Internal DNS | [Pi-hole](../services/pihole/README.md) | Makes services readable and easier to troubleshoot |
| Reverse proxying | [Reverse Proxy](../services/reverse-proxy/README.md) | Teaches internal HTTPS and service routing |
| Virtualization | [Proxmox](../services/proxmox/README.md) | Explains how workloads are separated |
| Backups | [Storage and Backups](storage-and-backups.md) | Shows why restore testing matters |
| Monitoring | [Monitoring](../services/monitoring/README.md) | Shows how metrics and logs support operations |
| Local AI | [Local AI](../services/local-ai/README.md) | Demonstrates local-first AI architecture |

## How To Use The Examples

The examples are templates for learning. They are not production config dumps.

- Read the related service doc first.
- Review the example file second.
- Replace placeholders only in private config.
- Keep real `.env` files, credentials, certificates, tunnel config, and exports out of Git.
- Test changes in a lab before relying on them.

## Public-Safe Mindset

Public documentation should explain the design without exposing private infrastructure. Use sanitized names such as `home.example.com`, broad network examples such as `10.10.0.0/24`, and fake data for screenshots or demos.

The goal is to learn the pattern, not copy a private deployment line for line.

## Related Docs

- [Documentation Index](docs-index.md)
- [Current Setup](current-setup.md)
- [Build Your Own Homelab](build-your-own.md)
- [Hardware](hardware.md)
- [Public-Safe Inventory](inventory-public.md)
- [Service Catalog](service-catalog.md)
- [Glossary](glossary.md)
- [How To Read Service Pages](how-to-read-service-pages.md)

# Viewer Guide

This guide explains how viewers can use the KeepItTechie homelab repo without getting lost in the number of docs. Pick the path that matches what you want to learn.

## Choose a Path

| If You Want To... | Start Here | Why |
|---|---|---|
| Tour the current lab | [Current Setup](current-setup.md) | See what is running, why it exists, and how the parts connect |
| Build something similar | [Build Your Own Homelab](build-your-own.md) | Follow a staged path that starts small |
| Learn the big picture | [Homelab Overview](overview.md) | Understand the main roles before opening deep dives |
| Study one service | [Service Catalog](service-catalog.md) | Pick a service by category and jump to its README |
| Understand diagrams | [Diagram Index](../diagrams/README.md) | Follow network, DNS, backup, proxy, AI, and monitoring flows |
| Understand future visuals | [Visual Assets Guide](visual-assets-guide.md) | Learn how screenshots, mockups, and thumbnails should be reviewed |
| Copy a safe pattern | [Sanitized Examples](../examples/README.md) | Learn from templates that use placeholders instead of private values |
| Decode unfamiliar terms | [Glossary](glossary.md) | Keep short definitions nearby while reading |

## Recommended Path

1. Start with the [Current Setup](current-setup.md).
2. Read [Build Your Own Homelab](build-your-own.md) if you want to build your own version in stages.
3. Use the [Homelab Overview](overview.md) to understand the main roles.
4. Review [Hardware](hardware.md) for hardware roles.
5. Browse the [Service Catalog](service-catalog.md).
6. Open the [diagram index](../diagrams/README.md).
7. Read the [service matrix](service-matrix.md) to understand what runs where.
8. Keep the [Glossary](glossary.md) open for unfamiliar terms.
9. Review [How To Read Service Pages](how-to-read-service-pages.md).
10. Pick one service area to study.
11. Compare the service README with the matching [sanitized examples](../examples/README.md).
12. Review the [Visual Assets Guide](visual-assets-guide.md) before adding images or mockups.
13. Use the [Security Notes](security-notes.md) before adapting any pattern.
14. Build safely in a lab before using a pattern for important services.

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
- Change one thing at a time so troubleshooting stays simple.

## Public-Safe Mindset

Public documentation should explain the design without exposing private infrastructure. Use sanitized names such as `home.example.com`, broad network examples such as `10.10.0.0/24`, and fake data in screenshots or demos.

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
- [Visual Assets Guide](visual-assets-guide.md)
- [Assets Index](../assets/README.md)

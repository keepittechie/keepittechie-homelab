# Glossary

This glossary explains common homelab terms used throughout the KeepItTechie homelab docs. The definitions are short on purpose: enough to understand the repo, then deep enough to know what to study next.

| Term | Beginner-Friendly Meaning |
|---|---|
| Homelab | A home-based lab used to learn real infrastructure skills with servers, networking, storage, apps, and automation. |
| Self-hosted | Running a service on infrastructure under direct control instead of relying only on a third-party hosted service. |
| LAN | The local network inside a home or lab. Devices on the LAN usually trust each other more than internet devices. |
| VLAN | A way to split one physical network into separate logical networks, often used to separate admin devices, servers, IoT, and guests. |
| Firewall | A policy layer that allows or blocks traffic between networks. In this repo, pfSense is the main firewall. |
| Router | The device or service that moves traffic between networks, such as LAN, VLANs, VPN, and the internet. |
| DNS | The system that turns names like `grafana.home.example.com` into network destinations. |
| DHCP | The service that gives clients network settings automatically, including address, gateway, and DNS servers. |
| Pi-hole | A DNS resolver that can block unwanted domains and answer local DNS names inside the lab. |
| Reverse proxy | A web routing layer that receives requests for friendly service names and forwards them to backend apps. |
| TLS | The encryption layer behind HTTPS. It helps protect browser-to-service traffic. |
| Certificate | A file used by TLS to prove a service name and enable encrypted connections. Public docs should never include private keys. |
| Internal DNS | DNS names that work inside the lab, such as `proxy.home.example.com`, and are not meant to be public internet records. |
| Service identity | The name users think of when using an app, such as `grafana.home.example.com`. |
| Machine identity | The name of the VM, container host, or physical machine running one or more services. |
| VPN | A private encrypted connection into the lab, often used to manage services remotely without making them public. |
| Cloudflare Tunnel | An outbound tunnel pattern used to publish selected services without opening broad inbound firewall ports. |
| Proxmox | The virtualization platform used to run VMs and containers in the lab. |
| Virtual machine | A full guest computer running on a hypervisor. It has its own operating system and resources. |
| Container | A lighter runtime unit for apps that shares the host kernel but keeps app files and processes separated. |
| Docker Compose | A YAML-based way to define and run one or more containers for an app stack. |
| NAS | Network-attached storage. A storage system shared across the network for files, media, and selected backup targets. |
| ZFS | A storage filesystem and volume manager known for snapshots, checksums, pools, datasets, and data integrity features. |
| Dataset | A ZFS-managed filesystem inside a pool. Datasets make it easier to apply separate settings and snapshots. |
| Snapshot | A point-in-time view of data that can help recover from accidental changes or deletes. |
| Scrub | A ZFS health check that reads stored data and verifies it against checksums. |
| Backup | A separate copy of important data or systems that can be used after failure, deletion, or bad changes. |
| Restore test | A controlled test that proves a backup can actually be restored. |
| Proxmox Backup Server | A backup platform built to store and manage Proxmox VM and container backups. |
| Monitoring | The practice of watching health signals so problems can be found before they become mysteries. |
| Metrics | Numeric measurements over time, such as CPU usage, memory use, disk space, and service response time. |
| Logs | Text records from systems and apps. Logs explain events that metrics alone cannot show. |
| Prometheus | A metrics collection and storage system often used with exporters and Grafana. |
| Grafana | A dashboard tool used to visualize metrics, logs, and service health. |
| Exporter | A small service that exposes metrics in a format Prometheus can scrape. |
| Blackbox check | A test that checks a service from the outside, such as whether a web page returns a healthy response. |
| Local AI | AI tools and models running on local infrastructure instead of depending entirely on external hosted APIs. |
| OpenAI-compatible endpoint | An API that follows the same general request style many OpenAI clients expect, but can point to a local backend. |
| Open WebUI | A browser-based interface used to interact with local or remote AI models. |
| Public-safe | Written or shown in a way that teaches the pattern without exposing private infrastructure details. |
| Sanitized example | A fake or generalized example that uses placeholders such as `home.example.com` instead of live values. |
| Private config | Real runtime config that may include domains, credentials, host details, paths, and other sensitive values. It should stay out of the public repo. |

## Related Docs

- [Viewer Guide](viewer-guide.md)
- [Documentation Index](docs-index.md)
- [How To Read Service Pages](how-to-read-service-pages.md)
- [Security Notes](security-notes.md)

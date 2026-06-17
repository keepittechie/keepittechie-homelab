# Homelab Overview Diagram

This diagram is a public-safe architecture placeholder for the KeepItTechie homelab. It shows service roles and traffic flow without exposing real public domains, real public IPs, private credentials, or raw exports.

```mermaid
flowchart TD
    internet[Internet] --> edge[Cloudflare Tunnel / VPN]
    edge --> firewall[pfSense Firewall]
    firewall --> lan[VLANs / LAN<br/>10.10.0.0/24 example]

    lan --> dns[DNS Layer<br/>Pi-hole Primary + Secondary]
    lan --> proxmox[Proxmox Virtualization]
    lan --> storage[Storage Layer]
    lan --> monitoring[Monitoring Layer]

    dns --> pihole1[pihole1.home.example.com]
    dns --> pihole2[pihole2.home.example.com]

    proxmox --> docker[Docker / App Hosts]
    proxmox --> media[Media Stack]
    proxmox --> ai[Local AI]
    proxmox --> personal[Personal Apps]
    proxmox --> automation[AWX / Ansible]

    docker --> proxy[NGINX Reverse Proxy<br/>proxy.home.example.com]
    docker --> wiki[Wiki.js]
    docker --> dashboard[Glance or Homepage Dashboard]

    storage --> nas[Synology NAS]
    storage --> zfs[Rocky Linux ZFS Storage]
    storage --> pbs[Proxmox Backup Server]

    monitoring --> grafana[Grafana<br/>grafana.home.example.com]
    monitoring --> prometheus[Prometheus]
    monitoring --> loki[Loki + Promtail]
    monitoring --> exporters[Node Exporter / cAdvisor / Blackbox]

    media --> plex[Plex]
    media --> servarr[Servarr Stack]
    media --> tdarr[Tdarr]

    ai --> openwebui[Open WebUI]
    ai --> llama[llama.cpp-compatible endpoint]

    personal --> finance[FinanceHQ]
    personal --> career[CareerFill]

    proxy --> selected[Selected Public Services Only]
    pbs --> restore[Restore Tests]
```

## Reading The Diagram

- Internet access is treated as controlled and intentional.
- pfSense remains the network policy point.
- Pi-hole provides internal DNS and filtering.
- Proxmox hosts most lab workloads.
- Storage, monitoring, media, AI, and personal apps are separated by role.
- Public access is limited to selected services, not admin tools.

## Public-Safe Notes

- Example DNS names use `home.example.com`.
- Example network references use `10.10.0.0/24`.
- Exact live hostnames, public domains, public IPs, and private credentials are intentionally omitted.

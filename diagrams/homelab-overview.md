# Homelab Overview Diagram

This diagram shows the public-safe high-level architecture of the KeepItTechie homelab. It focuses on service roles and traffic flow without exposing real public domains, real public IP addresses, exact host addresses, credentials, or raw exports.

## Diagram

```mermaid
flowchart TD
    Internet[Internet] --> Access[Cloudflare Tunnel / VPN]
    Access --> Firewall[pfSense Firewall]
    Firewall --> Networks[LAN / VLANs<br/>10.10.0.0/24 example]

    Networks --> DNS[DNS Layer<br/>Pi-hole Primary + Secondary]
    Networks --> Virt[Virtualization Layer<br/>Proxmox]
    Networks --> Storage[Storage Layer]
    Networks --> Monitoring[Monitoring Layer]
    Networks --> Clients[Admin Workstations<br/>and Client Devices]

    DNS --> LocalRecords[Local DNS Records<br/>home.example.com]
    DNS --> Filtering[DNS Filtering]

    Virt --> Docker[Docker / App Hosts]
    Virt --> Media[Media Services]
    Virt --> AI[Local AI Layer]
    Virt --> Apps[Personal Apps]
    Virt --> Docs[Documentation]
    Virt --> Automation[Automation Layer]

    Docker --> Proxy[NGINX Reverse Proxy<br/>proxy.home.example.com]
    Docker --> Dashboard[Dashboard<br/>dashboard.home.example.com]

    Storage --> NAS[Synology NAS<br/>nas.home.example.com]
    Storage --> ZFS[Linux ZFS Storage]
    Storage --> PBS[Proxmox Backup Server]

    Monitoring --> Grafana[Grafana<br/>grafana.home.example.com]
    Monitoring --> Metrics[Prometheus + Exporters]
    Monitoring --> Logs[Loki + Promtail]

    Media --> Plex[Plex]
    Media --> AutomationApps[Servarr-style Apps]
    Media --> Transcode[Tdarr / Transcode Jobs]

    AI --> WebUI[Open WebUI<br/>ai.home.example.com]
    AI --> Endpoint[OpenAI-Compatible API]
    AI --> Models[Local Model Storage]

    Apps --> Finance[FinanceHQ]
    Apps --> Career[CareerFill]

    Docs --> Wiki[Wiki.js]
    Automation --> AWX[AWX / Ansible]

    Proxy --> InternalWeb[Private Internal Web Apps]
    Access --> SelectedPublic[Selected Public Apps Only]
```

## How to Read This

Start at the top and follow traffic inward. Internet access reaches the lab only through controlled paths such as a tunnel or VPN. pfSense is the network policy point, Pi-hole handles internal DNS, and Proxmox hosts most workloads.

The lower layers show service categories rather than exact machine details. This keeps the diagram useful for learning while avoiding a public map of private infrastructure.

## Public-Safe Notes

- DNS names use examples such as `home.example.com`, `proxy.home.example.com`, and `grafana.home.example.com`.
- Network examples use `10.10.0.0/24` instead of exact host addresses.
- Real public domains, public IP addresses, account IDs, credentials, certificate paths, and production exports are intentionally omitted.
- Role labels are used when exact host identity does not help viewers understand the architecture.

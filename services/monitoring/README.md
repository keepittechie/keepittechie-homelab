# Monitoring

## Purpose

The monitoring stack provides visibility into host health, container health, service availability, logs, and performance trends. It helps answer what is broken, where to look first, and whether current behavior is normal.

## Why This Matters

Monitoring should start simple. A homelab does not need enterprise complexity on day one, but it does need enough visibility to catch failed services, full disks, overloaded hosts, and broken network paths.

This stack also gives viewers practical exposure to the difference between metrics, logs, dashboards, and service checks.

## Where It Fits in the Homelab

```text
Linux hosts, containers, services, and endpoints
  |
exporters and log shippers
  |
Prometheus and Loki
  |
grafana.home.example.com
```

Monitoring is private operational visibility. It should not become a public map of the homelab.

## Host / Runtime

| Field | Value |
|---|---|
| Runtime | Docker containers and exporters on app/infra hosts |
| Example DNS | `grafana.home.example.com`, `prometheus.home.example.com`, `loki.home.example.com` |
| Public access | No |
| Dashboard layer | Grafana |
| Metrics layer | Prometheus |
| Logs layer | Loki and Promtail |

## Storage / Data Layout

Monitoring stores time-series metrics, logs, dashboard definitions, and configuration. Public docs should describe retention and backup intent without publishing live scrape targets or log content.

Example generic paths:

| Data | Example Path | Backup Need | Notes |
|---|---|---|---|
| Grafana dashboards | `/mnt/storage/appdata/grafana` | High | Export dashboards or back up app data |
| Prometheus data | `/mnt/storage/appdata/prometheus` | Medium | Retention may be more important than long-term backup |
| Loki data | `/mnt/storage/appdata/loki` | Medium | Logs can contain sensitive details |
| Exporter configs | `/mnt/storage/appdata/monitoring` | High | Keep private targets out of public examples |

## Network / DNS

Monitoring endpoints should stay private:

```text
grafana.home.example.com    -> proxy.home.example.com
prometheus.home.example.com -> proxy.home.example.com
loki.home.example.com       -> proxy.home.example.com
```

Exporters should be reachable only from the monitoring stack or trusted admin networks.

## Key Responsibilities

- Show host metrics with Node Exporter.
- Show container metrics with cAdvisor.
- Collect metrics with Prometheus.
- Visualize metrics and logs with Grafana.
- Run endpoint checks with Blackbox Exporter.
- Collect logs with Promtail and Loki.
- Track network performance with a speedtest exporter if used.
- Track Proxmox health with a Proxmox exporter if used.

## Example Public-Safe Configuration

Sanitized monitoring target examples:

| Target | Exporter / Method | What It Shows | Alert Priority | Public Notes |
|---|---|---|---|---|
| Linux hosts | Node Exporter | CPU, memory, disk, load | High | Do not publish real target lists |
| Docker hosts | cAdvisor | Container CPU, memory, restarts | Medium | Keep container names sanitized |
| Web services | Blackbox Exporter | HTTP availability and response status | High | Use `home.example.com` examples |
| Proxmox | Proxmox exporter | VM and host metrics | High | Keep API details private |
| Internet speed | Speedtest exporter | Bandwidth trend | Low | Avoid exposing provider/account details |
| Logs | Promtail to Loki | Service and system logs | Medium | Logs may contain sensitive data |

Public-safe dashboard ideas:

| Dashboard | Purpose | Example Panels | Viewer Lesson |
|---|---|---|---|
| Homelab overview | Daily health check | Up/down, CPU, memory, disk | Start with simple signals |
| Proxmox health | Hypervisor visibility | VM status, host load, storage | Virtualization needs monitoring |
| Docker apps | Container visibility | Restarts, memory, CPU | Containers fail in observable ways |
| Storage health | NAS/ZFS awareness | Free space, snapshot age, scrub status | Storage fills up quietly |
| Network checks | Service reachability | HTTP checks, DNS checks, latency | Monitoring can catch routing issues |

## Backup and Restore Notes

- Back up Grafana dashboards and data sources.
- Back up Prometheus, Loki, and exporter configuration.
- Decide which metrics and logs need retention versus rebuild.
- Keep alert destinations and credentials private.
- Document the dashboards that matter most for recovery.

## Security Notes

- Keep Grafana, Prometheus, Loki, and exporters private.
- Do not publish screenshots showing private hostnames, user data, or logs.
- Restrict access to exporter endpoints.
- Treat logs as sensitive.
- Keep dashboard credentials and API details out of Git.

## Common Mistakes to Avoid

- Trying to monitor everything before monitoring the basics.
- Publishing dashboards that reveal infrastructure details.
- Collecting logs without thinking about sensitive data.
- Alerting on too many low-priority events.
- Forgetting to back up dashboard definitions.

## What Viewers Can Learn

- How metrics, logs, dashboards, and checks differ.
- Why monitoring should start with simple health signals.
- How exporters make Linux, containers, and services observable.
- Why private monitoring is safer than public dashboards.
- How monitoring supports backup and restore confidence.

## Future Improvements

- Add a sanitized dashboard inventory.
- Add example alert priorities.
- Add a "first five checks" troubleshooting section.

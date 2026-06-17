# Monitoring

## Purpose

The monitoring stack gives visibility into host health, container health, logs, uptime, and service performance. It helps answer: "Is the lab healthy, and where should I look first when something breaks?"

## Where It Fits

```text
Hosts, containers, services
  |
exporters and log shippers
  |
Prometheus and Loki
  |
Grafana dashboards and uptime checks
```

Monitoring is for operations visibility. It should not become a public status leak for private infrastructure.

## Host / Runtime

| Field | Value |
|---|---|
| Runtime | Docker containers and exporters on app/infra hosts |
| Example DNS | `grafana.home.example.com`, `prometheus.home.example.com` |
| Public access | No |
| Dashboard | Grafana |
| Availability checks | Uptime Kuma or similar dashboard checks |

## Key Dependencies

- Prometheus
- Grafana
- Node Exporter
- cAdvisor
- Blackbox Exporter
- Speedtest exporter
- Loki
- Promtail
- Proxmox exporter
- Reverse proxy for internal URLs

## Network / DNS

Monitoring endpoints should stay private:

```text
grafana.home.example.com    -> proxy.home.example.com
prometheus.home.example.com -> proxy.home.example.com
loki.home.example.com       -> proxy.home.example.com
```

Exporters should be reachable only from the monitoring stack or trusted admin networks.

## Backup Notes

- Back up Grafana dashboards and data sources.
- Back up Prometheus and Loki configuration.
- Decide how much metrics and log history is worth retaining.
- Keep alerting credentials and webhook URLs private.

## Security Notes

- Do not publish Grafana, Prometheus, or Loki publicly by default.
- Avoid dashboards that reveal private hostnames, internal URLs, or account data in public screenshots.
- Restrict exporter access.
- Keep API credentials out of committed dashboard configs.

## What Viewers Can Learn

- Why metrics and logs solve different problems.
- How exporters make Linux and container health visible.
- How to build a dashboard that answers practical questions.
- Why monitoring should be private in a homelab.

## Future Improvements

- Add a sanitized dashboard inventory.
- Add a "first five checks" troubleshooting section.
- Add example alert rules without private endpoints.

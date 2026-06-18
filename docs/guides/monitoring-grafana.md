# Homelab Monitoring with Grafana and Prometheus

This guide explains monitoring a homelab with Grafana, Prometheus, exporters, and logs.

## Guide Goal

This guide teaches how monitoring gives visibility into the homelab: what is up, what is slow, what is failing, and what needs attention.

The practical goal is not to build the biggest dashboard possible. The goal is to start with useful signals, understand what each monitoring component does, and avoid noisy alerts or public dashboards that reveal private infrastructure.

## What Readers Will Learn

- Why monitoring matters in a homelab.
- The difference between metrics, logs, and uptime checks.
- What Grafana does.
- What Prometheus does.
- What exporters do.
- Why alerts should be useful, not noisy.
- Why dashboards should not expose private URLs or sensitive service details publicly.

## Why Monitoring Matters

Services fail. Disks fill up. Containers restart. Backups can fail. DNS can break.

Without monitoring, troubleshooting starts with guessing. With basic monitoring, readers can answer better questions:

- Is the service down or only slow?
- Is the host overloaded?
- Did a container restart?
- Is storage filling up?
- Did DNS or routing break?
- Did the last backup run fail?

Monitoring turns guessing into evidence.

## Where Grafana Fits

Grafana is the dashboard layer. It visualizes metrics and logs so the lab is easier to understand at a glance.

A good dashboard should answer a question. For example:

- Are the core services up?
- Are hosts running out of CPU, memory, or disk?
- Are containers restarting?
- Are backup-related checks healthy?
- Did errors appear in logs around the time something failed?

Grafana dashboards should stay private unless they are recreated with demo data or carefully sanitized.

## Where Prometheus Fits

Prometheus collects metrics over time. It periodically scrapes targets such as Linux hosts, Docker hosts, Proxmox exporters, and endpoint checks.

For beginners, the key idea is simple:

```text
Exporter exposes metrics
  -> Prometheus scrapes metrics
  -> Grafana visualizes metrics
```

Prometheus configuration can reveal internal hosts, service names, ports, and labels. Public examples should use sanitized targets such as `docker1.home.example.com` or `proxmox.home.example.com`.

## Exporters and Targets

Exporters make systems observable by exposing metrics that Prometheus can collect.

Common monitoring pieces:

- Node Exporter shows Linux host CPU, memory, disk, load, and filesystem signals.
- cAdvisor shows container CPU, memory, restarts, and runtime behavior.
- Proxmox exporter shows virtualization host and VM health.
- Blackbox Exporter checks whether services respond.
- Speedtest exporter can show internet performance trends when useful.

Exporters should be reachable only from the monitoring stack or trusted admin networks.

## Logs with Loki and Promtail

Metrics show numbers. Logs explain events.

Loki stores logs. Promtail ships logs from systems or containers into Loki. Grafana can then search and display those logs next to metrics.

Logs are useful, but they can be sensitive. They may contain usernames, file paths, service URLs, request details, errors, tokens, or app data. Review logs carefully before sharing snippets publicly.

## Uptime Checks and Blackbox Monitoring

Blackbox Exporter checks whether a service responds from the monitoring point of view. It can test web endpoints, DNS, ICMP, and other simple checks depending on configuration.

Uptime checks are often the easiest place to start because they answer a direct question: is the service reachable?

Checking a service does not mean publishing its real URL. Public docs should use sanitized names such as `grafana.home.example.com` and `prometheus.home.example.com`.

## Public-Safe Examples

- Open the [monitoring flow diagram](../../diagrams/monitoring-flow.md).
- Walk through the [sanitized Prometheus example config](../../examples/prometheus/prometheus.yml).
- Use example dashboard categories instead of live dashboards.
- Explain metrics vs logs vs uptime checks.
- Review what should not be published.
- Use fake or demo dashboard panels if screenshots are ever added.

Do not include a live Grafana dashboard unless it is sanitized or recreated with demo data.

## Example Monitoring Plan

This table is a teaching example. It does not represent the live target list.

| Area | Method | Example Target | What It Answers | Priority |
|---|---|---|---|---|
| Linux hosts | Node Exporter | `node1.home.example.com` | Is the host healthy? | High |
| Containers | cAdvisor | `docker1.home.example.com` | Are containers running well? | High |
| Web services | Blackbox Exporter | `https://app.home.example.com` | Is the service reachable? | High |
| Proxmox | Proxmox exporter | `proxmox.home.example.com` | Are VMs and host resources healthy? | Medium |
| Logs | Promtail to Loki | App logs | What happened before failure? | Medium |

## Example Dashboard Ideas

| Dashboard | Purpose | Example Panels | Public-Safe Notes |
|---|---|---|---|
| Homelab Overview | Quick health check | Up/down, CPU, memory, disk | Use sanitized names if shared |
| Docker Hosts | Container visibility | Restarts, CPU, memory | Avoid exposing private container names if sensitive |
| Backups | Backup visibility | Last success, failures | Do not publish private backup job names |
| Network Checks | Uptime and latency | HTTP status, ping, DNS checks | Use sanitized service names |

## Common Mistakes

- Building dashboards before knowing what questions to answer.
- Making alerts too noisy.
- Exposing Grafana publicly without strong protection.
- Publishing dashboards with private URLs.
- Ignoring logs.
- Collecting metrics but never reviewing them.
- Monitoring everything except backups.
- Not documenting what each dashboard means.

## What Is Intentionally Not Shown

- Live Grafana dashboards.
- Real Prometheus target lists.
- Alert webhook URLs.
- Notification tokens.
- Private service URLs.
- Private hostnames.
- Raw logs.
- Real dashboard screenshots.
- Exact host IPs.
- Private backup job names.

## Commands and Examples

These commands use sanitized example names. Review command output before sharing it publicly because it can include private hostnames, redirects, headers, service names, and timing details.

```bash
# Check whether a service responds
curl -I https://grafana.home.example.com

# Test DNS for a monitoring service
dig grafana.home.example.com

# Run the repo's public-safety scan before sharing docs
python3 scripts/public_safety_scan.py
```

Related examples:

- [Monitoring Flow Diagram](../../diagrams/monitoring-flow.md)
- [Prometheus Example Notes](../../examples/prometheus/README.md)
- [Sanitized Prometheus Config](../../examples/prometheus/prometheus.yml)

## Next Steps

- Read the [Monitoring](../../services/monitoring/README.md) service doc.
- Study the [monitoring flow diagram](../../diagrams/monitoring-flow.md).
- Review the [sanitized Prometheus example](../../examples/prometheus/README.md).
- Start with uptime checks.
- Add host and container metrics next.
- Add logs after the basics are useful.
- Keep dashboards private or sanitized.

## Related Docs

- [Storage and Monitoring](../storage-monitoring.md)
- [Current Setup](../current-setup.md)
- [Service Catalog](../service-catalog.md)
- [Monitoring](../../services/monitoring/README.md)
- [Monitoring Flow Diagram](../../diagrams/monitoring-flow.md)
- [Prometheus Example](../../examples/prometheus/README.md)
- [Screenshot Policy](../screenshots-policy.md)
- [Pre-Publish Review](../pre-publish-review.md)
- [Glossary](../glossary.md)

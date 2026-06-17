# Prometheus Example

This example demonstrates a sanitized Prometheus scrape configuration for common homelab exporters.

It includes placeholder scrape jobs for:

- Prometheus itself.
- Node Exporter.
- cAdvisor.
- Blackbox Exporter.
- Proxmox exporter.

## What Must Be Changed Before Use

- Replace `home.example.com` targets in private config.
- Adjust ports to match the real exporters.
- Add authentication only in private configuration when required.
- Review retention, alerting, and storage settings for the real environment.

## What Should Never Be Committed

- Live scrape target lists if they reveal private infrastructure.
- API credentials.
- Alert destination URLs.
- Raw logs or screenshots that show private hosts.

## What Viewers Can Learn

This shows how Prometheus groups scrape targets by job and how Blackbox Exporter checks service reachability. It connects to the [Monitoring service doc](../../services/monitoring/README.md) and the [monitoring flow diagram](../../diagrams/monitoring-flow.md).

This is a sanitized example, not a production-ready drop-in config.

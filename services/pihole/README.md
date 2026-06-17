# Pi-hole

## Purpose

Pi-hole provides DNS filtering and local DNS visibility.

## Design

- Primary Pi-hole
- Secondary Pi-hole
- pfSense DHCP hands out DNS servers
- Internal hostnames use the homelab domain

## Document

- Upstream DNS strategy
- Local DNS records
- Conditional forwarding if used
- Gravity/adlist update process
- Backup/export process

## Security Notes

Do not expose Pi-hole admin interfaces publicly.

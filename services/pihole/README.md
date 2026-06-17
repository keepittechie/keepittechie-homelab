# Pi-hole

## Purpose

Pi-hole provides DNS filtering, local DNS visibility, and readable internal service names. The lab uses two Pi-hole VMs so DNS continues working if one resolver is offline.

## Where It Fits

```text
Client
  |
Pi-hole primary / secondary
  |
Upstream DNS or pfSense forwarding
```

Pi-hole is also where many internal service aliases can live, such as `grafana.home.example.com` or `proxy.home.example.com`.

## Host / Runtime

| Field | Value |
|---|---|
| Primary example host | `pontus` |
| Secondary example host | `priapus` |
| Runtime | Proxmox VMs |
| Example DNS | `pihole1.home.example.com`, `pihole2.home.example.com` |
| Public access | No |

## Key Dependencies

- pfSense DHCP configuration
- Upstream DNS resolver choice
- Local DNS records
- Reverse proxy DNS aliases
- Backup/export process for Pi-hole settings

## Network / DNS

Example public-safe records:

```text
pihole1.home.example.com -> 10.10.0.6
pihole2.home.example.com -> 10.10.0.7
proxy.home.example.com   -> 10.10.0.8
grafana.home.example.com -> 10.10.0.8
```

The important pattern is that clients receive both Pi-hole servers through DHCP. Services can then be reached by name instead of memorized IP addresses.

## Backup Notes

- Export Pi-hole settings after major DNS or adlist changes.
- Keep real exports private.
- Document important local DNS records in sanitized form.
- Restore both resolvers from the same intended baseline, then adjust host-specific settings.

## Security Notes

- Do not expose Pi-hole admin pages publicly.
- Keep admin authentication enabled.
- Avoid publishing full local DNS record lists.
- Keep API credentials out of dashboard configs committed to Git.

## What Viewers Can Learn

- How local DNS makes a homelab easier to use.
- Why two DNS servers improve reliability.
- How DNS filtering and internal aliases are different jobs.
- How DHCP, DNS, and reverse proxying work together.

## Future Improvements

- Add a sanitized local DNS record example.
- Document the primary-to-secondary sync process if one is used.
- Add a short DNS troubleshooting flow.

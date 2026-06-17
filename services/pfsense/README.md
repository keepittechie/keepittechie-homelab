# pfSense

## Purpose

pfSense is the main firewall and router for the homelab. It handles routing, DHCP, firewall policy, VLAN boundaries, VPN access, and the first layer of control between the lab and the internet.

## Where It Fits

```text
Internet
  |
pfSense
  |
LAN / lab networks
  |
Pi-hole, Proxmox, storage, apps, and client devices
```

pfSense is the policy point. Pi-hole handles DNS filtering, Proxmox hosts workloads, and the reverse proxy routes selected web apps, but pfSense decides which network paths are allowed.

## Host / Runtime

| Field | Value |
|---|---|
| Runtime | Dedicated firewall appliance or firewall VM |
| Example DNS | `firewall.home.example.com` |
| Example network | `10.10.0.0/24` |
| Public access | No |
| Admin access | Trusted LAN or VPN only |

## Key Dependencies

- WAN connection
- Managed switch or LAN switching
- Pi-hole DNS VMs
- Reverse proxy for internal service routing
- VPN configuration for remote admin access, if enabled

## Network / DNS

pfSense can hand out DNS servers through DHCP, usually pointing clients at both Pi-hole VMs:

```text
Primary DNS:   pihole1.home.example.com
Secondary DNS: pihole2.home.example.com
```

Firewall rules should be written around service needs rather than broad access. For example, clients may need DNS to Pi-hole, HTTPS to the reverse proxy, and storage access to NAS services, but they do not need direct access to every admin panel.

## Backup Notes

- Keep pfSense configuration backups in a private, encrypted location.
- Export after major network changes.
- Do not commit raw pfSense backups to this repo.
- Keep a short Markdown summary of major rule groups instead of publishing the full export.

## Security Notes

- Do not expose the pfSense web UI to the public internet.
- Keep WAN rules minimal.
- Use VPN or trusted LAN access for administration.
- Review port forwards and tunnel-published services separately.
- Remove or redact secrets before sharing screenshots.

## What Viewers Can Learn

- How a firewall fits into a self-hosted network.
- Why DNS, DHCP, VLANs, and firewall rules are connected.
- How to think about default-deny rules without overcomplicating a home lab.
- Why admin interfaces should stay private.

## Future Improvements

- Add a sanitized firewall rule philosophy table.
- Add a VLAN walkthrough using example networks.
- Add a restore checklist for replacing the firewall.

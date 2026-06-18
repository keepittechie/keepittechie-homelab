# pfSense

## Purpose

pfSense is the edge firewall and router for the homelab. It is the first major control point between the internet, trusted internal devices, lab services, and any network segments such as LAN, server, guest, or IoT networks.

In this repo, pfSense is documented as a design pattern, not as a raw firewall export.

## Why This Matters

Everything in a homelab eventually depends on the network. If DNS, DHCP, routing, or firewall policy is unclear, every other service becomes harder to troubleshoot.

pfSense matters because it teaches:

- Where network policy should live.
- Why admin services should stay private.
- How LAN and VLAN boundaries reduce risk.
- How DHCP and DNS decisions affect every client.
- Why publishing raw firewall backups is unsafe.

## Where It Fits in the Homelab

```text
Internet
  |
pfSense firewall/router
  |
LAN / VLANs
  |
Pi-hole DNS, Proxmox, storage, monitoring, apps, and clients
```

pfSense decides what traffic is allowed between networks. Pi-hole handles filtering and local DNS, Proxmox hosts workloads, and the reverse proxy provides clean web service names, but pfSense is still the policy gate.

## Host / Runtime

| Field | Value |
|---|---|
| Runtime | Dedicated firewall appliance or firewall VM |
| Example DNS | `firewall.home.example.com` |
| Example network | `10.10.0.0/24` |
| Public access | No |
| Admin access | Trusted LAN or VPN only |

## Network / DNS

pfSense can provide DHCP and hand clients the Pi-hole resolvers:

```text
Primary DNS:   pihole1.home.example.com
Secondary DNS: pihole2.home.example.com
```

Common pattern:

| Role | Handled By | Notes |
|---|---|---|
| Routing | pfSense | Moves traffic between networks |
| DHCP | pfSense | Hands out addresses and DNS settings |
| DNS filtering | Pi-hole | Blocks unwanted domains and resolves local aliases |
| Firewall policy | pfSense | Allows only required traffic |
| Public exposure decision | pfSense + tunnel/proxy design | Public access is intentional, not default |

## Key Responsibilities

- Route traffic between WAN, LAN, and any VLANs.
- Hand out DHCP leases and DNS settings.
- Keep DNS pinned to the intended resolvers.
- Limit traffic between network segments.
- Keep management interfaces private.
- Support VPN access for trusted remote administration.
- Provide a clean place to reason about firewall policy.

## Example Public-Safe Configuration

Example firewall rule philosophy:

| Source | Destination | Port | Action | Reason |
|---|---|---|---|---|
| Admin LAN | pfSense admin UI | HTTPS | Allow | Trusted admin access only |
| LAN clients | Pi-hole DNS | DNS | Allow | Clients should use approved DNS |
| LAN clients | Internet | Web traffic | Allow | Normal browsing and updates |
| Guest network | LAN services | Any | Deny | Guests should not reach private systems |
| Server network | Backup server | Backup traffic | Allow | Proxmox guests need backup access |
| WAN | pfSense admin UI | Any | Deny | Admin interfaces should never be public |

These are teaching examples. They are not a full firewall ruleset.

## Backup and Restore Notes

- Export pfSense config after major network changes.
- Store real exports in a private, encrypted location.
- Keep a written summary of important rule groups.
- Document WAN, LAN, VLAN, DHCP, and DNS intent without publishing secrets.
- Practice a recovery path for replacing the firewall or restoring the config.

## Security Notes

- Do not expose the pfSense web UI publicly.
- Do not commit raw pfSense XML backups.
- Do not publish public IPs, VPN configs, or certificate material.
- Avoid screenshots that reveal real domains, rules, or account details.
- Treat firewall exports like credentials because they can include sensitive material.

## Common Mistakes to Avoid

- Letting clients use random public DNS instead of the homelab DNS path.
- Creating broad allow rules between every VLAN.
- Publishing firewall screenshots without redaction.
- Forgetting to document why a rule exists.
- Treating port forwards as harmless convenience settings.

## What Readers Can Learn

- How a firewall anchors the rest of the lab.
- Why default-deny thinking makes networks easier to reason about.
- How DHCP, DNS, and firewall policy work together.
- How to document network intent without exposing real configs.

## Future Improvements

- Add a sanitized VLAN walkthrough.
- Add a private firewall backup checklist.
- Add a public-safe troubleshooting flow for DNS, DHCP, and routing.

# Security Notes

This repo is public-facing homelab documentation. It should teach the design without exposing the live lab.

## Never Commit

- Real `.env` files
- Passwords, recovery codes, or generated credentials
- API keys, OAuth credentials, or service account files
- Tunnel credentials
- SSH private keys or VPN keys
- Private certificates or certificate authority keys
- Backup encryption keys
- Raw pfSense, switch, NAS, or app exports
- Real public IP addresses
- Financial records, job application data, or private messages

## Safer Public Alternatives

| Private Item | Public-Safe Replacement |
|---|---|
| Real domain | `home.example.com` |
| Real subnet map | `10.10.0.0/24` example topology |
| Real IP-to-host export | Small sanitized table |
| App `.env` file | `.env.example` with `REPLACE_ME` |
| Firewall export | Markdown explanation of rule philosophy |
| Certificate files | Description of TLS approach |
| Database dump | Schema notes or fake sample data |
| Screenshots with private data | Cropped or recreated sanitized screenshots |

## Exposure Model

| Service Type | Recommended Exposure |
|---|---|
| pfSense, Proxmox, PBS, NAS | LAN or VPN only |
| Pi-hole admin | LAN or VPN only |
| Grafana, Prometheus, Loki | LAN or VPN only |
| AWX / Ansible | LAN or VPN only |
| FinanceHQ and CareerFill | Private only |
| Wiki.js public pages | Public only for intended namespaces |
| Nextcloud | Limited and hardened if exposed |
| Plex | Limited and authenticated if exposed |

## Documentation Review Checklist

Before committing:

1. Check `git status` and review every changed file.
2. Search for secret-looking strings.
3. Replace real hostnames with `home.example.com` examples.
4. Replace real public IPs with documentation ranges or sanitized internal examples.
5. Remove raw exports and generated backups.
6. Confirm `.env.example` contains placeholders only.

## Recommended Scan

Before committing, run `git status` and a sensitive-string scan for private key headers, credential assignments, tunnel credentials, and generated secrets. Keep the exact scan command out of committed docs so the docs do not match their own warning pattern.

A match is not always a leak, but it deserves review before publishing.

## What Viewers Should Take Away

Security in a homelab is mostly about good boundaries:

- Keep admin tools private.
- Publish fewer services.
- Use DNS and reverse proxying deliberately.
- Keep secrets in a password manager or private runtime files.
- Document enough to rebuild, not enough for someone else to access the lab.

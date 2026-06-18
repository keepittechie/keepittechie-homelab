# AWX / Ansible Automation

## Purpose

AWX provides a web interface for Ansible automation. It helps run playbooks, manage inventories, schedule jobs, store job history, and organize repeatable administration tasks.

## Why This Matters

Automation is where a homelab starts becoming repeatable. AWX can teach readers how to turn manual tasks into controlled workflows, but it also handles sensitive material such as inventories, credentials, and job output.

The public repo should teach the pattern without publishing real automation secrets or host inventories.

## Where It Fits in the Homelab

```text
Admin user
  |
awx.home.example.com
  |
AWX
  |
Ansible inventories, credentials, and playbooks
  |
Homelab services and hosts
```

AWX is an admin tool and should stay private.

## Host / Runtime

| Field | Value |
|---|---|
| Runtime | App VM or containerized AWX deployment |
| Example DNS | `awx.home.example.com` |
| Public access | No |
| Primary data | Inventories, projects, job templates, job history |
| Admin access | Trusted LAN or VPN only |

## Storage / Data Layout

Example layout:

| Data | Example Path | Backup Need | Notes |
|---|---|---|---|
| AWX config/state | `/mnt/storage/appdata/awx` | High | Contains automation state |
| Project checkout | `/opt/apps/example/awx-projects` | Medium | Public-safe playbooks can live in Git |
| Private inventory | `/mnt/storage/appdata/awx/private-inventory` | Critical | Never publish real inventory |
| Backups | `/mnt/storage/backups/awx` | High | Keep private |

## Network / DNS

Example:

```text
awx.home.example.com -> proxy.home.example.com
```

AWX should be reachable only from trusted admin networks.

## Key Responsibilities

- Run Ansible playbooks from a web interface.
- Organize inventories and host groups.
- Store credentials privately.
- Define job templates and schedules.
- Track job output and history.
- Provide guardrails for repeatable maintenance.

## Example Public-Safe Configuration

Sanitized automation table:

| Automation Area | Example | Risk If Public | Safe Documentation Approach |
|---|---|---|---|
| Inventory | `dns`, `storage`, `monitoring` groups | Reveals hostnames and access paths | Use sanitized group names |
| Credentials | SSH or API access | Direct system access | Describe credential purpose only |
| Playbooks | Update check, backup check, report job | Could run destructive tasks | Share read-only examples first |
| Job templates | Weekly health report | Reveals job history and targets | Use fake targets |
| Variables | Service config values | May include private paths or secrets | Use placeholders |

## Backup and Restore Notes

- Back up AWX database and configuration privately.
- Keep credentials and private inventory out of public Git.
- Keep public-safe playbooks separate from private operational playbooks.
- Test restore of job templates and project links.
- Document what can be recreated versus what must be backed up.

## Security Notes

- Do not publish AWX publicly.
- Do not commit real inventories, machine credentials, or vault material.
- Use read-only playbooks for public demos.
- Keep destructive jobs guarded.
- Review job output before sharing screenshots.

## Common Mistakes to Avoid

- Publishing real inventories by accident.
- Storing credentials in playbooks.
- Running broad automation without dry-run or guardrails.
- Treating job output as safe to share.
- Giving AWX more network reach than it needs.

## What Readers Can Learn

- How automation fits into a homelab.
- Why inventories and credentials need boundaries.
- How to turn maintenance into repeatable jobs.
- Why safe automation starts with read-only checks.
- How to document automation without exposing access.

## Future Improvements

- Add sanitized inventory group examples.
- Add a read-only homelab report playbook idea.
- Add guardrails for update and reboot jobs.

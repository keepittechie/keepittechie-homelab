# AWX / Ansible Automation

## Purpose

AWX provides a web interface for Ansible automation. It helps turn repeatable server administration tasks into controlled jobs with inventories, credentials, schedules, and logs.

## Where It Fits

```text
Admin user
  |
AWX
  |
Ansible inventories and playbooks
  |
Linux hosts, VMs, and services
```

AWX is useful for running safe checks, updates, reporting, and repeatable maintenance. It should be treated like an admin tool.

## Host / Runtime

| Field | Value |
|---|---|
| Example host | `zelus` or automation VM |
| Runtime | AWX on Linux / containers |
| Example DNS | `awx.home.example.com` |
| Public access | No |
| Control target | Homelab hosts and services |

## Key Dependencies

- Ansible project repo
- Inventory files
- SSH access to managed hosts
- AWX credentials stored privately
- pfSense and DNS paths to target hosts

## Network / DNS

AWX should be reachable only from trusted admin networks:

```text
awx.home.example.com -> proxy.home.example.com
```

Managed hosts should be grouped by role, such as DNS, storage, media, monitoring, and app servers.

## Backup Notes

- Back up AWX project configuration and database state.
- Keep credentials and vault material private.
- Keep playbooks in Git where safe.
- Keep private inventory in ignored paths.

## Security Notes

- Do not publish AWX publicly.
- Never commit real Ansible Vault passwords, SSH keys, or machine credentials.
- Use read-only jobs for demos when possible.
- Keep destructive jobs guarded and documented.

## What Viewers Can Learn

- How automation fits into a homelab.
- Why inventories and credentials need clear boundaries.
- How to turn manual maintenance into repeatable jobs.
- Why "automation" should include safety checks, not just speed.

## Future Improvements

- Add sanitized inventory group examples.
- Add a read-only homelab report playbook example.
- Add guardrail notes for update and reboot jobs.

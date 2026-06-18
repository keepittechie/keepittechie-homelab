# FinanceHQ

## Purpose

FinanceHQ is a local-first personal finance app. In this repo, it is documented as a private app architecture pattern, not as a place to publish real financial data.

## Why This Matters

Personal finance data is highly sensitive. FinanceHQ is useful for teaching local-first app deployment, private dashboards, app backups, and data boundaries, but the real records, imports, reports, and screenshots must stay private.

## Where It Fits in the Homelab

```text
Admin browser
  |
finance.home.example.com
  |
Reverse proxy
  |
FinanceHQ app and database
```

FinanceHQ belongs in the private app tier.

## Host / Runtime

| Field | Value |
|---|---|
| Runtime | App VM or container |
| Example DNS | `finance.home.example.com` |
| Public access | No |
| Data type | Personal financial workflows |
| Demo data | Fake data only |

## Storage / Data Layout

Example layout:

| Data | Example Path | Backup Need | Notes |
|---|---|---|---|
| App config | `/opt/apps/example/financehq` | High | Keep private values out of Git |
| Database | `/mnt/storage/appdata/financehq/db` | Critical | Contains sensitive records |
| Upload/import area | `/mnt/storage/appdata/financehq/imports` | Critical | Never publish real files |
| Backups | `/mnt/storage/backups/financehq` | Critical | Private backup location only |

## Network / DNS

Example:

```text
finance.home.example.com -> proxy.home.example.com
```

The app should stay private. Public content should use fake screenshots and fake records.

## Key Responsibilities

- Provide a local-first finance workflow.
- Keep financial data under private control.
- Support private reporting and review.
- Demonstrate personal app hosting patterns.
- Require serious backup and restore planning.
- Keep public docs focused on architecture, not data.

## Example Public-Safe Configuration

Public-safe boundary table:

| Can Document Publicly | Keep Private | Notes |
|---|---|---|
| App architecture | Real transactions | Use fake records only |
| Deployment pattern | Account names and institutions | Avoid screenshots with private labels |
| Backup categories | Database dumps | Mention process, not contents |
| Demo workflows | CSV filenames and imports | Use generated sample data |
| Lessons learned | Reports and balances | Do not publish financial summaries |

## Backup and Restore Notes

- Back up the database privately.
- Back up configuration without credentials.
- Test restores with fake or redacted data.
- Keep import files, reports, and exports out of public Git.
- Document restore steps without exposing records.

## Security Notes

- Keep the app LAN/VPN-only.
- Do not publish real financial data.
- Treat logs and imports as sensitive.
- Do not commit private database paths or dumps.
- Use fake demo data in public docs.

## Common Mistakes to Avoid

- Sharing screenshots with real balances or transaction names.
- Treating import filenames as harmless.
- Backing up the app without the database.
- Publishing logs that contain imported descriptions.
- Putting personal app routes behind public access for convenience.

## What Readers Can Learn

- How to host a private personal app.
- Why local-first apps need clear data boundaries.
- How to document architecture without exposing the data.
- Why backup priority is high for personal databases.

## Future Improvements

- Add fake sample workflows.
- Add a private app restore checklist.
- Add a sanitized architecture diagram.

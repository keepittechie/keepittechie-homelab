# FinanceHQ

## Purpose

FinanceHQ is a local-first financial command center. It is documented here as a personal app pattern, not as a place to publish real financial data.

## Where It Fits

```text
Admin browser
  |
finance.home.example.com
  |
Reverse proxy
  |
FinanceHQ app and database
```

FinanceHQ belongs in the private app tier. It can be useful for teaching local-first app deployment, but its data is too sensitive for public examples.

## Host / Runtime

| Field | Value |
|---|---|
| Runtime | App VM or container |
| Example DNS | `finance.home.example.com` |
| Public access | No |
| Data type | Personal financial workflows |
| Repo boundary | Architecture only, sanitized examples only |

## Key Dependencies

- App runtime
- Database
- Reverse proxy for private access
- Backup process
- Sanitized sample data for public docs

## Network / DNS

FinanceHQ should stay private:

```text
finance.home.example.com -> proxy.home.example.com
```

Do not publish public routes, real account data, or screenshots with financial details.

## Backup Notes

- Back up the database privately.
- Back up app configuration without secrets.
- Test restores with fake or redacted data.
- Keep exports and reports out of this public repo.

## Security Notes

- Keep the app LAN/VPN-only.
- Do not commit real transactions, account names, CSV filenames, or statements.
- Use fake sample data for screenshots and docs.
- Treat logs as sensitive if they include imported descriptions.

## What Viewers Can Learn

- How to host a personal app privately.
- Why local-first tools need strong data boundaries.
- How to document app architecture without leaking the data it manages.
- How backups differ for apps with sensitive databases.

## Future Improvements

- Add a sanitized deployment diagram.
- Add fake sample data examples.
- Add a private-app security checklist.

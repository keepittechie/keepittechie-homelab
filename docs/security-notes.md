# Security Notes

## Do Not Commit

- `.env`
- API keys
- Tunnel credentials
- SSH private keys
- VPN private keys
- Password exports
- Private certificates
- Full firewall backups with secrets
- Real public IP addresses

## Safer Alternatives

| Sensitive Item | Public Repo Alternative |
|---|---|
| `.env` | `.env.example` |
| Real IP map | Sanitized topology |
| API key | `REPLACE_ME` placeholder |
| Firewall export | Markdown explanation |
| Private certificate | Description of certificate flow |

## Access Model

- Private admin apps should stay LAN/VPN only.
- Public services should sit behind a reverse proxy or tunnel.
- Use strong auth on anything exposed.
- Prefer service accounts and scoped API keys.
- Rotate credentials after accidental exposure.

## Repo Hygiene

Before every commit:

```bash
git status
grep -R "token\|password\|secret\|api_key\|PRIVATE KEY" -n . --exclude-dir=.git
```

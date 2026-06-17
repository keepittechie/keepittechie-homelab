# CareerFill

## Purpose

CareerFill is a local-first job application and career workflow tool. It supports job search organization, interview preparation, and application tracking without treating private career data as public repo content.

## Where It Fits

```text
Admin browser
  |
career.home.example.com
  |
Reverse proxy
  |
CareerFill app and database
```

CareerFill is a good example of using homelab infrastructure to solve a personal workflow problem.

## Host / Runtime

| Field | Value |
|---|---|
| Runtime | App VM or container |
| Example DNS | `career.home.example.com` |
| Public access | No |
| Data type | Job applications, interview notes, recruiter messages |
| Repo boundary | Sanitized architecture and fake examples only |

## Key Dependencies

- App runtime
- Database
- Reverse proxy route
- Backup process
- Optional local AI support for drafting or prep workflows

## Network / DNS

CareerFill should stay private:

```text
career.home.example.com -> proxy.home.example.com
```

If screenshots are used in content, they should use fake companies, fake job posts, and fake notes.

## Backup Notes

- Back up the database privately.
- Back up app configuration without credentials.
- Keep generated resumes, recruiter messages, and interview notes out of public Git.
- Restore with fake data when demonstrating the process publicly.

## Security Notes

- Do not publish real job applications or recruiter messages.
- Keep personal identifiers out of examples unless intentionally public.
- Treat AI prompts and outputs as private if they include career details.
- Keep the app LAN/VPN-only.

## What Viewers Can Learn

- How a homelab can support real personal workflows.
- How to deploy private productivity apps.
- How to separate app architecture from private user data.
- How local AI can help without exposing sensitive context.

## Future Improvements

- Add fake sample workflows.
- Add a private app restore checklist.
- Add a short section on local AI integration boundaries.

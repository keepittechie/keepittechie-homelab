# CareerFill

## Purpose

CareerFill is a local-first career and job application workflow app. It supports job search organization, interview preparation, and application tracking without publishing private career data.

## Why This Matters

Career data can include resumes, job applications, recruiter messages, interview notes, personal contact details, and salary context. CareerFill is useful for teaching private app hosting and local-first workflows, but public docs must stay architecture-focused.

## Where It Fits in the Homelab

```text
Admin browser
  |
career.home.example.com
  |
Reverse proxy
  |
CareerFill app and database
```

CareerFill is a private personal workflow app. It can also connect to local AI workflows, but prompts and outputs should be treated as private when they contain career details.

## Host / Runtime

| Field | Value |
|---|---|
| Runtime | App VM or container |
| Example DNS | `career.home.example.com` |
| Public access | No |
| Data type | Job applications, interview prep, notes |
| Demo data | Fake companies and fake applications only |

## Storage / Data Layout

Example layout:

| Data | Example Path | Backup Need | Notes |
|---|---|---|---|
| App config | `/opt/apps/example/careerfill` | High | Keep private values out of Git |
| Database | `/mnt/storage/appdata/careerfill/db` | High | Contains private workflow data |
| Generated files | `/mnt/storage/appdata/careerfill/generated` | Medium | May include resumes or letters |
| Backups | `/mnt/storage/backups/careerfill` | High | Private backup location only |

## Network / DNS

Example:

```text
career.home.example.com -> proxy.home.example.com
```

The app should stay private. Public demos should use fake job posts, fake companies, and fake notes.

## Key Responsibilities

- Organize career workflows.
- Keep job application data private.
- Support interview prep and live-call notes.
- Demonstrate local-first app deployment.
- Optionally connect to local AI without exposing private prompts.
- Keep architecture docs separate from user data.

## Example Public-Safe Configuration

Public-safe boundary table:

| Can Document Publicly | Keep Private | Notes |
|---|---|---|
| App architecture | Real resumes | Use fake resume snippets only |
| Workflow categories | Recruiter messages | Do not publish emails or names |
| Backup strategy | Job application records | Use fake applications |
| Local AI pattern | Prompt history with real context | Use generic prompt examples |
| Lessons learned | Interview notes | Keep sensitive notes out of Git |

## Backup and Restore Notes

- Back up the database privately.
- Back up app configuration without credentials.
- Keep generated resumes, recruiter messages, and interview notes out of public Git.
- Test restores with fake data.
- Document whether generated files are included in backups.

## Security Notes

- Keep the app LAN/VPN-only.
- Do not publish real job applications or recruiter messages.
- Treat AI prompts and outputs as sensitive when they include career details.
- Do not publish real resume details.
- Avoid screenshots with personal identifiers.

## Common Mistakes to Avoid

- Using real companies or messages in demos.
- Publishing generated resume or cover letter drafts.
- Backing up database state without generated files if they matter.
- Sending private career context to public tools accidentally.
- Treating local apps as safe to expose because they are personal.

## What Viewers Can Learn

- How a homelab can support real personal workflows.
- How to deploy private productivity apps.
- How local AI can help while keeping context private.
- How to document a personal app without exposing its contents.

## Future Improvements

- Add fake sample workflows.
- Add a restore checklist.
- Add local AI integration boundaries.

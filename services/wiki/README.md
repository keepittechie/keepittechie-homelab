# Wiki.js

## Purpose

Wiki.js is the lab knowledge base. It is used for documentation, runbooks, notes, and content planning while keeping public pages separate from private admin material.

## Where It Fits

```text
Browser
  |
wiki.home.example.com
  |
Reverse proxy
  |
Wiki.js app and database
```

This public GitHub repo is the viewer-friendly version of the lab. Wiki.js can hold deeper private operational notes that should not be copied here.

## Host / Runtime

| Field | Value |
|---|---|
| Runtime | Docker app or VM-hosted service |
| Example host | `heimdall` or app VM |
| Example DNS | `wiki.home.example.com` |
| Public access | Partial, depending on namespace |
| Database | Private app database |

## Key Dependencies

- Reverse proxy
- App database
- Authentication provider or local accounts
- Backup process for content and uploads
- Clear public/private namespace rules

## Network / DNS

Example:

```text
wiki.home.example.com -> proxy.home.example.com
```

Private admin pages should require authentication. Public pages should be reviewed before publishing.

## Backup Notes

- Back up the Wiki.js database.
- Back up uploaded assets.
- Keep private admin exports out of this public repo.
- Document page ownership and public/private boundaries.

## Security Notes

- Do not allow anonymous access to private namespaces.
- Review screenshots and copied notes for secrets.
- Keep auth credentials private.
- Avoid copying raw operational notes directly into public docs.

## What Viewers Can Learn

- Why a homelab needs documentation.
- How public docs and private runbooks can coexist.
- How to turn messy notes into teachable material.
- Why documentation is part of operations, not an afterthought.

## Future Improvements

- Add a sanitized content tree.
- Add a public/private page review checklist.
- Add backup and restore steps for Wiki.js.

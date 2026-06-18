# Environment File Example

This example shows how to publish safe placeholders for an app environment file.

`app.env.example` is safe because it uses placeholder values. A real `.env` file is not safe because it often contains database credentials, app secrets, API keys, tokens, and private service URLs.

## What Must Be Changed Before Use

- Copy the pattern into a private `.env` file.
- Replace `CHANGE_ME` values privately.
- Replace `app.home.example.com` only in private runtime config.
- Confirm the real `.env` file is ignored by Git.

## What Should Never Be Committed

- Real `.env` files.
- Database passwords.
- App signing secrets.
- API keys or service tokens.
- Private URLs that reveal internal infrastructure.

## What Readers Can Learn

Readers can learn why `.env.example` belongs in a public repo and `.env` belongs outside Git. This connects to the [pre-publish review checklist](../../docs/pre-publish-review.md) and the [Docker Compose examples](../docker-compose/README.md).

This is a sanitized example, not a production-ready drop-in config.

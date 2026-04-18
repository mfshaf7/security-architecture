# Operator Orchestration Service Idea List And Command-Family Review

- date: 2026-04-18
- scope: broker-owned idea list projection and broker-owned `/idea` command-family descriptor
- owner repo: `operator-orchestration-service`
- related repos:
  - `openclaw-telegram-enhanced`
  - `platform-engineering`
- security owner: `security-architecture`
- status: approved-bounded-expansion

## Summary

This expansion is approved as a bounded internal runtime change.

The key requirement is that the broker remains the owner of workflow semantics
and record visibility, while Telegram stays a rendering adapter:

- `/idea help` must consume a broker-owned command-family descriptor
- `/idea list` must render a bounded normalized projection
- `/idea show <idea-id>` must render a single broker-owned record projection

Approved scope:

- `GET /v1/workflows/idea-command`
- `GET /v1/ideas`
- Telegram `/idea list`
- Telegram `/idea show <idea-id>`

Still not approved:

- raw OpenProject collection passthrough
- arbitrary backlog browsing or search
- public ingress
- governed AI triage activation

## Review Areas

### Identity

- caller authentication stays on the existing broker runtime boundary
- no new human or machine identity is introduced by the list surface
- Telegram remains a caller, not a credential owner

### Secrets

- no new secret class is introduced
- OpenProject token custody remains broker-owned
- the Telegram adapter still must not hold OpenProject credentials

### Delivery

- this remains a Git-managed internal runtime expansion
- stage proof must include the list and show surfaces before the operator model
  is treated as complete

### Runtime

- listing is acceptable only as a bounded broker projection with pagination
- status-bearing summaries are encouraged because they improve operator clarity
  without widening authority
- the service must not become a generic OpenProject browsing API

### AI

- the command-family descriptor may mention deferred triage, but this change
  does not activate AI-assisted decisions

## Required Controls

1. `/idea help` uses the broker-owned command-family descriptor, not
   Telegram-local help
2. `/idea list` returns bounded normalized items with canonical status
3. `/idea show <idea-id>` returns a single broker-owned normalized projection
4. Telegram replies surface current status explicitly instead of only a record
   reference
5. stage verification proves `/idea help`, `/idea list`, `/idea show <idea-id>`,
   and `/idea <text>` together

## Decision

Approved as a bounded internal API and operator-surface expansion.

The security posture remains acceptable because the change improves operator
visibility while keeping backend semantics, secret custody, and workflow truth
inside the broker boundary.

# Operator Orchestration Service Workflow Catalog And Read Projection Review

- date: 2026-04-18
- scope: broker-owned workflow descriptors, normalized record reads, and source lookup for the bounded idea-capture workflow
- owner repo: `operator-orchestration-service`
- related repos:
  - `openclaw-telegram-enhanced`
  - `platform-engineering`
- security owner: `security-architecture`
- status: approved-bounded-expansion

## Summary

This expansion is approved as a bounded internal runtime change.

The important correction is architectural, not cosmetic:

- canonical `/idea` guidance now moves out of `openclaw-telegram-enhanced`
- `operator-orchestration-service` becomes the owner of workflow descriptors and
  normalized record reads for broker-owned workflows
- Telegram stays a rendering adapter instead of becoming the source of workflow
  truth

Approved scope:

- `GET /v1/workflows`
- `GET /v1/workflows/idea-capture`
- `GET /v1/ideas/{idea_id}`
- `POST /v1/ideas/lookup`

Still not approved:

- generic OpenProject browsing or passthrough APIs
- public ingress
- AI-assisted triage as a governed AI flow

## Review Areas

### Identity

- caller authentication remains explicit and separate from operator identity
- the new read/catalog endpoints stay on the same internal caller boundary and
  do not introduce a new identity model

### Secrets

- no new secret class is introduced by this expansion
- OpenProject credential custody remains broker-owned
- Telegram still must not hold backend credentials

### Delivery

- this is still a Git-managed internal runtime change, not a live bypass
- the corrected `/idea help` ownership requires coordinated owner-repo and
  stage-rollout evidence before it can be treated as operational truth

### Runtime

- the widened surface is acceptable because it remains bounded to broker-owned
  workflows and broker-owned record projections
- the service must not become a generic OpenProject proxy
- lookup must stay keyed to broker-owned source identity, not arbitrary
  OpenProject search

### AI

- the new workflow descriptor endpoint may describe deferred AI phases, but it
  does not itself activate AI triage
- no governed AI classification changes in this expansion

## Required Controls

1. source adapters consume broker-owned workflow descriptors instead of
   fabricating workflow semantics locally
2. read responses remain normalized broker projections, not raw OpenProject API
   payloads
3. no local fallback that reintroduces Telegram-owned workflow truth
4. stage verification proves `/idea help` and `/idea <text>` against the new
   broker-owned contract

## Decision

Approved as a bounded internal API expansion for `operator-orchestration-service`.

The security posture remains acceptable because the change strengthens the
workflow ownership boundary instead of widening authority into a generic backend
proxy.

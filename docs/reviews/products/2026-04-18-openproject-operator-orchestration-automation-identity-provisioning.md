# OpenProject Operator-Orchestration Automation Identity Provisioning

- date: 2026-04-18
- scope: machine identity and broker credential for OpenProject-backed idea workflows
- owner repo: `platform-engineering`
- related repos:
  - `operator-orchestration-service`
- status: change-reviewed

## Summary

Provisioning a dedicated OpenProject automation user for
`operator-orchestration-service` is the correct control.

The implemented model is acceptable provided the credential remains component-
owned, the account stays non-admin, and the project role set is limited to the
minimum needed for `workspace-proposals`.

Live follow-up on 2026-04-18 found that the earlier `Reader` plus
`Work package editor` set was under-permissioned for API-backed capture. The
approved minimum role set is corrected below.

## Review Areas

### Identity

- the automation user must be distinct from all human operator accounts
- the account must remain non-admin
- project access should be limited to:
  - `Reader`
  - `Work package creator`
  - `Work package editor`
- scope should remain the dedicated `workspace-proposals` project

### Secrets

- the API token must be single-purpose
- the token should be stored under the broker component scope:
  - `kv/components/operator-orchestration-service/prod/openproject`
- the token should not be stored under `kv/products/openproject/prod/*`
  because the OpenProject runtime does not consume it
- the plaintext token should be handled only at creation or deliberate rotation

### Runtime

- OpenProject remains the canonical backlog store
- the broker credential is not an OpenProject runtime secret
- no OpenProject namespace runtime should receive this token unless a separate
  runtime integration explicitly requires it and is reviewed

### AI

- this credential does not change the AI-governance posture by itself
- it only enables the future broker write path into OpenProject
- operator approval remains required for durable backlog outcomes

## Required Controls

1. dedicated automation user `operator-orchestration-service`
2. non-admin status preserved
3. project-scoped membership on `workspace-proposals`
4. minimum role set:
   - `Reader`
   - `Work package creator`
   - `Work package editor`
5. named single-purpose API token
6. Vault path under the broker component scope
7. rotation path documented before runtime admission

## Decision

Approved for the phase-1 OpenProject backlog integration.

This does not yet approve:

- broker runtime admission
- Kubernetes secret delivery to the broker
- broader service-to-service identity design for the broker runtime

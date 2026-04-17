# Operator Orchestration Service Proposed Component Review

- date: 2026-04-18
- scope: proposed shared operator-facing workflow service
- owner repo: `operator-orchestration-service`
- security owner: `security-architecture`
- status: proposed-component-reviewed

## Summary

`operator-orchestration-service` is an appropriate new shared component for
bounded operator workflow brokering. It should exist as a separate service layer
instead of embedding workflow orchestration directly into
`openclaw-telegram-enhanced/`.

This review covers the proposed component role only. It does not admit the
component into active workspace inventory or approve a live deployment.

## Why The Separate Component Is Correct

- Telegram channel code changes faster than workflow and backend contracts
- the service must mediate between operator surfaces, AI-assist paths, and
  canonical backend systems such as OpenProject
- the trust boundary is broader than a Telegram plugin but narrower than a
  platform release-authority repo

## Review Areas

### Identity

- future runtime identity must be separate from Telegram plugin identity
- the service must authenticate callers such as Telegram adapters explicitly
- operator identity and service identity must remain distinct in audit events

### Secrets

- OpenProject and model-provider credentials must not live in
  `openclaw-telegram-enhanced/`
- credential custody should move to Vault when the service becomes live
- rotation and ownership must be defined before admission to active deployment

### Delivery

- no governed deployment path exists yet for this component
- admission into active inventory should wait until runtime ownership and
  platform rollout shape are explicit

### Runtime

- the service should expose bounded workflow endpoints, not a general chat or
  action surface
- canonical systems such as OpenProject remain the system of record
- the service must not directly mutate workspace contracts

### AI

- model output must remain structured and reviewable
- operator approval remains mandatory for durable workflow outcomes
- local-model assistance may exist before a governed AI path is active, but it
  must not be mislabeled as governed

## Conditions Before Admission

Before this component moves from proposed to admitted, require at least:

1. a concrete component architecture view in `security-architecture`
2. repo-local operator and architecture guidance in the owner repo
3. explicit service auth and audit model
4. backend credential custody and rotation story
5. health, version, and operator visibility contract
6. documented runtime owner and deployment shape

## Decision

Approved as a proposed shared component direction.

Not yet approved for:

- active runtime admission
- governed AI status
- autonomous workflow effects without operator approval

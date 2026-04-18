# Operator Orchestration Service Runtime Admission Review

- date: 2026-04-18
- scope: runtime admission for the first shared broker deployment and stage `/idea` capture path
- owner repo: `operator-orchestration-service`
- platform runtime owner: `platform-engineering`
- security owner: `security-architecture`
- status: approved-runtime-admission

## Summary

Runtime admission is approved for `operator-orchestration-service` as an active
shared component with a bounded phase-1 workflow:

- shared internal runtime only
- internal ClusterIP service only
- explicit caller authentication
- OpenProject write path only
- no governed AI triage path yet

This review supersedes the earlier proposed-component-only review for purposes
of active repo and component admission.

## Admitted Scope

Approved:

- shared runtime deployment through `platform-engineering`
- Vault plus External Secrets delivery of broker-owned OpenProject credentials
- broker-owned caller secret used by the stage OpenClaw gateway for `/idea`
  capture
- bounded `POST /v1/ideas/capture` workflow into the `workspace-proposals`
  OpenProject project
- operator-visible health, readiness, and version endpoints

Not approved in this admission:

- AI-assisted triage as a governed AI flow
- direct product or component admission mutation
- product-facing public ingress
- prod OpenClaw caller wiring

## Review Areas

### Identity

- the service has its own machine identity and Kubernetes runtime
- caller authentication is explicit and separate from operator identity
- phase 1 caller allowlist should remain narrow and should start with the stage
  OpenClaw gateway only

### Secrets

- OpenProject token custody is correctly separated from Telegram runtime config
- broker runtime secret paths must stay component-owned
- the shared caller secret is acceptable for phase 1 if it is Vault-delivered,
  auditable, and not reused outside the broker workflow

### Delivery

- runtime admission must use Git-managed platform manifests and Argo
  reconciliation
- image pinning and change-record evidence are required before calling the
  runtime admitted and live
- shared runtime deployment is the correct owner layer; this should not be
  embedded into `openclaw-telegram-enhanced`

### Runtime

- the bounded endpoint surface is appropriate
- `/healthz`, `/readyz`, and `/version` are required and sufficient for phase 1
  operator visibility when combined with one real capture test
- OpenProject remains the canonical record and the broker does not directly
  mutate workspace contracts

### AI

- phase 1 capture admission is not a governed AI admission
- any later `triage` path must remain labeled `local` or `integrated` until the
  governed AI access path is actually active and reviewed

## Required Controls

Admission depends on these controls being present in the merged owner and
platform changes:

1. broker repo governance lane and security-tagged change-record evidence
2. active workspace repo and component inventory entries
3. component-owned OpenProject API token path in Vault
4. component-owned caller secret path in Vault
5. internal-only service exposure
6. explicit allowed caller ids and caller secret enforcement
7. real capture-path audit events and stage verification evidence

## Decision

Approved for active workspace admission and stage-first shared runtime
deployment, subject to the controls above.

Future expansion to AI-assisted triage, additional callers, or wider
environment reach requires a fresh change review.

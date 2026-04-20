# Operator Orchestration Service

## Role

`operator-orchestration-service` is the shared operator workflow broker for
bounded operator-initiated workflows that originate from fast interaction
surfaces such as Telegram and terminate in canonical backend systems such as
OpenProject.

It is not a channel plugin, not a model-policy authority, and not a platform
release authority.

## Trust Boundary

This component sits at a multi-system trust boundary:

- operator-facing chat surfaces call it
- the service authenticates machine callers separately from human operators
- the service holds backend credentials that must not live in Telegram adapters
- the service emits audit records for workflow requests and durable backend
  writes

Current bounded idea workflow family:

- capture a new idea
- read one broker-owned idea projection
- list recent idea records through a bounded projection
- record operator-authored triage
- record bounded operator decision outcomes
- record internal evaluation metadata without exposing a Telegram command
- consume an already accepted proposal into the separate OpenProject delivery
  ART project through an internal-only broker route

Local fast-iteration work is allowed through the `dev-integration`
`idea-workflow` and `accepted-idea-delivery` profiles, but those lanes stay
local-only and do not count as governed stage evidence.

AI triage remains deferred.

## Current Admitted Runtime Shape

- owner repo: `operator-orchestration-service`
- platform runtime owner: `platform-engineering`
- expected namespace: `operator-orchestration-service`
- expected Argo application: `operator-orchestration-service`
- expected service exposure: internal ClusterIP only
- expected primary caller in phase 1: stage OpenClaw Telegram adapter
- canonical backend targets:
  - OpenProject project `workspace-proposals`
  - internal accepted-idea handoff into OpenProject project
    `workspace-delivery-art`

## Security Model

### Identity

- caller authentication uses an explicit shared caller secret plus allowlisted
  caller ids
- operator identity remains part of the request payload and audit event
- service identity and operator identity must not be collapsed

### Secrets

- the OpenProject API token belongs to the broker component, not to
  `openclaw-telegram-enhanced`
- the caller-auth secret is broker-owned runtime secret material
- secret delivery should use Vault plus External Secrets, not repo-local env
  files or product-owned static credentials

### Delivery

- runtime deployment is platform-owned and reconciled through Argo
- the service should be image-pinned and Git-managed like other admitted shared
  runtimes
- Telegram channel code must remain a thin adapter, not the deployment or
  secret-delivery owner
- accepted-idea consumption must remain an internal broker action until a
  separate operator surface is explicitly reviewed and admitted

### Runtime

- only bounded workflow endpoints are allowed
- `/healthz`, `/readyz`, and `/version` are required operator-visible
  attestation surfaces
- workflow descriptors and read projections are allowed only for broker-owned
  workflows and records
- canonical record mutation remains behind explicit operator action at the
  workflow layer

### AI

- phase 1 capture admission does not approve any governed AI invocation path
- future AI-assisted triage must continue to follow
  [../../standards/ai-security-and-governance.md](../../standards/ai-security-and-governance.md)
  and the governed model-profile controls before it is called `governed`

## Key Risks

- secret sprawl if backend credentials leak back into Telegram adapters
- caller spoofing if shared caller identity is not enforced and audited
- governance drift if the service starts mutating workspace contracts directly
- trust-boundary widening if AI triage is enabled without the governed AI path

## Required Companion Artifacts

- runtime-admission review:
  [../../reviews/components/2026-04-18-operator-orchestration-service-runtime-admission.md](../../reviews/components/2026-04-18-operator-orchestration-service-runtime-admission.md)
- workflow-catalog and read-projection review:
  [../../reviews/components/2026-04-18-operator-orchestration-service-workflow-catalog-and-read-projection.md](../../reviews/components/2026-04-18-operator-orchestration-service-workflow-catalog-and-read-projection.md)
- idea-list and command-family review:
  [../../reviews/components/2026-04-18-operator-orchestration-service-idea-list-and-command-family.md](../../reviews/components/2026-04-18-operator-orchestration-service-idea-list-and-command-family.md)
- dev-integration idea-workflow review:
  [../../reviews/components/2026-04-18-operator-orchestration-service-dev-integration-idea-workflow.md](../../reviews/components/2026-04-18-operator-orchestration-service-dev-integration-idea-workflow.md)
- dev-integration accepted-idea-delivery review:
  [../../reviews/components/2026-04-20-operator-orchestration-service-dev-integration-accepted-idea-delivery.md](../../reviews/components/2026-04-20-operator-orchestration-service-dev-integration-accepted-idea-delivery.md)
- accepted-idea delivery consume review:
  [../../reviews/components/2026-04-20-operator-orchestration-service-accepted-idea-delivery-consume.md](../../reviews/components/2026-04-20-operator-orchestration-service-accepted-idea-delivery-consume.md)
- AI governance standard:
  [../../standards/ai-security-and-governance.md](../../standards/ai-security-and-governance.md)

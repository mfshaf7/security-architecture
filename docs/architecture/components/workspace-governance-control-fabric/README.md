# Workspace Governance Control Fabric

## Role

`workspace-governance-control-fabric` is the governance runtime implementation
component for workspace validation planning, readiness/admission evaluation,
receipts, ledger behavior, and operator-facing governance runtime APIs.

It consumes workspace-governance authority contracts. It does not own policy
truth, release authority, security standards, Workspace Delivery ART state, or
product-specific runtime implementation.

## Trust Boundary

This component sits between governed workspace truth and runtime decision
support:

- reads contracts and policy from `workspace-governance`
- exposes API, worker, CLI, receipt, and ledger surfaces
- will use platform-owned runtime and storage once admitted
- may feed operator workflows and future governance console views
- must not mutate upstream authority stores directly

The current dev-integration profile is `active`. It provides a local-k3s API
Deployment, ClusterIP Service, persistent PostgreSQL StatefulSet/PVC, and
database migration Job for fast local runtime iteration. It is not governed
stage or production evidence.

## Current Admitted Runtime Shape

- owner repo: `workspace-governance-control-fabric`
- platform runtime owner: `platform-engineering`
- workspace authority owner: `workspace-governance`
- security owner: `security-architecture`
- current runtime lane: source plus active local-k3s `dev-integration` API and
  PostgreSQL profile
- stage/prod status: not admitted

## Security Model

### Identity

- future API and worker identity must be distinct from operator identity
- operator approval remains outside the runtime implementation
- caller identity and request correlation must be attributable before
  activation

### Secrets

- no repo-local platform secret ownership is approved
- future storage and runtime credentials belong to platform-managed delivery
  through Vault and External Secrets
- raw evidence or operational context must not leak through logs or packets

### Delivery

- source implementation lands here
- platform deployment state and promotion gates remain in
  `platform-engineering`
- workspace rules and maturity contracts remain in `workspace-governance`
- stage rehearsal cannot be claimed from the dev-integration profile

### Runtime

- runtime commands must fail closed when authority contracts, component
  inventory, or profile state cannot be proven
- persistent dev-integration state requires read-only shared smoke
- mutating ledger or receipt smoke requires a separate disposable companion
  profile

### AI

- the control fabric may later prepare governed context or readiness decisions
  for AI-assisted workflows
- it must not become an unapproved model gateway or autonomous mutation path
- any model invocation path remains subject to governed AI profile and
  platform-access controls

## Principal Risks

- policy-source confusion if implementation starts owning workspace contracts
- runtime-lane drift if dev-integration or stage assumptions are not recorded
- ledger or receipt integrity loss if persistent state lacks custody controls
- AI-governance bypass if readiness/admission outputs are treated as autonomous
  decisions
- evidence leakage if raw operational context is projected without redaction

## Required Companion Artifacts

- control-fabric operator surface review:
  [../../../reviews/components/2026-04-30-workspace-governance-control-fabric-operator-surface.md](../../../reviews/components/2026-04-30-workspace-governance-control-fabric-operator-surface.md)
- component inventory:
  [`../../platform/component-inventory.md`](../../platform/component-inventory.md)
- workspace governance contract:
  `workspace-governance/contracts/governance-control-fabric-operator-surface.yaml`
- dev-integration profile registry:
  `workspace-governance/contracts/developer-integration-profiles.yaml`

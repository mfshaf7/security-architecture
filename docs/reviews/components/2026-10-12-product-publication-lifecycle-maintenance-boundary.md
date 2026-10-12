# Product Publication Lifecycle Maintenance Security Delta

## Summary

- date: 2026-10-12
- owner repo: `security-architecture`
- delivery initiative: `openproject://work_packages/894`
- parent feature: `openproject://work_packages/924`
- security review item: `openproject://work_packages/1271`
- following OOS source item: `openproject://work_packages/1272`
- following Platform commissioning item: `openproject://work_packages/1273`
- decision URI:
  `security-architecture://product-publication/decisions/lifecycle-maintenance-v1`
- governing architecture packet:
  `wgcf://artifacts/delivery-art/sha256/9615edbd0d60d3066e7e6e861f10844b2d2413658002a717b3e48d5f4bd10f47`
- reviewed source:
  - Workspace Governance ordered lifecycle contract:
    `workspace-governance@fab38a8266512b0004081039b017904c9c55f288`
  - Workspace Governance Control Fabric readiness implementation:
    `workspace-governance-control-fabric@9d3e5ef1b8fafac1bf0970a7d997021c37052535`
  - Operator Orchestration Service inactive lifecycle capability:
    `operator-orchestration-service@786d01c8b1e144f51cc38f6a40d6d986222ac634`
  - Governance Operations Console corrected maintenance routing:
    `governance-operations-console@9c1b9117a98a59662ba570d90bce01bc0b869fb0`
  - existing Platform Product Publication composition:
    `platform-engineering@8f10ea3feae00569e182be7649554479bea32f90`
- decision: `approved-with-findings`

The reviewed source safely supports one bounded lifecycle-maintenance sequence
for the Governance Operations Console in single-operator, loopback-only
`dev-integration`. The sequence reuses Workspace Registry for product lifecycle
and Product Publication for publication posture. It introduces no new service,
authority, identity, database, control plane, or ART item.

Security approves the existing `internal` target plus the exact `unpublish`,
`archive`, and `restore` path needed to move through `unlisted` and `archived`.
The approval is inseparable from the ordered owner-manifest and Workspace
Inventory evidence below. `client` and `public` remain denied.

## Scope Delta

### Design Intent

Feature `#924` adds lifecycle maintenance around the already commissioned
Product Publication workflow. Workspace Registry remains the only product
lifecycle mutator. Product Publication remains the only publication-posture
mutator. WGCF evaluates fresh owner evidence, OOS journals the exact ordered
publication actions, the Console routes the operator to the authoritative
workflow, Security constrains the action set, and Platform commissions and
proves the full sequence.

The lifecycle axes must not be collapsed. Product retirement does not archive
publication, publication restoration does not restore product lifecycle, and
neither operation restores runtime, release, access, or Security acceptance.

### Implemented Control

Workspace Governance now defines the only valid sequence: unpublish a listed
active product before retirement, bind retirement in a fresh schema-v2 owner
manifest before archive, restore product lifecycle before publication restore,
and bind that restore event plus the archived publication receipt before the
publication returns to `unlisted`.

WGCF already validates schema-v2 inventory lifecycle bindings for `archive` and
`restore`. OOS already implements the action transitions, version chain,
idempotency, prior-receipt binding, and lifecycle-maintenance denial gate. Its
source gate is intentionally inactive. The corrected Console does not mutate
maintenance state directly or reuse a stale manifest. It rereads current
Workspace Registry state and the durable Product Publication result, then
routes the next step to one of those existing owner surfaces.

### Operating Evidence

The Workspace Governance sequence repair merged through PR
[#264](https://github.com/mfshaf7/workspace-governance/pull/264). The Console
maintenance correction merged through PR
[#68](https://github.com/mfshaf7/governance-operations-console/pull/68).
Both passed their owner validation, exact-head CI, human review, protected
merge, and strict branch-lifecycle cleanup.

That is source evidence, not live acceptance. OOS lifecycle maintenance remains
source-inactive, no current Platform policy commissions it, and the required
fresh owner manifests do not yet exist. Work items `#1272` and `#1273` own
those remaining controls under the ordered requirements in this decision.

## Review Areas

### Exact Approved Sequence

Platform `#1273` may commission only this sequence, with every owner manifest
committed and reviewed from current owner-repository truth before it is used:

1. Verify the current baseline is Workspace Registry `active` and Product
   Publication `internal`; commit a fresh owner manifest for that exact
   active/`internal` state.
2. Product Publication `unpublish` moves only `internal` to `unlisted`.
3. Workspace Registry `retire` appends the immutable retirement receipt and
   history event.
4. Commit a fresh schema-v2 owner manifest for the exact
   retired/`unlisted` state, bound to that retirement receipt and event.
5. Product Publication `archive` moves only `unlisted` to `archived`, preserving
   the exact prior publication receipt.
6. Workspace Registry `restore` appends the immutable restore receipt and
   history event and binds its prior lifecycle event.
7. Commit a fresh schema-v2 owner manifest for the exact active/`unlisted`
   restoration state, bound to the restore receipt, event, and prior event.
8. Product Publication `restore` moves only `archived` to `unlisted`, binding
   both that owner lifecycle evidence and the exact archived publication receipt.
9. Product Publication may then independently `publish` from `unlisted` to the
   already approved `internal` tuple to restore the original baseline.
10. Commit a fresh schema-v2 owner manifest for the final exact
    active/`internal` state and verify Workspace Registry, Product Publication,
    Console projection, OOS journal, WGCF ledger, and Platform health agree.

No step may copy a prior command's `manifest_source`, infer owner state from UI
state, skip a Workspace Registry transition, rewrite history, or claim a later
step from an earlier receipt. A failed or interrupted step must stop at the
last durable state and resume from fresh authoritative readback.

### Target And Action Decision Matrix

| Target/action | Security treatment | Constraint |
| --- | --- | --- |
| `internal` / `publish` | approved | Only `unlisted` to the fixed workspace-authenticated internal tuple. |
| `unlisted` / `unpublish` | approved | Only an active listed product with a fresh manifest for its exact current listed posture. |
| `archived` / `archive` | approved | Only retired/`unlisted` with fresh schema-v2 retirement evidence. |
| `unlisted` / `restore` | approved | Only active lifecycle after Registry restore, with fresh schema-v2 restore evidence and the exact archived publication receipt. |
| `client` | denied | No client endpoint, identity, authorization, or access acceptance exists. |
| `public` | denied | No public exposure, identity, authorization, or access acceptance exists. |
| `update` | not added by this decision | Lifecycle maintenance does not require a general listed-posture update authority. |

### Identity And Authorization

The browser principal, Console machine caller, operator, OOS workflow
authority, WGCF readiness caller, Workspace Registry lifecycle authority,
Security reviewer, Platform activator, product owner, and human source reviewer
remain distinct. The Console may route intent but cannot assert lifecycle,
publication, source, Security, or Platform authority.

This decision remains limited to the existing local, single-operator lane.
Remote, shared, multi-user, client, public, stage, or production operation is
not approved.

### Secrets And Data

Existing Console-to-OOS and OOS-to-WGCF credentials remain server-side. No new
secret or identity is approved. Owner manifests, lifecycle evidence, packets,
receipts, logs, source, and review artifacts must remain secret-free and use
synthetic operator-safe data.

### Delivery And Evidence Integrity

Each owner manifest must bind a current source snapshot and must be committed
before WGCF evaluates it. Schema-v2 manifests must bind the exact Workspace
Inventory receipt, history event, prior event, record version, record digest,
and resulting lifecycle state. OOS must preserve the publication version and
previous-receipt chain and reject contradictory, stale, unauthorized, or
replayed input before journal mutation.

The current architecture packet does not enumerate the complete sequence and
describes lifecycle source activation too narrowly. After `#1271` closes and
before `#1272` starts, a material superseding packet must bind this decision,
the corrected source heads, the owner-manifest Landing Units, the exact
cross-repo order, and positive and negative full-sequence conformance cases.
This is a correction to Epic `#894`, not a new initiative or child.

### Runtime, Rollback, And Recovery

OOS `#1272` may activate only:

- target postures `internal`, `unlisted`, and `archived`;
- the already implemented `archive` and `restore` lifecycle actions; and
- the exact Security decision URI, merged revision, and digest for this review.

The existing fixed action bindings continue to constrain source and target
postures. Client and public targets remain rejected before WGCF access or
journal mutation.

Platform `#1273` must prove every positive step, every prohibited ordering,
authorization mismatch, stale-manifest rejection, replay conflict, process
loss, restart, durable readback, rollback, and final baseline reconciliation.
Rollback may disable runtime bindings, but it must not delete or rewrite owner
source, Workspace Inventory history, WGCF ledger entries, OOS journal entries,
publication receipts, or review evidence.

The safe interruption states are active/`unlisted`, retired/`unlisted`,
retired/`archived`, or active/`archived`. Recovery rereads both owner systems
and continues the same ordered sequence. It never invents a compensating
direct mutation.

### Visibility, Documentation, And AI

The Console must show the current Registry lifecycle, durable publication
posture, next authoritative owner surface, and blocked contradictions without
claiming success from source merge or Security review. The Platform runbook is
the primary operator procedure for commissioning and recovery.

No model selects the action, owner evidence, lifecycle transition, publication
target, Security decision, approval, or activation. No AI action path is
introduced or approved.

## Findings And Residual Constraints

1. **Architecture sequence: open downstream control.** The current packet must
   be superseded after this review closes and before `#1272` starts.
2. **Source activation: open downstream control.** OOS lifecycle maintenance
   remains inactive until `#1272` binds this exact merged decision.
3. **Owner evidence and operating acceptance: open downstream control.** The
   fresh manifests and full composed proof belong to `#1273`; static or copied
   evidence is insufficient.
4. **Client and public exposure: denied.** This decision creates no access
   authority or broader audience.
5. **No new mechanism.** Workspace Registry and Product Publication remain the
   only mutation owners; a direct Product Maintenance mutation path is denied.

## Decision

`approved-with-findings`

Security emits
`gate:product-publication-lifecycle-maintenance-activation` for the bounded OOS
source activation and Platform commissioning described above. Approval covers
only the exact `internal` -> `unlisted` -> `archived` -> `unlisted` ->
`internal` publication sequence, coordinated with Registry `active` ->
`retired` -> `active` lifecycle and fresh owner evidence at every required
boundary.

The review owner is `security-architecture`. Findings 1 and 2 must close before
runtime activation; finding 3 closes only with `#1273` operating evidence and
final current-state reconciliation. Any broader target, direct mutation path,
new identity, remote exposure, new service, or changed trust boundary requires
a fresh Security decision.

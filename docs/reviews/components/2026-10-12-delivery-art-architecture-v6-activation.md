# Delivery ART Architecture V6 Activation Security Delta

## Summary

- date: 2026-10-12
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.workspace-governance`
  - `repos.operator-orchestration-service`
  - `repos.workspace-governance-control-fabric`
  - `components.operator-orchestration-service`
  - `components.workspace-governance-control-fabric`
- related active initiative: `openproject://work_packages/894`
- related improvement candidate:
  `workspace-governance/reviews/improvement-candidates/2026-10-12-product-publication-activation-ownership-regression.yaml`
- superseded activation conditions:
  [`2026-10-08-delivery-art-architecture-v6-activation-ownership.md`](2026-10-08-delivery-art-architecture-v6-activation-ownership.md)
- exact reviewed consumer heads:
  - [operator-orchestration-service#315](https://github.com/mfshaf7/operator-orchestration-service/pull/315), head `654883afb4eede2e169ef25daa22c176848df27d`
  - [workspace-governance-control-fabric#103](https://github.com/mfshaf7/workspace-governance-control-fabric/pull/103), head `e8cc466aae57111ca6663783fbdd6dc45443ee6f`
- reviewed Workspace Governance v6 authority:
  - [workspace-governance#240](https://github.com/mfshaf7/workspace-governance/pull/240), merge `052261b14196d52318767e1bf371b1c156c0ac26`
  - [workspace-governance#241](https://github.com/mfshaf7/workspace-governance/pull/241), merge `f81c52a45c81e24188a01d71ae54813270eebf0d`
- review triggers:
  - `delivery-art-v6-current-version-activation`
  - `delivery-art-v6-source-snapshot-revision-binding`
  - `delivery-art-v6-security-source-commissioning-order`
  - `delivery-art-v6-historical-session-preservation`
- decision: `approved`

The exact OOS and WGCF heads are approved for the controlled
`dev-integration` activation of the already-reviewed Architecture Packet v6
contract. This delta replaces only the obsolete activation conditions that
required new work under closed Epic 1203. It does not weaken or replace the
v6 source-activation control.

This approval does not itself activate v6, deploy either consumer, approve
stage or production, or claim operating evidence. Activation remains ordered:
Security review, exact consumer merges, Workspace Governance authority
cutover, consumer deployment, and live v6 proof.

## Scope Delta

### Design Intent

The v6 design is unchanged from the 2026-10-08 review. Every
`before_runtime_activation` gate must bind the exact source owner, repository
revision, source field and observed posture, source activation Landing Unit,
commissioning Landing Units, and the Security-to-source-to-commissioning
ordering path.

### Implemented Control

The reviewed consumer heads change only version posture and its acceptance
proof:

1. OOS admits v6 as the sole format for new architecture persistence and work
   start, while v1-v5 remain immutable historical evidence.
2. WGCF admits v6 as the sole format for new canonical custody and fresh
   architecture readiness, while v1-v5 remain readable for already-bound work.
3. Both consumers retain the v6 negative tests for missing, mismatched, and
   unordered activation ownership.

The full OOS suite passed 1,273 tests with no failures. The full WGCF suite
passed 489 tests with no failures. These are pre-merge source results, not
operating evidence.

### Session Inventory And Cutover

The live OOS dev-integration inventory immediately before this review contains
three retained sessions:

- `delivery-892`: cleanup-blocked and not architecture-bound;
- `delivery-898`: cleanup-blocked and bound to immutable schema v3 artifact
  `architecture-packet:delivery-898-v1`;
- `delivery-900`: cleanup-blocked and bound to immutable schema v3 artifact
  `architecture-packet:delivery-900-v1`.

There is no v5-bound active session and no session that requires rebinding or
rewriting. The three sessions remain cleanup-only historical residue; this
activation neither deletes them nor treats them as current work.

The first new v6 Architecture Packet will cover the remaining open scope of
Epic 894. That packet is operating proof of the activated control, not a new
repair story and not a child of closed Epic 1203.

## Review Areas

### Identity

No identity or approval authority changes. OOS remains workflow author, WGCF
remains custody/readiness authority, Security remains security acceptance
authority, and Platform remains runtime commissioning authority.

### Secrets

No secret path changes. Activation evidence remains bounded source metadata;
credentials, private keys, tokens, and raw command output are prohibited.

### Delivery

The change prevents a downstream commissioning owner from being asked to
activate a source state it does not own. Exact owner/revision evidence and
ordered Landing Units remain mandatory. A mixed current-version posture is
blocked by sequencing Workspace Governance authority activation after both
reviewed consumer merges.

### Runtime

The reviewed heads grant no stage or production authority. Existing v1-v5
packets remain immutable, and cleanup-only sessions retain their exact bound
artifacts. Dev-integration deployment must expose v6 consistently in OOS and
WGCF before a fresh v6 packet is accepted as operating proof.

### AI

No model, prompt, or AI-authorized action path changes.

## Residual Risk And Activation Conditions

No finding or accepted risk is created. Activation remains conditional on:

- merging the exact reviewed OOS and WGCF heads, or obtaining a new delta
  review if their security-relevant semantics change;
- activating Workspace Governance only after those exact consumer merges and
  binding the resulting merged revisions in its activation evidence;
- preserving the recorded session inventory without rebinding historical
  packets;
- deploying exact merged consumer revisions together in `dev-integration`;
- persisting and resolving a fresh v6 Architecture Packet for active Epic 894
  before its remaining source-backed work begins; and
- keeping stage and production out of scope pending separate review and
  operating evidence.

Failure of a condition blocks cutover or requires rollback to v5. It is not
implicit risk acceptance.

## Decision

`approved`

Approved:

- the exact OOS and WGCF heads listed above;
- v6 current-version posture in `dev-integration` after ordered merge and
  authority cutover;
- immutable v1-v5 read compatibility;
- retention of the three cleanup-only sessions at their existing bindings;
- replacing the obsolete closed-1203 activation condition with
  candidate-linked maintenance and the first fresh v6 packet for active Epic
  894.

Not approved:

- stage or production activation;
- rewriting, rebinding, or deleting historical sessions as part of cutover;
- a mixed current-version posture;
- treating pre-merge tests as operating evidence; or
- bypassing Security, source-owner, WGCF, OOS, Platform, or human-review
  authority.

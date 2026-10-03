# Delivery ART Architecture V5 Evidence Ownership Security Delta

## Summary

- date: 2026-10-03
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.workspace-governance`
  - `repos.operator-orchestration-service`
  - `repos.workspace-governance-control-fabric`
  - `components.operator-orchestration-service`
  - `components.workspace-governance-control-fabric`
- related Delivery initiative: `openproject://work_packages/1203`
- related improvement candidate:
  `workspace-governance/reviews/improvement-candidates/2026-10-03-post-merge-review-packet-architecture-recovery-regression.yaml`
- reviewed changes:
  - [workspace-governance#229](https://github.com/mfshaf7/workspace-governance/pull/229), merge `acad88ce4489a96a48bee75cd19abfa44518efda`
  - [workspace-governance#230](https://github.com/mfshaf7/workspace-governance/pull/230), merge `cd75086b7ab0266cfb055d22ab3bc02fadb9f2ba`
  - [operator-orchestration-service#268](https://github.com/mfshaf7/operator-orchestration-service/pull/268), merge `1c99cc98cc8beebbb56d37307bc1b2e8b2fded1d`
  - [operator-orchestration-service#269](https://github.com/mfshaf7/operator-orchestration-service/pull/269), merge `a1458b2ce5888e4c00b0ff66724e64d656ce25b8`
  - [workspace-governance-control-fabric#95](https://github.com/mfshaf7/workspace-governance-control-fabric/pull/95), merge `897bb984fe6821a9872595d1f5e70b0ce42ab419`
- review triggers:
  - `delivery-art-v5-evidence-owner-attribution`
  - `delivery-art-v5-readiness-phase-separation`
  - `delivery-art-v5-fail-closed-version-activation`
  - `delivery-art-v5-validation-termination`
- decision: `approved`

Architecture Packet v5 is approved for the controlled `dev-integration`
activation sequence described below. It corrects evidence attribution without
moving artifact authorship, custody, Security approval, deployment authority,
or ART mutation authority across existing trust boundaries.

This review does not activate v5, approve stage or production use, or claim
operating evidence. Architecture Packet v4 remains current until the explicit
source activation, consumer deployment, active-session inventory, and fresh
Delivery 1203 packet are complete.

## Scope Delta

### Design Intent

V1 through v4 use `applies_to_work_item_ids` both for the work-item outcomes a
conformance case proves and, operationally, for selecting which Landing Unit
must supply evidence. V5 separates those meanings:

- `applies_to_work_item_ids` remains the acceptance and outcome scope.
- `evidence_owner_landing_unit_id` names the one Landing Unit accountable for
  producing an atomic case.
- causal validation requires the evidence owner's execution ordering followed
  by child-to-parent closure to reach every externally applicable outcome.
- readiness selects evidence by exact owner and exact phase, so merge-ready
  proof is required before merge and operating-ready proof is acquired after
  merge before finalization.

This is a narrowing of evidence authority. It does not allow a Landing Unit to
prove an unrelated outcome merely because work-item scopes overlap.

### Implemented Control

The reviewed merged source provides three independent layers:

1. Workspace Governance defines the staged v5 schema, causal semantics, shared
   owner-and-phase parity vectors, immutable v1-v4 posture, and activation
   gates.
2. OOS validates v5, separates outcome cases from evidence-owner cases in work
   contract v2, acquires owned operating-ready evidence after merge, preserves
   earlier-phase evidence, and refuses v5 persistence or work start while v4
   remains current.
3. WGCF independently validates evidence-owner existence and causal closure,
   selects one exact packet Landing Unit and readiness phase, and refuses new
   v5 custody or fresh architecture readiness while v4 remains current.

All three causal parent-closure implementations now keep a visited-node set.
A malformed cyclic descendant map returns the pre-existing cycle validation
error instead of hanging a validator or service process.

The shared parity fixture proves that source and runtime Landing Units receive
only their own phase-specific cases even when every case contributes to the
same Feature outcome.

### Operating Evidence

There is no v5 operating evidence yet because v5 is deliberately staged. The
merged changes and passing CI prove source behavior only. The existing v4
runtime remains authoritative.

The controlled activation sequence must preserve this order:

1. activate v5 in Workspace Governance;
2. activate the matching OOS and WGCF version postures;
3. deploy and verify the exact consumer revisions in `dev-integration`;
4. inventory active OOS sessions immediately before current-pointer cutover;
5. persist a fresh v5 packet for Delivery 1203 and verify exact owner-and-phase
   behavior before normal work resumes.

Non-pristine sessions remain bound to their immutable architecture reference;
they are not silently migrated. Any incompatible session requires an explicit
recovery or supersession decision.

## Review Areas

### Identity

No new human or machine identity is introduced. OOS remains the authenticated
artifact author and ART workflow owner. WGCF remains the independent custody
and readiness service. Security Architecture remains the review authority.
The new evidence-owner field is a workflow accountability binding, not an
authorization credential and not a substitute for caller authentication.

### Secrets

No new secret, credential projection, or storage path is introduced. Existing
bounded caller identities and secret-delivery controls remain unchanged. The
new owner and phase metadata is safe to include in the existing structured
artifact; raw runtime output and credentials remain prohibited.

### Delivery

The main threat is false proof attribution: a supporting Landing Unit could be
made responsible for evidence it cannot produce, or could accidentally satisfy
an outcome owned elsewhere through list overlap. Exact Landing Unit selection
and causal closure address that threat. The shared parity vector reduces
cross-repo semantic drift, while separate activation commits keep the dormant
consumer capability from becoming live merely because parsers understand v5.

The activation PRs must preserve v1-v4 read compatibility and must not rewrite
existing packets or session bindings. Rollback is the coordinated restoration
of v4 as current before new v5 work starts; a mixed current-version posture is
blocked.

### Runtime

Operating-ready cases may be acquired only after merged source is proven and
before finalization. Merge-ready evidence remains immutable while later
operating evidence is appended under a phase-scoped identity. WGCF evaluates
the matching phase independently; OOS cannot self-declare readiness.

Malformed cyclic parent input is bounded and terminating. Version-skew risk is
controlled by keeping v5 staged in every component until source activation,
consumer deployment, and session inventory are complete.

### AI

This change introduces no model decision, model access, prompt path, or
AI-authorized action. Existing human approval and bounded workflow controls are
unchanged.

## Threat And Control Mapping

| Threat | Reviewed control | Judgment |
| --- | --- | --- |
| Outcome overlap assigns proof to the wrong Landing Unit | exact `evidence_owner_landing_unit_id` plus shared parity vector | sufficient |
| Pre-merge and post-merge proof are conflated | exact readiness-phase selection and first-class post-merge acquisition | sufficient |
| An evidence owner cannot causally produce an applicable outcome | execution-order and child-to-parent causal closure | sufficient |
| Cyclic input consumes an unbounded validator loop | visited-node termination plus regression cases in all consumers | sufficient |
| One consumer activates before the others | v4 remains current; v5 custody, readiness, persistence, and work start fail closed | sufficient |
| Existing work is silently rebound during cutover | immutable packet references and required active-session inventory | sufficient |

## Residual Risk And Activation Conditions

No security finding or accepted risk is created by this delta. The remaining
items are activation evidence, not waived controls:

- exact activation commits must be reviewed and merged in the declared order;
- OOS and WGCF deployed revisions must match the activated contract posture;
- the active-session inventory must be captured immediately before cutover;
- the first Delivery 1203 v5 packet must pass both consumers and bind every
  case to one exact evidence owner and readiness phase;
- stage and production remain out of scope until separately reviewed operating
  evidence exists.

Failure of any condition blocks activation or requires rollback to the v4
current posture. It does not become implicit risk acceptance.

## Decision

`approved`

Approved:

- the v5 separation of outcome applicability from evidence ownership;
- causal evidence-owner closure and exact phase selection;
- immutable v1-v4 compatibility;
- controlled `dev-integration` activation using the ordered gates above;
- post-merge acquisition of owned operating-ready evidence before
  finalization.

Not approved:

- stage or production activation;
- silent migration or rewriting of an existing session or packet;
- a mixed current-version posture across Workspace Governance, OOS, and WGCF;
- bypassing WGCF readiness, OOS workflow authority, human review, or the
  immediate pre-cutover session inventory.

# Delivery ART Architecture V6 Activation Ownership Security Delta

## Summary

- date: 2026-10-08
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.workspace-governance`
  - `repos.operator-orchestration-service`
  - `repos.workspace-governance-control-fabric`
  - `components.operator-orchestration-service`
  - `components.workspace-governance-control-fabric`
- related Delivery initiative: `openproject://work_packages/1203`
- related improvement candidate:
  `workspace-governance/reviews/improvement-candidates/2026-10-08-delivery-plan-activation-ownership-regression.yaml`
- reviewed changes:
  - [workspace-governance#240](https://github.com/mfshaf7/workspace-governance/pull/240), merge `052261b14196d52318767e1bf371b1c156c0ac26`
  - [workspace-governance#241](https://github.com/mfshaf7/workspace-governance/pull/241), merge `f81c52a45c81e24188a01d71ae54813270eebf0d`
  - [operator-orchestration-service#284](https://github.com/mfshaf7/operator-orchestration-service/pull/284), reviewed head `dc3fe503492017c5d0a859be6065b4809f7d22d1`
  - [workspace-governance-control-fabric#98](https://github.com/mfshaf7/workspace-governance-control-fabric/pull/98), reviewed head `301ff803bff58be36b3d9c62f41744cd028579b1`
- review triggers:
  - `delivery-art-v6-source-activation-ownership`
  - `delivery-art-v6-source-snapshot-revision-binding`
  - `delivery-art-v6-security-source-commissioning-order`
  - `delivery-art-v6-fail-closed-version-activation`
- decision: `approved`

Architecture Packet v6 is approved for the controlled `dev-integration`
activation sequence described below. The change closes a planning-integrity
gap: a runtime commissioning plan can no longer omit the source-owner change
needed to activate an embedded runtime gate.

This review does not activate v6, approve stage or production use, or claim
operating evidence. Architecture Packet v5 remains current until the explicit
consumer merge, activation, deployment, session inventory, and fresh Delivery
1203 packet are complete.

## Scope Delta

### Design Intent

V5 proves work-item scheduling, human gates, source landing order, and exact
evidence ownership, but it does not require a runtime-activation gate to name
the repository that owns the source prerequisite. V6 adds one
`runtime_activation_chains` entry for every `before_runtime_activation` gate.
Each chain binds:

- the source owner and whether its source is already ready or requires change;
- exact source evidence: repo, revision, path, field, observed value, and
  observed posture;
- the separate source activation Landing Unit when a source change is needed;
- the commissioning Landing Units controlled by the human gate; and
- source and work-item order from human authority, through source activation,
  to commissioning.

The evidence revision must equal the source snapshot commit for the declared
owner. This binding was added by Workspace Governance #241 after review found
that the original staged contract accepted any syntactically valid 40-character
revision. OOS and WGCF now contain independent negative cases for the same
mismatch.

### Implemented Control

The reviewed source provides three independent layers:

1. Workspace Governance defines staged v6 schema and semantic truth, including
   exact runtime-gate coverage, owner binding, source-snapshot revision binding,
   separate activation and commissioning units, and ordered execution.
2. OOS validates and projects v6 using current v5 evidence-owner semantics but
   refuses v6 persistence and new work while v5 remains current.
3. WGCF independently validates the same activation chain and readiness
   selection but refuses v6 custody and fresh architecture readiness while v5
   remains current.

The shared Epic 1203-shaped parity vector fixes the expected order as Security
authority, OOS-owned source activation, then Platform commissioning. It does
not itself activate any runtime or mutate ART.

### Operating Evidence

There is no v6 operating evidence because v6 is deliberately staged. The
merged authority changes, exact open consumer heads, and passing local suites
prove source behavior only. V5 remains authoritative in the running workflow.

The controlled activation sequence must preserve this order:

1. merge the exact reviewed OOS and WGCF consumer heads;
2. activate v6 in Workspace Governance and both consumers in one declared
   cross-repo sequence;
3. deploy and verify exact consumer revisions in `dev-integration`;
4. inventory and disposition non-pristine OOS sessions immediately before
   current-pointer cutover; and
5. create the required OOS activation ART child, persist a fresh v6 packet for
   Delivery 1203, and verify Security-to-source-to-commissioning behavior.

Existing packets and sessions remain immutable. No historical packet is
rewritten as v6.

## Review Areas

### Identity

No new identity or approval authority is introduced. The source-owner field is
a planning and evidence binding, not a credential. OOS remains workflow and
artifact author, WGCF remains independent custody/readiness authority, Security
remains human review authority, and Platform remains commissioning authority.

### Secrets

No new secret, credential projection, or secret storage path is introduced.
The activation evidence is structured repository metadata and must not contain
tokens, raw credentials, private keys, or unrestricted command output.

### Delivery

The main threat is an apparently executable plan that skips a source-owned
state transition and asks a downstream commissioning owner to activate
something it cannot change. Exact owner, separate Landing Unit, gate coverage,
and graph ordering reject that shape.

A second threat is evidence substitution: a packet could cite the right repo
but a different revision. Source-snapshot equality now rejects that condition
in all three validators. The actual path, field, and observed value still must
be captured by the bounded architecture-authoring workflow from the cited
revision; the structured claim is not independent runtime attestation.

### Runtime

V6 remains dormant. Schema acceptance does not grant custody, readiness,
persistence, work-start, deployment, or commissioning authority. A mixed
current-version posture is blocked, and rollback restores v5 as current before
any v6 work starts.

### AI

This change introduces no model decision, prompt path, or AI-authorized action.
Existing operator acceptance and human review remain required.

## Threat And Control Mapping

| Threat | Reviewed control | Judgment |
| --- | --- | --- |
| Runtime commissioning omits a required source-owner transition | exact runtime-gate coverage plus owner source posture | sufficient |
| Source activation is assigned to the commissioning owner | separate owner-bound activation Landing Unit | sufficient |
| Source evidence cites an unrelated revision | equality with the owner's source-snapshot commit | sufficient |
| Activation occurs before Security authority | work-item prerequisite and source-graph path from authority to activation | sufficient |
| Commissioning occurs before source activation | exact activation-to-commissioning source path | sufficient |
| One consumer activates before the others | v5 stays current; v6 custody, readiness, persistence, and work start fail closed | sufficient |
| Existing work is silently rebound | immutable packet references and required pre-cutover session inventory | sufficient |

## Residual Risk And Activation Conditions

No security finding or accepted risk is created by this staged delta. The
remaining items are activation evidence, not waived controls:

- OOS and WGCF must merge the exact reviewed heads or receive a new delta
  review for changed security-relevant semantics;
- activation commits must preserve v1-v5 compatibility and the v6 negative
  revision case;
- deployed OOS and WGCF revisions must match the activated contract posture;
- the architecture-authoring workflow must read the cited revision when it
  records path, field, observed value, and posture;
- non-pristine session inventory must be captured immediately before cutover;
- the fresh Delivery 1203 packet must contain the separate OOS activation child
  before Platform commissioning; and
- stage and production remain out of scope until separately reviewed operating
  evidence exists.

Failure of any condition blocks activation or requires rollback to v5. It does
not become implicit risk acceptance.

## Decision

`approved`

Approved:

- staged v6 activation ownership and source-snapshot revision binding;
- independent OOS and WGCF validation at the reviewed heads;
- immutable v1-v5 compatibility;
- the ordered `dev-integration` activation sequence above.

Not approved:

- stage or production activation;
- treating declared source evidence as independent runtime attestation;
- silent migration or rewriting of an existing session or packet;
- a mixed current-version posture;
- bypassing Security authority, source-owner implementation, WGCF readiness,
  OOS workflow authority, human review, or the pre-cutover session inventory.

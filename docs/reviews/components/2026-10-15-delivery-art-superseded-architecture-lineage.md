# Delivery ART Superseded Architecture Lineage Security Delta

## Summary

- date: 2026-10-15
- owner repo: `security-architecture`
- affected review subject: `components.workspace-governance-control-fabric`
- delivery initiative: `openproject://work_packages/1275`
- governed Platform item: `openproject://work_packages/1291`
- related improvement candidate:
  `workspace-governance/reviews/improvement-candidates/2026-10-14-delivery-art-human-gate-topology-regression.yaml`
- exact reviewed source:
  - [workspace-governance-control-fabric#110](https://github.com/mfshaf7/workspace-governance-control-fabric/pull/110), head `1a8d22e76a2b2af406af613bb314d5cf4f0271ca`
- review triggers:
  - `delivery-art-active-architecture-semantic-validation`
  - `delivery-art-superseded-architecture-custody-lineage`
  - `delivery-art-review-packet-predecessor-validation`
- decision: `approved`

Security approves the exact reviewed head for `dev-integration` and source
merge. The change corrects a historical-artifact compatibility regression: an
active, semantically valid Architecture Packet could not reach readiness when
its immutable `custody.supersedes` ancestor predated the current topology
rules.

The approval does not relax validation of the active Architecture Packet or
of Review Packet predecessor chains. It does not approve stage or production
activation and does not create new identity, storage, service, workflow, or
runtime authority.

## Scope Delta

### Design Intent

The active Architecture Packet remains the current decision contract and must
pass every current semantic, topology, custody, and integrity rule. A packet
named only by that active packet's `custody.supersedes` field is historical
lineage: its canonical bytes and custody receipt must still resolve exactly,
but its superseded design is not reactivated and judged against later semantic
rules.

Review Packet predecessor chains remain active completion lineage and continue
to receive full semantic validation. The distinction is based on the declared
artifact relationship, not on caller choice or artifact age.

### Implemented Control

The reviewed WGCF head:

- validates the active Architecture Packet before traversing its lineage;
- resolves a superseded Architecture Packet through exact canonical digest,
  stored artifact, and custody-receipt checks;
- does not recursively apply current architecture semantics to that historical
  predecessor;
- continues full validation and recursion for Review Packet predecessors; and
- rejects an active packet whose own dependency graph is cyclic.

Focused regression tests prove that a cyclic active packet is denied, a
corrected successor may supersede that immutable packet, and later readiness
can resolve the corrected active packet. The previously established historical
schema compatibility case remains covered. The complete WGCF suite passed 504
tests with no failures. These results are pre-merge source evidence, not an
operating-readiness claim.

### Operating Evidence

Operating evidence remains pending until the exact reviewed head is merged,
deployed through the existing WGCF `dev-integration` profile, and the blocked
Delivery ART readiness request is replayed successfully. That replay must
resolve the already-persisted active packet and its exact custody lineage; it
must not rewrite either artifact.

## Review Areas

### Identity

No identity or human-approval boundary changes. OOS remains workflow author,
WGCF remains custody and readiness authority, Security remains review
authority, Platform remains runtime authority, and `mfshaf7` remains the human
reviewer and merger.

### Secrets

No secret path, token scope, or credential projection changes.

### Delivery

The repair preserves fail-closed validation for current decisions while
preventing later semantic rules from retroactively invalidating immutable
superseded architecture evidence. Exact digest and custody checks remain
mandatory before historical lineage is accepted.

### Runtime

No API route, network exposure, storage backend, deployment topology, or
runtime action is added. The merged revision must replace the current WGCF
`dev-integration` image before readiness replay; stage and production remain
unchanged.

### AI

No model, prompt, inference, or AI-authorized action path changes.

## Decision

`approved`

Approved:

- merge of exact WGCF head `1a8d22e76a2b2af406af613bb314d5cf4f0271ca`;
- bounded `dev-integration` deployment and readiness replay;
- integrity-and-custody-only traversal of an Architecture Packet referenced
  solely as the active packet's superseded ancestor; and
- continued full semantic validation of the active Architecture Packet and
  Review Packet predecessor lineage.

Not approved:

- bypassing canonical digest or custody-receipt verification;
- accepting a semantically invalid active Architecture Packet;
- weakening Review Packet predecessor validation;
- rewriting historical artifacts; or
- stage or production activation.

# Delivery ART Evidence Custody And Source Provenance Security Delta

## Summary

- date: 2026-08-09
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.platform-engineering`
  - `repos.workspace-governance`
  - `repos.workspace-governance-control-fabric`
  - `repos.operator-orchestration-service`
  - `components.workspace-governance-control-fabric`
  - `components.operator-orchestration-service`
- security ART item: `openproject://work_packages/805`
- architecture correction: `openproject://work_packages/809`
- implementation follow-ups:
  - `openproject://work_packages/811`
  - `openproject://work_packages/810`
  - `openproject://work_packages/802`
  - `openproject://work_packages/803`
  - `openproject://work_packages/804`
  - `openproject://work_packages/806`
- reviewed contract merge:
  [workspace-governance#139](https://github.com/mfshaf7/workspace-governance/pull/139)
- reviewed contract commit:
  [`bf64af3`](https://github.com/mfshaf7/workspace-governance/commit/bf64af372d54984bd544d4eb7e987cc73cc91652)
- review triggers:
  - `delivery-art-evidence-custody-boundary`
  - `delivery-art-source-provenance-integrity`
  - `delivery-art-object-storage-and-lifecycle`
  - `delivery-art-safe-openproject-projection`
- decision: `approved-with-findings`

The corrected design separates evidence authorship, governance custody,
physical storage, and ART work-state projection. OOS authors and validates
Delivery ART source artifacts, WGCF owns their governance registry and custody
receipts, Platform owns the physical object-storage runtime, and OpenProject
stores only bounded evidence references.

This decision approves that architecture and bounded implementation work. It
does not claim that shared custody is running, that any service identity or
storage profile exists, or that stage or production use is authorized.

## Scope Delta

### Design Intent

The prior design treated OpenProject attachments as the durable evidence
backend and assigned custody to OOS. The corrected design requires this write
order:

1. OOS validates the source artifact and computes its canonical digest.
2. WGCF persists the content-addressed artifact through Platform-owned object
   storage.
3. WGCF records registry metadata and issues an immutable custody receipt.
4. OOS writes only the artifact reference, digest, and custody-receipt
   reference to OpenProject before performing the guarded ART transition.

The approved artifact classes are currently limited to the Delivery ART
architecture packet, work-start record, and Review Packet. The registry is not
a general log, command-output, context-packet, or arbitrary attachment store.

### Implemented Control

The reviewed implementation is contract and schema only:

- RFC 8785 canonicalization with SHA-256 content addressing
- exact source base and head provenance for source-backed evidence
- real-Git evidence when a claim depends on Git history
- append-only corrections with same-subject, digest-bound supersession
- opaque WGCF registry references that do not expose storage topology
- Platform storage receipts bound into WGCF custody receipts
- registry-first ordering before OpenProject mutation
- idempotent duplicate-digest reuse
- preservation of durable artifacts when OpenProject projection fails
- explicit lifecycle control instead of compensating deletion

No Platform object store, WGCF registry endpoint, OOS persistence client, or
live OpenProject projection change is implemented or approved as operating by
this review.

### Operating Evidence

There is no operating evidence for the target custody path yet. Contract
validation and the merged schema prove only the intended structure and local
integrity rules. The following remain unproven until their owning ART items
land:

- profile-scoped service identities and authorization
- encrypted object persistence and tenant/profile isolation
- registry and storage atomicity or recoverable reconciliation
- backup and content-address-preserving restore
- authorized retention and deletion lifecycle behavior
- OOS retry and replay behavior against the real WGCF boundary
- bounded OpenProject reference projection
- end-to-end dogfood on initiative 698

## Review Areas

### Identity

The target path introduces two machine trust edges: OOS to WGCF and WGCF to
Platform storage. Implementation must provide distinct workload identities,
method-scoped authorization, profile scoping, and request attribution. WGCF
must reject callers that are not allowed to register the declared artifact
class, and Platform storage credentials must not grant OOS direct object-store
access.

Custody receipt `service_identity_ref` values must resolve to the identity that
performed the registry write. Human identity is required for retention,
deletion, exception, and break-glass decisions; a workflow retry is not such an
authorization.

### Secrets

Delivery ART packets can contain internal source paths, repository metadata,
review context, and operational references. They must be encrypted in transit
and at rest, inaccessible through public object URLs, and omitted from normal
service logs. Storage credentials belong to Platform-managed secret delivery,
not source repositories or OpenProject.

The custody receipt and OpenProject projection must remain reference-only.
Neither may embed artifact bodies, credentials, raw validator output, or
storage topology. Payload type and size limits must be enforced before storage
to prevent the registry from becoming an unbounded evidence dump.

### Delivery

The authority split is approved only while these boundaries remain true:

- Workspace Governance owns schemas, policy, readiness meaning, and evidence
  obligations.
- OOS owns artifact authorship, semantic validation, and ART mutation.
- WGCF owns registry metadata, custody receipts, and governance-ledger events;
  it owns neither artifact meaning nor ART mutation.
- Platform owns physical storage, runtime identity delivery, backup, restore,
  and deployment state.
- Security Architecture owns custody and source-provenance judgment.
- CGG remains the operational-context admission and context-custody system; it
  is not the Delivery ART evidence registry.

OpenProject is a projection and work-state authority, not the artifact store.
The removal of attachment custody must not be reintroduced as a fallback when
WGCF or Platform is unavailable.

### Runtime

The runtime must fail closed before ART mutation when registry persistence is
unavailable or integrity validation fails. A successful artifact write followed
by an OpenProject write failure preserves the artifact and retries only the
bounded reference projection. It must not delete and recreate evidence as
compensation.

Duplicate digest retries must resolve to the existing artifact and custody
receipt without creating conflicting identity. Registry metadata and storage
state must be reconcilable after partial failure. Digest verification is
required before persistence acknowledgement and after restore.

Retention and deletion are separate lifecycle operations. They require policy,
actor, reason, target, and receipt evidence. Artifact-body deletion must not
erase the custody receipt, ledger history, or supersession chain needed to
explain prior ART decisions.

Backup and restore must preserve the content address. A restore that changes
bytes, rebinds a digest, or silently rewrites a registry reference fails the
control. Stage and production remain denied until those controls and their
operating evidence receive a fresh security review.

### AI

This change does not approve model access to Delivery ART artifacts. If an AI
workflow later needs their content, it must use the approved context-admission
and governed model-access path. Possession of a WGCF artifact reference does
not grant projection authority to a model.

## Threat And Control Mapping

| Threat | Required control | Owning follow-up |
| --- | --- | --- |
| Artifact substitution after review | canonical digest verification at producer, registry, and restore boundaries | #810, #802 |
| Confused-deputy write or read | distinct service identities and method/profile-scoped authorization | #811, #810, #802 |
| Replay creates conflicting evidence | deterministic content address and duplicate-digest idempotency | #810, #802 |
| Registry and storage diverge | storage receipt binding, fail-closed acknowledgement, and reconciliation evidence | #811, #810 |
| Sensitive content leaks through metadata | opaque references, bounded receipts, no body or storage topology in OpenProject | #810, #802 |
| Workflow failure erases evidence | preserve-on-projection-failure and prohibit compensating deletion | #810, #802 |
| Unauthorized retention or deletion | explicit human-attributed lifecycle control with immutable audit evidence | #811, #810 |
| Restore breaks prior decisions | content-address-preserving backup/restore verification | #811, #810 |
| Synthetic proof claims Git causality | exact revisions and `real-git` evidence for Git-history claims | #802, #803 |

## Findings And Required Follow-up

1. Platform object storage is not implemented. #811 must provide the
   profile-scoped storage, workload identity, encryption, isolation, storage
   receipt, backup, restore, retention, deletion, and denial tests.
2. WGCF custody is not implemented. #810 must implement the registry,
   content/digest verification, idempotency, immutable custody receipts,
   supersession checks, authorization, reconciliation, and lifecycle audit
   boundary without taking artifact authorship.
3. OOS producer and projection behavior is not implemented. #802 must validate
   and persist through WGCF before OpenProject mutation, project only safe
   references, and prove retry, replay, partial-failure, and stale-reference
   behavior.
4. Structured readiness evaluation and duplicate quality cleanup remain
   pending under #803 and #804. Neither owner may recreate custody or ART
   semantic authority as a convenience.
5. No operating evidence exists. #806 must dogfood the complete path on
   initiative 698 and preserve exact Review Packet, custody, storage, and ART
   projection references.

These findings are already routed to active ART work. No parallel remediation
record is created by this review. A failure in any required control blocks the
dependent runtime item rather than being accepted implicitly.

## Decision

`approved-with-findings`

Approved:

- the corrected owner split and write sequence
- content-addressed Delivery ART artifact custody through WGCF and
  Platform-owned storage
- immutable, opaque custody receipts and append-only supersession
- exact source provenance and real-Git fidelity for Git-history claims
- bounded `dev-integration` implementation work under #811, #810, #802, #803,
  and #804
- preservation and retry semantics when OpenProject projection fails
- explicit retention/deletion lifecycle separation

Not approved:

- any claim that the custody runtime currently exists
- direct OOS access to Platform object storage
- WGCF artifact authorship, workspace-policy ownership, security approval, or
  ART mutation
- OpenProject attachment custody or artifact-body projection
- CGG substitution as the Delivery ART evidence store
- anonymous, shared, or overprivileged service identity
- public object access, unbounded payloads, or raw content in receipts/logs
- automatic or compensating deletion
- stage, production, or general operating readiness

The design may proceed to #811. Runtime activation remains fail-closed until
the implementation sequence lands and #806 produces operating evidence for a
fresh security judgment where the target lane requires it.

## Related Artifacts

- [Security delta review process](../security-delta-review-process.md)
- [Security review checklist](../security-review-checklist.md)
- [WGCF security view](../../architecture/components/workspace-governance-control-fabric/README.md)
- [OOS security view](../../architecture/components/operator-orchestration-service/README.md)
- [Delivery ART operator-path contract](https://github.com/mfshaf7/workspace-governance/blob/bf64af372d54984bd544d4eb7e987cc73cc91652/contracts/delivery-art-operator-path.yaml)
- [Custody receipt schema](https://github.com/mfshaf7/workspace-governance/blob/bf64af372d54984bd544d4eb7e987cc73cc91652/contracts/schemas/delivery-art-custody-receipt.schema.json)

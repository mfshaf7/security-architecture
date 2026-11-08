# Exact local archives for bounded image recovery

## Summary

- Date: 2026-11-08.
- Classification: operator-approved Platform owner maintenance, outside ART.
- Landing Unit Decision: `feature_single_landing_unit`,
  `maintenance-image-recovery-acceptance-20261108`.
- Subject: existing finite root image checker and Console consumer recovery.
- Decision: approved for source landing after required owner checks; commissioning
  requires exact merged-source binding in the existing finite decision.

## Scope Delta

The intended result is to recover the approved image without depending on a
registry download after destructive cache removal. A real MinIO executable
mismatch was detected, but replacement failed when its original upstream denied
access. Exact-digest manual recovery passed an 18-image scan. A later distinct
Temporal admin-tools mismatch was incorrectly treated by the outer lifecycle as
replaying the earlier artifact. The physical cause of the byte changes is
unproven; neither observation establishes a Console source or mutable-data defect.

Candidate Platform `4994a3de722d3b44631f09892a93987f6d7d1430`, tree
`1567fbce22e74f6bab9af92d98d5aed1957b0e67`, implements the existing recovery
boundary. Before removal it exports original compressed content into its existing
root-owned state and validates the OCI graph against the admitted immutable
reference. Every included blob hash and size, exact root name, unique Linux/amd64
manifest, configuration and required layers must match. Archive members are
bounded and inspected without extracting paths; links, traversal, duplicates,
unsafe custody and incomplete or foreign content are rejected. Verification uses
bounded streaming buffers. No new runtime service, registry or resident cache is
created.

Replacement reimports that retained archive, restores only original aliases and
checks unpacked files against trusted content. Missing original bytes or a bad
archive block before removal. Import begins with a durable per-image incident
phase; uncertain import is not blindly replayed. Fresh byte proof may establish
that an import finished. A crash before that import can resume it from the exact
validated archive without repeating image removal. A missing image without its
matching incident and archive remains blocked.

The outer lifecycle permits a disjoint new damaged image while earlier verified
replacements await readiness. It retains original controller UIDs, desired
replicas, original mismatch evidence and retired-pod history, without repeating
completed deletion. Root incidents retain one attempt per image. The bounded
lifecycle, owner-idle guard, unmanaged-consumer refusal and final readiness proof
remain authoritative. Operator-required failures are not silently cleared.

## Review Areas

Runtime/host control: the existing root-installed helper alone accesses native
containerd image operations. It still accepts only finite actions, not caller
paths, images, namespaces or commands. Source and root policy hashes must match
the accepted Platform tree. Archive import is limited to the original admitted
OCI graph; this is not host execution or a generic container import API.

Identity/secrets: original scoped identities and caller boundaries remain.
Archives contain public image content, not container writable layers, data volumes
or provider credentials. Console, OOS and models gain no root or archive access.

Delivery: use Gary publication, delegated human review, exact composed Security
acceptance and deliberate helper reinstallation before normal commissioning.
Other accepted sources, durable manifest and worker digest are unchanged.
Rollback restores the prior accepted source/helper decision while preserving
archives, incidents and owner data for inspection. It does not erase failures.

## Validation and operating evidence

Thirty-one focused OCI/integrity/consumer-recovery tests pass, including unavailable
upstream, invalid and incomplete archives, unsafe paths, failed export before
removal, uncertain import, interrupted metadata and disjoint-image boundaries.
The candidate verifier also validates a real export of the approved MinIO image
and reconstructs its 891 baseline entries with native content unavailable and
registry access disabled, including the expected executable hash and zero network
calls.
All local CI-equivalent commands passed in exact-head canonical/CI contexts,
including chart and Terraform checks. Source identity validation additionally
proved its declared pinned inventory; sandbox tests retained their isolated CI
context, while real publication admission used current canonical inventory.
Platform PR376 carries the exact candidate and validation evidence; exact-head
CI and delegated owner approval remain required before source merge.
These are source checks; real local import, restored consumers, exact helper
hashes and native Console reads remain commissioning obligations.

## Decision

Approved within the existing local dev-integration recovery boundary after
required checks and exact source binding. No new finding, waiver, provider
permission, unbounded retry or ART item is introduced. Main agent retains
Security closure and final landing judgment under the operator's standing
execution delegation; Gary authors and the delegated human reviews/merges.
This is not an independent external attestation or a guarantee of recovery from
unavailable trusted content, damaged verifiers or recurring hardware faults.

CI caught one test fixture reading the local installed policy. The corrected
fixture supplies its own temporary policy; all 31 affected cases pass with an
absent ambient installation. Production recovery code is unchanged by this
correction. Required exact-head CI must pass before source merge.


## Final source binding

Platform PR376 merged as `56d9097edd7da6a9b4a6a72388386b793ae5b290`, tree
`1567fbce22e74f6bab9af92d98d5aed1957b0e67`, identical to the reviewed Gary
candidate. Final required CI and delegated approval pass. The finite composed
YAML and matching prose bind this exact merged source; generated Security record
indexing follows the owner merge. Commissioning and native recovery remain
separate operating evidence.

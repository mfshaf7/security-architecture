# Clean program-cache rereads before image replacement

## Summary

- Date: 2026-11-09.
- Classification: operator-authorized Platform recovery maintenance outside ART.
- Landing Unit Decision: `feature_single_landing_unit`,
  `runtime-cache-readback-acceptance-20261109`.
- Decision: approved for source landing after required checks; installation
  requires the exact merged source in the existing composed acceptance decision.

This extends the [interrupted recovery review](2026-11-09-runtime-recovery-correctness.md).
The pending editor batch is excluded.

## Scope Delta

Platform candidate `d439c6f0e2a5e6647ed9d0d69c8a55a8707d2f44`, tree
`6338b3cce0b282544dea15419529d7087c67274d`, adds a bounded reread before
the existing verifier spends an image-replacement attempt.

For an immutable regular-file hash mismatch, regenerate the independently
verified baseline. Request `POSIX_FADV_DONTNEED` through a read-only descriptor
inside the existing read-only image view, then hash the image again. Reject
escaped paths and links. A matching reread must survive a separate fresh native
view before recovery is reported. Advice failure, persistent bad bytes and
recurrence remain corruption; existing archive/attempt guards are not relaxed.

Root receipts retain before/after hash evidence. Reusing a recent confirmation
requires the same boot, helper, policy and image set. The existing idle-checked
maintenance path requests its retained supervisor after proven cache recovery;
it does not replace the image for that case.

## Review Areas

Runtime/host control: the existing finite root helper remains the only automatic
image checker. Admission stays limited to the same explicit local namespaces and
public repositories. Cache advice uses no write descriptor, sync, direct host
snapshot path, caller path, new root action or global cache reset. Container
writable layers and persistent volumes remain outside the image view. Unsupported
advice preserves the original verification and recovery boundary.

Delivery: Gary authors; the delegated human reviews and merges. Platform lands
first, followed by the generated Security owner-record index and exact merged
pin/tree in the existing finite decision. Deliberate installation and native
readiness remain separate from source acceptance. Rollback preserves incidents,
archives, original controller identities and mutable data.

Identity/secrets/AI: no new principal, provider access, credential handling or
model authority. Other composed source pins, durable manifest and worker digest
remain inherited. Only public image path/hash metadata is added to root receipts.

## Validation And Operating Evidence

Forty-three focused integrity/archive/consumer tests pass, covering read-only
descriptors, fresh trusted bytes, persistent mismatch, unsupported advice,
escaped paths and links, metadata-only differences, recurrence through another
mount, helper/policy proof identity and idle-checked supervisor resumption.
Full local CI-equivalent and required exact-head provider checks precede merge.

Manual native diagnostics found two previously verified program files reading
incorrect hashes. Python and an independent checksum tool agreed on the wrong
reads. Targeted advice restored reads temporarily; some later views/processes
again read incorrect bytes. A separately inspected one-time clean page-cache
reset restored both trusted hashes in a new process without program-file
replacement. That reset is operator maintenance, not an automatic capability
added by this candidate. The candidate explicitly refuses to call a recurring
fresh-view mismatch recovered.

The isolated same-image Ruby probe compiled 3,321 application files and completed
276 collections with no credentials or data mounts; its Pod was removed. This
does not establish Rails startup or hardware reliability. Manual recovery and
source tests are not an automatic fault-recovery witness. Installation and fresh
complete-runtime proof remain commissioning obligations.

## Decision

Approved within the existing local dev-integration verifier boundary after exact
checks and merged-source binding. No new finding, waiver, ART item, global cache
policy or physical-memory control is introduced. Main agent retains Security
closure and final landing judgment under standing operator delegation; this is
not an independent external attestation or a guarantee against recurring memory
faults.


## Final Source Binding

Platform PR378 merged as `9a62f4789e8bc9d43206c04e9e1bf2d5e1aeca9d`, tree
`6338b3cce0b282544dea15419529d7087c67274d`, identical to the reviewed Gary candidate.
Full post-commit local `make validate`, 43 focused tests, required exact-head
provider checks and delegated approval pass. The existing composed decision and
prose bind this exact merged source. Installation and current operating readiness
remain separate commissioning obligations.

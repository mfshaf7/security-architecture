# Interrupted runtime recovery correctness

## Summary

- Date: 2026-11-09.
- Classification: operator-authorized Platform maintenance outside ART.
- Landing Unit Decision: `feature_single_landing_unit`,
  `runtime-recovery-acceptance-20261109`.
- Decision: approved for source landing; commissioning requires the exact merged
  Platform source in the existing composed acceptance decision.

This extends the [verified archive recovery review](2026-11-08-image-recovery-archives.md).
It repairs interrupted recovery within the existing finite root-helper boundary.
The pending Console editor batch is excluded.

## Scope Delta

Reviewed Platform candidate `8e630ca7629dcabba756cb4df66d261125120c12`, tree
`560b5cae97a38fdabb362fe80d4782ed4c6113ed`.

Image restoration supplies the admitted repository as the native import base
name, preventing generated temporary repository identities. Existing historical
CRI aliases require inspected operator recovery, never Pod-status rewriting.
Every unresolved incident retains its exact admitted digest in verification,
including when another digest of the same repository is present. Missing-image
restoration still requires its matching trusted archive and incident phase;
uncertain imports are not replayed.

Maintenance retains pending recovery journals, original consumer identities and
evidence rather than replacing them with an unrelated runtime-fault record.
Pre-boot verifier views are reclaimed only under the existing exclusive helper
lock, with the reserved root-state path, exact snapshot lease label, a valid
admitted baseline chain, both creation times before boot, an unmounted View
snapshot and safe empty directory custody. Current, mounted, foreign, mutable,
nonempty and unsafe paths remain excluded. Removal uses exact native identities
and empty-directory removal; no recursive deletion is introduced.

## Review Areas

Runtime/host control: only the existing root-installed finite helper performs
image-cache and verifier-view operations. No caller-supplied command, path,
namespace or image is accepted. Native container writable layers, persistent
volumes and business data remain outside its scope. This is not an automatic
program-file overwrite API or an expansion into stage/production recovery.

Identity/secrets/AI: no credential, provider or model privilege changes. Public
image archives retain their existing root custody. Models and the Console gain
no root-helper access. The original identity, secrets, delivery and AI acceptance
is inherited without expanding those authorities.

Delivery: Platform source merges first; the dependent generated Security record
index and exact merged-source decision follow before deliberate installation.
Gary authors implementation; delegated human review/merge remains distinct.
Rollback restores the prior accepted source/helper while preserving incidents,
archives, original consumer evidence and mutable data.

## Validation And Operating Evidence

All 36 focused integrity/archive/consumer tests pass on the current boot. They
cover pending-journal retention, same-repository missing-image coverage,
uncertain-import refusal, canonical import arguments and denial of current,
mounted, active, foreign, symlink, nonempty and unsafe verifier views.

A real exact PostgreSQL archive was descriptor-verified and imported without
unpacking into a separate native metadata namespace. It produced only the
canonical admitted name; the temporary namespace was removed. This proves
native import naming, not automatic production fault recovery. Full owner
validation and exact-head provider checks are required before merge.

Manual repairs and native crashes are retained in operator-private evidence.
These source tests do not establish hardware reliability, successful startup or
fully automatic recovery from every outage. Those remain separate live proofs.

## Decision

Approved within the existing local dev-integration recovery boundary after
required checks and exact merged-source binding. Main agent retains Security
closure and final landing judgment under standing operator delegation. This is
not an independent external attestation. No new finding, waiver, ART item,
unbounded retry or hardware-reliability claim is introduced.


## Final Source Binding

Platform PR377 merged as `4f6061a18038f008ea2edca010b73d2979c1793c`, tree
`560b5cae97a38fdabb362fe80d4782ed4c6113ed`, identical to the reviewed Gary candidate.
Full local `make validate` and post-commit focused/base/chart/release checks pass,
as do required exact-head GitHub checks and delegated approval. The existing
composed YAML and matching prose bind this exact merged source. The generated
Security record index includes its owner record. Installation and current-boot
consumer readiness are separate commissioning obligations.

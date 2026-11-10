# Verified release of runtime check failures

## Summary

- Date: 2026-11-10.
- Classification: operator-authorized Platform recovery maintenance outside ART.
- Landing Unit Decision: `child_isolated_landing_unit`,
  `runtime-latch-acceptance-20261110`; separate Security review and activation
  authority follows the Platform source landing.
- Decision: approved within the bounded source and operating obligations below.

This delta extends [interrupted recovery correctness](2026-11-09-runtime-recovery-correctness.md).
It addresses the inspected case where fresh healthy images could not release a
retained verification failure. Shared project-runtime feature implementation,
automatic K3s restarts and hardware reliability are excluded.

## Scope Delta

Platform records eligibility only for a failed image check entered from a healthy
recovery journal. The existing startup and maintenance timer share one durable
verification attempt per boot, saved before checking under the exclusive owner
guard. A busy owner or pending Helm operation defers without losing the journal
or spending the attempt. A successful earlier attempt does not reset the budget
or authorize release of a later unrelated failure. Legacy error text is not
interpreted as permission.

The exact root checker now projects pending repair phases separately from byte
health. Automatic resumption requires fresh same-boot, exact accepted-helper and
policy proof, nonempty complete image coverage, zero corruptions and no pending
repair. This only resumes existing readiness checks. It cannot call repair,
repeat imports, quiesce consumers, reset repair guards, change namespaces or
restart the cluster. The root check's existing inspection-view cleanup and
proven absent-alias reconciliation remain inherited behavior, not a new action.

An incomplete or uncertain repair, missing evidence, frontend failure, unsafe
custody, unknown legacy latch, stale helper/policy or corrupt image remains
blocked. The policy can disable automatic verification resumption. Original
consumer identities, replacement guards and failure/recheck proof remain in
private custody. Normal owner bindings, frontend checks and root consumer
confirmation still gate the completed recovery.

## Review Areas

Runtime/host: no new root action or caller-controlled path, image, command or
namespace is admitted. Verification uses the root-installed finite checker and
its existing exclusive lock. Mutable data, credentials, writable container
layers and unique source remain outside image recovery authority.

Delivery: Gary authors implementation; delegated mfshaf7 reviews and merges
exact checked source. Platform lands first, then this dependent review/index and
the paired composed acceptance bind the exact Platform commit and tree. Deliberate
helper installation and native qualification follow acceptance, never precede it.
Rollback preserves journals, archives and application data while restoring the
prior accepted source/helper/policy or disabling the reviewed resume flag.

Identity/secrets/AI inherit the existing composed boundary unchanged. The Console,
models and browser receive no new recovery authority. The main agent retains
Security closure and final landing judgment under standing delegation; this
review is not independent external attestation.

## Validation And Operating Obligations

Reviewed Gary Platform candidate `21f6768d6be4d503cc881aa69daca8b779bcc95f`, tree
`fab6bf61fe38668665639af2951292e6ba157c3e`. All 57 focused recovery, image-integrity
and archive tests pass. This candidate reference is source-review evidence;
runtime acceptance still requires its actual merged commit and identical tree.

Focused tests exercise corrupt/stale/incomplete proof, root repair phases,
policy disable, owner contention, failure provenance, persistent per-boot guards,
retained-supervisor routing and confirmation-gated readiness. Full local owner
CI-equivalent checks, exact-head hosted checks and delegated approval are required
before merge. The exact candidate and merged tree binding are recorded below
after verification; no unlanded source is accepted for runtime installation.

Controlled native qualification must make the verifier temporarily unavailable
without corrupting an image or business data, then let the existing timer and
supervisor perform recheck and readiness without manual journal release. Retain
that evidence privately and require a fresh core-online receipt. This does not
claim proof of a real power outage, a hardware fault or all possible corruption.

## Decision

Approved for the described local dev-integration boundary after exact source
binding, validation and owner evidence. No finding, waiver, ART item, new daemon
or privileged cluster restart is introduced. Uncertain repairs remain subject
to explicit operator inspection.

## Final Source Binding

Platform PR380 merged as `a86088fdd6b0c323b21a23a7fd51f63bbf374b16`, tree
`fab6bf61fe38668665639af2951292e6ba157c3e`, identical to the reviewed Gary candidate.
All 57 focused tests, 72 owner Makefile validation commands, four Helm renders
and stage/prod release checks pass locally. Required hosted validate and
repo-posture checks pass; delegated mfshaf7 approval covers the exact Gary head.
The paired composed YAML, matching current Markdown source list and generated
owner-record index carry this accepted source. Native installation/recovery
qualification remains separate operating evidence.

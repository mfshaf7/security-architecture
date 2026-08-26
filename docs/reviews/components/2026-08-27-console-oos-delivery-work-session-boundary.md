# Console To OOS Delivery Work-Session Boundary Review

## Summary

- date: 2026-08-27
- owner repo: `security-architecture`
- delivery ref: `openproject://work_packages/1025`
- governing architecture:
  `wgcf://artifacts/delivery-art/sha256/09618912836c6ce253fabdac4f7944736efed0b22d61676a2ca04dc6f76b0927`
- reviewed source:
  - Operator Orchestration Service:
    `operator-orchestration-service@f311d74028ffa2d31ed428eb4d1001f462102493`
  - Governance Operations Console reviewed head:
    `governance-operations-console@da7e6d2686f308534afd4abf1bef4530845ab994`
  - Governance Operations Console merged revision:
    `governance-operations-console@6b87c5c56f450d803a7e17108d53425523799e61`
- OOS finalized Review Packet:
  `wgcf://artifacts/delivery-art/sha256/60396fe620cd6291ab28ffe9db5e7ba2a91d660d951f9afa4664c9dea93809c7`
- Console finalized Review Packet:
  `wgcf://artifacts/delivery-art/sha256/9ae05df7ced78a6fdf3f255054665a687c4f1634dcb529bc0fcfaf34cba2eb02`
- decision: `approved-with-findings`

The OOS work-session API source is acceptable as an inactive, caller-bound
workflow boundary. It exposes OOS-owned session semantics without giving the
browser Git authority, source-execution authority, OpenProject credentials, or
the ability to fabricate progress, receipts, or completion.

The Console adapter has now landed at the exact reviewed head and merged
revision above. This decision permits ART `#1027` to run a bounded
`dev-integration` commissioning exercise for the source executor and composed
path. It does not permit normal mutable operator availability. That remains
blocked until the executor identity, admitted roots, typed actions, positive
and negative proof, teardown, and resulting evidence have been reviewed.

## Scope Delta

### Design Intent

- keep the Console as the normal operator interaction and presentation layer;
- keep work-session semantics, validation, exact next action, coordination
  state, command receipts, and ART mutation in OOS;
- keep source observations and source actions behind one explicit executor;
- keep OOS caller credentials and operator attribution server-side;
- reject stale, replayed, conflicting, unauthorized, unavailable, or
  incomplete execution without projecting success; and
- add no Console workflow database, browser Git client, generic command API, or
  second execution engine.

### Implemented Control

The reviewed OOS source provides:

- versioned read, start, continue, and close routes;
- caller-specific credential enforcement for every work-session route;
- operator-to-caller binding for existing sessions and start decisions;
- exact expected-session revisions and stale-write rejection;
- deterministic command identities, request digests, per-command replay, and
  per-work-item mutation serialization;
- durable terminal command receipts and explicit reconciliation when a prior
  command has no terminal outcome;
- browser-safe next-action projections that remove host commands; and
- an unconfigured runtime boundary that returns `503` because the shared OOS
  runtime does not yet instantiate a source executor.

The reviewed Console source provides:

- same-origin read, start, and continue routes that keep OOS credentials,
  caller identity, and operator attribution server-side;
- strict work-session projection and receipt validation before returning data
  to the browser;
- stable command identities and exact expected-session revisions;
- reconstruction of the accepted start decision from a fresh caller-bound OOS
  draft rather than browser-supplied decision authority;
- explicit disconnected-preview behavior only when OOS is unconfigured; and
- fail-closed configured-live behavior that never converts OOS or executor
  failure into local success.

### Operating Evidence

The OOS and Console Review Packets prove both source revisions, local contract
behavior, and a contract-faithful sandbox composition of the same-origin
Console routes with the OOS work-session API. The Console repository check also
passed for the reviewed head in GitHub Actions run `33004113670`.

No admitted source-executor identity, source mount, typed source action, or
shared-runtime end-to-end proof exists yet. The sandbox proof is implementation
evidence, not operating evidence for normal mutable use.

## Review Areas

### Identity And Authorization

The source-level caller and operator binding is acceptable for the next local
implementation slice. The Console server must use a caller-specific credential
for `governance-operations-console`; a shared fallback credential is not
acceptable for work-session routes. The browser must not choose or receive the
caller id, caller credential, executor id, or operator authority.

Activation must prove distinct and attributable Console, OOS, operator, and
source-executor identities. Synthetic operator attribution remains local
`dev-integration` evidence only and cannot support stage or production claims.

### Secrets

No new runtime secret path is approved here. The Console caller credential and
any source-executor credential must use the admitted Platform-owned secret
projection path, remain absent from browser responses, source, receipts,
status projections, and logs, and be scoped to the exact consumer.

The source executor must not inherit OOS backend credentials or expose GitHub,
OpenProject, WGCF, or provider credentials to the Console.

### Delivery And Source Authority

The browser and Console server are not source authorities. The source executor
must bind every observation or action to the exact owner repo, admitted source
root, Landing Unit, branch, base revision, head revision, worktree, work item,
session, operator, and command id. It must expose typed actions only; an
arbitrary shell or client-selected executable endpoint is prohibited.

Repository paths require canonical-path validation and an explicit allowlist.
The executor may receive only the source roots needed by the active session.
A broad workspace mount or caller-selected path is not approved by this
review.

### Runtime, Audit, And Recovery

Unavailable or unadmitted executor state must remain `503` and must never fall
back to fixture success. Every command needs an audit event binding caller,
operator, work item, session, action, command id, expected revision, source
revision, result, and receipt reference without secret or raw source content.

Retry must reuse the original command identity. Conflicting reuse, stale
revision, caller substitution, source substitution, missing terminal receipt,
or post-action receipt failure must stop automatic progress and expose an
operator reconciliation state. Rollback must disable new executor actions
while preserving ART, Git, Review Packet, readiness, denial, and failure
evidence.

### AI And Agentic Influence

An advisor or model may explain state or draft operator input, but it must not
become the authenticated caller, choose the executor, submit a mutation without
the accountable operator action, or supply source observations. Authorization,
revision checks, action validation, and completion remain deterministic OOS and
owner-executor controls outside the model.

## Findings And Activation Gates

1. **The admitted source executor does not yet exist in the shared runtime.**
   ART `#1027` may commission the executor under a bounded proof scope. It must
   prove the exact identity, allowlisted source roots, typed action surface,
   least-privileged filesystem and network access, audit projection, recovery
   behavior, negative cases, and runtime teardown before normal availability is
   considered.
2. **Composed operating evidence is still absent.** Security Architecture must
   accept the positive and negative `#1027` evidence against the exact merged
   OOS and Console revisions before normal mutable operator use. A changed
   executor shape, credential projection, source mount, or action surface
   requires fresh delta evaluation.
3. **Authenticated human identity is not present.** Local synthetic attribution
   is acceptable only for bounded `dev-integration`; stage or production use
   remains outside this decision.

These findings do not block the controlled commissioning actions required to
produce `#1027` evidence. They do block normal mutable runtime availability and
any claim that the end-to-end execution path is already operating-ready.

## Decision

`approved-with-findings`

Approved:

- the exact OOS source-level work-session API at the reviewed revision;
- the exact merged Console same-origin adapter at the reviewed revision;
- the Console-to-OOS and OOS-to-source-executor architecture;
- the sandbox composition evidence already finalized for ART `#1026`; and
- a bounded ART `#1027` commissioning exercise needed to produce executor and
  composed-runtime evidence.

Not approved:

- normal mutable `dev-integration` availability outside the bounded `#1027`
  commissioning exercise;
- a browser-held OOS credential, browser-derived Git or completion truth, or
  direct browser access to OOS, OpenProject, WGCF, Git, or the executor;
- shared caller credentials for work-session routes;
- arbitrary shell execution, caller-selected source paths, or broad workspace
  access;
- fixture fallback in configured live mode;
- model-direct action or completion;
- stage, production, external, or multi-user operation; or
- treating source or sandbox proof as shared-runtime operating evidence.

Security Architecture retains normal-availability judgment. ART `#1027` may
temporarily exercise the mutable path only within the controlled commissioning
scope needed to satisfy the gates above. It must fail closed and tear down that
path if the evidence is incomplete or a negative case fails.

## Related Artifacts

- [Security delta review process](../security-delta-review-process.md)
- [Governed agent action boundary](2026-08-24-governed-agent-action-boundary.md)
- [Work Design composition boundary](2026-08-25-work-design-dev-integration-composition-boundary.md)
- [OOS work-session API change record](https://github.com/mfshaf7/operator-orchestration-service/blob/f311d74028ffa2d31ed428eb4d1001f462102493/docs/records/change-records/2026-08-27-delivery-work-session-api.md)
- [Console pull request #9](https://github.com/mfshaf7/governance-operations-console/pull/9)
- [Console security and data boundaries](https://github.com/mfshaf7/governance-operations-console/blob/6b87c5c56f450d803a7e17108d53425523799e61/docs/security-and-data-boundaries.md)

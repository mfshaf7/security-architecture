# Governance Operations Console Proposal Live Integration Security Delta

## Summary

- date: 2026-08-16
- owner repo: `security-architecture`
- affected review subject: `repos.governance-operations-console`
- delivery initiative: `openproject://work_packages/417`
- security evidence item: `openproject://work_packages/860`
- architecture packet:
  `wgcf://artifacts/delivery-art/sha256/8fa47a1cbf57df40fbbac6839781cbd3d0cd9721439d7864e9421308af993957`
- review trigger: `governance-console-live-integration`
- decision: `approved-with-findings`

This review approves the exact merged source for the first OOS-backed Proposal
integration in the Governance Operations Console. Approval is limited to a
single-operator, loopback `dev-integration` rehearsal. It does not approve a
shared Console runtime, trusted human identity, stage or production exposure,
or application of a prepared handoff to Delivery or Prototype.

### Exact Source Binding

| Owner | Pull request | Merged source | Reviewed evidence |
| --- | --- | --- | --- |
| Platform Engineering | [platform-engineering#212](https://github.com/mfshaf7/platform-engineering/pull/212) | [`2d8c4817869a4ced2f996c1736da4fb23b8b7904`](https://github.com/mfshaf7/platform-engineering/commit/2d8c4817869a4ced2f996c1736da4fb23b8b7904) | `docs/records/change-records/2026-08-16-openproject-proposal-workflow-state.md` |
| Operator Orchestration Service | [operator-orchestration-service#133](https://github.com/mfshaf7/operator-orchestration-service/pull/133) | [`abedd463074246c0342ed5544cb26152075c7277`](https://github.com/mfshaf7/operator-orchestration-service/commit/abedd463074246c0342ed5544cb26152075c7277) | `docs/records/change-records/2026-08-16-proposal-workflow-live-api.md` |
| Governance Operations Console | [governance-operations-console#4](https://github.com/mfshaf7/governance-operations-console/pull/4) | [`b51e255291805d50917711195458e03ffc7ef571`](https://github.com/mfshaf7/governance-operations-console/commit/b51e255291805d50917711195458e03ffc7ef571) | `docs/product/proposal-live-integration.md` and `docs/security-and-data-boundaries.md` |

The merge order is Platform, OOS, then Console. This Security Architecture
change is the final source Landing Unit before the separate live operating
proof in work item `#861`. A missing commit, a commit not reachable from the
owner repository's `origin/main`, a reordered dependency, or a stale generated
security index prevents this review from serving as readiness evidence.

## Scope Delta

### Design Intent

- Keep Workspace Proposals as canonical record and history authority.
- Put Proposal command policy and OpenProject mutation behind authenticated,
  bounded OOS APIs.
- Keep the OOS caller credential and fixed machine attribution on the Console
  server; the browser uses same-origin Console routes only.
- Use expected record versions and deterministic command identifiers to reject
  stale writes and make accepted retries idempotent.
- Make backend unavailability visible and disable mutation instead of silently
  falling back to fixtures.
- Stop the first integration tranche at a prepared handoff. Target application
  remains unavailable until a target-owned adapter and receipt exist.

### Implemented Control

The exact reviewed source implements these controls:

- Platform provisions one optional, non-searchable, non-filterable Proposal
  workflow-state field bounded to 32,768 characters and validated against a
  versioned JSON Schema before OOS writes it.
- OOS exposes authenticated Proposal projection, command, event, and history
  routes. Commands bind the requested Proposal, authenticated caller,
  operator identifier, expected record reference, lock version, source status,
  command identifier, and declared mutation authority.
- OOS rejects caller/operator mismatch, stale source state, conflicting command
  reuse, invalid state, malformed records, and history beyond its bounded scan.
- OOS persists state through the OpenProject lock version and records structured
  events as comments attributed to the admitted automation user. History reads
  ignore comments not authored by that identity and validate every decoded
  event before returning it.
- The Console sends OOS credentials only from its server adapter. The browser
  receives no caller secret and never calls OpenProject directly.
- The Console limits the first list projection to 25 records, uses an eight
  second OOS timeout, refreshes every 15 seconds only while visible, and uses
  `no-store` responses.
- Configured OOS failure yields an offline live projection and disabled writes.
  Synthetic fixtures are used only when live mode is explicitly unconfigured.
- Handoff records a prepared packet only. The implementation cannot claim that
  Delivery or Prototype accepted or applied the work.

### Operating Evidence

Available evidence is source, build, and owner-lane evidence:

- Platform PR `#212`, OOS PR `#133`, and Console PR `#4` are merged in the
  required order at the exact commits above.
- Platform proved field provisioning, schema-valid round trip in a rolled-back
  transaction, rejection of oversized data, and no mutation of existing
  Proposal records.
- OOS passed its contract, OpenAPI, mutation, runtime-image, and workflow tests,
  including optimistic concurrency, replay, caller binding, author-filtered
  history, and prepared-handoff behavior.
- Console passed repository validation, architecture guards, 333 semantic
  tests, TypeScript, production build, and production dependency audit.
- The generated security change-record index includes the merged OOS Proposal
  API change record and is regenerated only after the three owner Landing Units
  above are present locally at their merged revisions.

This is not end-to-end operating evidence. Work item `#861` must prove the
configured Console-to-OOS-to-OpenProject path and its negative cases before the
Feature can close.

## Review Areas

### Identity

The OOS caller is a machine identity. For the first rehearsal,
`GOVERNANCE_CONSOLE_OPERATOR_ID` must equal the effective `OOS_CALLER_ID`
because OOS rejects command operator attribution that differs from the
authenticated caller. This provides machine attribution, not trusted human
identity.

The Console's same-origin mutation routes still have no authenticated human
session or server-side human authorization. Existing finding `GOC-SEC-02`
therefore remains an expansion gate. The reviewed path is acceptable only on a
controlled single-operator loopback runtime. Shared or multi-user exposure is
blocked until trusted identity, session, authorization, and operator
attribution are separately reviewed.

### Secrets

`OOS_CALLER_SECRET` is a new runtime credential. It must be injected into the
Console server by the admitted runtime owner, mapped to the exact OOS caller,
and excluded from source, browser bundles, `NEXT_PUBLIC_*` variables, logs,
fixtures, and Review Packet payloads. The Console source satisfies the
server-only boundary; work item `#861` must prove runtime delivery without
revealing the value.

This review does not approve a new long-lived secret store, shared secret
distribution path, or production rotation policy.

### Delivery

The source dependency order is complete and reviewable. Security Architecture
does not own the Platform field, OOS command implementation, Console adapter,
or live runtime. This review binds those merged owner revisions and preserves
independent rollback:

1. disable the Console live configuration;
2. revert the Console adapter Landing Unit if needed;
3. revert OOS Proposal routes after consumers stop using them; and
4. remove the optional Platform field only through Platform-owned rollback.

Prepared handoffs remain inert during rollback because no target application
adapter is approved in this tranche.

### Runtime

The approved runtime boundary is local `dev-integration` and loopback Console
access. No ingress, shared endpoint, stage, production, or public application
route is approved. Backend timeout, stale-version rejection, repository gate,
duplicate command, and target unavailability must remain bounded and visible.

The fixed polling model is adequate for this first local slice. It is not a
general realtime or high-volume design, and it must be reevaluated before the
record volume, user count, or exposure boundary expands.

### Visibility And Audit

Canonical Proposal state and OOS-authored events are durable in OpenProject.
OOS receipts bind command, proposal, accepted version, event, and owner. The
Console presents this backend state but is not evidence authority.

OOS stdout audit remains operational telemetry rather than durable history.
The existing browser-memory Console agent finding `GOC-SEC-04` is unaffected
and does not become Proposal workflow evidence.

### AI

The Proposal integration adds no model call, tool invocation, or AI decision
path. Existing Console AI finding `GOC-SEC-01` remains unchanged and outside
this approval.

## Findings And Gates

No new remediation-register finding is required for this bounded source
landing. The following existing expansion gates remain active:

1. `GOC-SEC-01`: local Ollama is not a governed AI access path.
2. `GOC-SEC-02`: the Console has no trusted human identity or server-side human
   authorization.
3. `GOC-SEC-03`: local host readiness metadata is not approved for shared
   exposure.
4. `GOC-SEC-04`: browser-memory agent evidence is not a durable audit trail.

Work item `#861` is the required follow-up for operating evidence. It must prove
the positive flow and bounded failures without weakening these gates or
claiming target application.

## Decision

`approved-with-findings`

Approval is limited to:

- the exact Platform, OOS, and Console merged commits in this review
- local `dev-integration` and loopback Console use
- one admitted OOS machine caller whose configured operator ID matches it
- server-only OOS credential delivery
- canonical Proposal read, capture, triage, disposition, history, and prepared
  handoff
- explicit refresh and bounded polling
- source, build, and owner-lane validation already recorded

Approval excludes:

- shared, client-visible, stage, production, or public runtime exposure
- trusted human identity, session, or authorization claims
- browser access to OOS credentials or direct OpenProject access
- AI-driven Proposal decisions or actions
- application of work to Delivery or Prototype
- any claim that the end-to-end live path is operating before `#861` closes

## Related Artifacts

- [Source-graduation review](2026-07-31-governance-operations-console-source-graduation.md)
- [Owner-repository admission review](2026-07-31-governance-operations-console-owner-repository-admission.md)
- [Baseline security delta](2026-07-30-governance-operations-console-baseline-security-delta.md)
- [Security delta review process](../security-delta-review-process.md)
- [Security review checklist](../security-review-checklist.md)

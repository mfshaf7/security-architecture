# Proposal-To-Delivery Application Security Delta

## Summary

- date: 2026-08-21
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.governance-operations-console`
  - `repos.operator-orchestration-service`
  - `components.operator-orchestration-service`
- delivery initiative: `openproject://work_packages/868`
- security evidence item: `openproject://work_packages/878`
- runtime evidence item: `openproject://work_packages/877`
- architecture packet:
  `wgcf://artifacts/delivery-art/sha256/1b830e9400a020e3c0465927475b210aacee886e993a1072d20645f7af4236e4`
- review triggers:
  - `governance-console-live-integration`
  - `broker-runtime-and-caller-surface`
  - `openproject-delivery-adapter-and-api`
- decision: `approved-with-findings`

This review approves the exact Proposal-to-Delivery application boundary listed
below for single-operator, loopback `dev-integration`. The Console may submit an
explicit application request through its same-origin server route, and OOS may
create or reuse one canonical top-level Delivery Epic and record the resulting
Proposal backlink and receipt.

The approval does not authorize shared Console access, trusted human identity,
stage or production exposure, Prototype application, or deeper Delivery work
decomposition.

### Exact Source And Evidence Binding

| Owner | Pull request or evidence | Exact revision or digest |
| --- | --- | --- |
| Operator Orchestration Service | [OOS PR #137](https://github.com/mfshaf7/operator-orchestration-service/pull/137) | [`c28c110807dfc953d360141d3ddc194de6ce8981`](https://github.com/mfshaf7/operator-orchestration-service/commit/c28c110807dfc953d360141d3ddc194de6ce8981) |
| Governance Operations Console | [Console PR #5](https://github.com/mfshaf7/governance-operations-console/pull/5) | [`f43488e6005b8c1d692d9a8f9fab235834e4daa5`](https://github.com/mfshaf7/governance-operations-console/commit/f43488e6005b8c1d692d9a8f9fab235834e4daa5) |
| Platform Engineering | `openproject://work_packages/877`, attachment `delivery-868-877-devint-proof.json` | source revision [`0eb98626f326a7b379743871eea27f8a4f2368f6`](https://github.com/mfshaf7/platform-engineering/commit/0eb98626f326a7b379743871eea27f8a4f2368f6); evidence digest `sha256:f77faf45b3f0ebd6ee01ba41a2c19288d7ab57f266c451592a2432f066246fd3` |

The required landing order was OOS, Console, runtime proof, then Security
Architecture. This review is not reusable for different source revisions or a
broader runtime boundary without a fresh delta decision.

## Scope Delta

The [2026-08-16 Proposal live-integration review](2026-08-16-governance-operations-console-proposal-live-integration.md)
approved canonical Proposal reads and versioned workflow commands but
explicitly excluded target application. This delta reviews the newly activated
target mutation and closes only that earlier exclusion for local
`dev-integration`.

### Design Intent

- Keep the browser on same-origin Console routes and keep OOS credentials on
  the Console server.
- Keep OOS as the sole Proposal application and OpenProject mutation authority.
- Bind an application to the accepted Proposal, expected source version,
  prepared handoff packet, Delivery route, operator attribution, and stable
  application identity.
- Create or reuse only one top-level Delivery Epic; Delivery intake and work
  design own later execution decomposition.
- Treat target creation as durable even if a later source-state write or
  response fails. Retry must recover by backlink and must not delete or
  duplicate the target.
- Report completion only from canonical applied state with a target record and
  target receipt.

### Implemented Control

The exact reviewed source implements these controls:

- The browser calls the Console's same-origin
  `POST /api/proposals/{proposalId}/handoff/apply` route. The route delegates to
  server-only code; neither the OOS caller secret nor OpenProject authority is
  exposed to client code.
- The Console derives one stable application ID from the canonical numeric
  Proposal identity and sends the accepted source status, record reference,
  record version, and prepared packet reference to OOS.
- OOS authenticates the admitted machine caller, validates the accepted source
  version and Delivery route, enforces the repository gate, and owns all target
  creation or reuse.
- OOS binds the application receipt to source and target references, persists
  the Delivery backlink, and projects `applied` only with complete target
  evidence.
- Replays return the same target and receipt. Stale source, unresolved
  repository custody, invalid caller, target outage, and inconsistent target
  evidence fail closed.
- Partial success is repaired by reading the durable backlink and completing
  source state. The implementation does not compensate by deleting a valid
  Delivery target.
- The Console refreshes canonical state after success or failure and does not
  synthesize optimistic completion.

### Operating Evidence

The disposable `accepted-idea-delivery-mutation-smoke` session bound clean
`main` revisions for OOS, Console, and Platform. It proved:

- target outage returned `502` through the Console route and did not report
  success;
- one accepted Proposal produced one top-level Delivery Epic;
- the Proposal backlink and returned target reference matched;
- canonical handoff state became `applied` with exactly one applied event;
- replay returned `200`, reused the same receipt and target, and kept the
  Delivery target count at one; and
- teardown removed the disposable namespace and backend records while retaining
  the redacted evidence artifact.

The evidence is sufficient for the bounded local decision. It is not governed
stage evidence: the application scenario was captured as a focused run in the
disposable profile rather than as a reusable stage rehearsal.

## Review Areas

### Identity And Authorization

OOS uses a distinct machine caller and rejects mismatched caller/operator
attribution. This is adequate for a controlled single-operator local runtime.

The Console still has no authenticated human session or server-side human
authorization for its same-origin mutation route. Existing finding
`GOC-SEC-02` remains an expansion gate. Loopback placement and a fixed
operator identity are containment, not proof of human authorization.

### Secrets

`OOS_CALLER_SECRET` remains server-only in the reviewed source and was not
present in the redacted runtime evidence. The local profile proves usable
runtime injection, but it does not prove governed stage secret delivery,
rotation, or recovery. Those controls require the Platform-owned secret path
and a fresh review before any shared runtime is admitted.

### Delivery And Runtime

OOS, Console, Platform proof, and Security review remain independent landing
and rollback units. Disabling the Console live configuration or reverting its
adapter stops new requests without requiring deletion of canonical Delivery
records already created. OOS rollback requires consumers to stop using the
application route first.

The approved runtime remains loopback-only `dev-integration`. No ingress,
shared endpoint, stage, production, or public route is approved. A later stage
rehearsal must promote the focused application scenario into a repeatable
profile proof or provide an equivalent governed test with exact image and
manifest binding.

### Visibility And Audit

OpenProject holds the canonical Proposal, Delivery target, backlink, and
workflow events. OOS returns deterministic application receipts, while the ART
holds the redacted runtime evidence and exact source revisions. Console state
is a projection and is not evidence authority.

Browser-memory agent history and process stdout are not substitutes for these
durable records. Existing finding `GOC-SEC-04` remains unchanged.

### AI

This delta adds no model call, AI decision, or tool-execution path. Existing
Console AI finding `GOC-SEC-01` remains outside this approval.

## Findings And Expansion Gates

No new remediation-register entry is required for this bounded local
application. Existing Console findings remain active, and these explicit
expansion gates apply:

1. Shared or multi-user Console exposure requires authenticated human identity,
   session authorization, and attributable operator propagation.
2. Stage or production use requires governed secret delivery and rotation
   evidence for the Console-to-OOS caller.
3. Stage promotion requires repeatable positive and negative application proof
   bound to exact deployed images and rendered manifests.
4. Any broader target shape, including Prototype application or automatic
   Delivery decomposition, requires a new architecture and security delta.

## Decision

`approved-with-findings`

Approval is limited to:

- the exact OOS, Console, and Platform revisions and runtime-evidence digest in
  this review;
- single-operator, loopback `dev-integration`;
- server-only OOS credential handling;
- explicit operator application of one accepted, prepared Proposal handoff;
- OOS-owned creation or reuse of one top-level Delivery Epic;
- deterministic replay, backlink repair, and canonical applied-state evidence;
  and
- the existing repository gate and bounded failure behavior.

Approval excludes:

- shared, client-visible, stage, production, or public runtime exposure;
- trusted human identity, session, or authorization claims;
- browser-held credentials or direct Console-to-OpenProject mutation;
- AI-driven Proposal application;
- Prototype target application;
- automatic Delivery decomposition; and
- reuse of this decision for source or runtime revisions not listed above.

## Related Artifacts

- [Prior Proposal live-integration review](2026-08-16-governance-operations-console-proposal-live-integration.md)
- [Console owner-repository admission](2026-07-31-governance-operations-console-owner-repository-admission.md)
- [OOS Proposal-to-Delivery change record](https://github.com/mfshaf7/operator-orchestration-service/blob/c28c110807dfc953d360141d3ddc194de6ce8981/docs/records/change-records/2026-08-21-proposal-delivery-application.md)
- [Console Proposal integration operator surface](https://github.com/mfshaf7/governance-operations-console/blob/f43488e6005b8c1d692d9a8f9fab235834e4daa5/docs/product/proposal-live-integration.md)
- [Security delta review process](../security-delta-review-process.md)
- [Security review checklist](../security-review-checklist.md)

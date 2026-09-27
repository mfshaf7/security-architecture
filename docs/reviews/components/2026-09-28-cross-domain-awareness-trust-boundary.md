# Cross-Domain Awareness Trust-Boundary Security Delta

## Summary

- date: 2026-09-28
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.workspace-governance`
  - `repos.operator-orchestration-service`
  - `repos.workspace-governance-control-fabric`
  - `repos.governance-operations-console`
- delivery initiative: `openproject://work_packages/900`
- parent feature: `openproject://work_packages/933`
- security evidence item: `openproject://work_packages/1200`
- architecture packet:
  `wgcf://artifacts/delivery-art/sha256/d10853c5d2bfa2a3ee556de42124ad9f1d1b4a1b8a4c165cf44b0b12c25d4067`
- decision: `approved-with-findings`

This review approves the exact merged contract, journal, readiness, history,
and Console-composition revisions listed below for controlled,
single-operator, loopback `dev-integration` activation. It emits
`gate:cross-domain-security-acceptance` for those revisions so Platform
Engineering can perform work item `#1201`.

This decision is source acceptance, not operating proof. The boundary is not
operating-ready until `#1201` proves configured source availability, restart,
rollback, cleanup, and the absence of configured fixture fallback.

### Exact Source Binding

| Owner | Pull request | Merged source | Reviewed evidence |
| --- | --- | --- | --- |
| Workspace Governance | [workspace-governance#197](https://github.com/mfshaf7/workspace-governance/pull/197) | [`62d60d6`](https://github.com/mfshaf7/workspace-governance/commit/62d60d6) | Canonical lifecycle-transition projection contract |
| Workspace Governance | [workspace-governance#198](https://github.com/mfshaf7/workspace-governance/pull/198) | [`5f2d078ede6f67e18ba165739c748d181bd8b8d6`](https://github.com/mfshaf7/workspace-governance/commit/5f2d078ede6f67e18ba165739c748d181bd8b8d6) | Delivery ART evidence profile |
| Operator Orchestration Service | [operator-orchestration-service#241](https://github.com/mfshaf7/operator-orchestration-service/pull/241) | [`72bebb8`](https://github.com/mfshaf7/operator-orchestration-service/commit/72bebb8) | Canonical lifecycle-transition journal |
| Operator Orchestration Service | [operator-orchestration-service#242](https://github.com/mfshaf7/operator-orchestration-service/pull/242) | [`530e50f12e0e059c33902a551b72f000b82cd82e`](https://github.com/mfshaf7/operator-orchestration-service/commit/530e50f12e0e059c33902a551b72f000b82cd82e) | Canonical workflow-activity projection |
| Workspace Governance Control Fabric | [workspace-governance-control-fabric#84](https://github.com/mfshaf7/workspace-governance-control-fabric/pull/84) | [`a5d3e5c`](https://github.com/mfshaf7/workspace-governance-control-fabric/commit/a5d3e5c) | Lifecycle-transition readiness evidence |
| Workspace Governance Control Fabric | [workspace-governance-control-fabric#85](https://github.com/mfshaf7/workspace-governance-control-fabric/pull/85) | [`ca29511`](https://github.com/mfshaf7/workspace-governance-control-fabric/commit/ca29511) | Isolated evidence-acquisition profile |
| Workspace Governance Control Fabric | [workspace-governance-control-fabric#86](https://github.com/mfshaf7/workspace-governance-control-fabric/pull/86) | [`5b5e066`](https://github.com/mfshaf7/workspace-governance-control-fabric/commit/5b5e066) | Owner-evidence operating contract |
| Workspace Governance Control Fabric | [workspace-governance-control-fabric#87](https://github.com/mfshaf7/workspace-governance-control-fabric/pull/87) | [`70eb1f25a56fcda5ed57f3cf79425af8025e8d4f`](https://github.com/mfshaf7/workspace-governance-control-fabric/commit/70eb1f25a56fcda5ed57f3cf79425af8025e8d4f) | Bounded governance-history projection |
| Governance Operations Console | [governance-operations-console#39](https://github.com/mfshaf7/governance-operations-console/pull/39) | [`f70e58f`](https://github.com/mfshaf7/governance-operations-console/commit/f70e58f) | Lifecycle-transition owner projection |
| Governance Operations Console | [governance-operations-console#40](https://github.com/mfshaf7/governance-operations-console/pull/40) | [`20a406f`](https://github.com/mfshaf7/governance-operations-console/commit/20a406f) | Owner-attention composition |
| Governance Operations Console | [governance-operations-console#41](https://github.com/mfshaf7/governance-operations-console/pull/41) | [`a35da32c23af7e2ec530a67d0a04abd70a599cb2`](https://github.com/mfshaf7/governance-operations-console/commit/a35da32c23af7e2ec530a67d0a04abd70a599cb2) | Canonical governance-activity composition |

The Console identity and runtime-operability reviews remain authoritative for
the inherited single-operator loopback runtime. A source revision outside this
table or an expanded runtime boundary requires a new delta review.

## Scope Delta

### Design Intent

- Keep lifecycle state, attention, and activity truth with their canonical
  owners while giving the Console one read-only awareness projection.
- Keep OOS as workflow and journal authority, WGCF as readiness and governance
  history authority, and Workspace Governance as contract authority.
- Keep the Console free of a competing database, raw-artifact store, approval
  authority, or lifecycle mutation authority.
- Expose bounded evidence routes and owner-projected next actions without
  exposing credentials, raw payloads, private paths, or approval internals.
- Make configured missing, malformed, stale, partial, contradictory, or
  truncated source truth explicit and prevent fixture fallback after live
  configuration is selected.

### Implemented Control

OOS exposes caller-bound, read-only lifecycle journal and workflow-activity
projections. WGCF exposes separately authenticated readiness and governance
history projections. The two authorities use distinct server-only caller
credentials and preserve evidence references rather than copying raw evidence
into the Console.

The Console's same-origin server adapters validate both owner schemas, bound
pagination to five pages of one hundred records per source, merge records
deterministically in memory, and reject identity or content conflicts. Source
availability, partial results, staleness, and truncation remain visible. The
browser receives bounded operational metadata and safe evidence references;
it does not receive owner credentials or raw backend diagnostics.

The Console persists none of this projection. It cannot approve, retry,
repair, mutate, or close owner work through these read paths. If either live
source is configured, its failure cannot be replaced with fixture success.
Disconnected preview data remains available only when neither owner source is
configured.

### Operating Evidence

The exact revisions above passed their owner-repository validation and
CI-equivalent landing proof. The Console revision passed architecture checks,
460 semantic tests, TypeScript checking, a production build, repository
validation, and dependency audit. The WGCF revision passed its complete owner
test surface, including governance-history authorization and bounded response
tests. The OOS and Workspace Governance revisions passed their respective
contract, schema, and repository validation surfaces.

This is implemented-control evidence, not final runtime evidence. `#1201`
must prove the exact approved revisions together in configured
`dev-integration`, including live-source selection, restart, rollback, cleanup,
and negative fixture-disconnection behavior.

## Review Areas

### Identity And Authorization

No new human identity or browser authorization mechanism is introduced. The
boundary inherits the approved Console identity posture: one operator,
loopback-only, with the local operating-system account as trust root.

OOS and WGCF use distinct caller identities and secrets. Caller credentials
grant only their documented read projections. Lifecycle mutation, owner
approval, ART state change, and release authority remain outside this
boundary.

### Secrets And Data Handling

Owner endpoints, caller identities, and caller secrets are server-only and
must not enter browser bundles, `NEXT_PUBLIC_*` values, logs, fixtures, ART
descriptions, Review Packets, or exported activity data. Platform owns secure
delivery, rotation, revocation, and cleanup of those runtime values.

Governance activity is allowlisted operational metadata. Raw owner payloads,
private filesystem paths, credentials, approval internals, and unrestricted
artifact contents are excluded. Export remains bounded to the same safe
projection shown in the Console.

### Failure, Freshness, And Partial Truth

Configured owner failure is explicit. Missing, malformed, stale,
contradictory, conflicting, partial, or truncated truth cannot become a
healthy projection and cannot fall back to fixtures. Pagination bounds are a
resource control, and truncation must remain visible rather than silently
dropping records.

The merged view preserves source attribution. A healthy response from one
owner does not conceal failure from the other owner, and a record conflict
fails closed rather than choosing a source opportunistically.

### Evidence, Audit, And Next Actions

Evidence routes remain owner references. They do not prove approval merely by
being present, and the Console does not become an artifact repository.
Owner-projected next actions are advisory routing metadata, not executable
authority. Canonical mutation and completion evidence continues to come from
the owning service and finalized Review Packet.

### Delivery, Rollback, And Availability

Platform may activate only the exact revisions listed above and only after
this decision. `#1201` must prove configured availability, restart behavior,
rollback, cleanup, and fixture disconnection. Rollback must be possible by
removing the Console source configuration and credentials without deleting
OOS journals, WGCF evidence, ART state, or owner records.

No shared, remote, stage, production, or public route is approved. Availability
of the Console view does not prove owner workflow success or release
readiness.

### AI

This delta adds no model call, prompt boundary, AI-selected action, tool
invocation, or AI approval authority. Existing AI-governance findings remain
unchanged.

## Findings And Activation Ceiling

1. **The local operating-system account remains the trust root.** Federated
   identity, shared access, MFA, and remote revocation require separate review.
2. **Credential operations remain a Platform responsibility.** Runtime
   delivery, rotation, revocation, and cleanup must be proven in `#1201`.
3. **The Console is a bounded read model.** It must not gain persistence,
   mutation, approval, or raw-artifact authority through this integration.
4. **Partial and stale truth remains visible.** A healthy owner cannot mask an
   unavailable owner, and configured live mode cannot use fixture fallback.
5. **Operating readiness is still pending.** This source decision permits
   `#1201`; it does not substitute for its exact-revision runtime proof.

These findings are activation limits, not reasons to add another child under
Feature `#933`.

## Decision

`approved-with-findings`

Approved:

- the exact source revisions bound above;
- distinct caller-bound OOS and WGCF read authority;
- bounded lifecycle, attention, readiness, history, and activity projections;
- deterministic in-memory Console composition without a Console database;
- owner evidence references and owner-projected advisory next actions;
- explicit missing, stale, partial, conflicting, and truncated source posture;
- fixture-free behavior after live configuration is selected; and
- controlled, single-operator, loopback `dev-integration` activation proof in
  `#1201`.

Not approved:

- any source revision not bound above;
- shared, remote, multi-user, stage, production, or public exposure;
- exposing credentials, raw owner payloads, private paths, approval internals,
  or unrestricted artifacts to the browser;
- Console persistence, mutation, approval, retry, repair, or closure authority;
- treating owner references or projected next actions as completed evidence;
- fixture fallback after live configuration is selected; or
- claiming operating readiness before `#1201` completes.

## Related Artifacts

- [Console identity activation review](2026-09-27-governance-operations-console-identity-activation.md)
- [Console runtime operability review](2026-09-27-governance-operations-console-runtime-operability.md)
- [Identity and access architecture](../../architecture/domains/identity-and-access.md)
- [Secrets and recovery architecture](../../architecture/domains/secrets-and-recovery.md)
- [GitOps and machine trust architecture](../../architecture/domains/gitops-and-machine-trust.md)
- [Security delta review process](../security-delta-review-process.md)
- [Security review checklist](../security-review-checklist.md)

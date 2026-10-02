# Workspace Intake And Inventory Post-Maintenance Re-Acceptance

## Summary

- date: 2026-10-02
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.platform-engineering`
  - `repos.workspace-governance`
  - `repos.workspace-governance-control-fabric`
  - `repos.operator-orchestration-service`
  - `repos.governance-operations-console`
- predecessor review:
  [`2026-10-02-workspace-intake-inventory-maintenance-reacceptance.md`](2026-10-02-workspace-intake-inventory-maintenance-reacceptance.md)
- maintenance tracking:
  `openproject://work_packages/1210`
- decision: `approved-with-findings`

The predecessor review remains the trust-boundary decision for Workspace Intake
and Inventory. Subsequent merged maintenance advanced three repository heads,
and the runtime correctly refused to combine an older accepted Workspace
Governance authority checkout with current `origin/main`. This delta review
binds the new exact heads after proving that the intervening changes do not
widen the identity, secret, delivery, runtime, or AI boundary.

This review does not claim operating readiness. Platform must pin the merged
revision containing this review and item #1210 must still produce direct,
credential-bound Intake and Inventory operating evidence.

### Exact Source Binding

| Owner | Accepted revision | Delta from predecessor | Security judgment |
| --- | --- | --- | --- |
| Workspace Governance | [`0acb5e4c9a833fba9b49ba0737e15b8e55d57b07`](https://github.com/mfshaf7/workspace-governance/commit/0acb5e4c9a833fba9b49ba0737e15b8e55d57b07) | Work-home routing controls and closed improvement records after the runtime repair. | No Intake/Inventory authority, credential, composition, or write-scope change. |
| Workspace Governance Control Fabric | [`e31688369a3f59c76762b8f9359bd2acc478dcb4`](https://github.com/mfshaf7/workspace-governance-control-fabric/commit/e31688369a3f59c76762b8f9359bd2acc478dcb4) | Unchanged. | Existing readiness boundary remains accepted. |
| Operator Orchestration Service | [`8a401e8a44c568bf858efcf68cfb999ec0712f11`](https://github.com/mfshaf7/operator-orchestration-service/commit/8a401e8a44c568bf858efcf68cfb999ec0712f11) | Owner-maintenance repository identity and base-owned evidence-profile preflight controls. | No Intake/Inventory route, caller, GitHub App, token, path, or runtime-binding change. |
| Governance Operations Console | [`d17912691a6dd99335c327637eda98c4105d98eb`](https://github.com/mfshaf7/governance-operations-console/commit/d17912691a6dd99335c327637eda98c4105d98eb) | Unchanged. | Console remains outside commissioning authority. |
| Platform Engineering | [`5e06285725ab8f35b81bcc8db9b9b69bc50172c8`](https://github.com/mfshaf7/platform-engineering/commit/5e06285725ab8f35b81bcc8db9b9b69bc50172c8) | Current clean control-plane head before the downstream pin update. | The downstream change may update exact revision metadata and operator guidance only; any runtime or identity expansion requires another review. |

The `security-architecture` revision used by Platform must be the eventual
merged commit containing this review. The review cannot name or approve its own
future merge commit before human review and merge occur.

## Scope Delta

### Design Intent

- Preserve the predecessor review and all of its compensating controls.
- Accept only current merged source that has no Intake/Inventory trust-boundary
  delta.
- Keep Workspace Governance `origin/main` as the exact authority checkout; do
  not use an older detached authority revision as a runtime workaround.
- Keep #1210 as the existing operating-proof item and create no replacement
  Defect chain.

### Implemented Control

- Workspace Governance still owns the canonical Intake and Inventory records.
- OOS still enforces the same branch namespaces, allowed paths, authenticated
  callers, exact-head review, and human-only merge boundary.
- WGCF still supplies non-mutating readiness under the same dedicated caller.
- Platform still owns credential custody, source pinning, runtime projection,
  revocation, rollback, and cleanup.
- The Console remains a server-side consumer and cannot establish
  commissioning readiness.

### Operating Evidence

Repository history proves the maintenance deltas and exact current heads. A
live attempt also proved the fail-closed authority rule: the composition
rejected the predecessor Workspace Governance revision because it no longer
matched landed `origin/main`, then rolled back the profiles it had started.

Positive Intake and Inventory status, restart, invalid-caller denial,
revocation, rollback, cleanup, and final activation remain future operating
evidence owned by Platform and #1210.

## Review Areas

### Identity

No identity, App, installation, repository selection, human reviewer, or
permission changes are introduced. Agent Gary remains source author only;
`mfshaf7` remains reviewer and merger.

### Secrets

No secret path, credential class, projection shape, token lifetime, or custody
owner changes. Tokens and private keys remain excluded from source, receipts,
logs, ART text, and model context.

### Delivery

The only delivery change is exact-head rebinding after unrelated merged
maintenance. Protected `main`, exact-head human review, trusted owner checks,
no App bypass, and canonical merged readback remain mandatory.

### Runtime

No service, route, mount, state root, caller binding, namespace, or write scope
changes. Activation remains limited to single-operator loopback
`dev-integration` through `refinement-catalog`.

### AI

No model call, model-selected action, prompt boundary, AI approval, or new tool
authority is introduced.

## Findings And Activation Conditions

1. Platform must land a dependent pin update that references the merged commit
   containing this review and the exact accepted owner revisions above.
2. Platform must rerun its identity validation and focused tests after the pin
   update.
3. Item #1210 must produce capability-specific live evidence; source
   re-acceptance alone is not completion.
4. Any source delta beyond revision metadata and operator guidance requires a
   new review instead of inheriting this decision.

The owner for conditions 1 through 3 is `platform-engineering`. Condition 4 is
enforced jointly by Platform and Security review. No exception or accepted risk
is created.

## Decision

`approved-with-findings`

Approved:

- the exact owner revisions listed above;
- a downstream Platform-only exact-source pin and operator-guidance refresh;
- the existing identity, caller, path, review, merge, revocation, rollback, and
  cleanup controls from the predecessor review; and
- continuation of operating proof under existing item #1210.

Not approved:

- an older detached Workspace Governance authority checkout;
- compatible-but-unbound source revisions;
- any broader identity, repository, path, permission, secret, runtime, Console,
  or AI authority;
- source acceptance presented as operating evidence; or
- replacement ART Defects for the repository, review, activation, or Landing
  Unit steps.

## Related Artifacts

- [Maintenance re-acceptance](2026-10-02-workspace-intake-inventory-maintenance-reacceptance.md)
- [Controlled activation review](2026-10-02-workspace-intake-inventory-controlled-activation.md)
- [Security delta review process](../security-delta-review-process.md)
- [Identity and access architecture](../../architecture/domains/identity-and-access.md)
- [Secrets and recovery architecture](../../architecture/domains/secrets-and-recovery.md)
- [GitOps and machine trust architecture](../../architecture/domains/gitops-and-machine-trust.md)

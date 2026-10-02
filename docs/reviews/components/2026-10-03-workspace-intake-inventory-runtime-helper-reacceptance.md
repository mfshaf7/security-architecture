# Workspace Intake And Inventory Runtime Helper Re-Acceptance

## Summary

- date: 2026-10-03
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.platform-engineering`
  - `repos.workspace-governance`
  - `repos.workspace-governance-control-fabric`
  - `repos.operator-orchestration-service`
  - `repos.governance-operations-console`
- predecessor review:
  [`2026-10-02-workspace-intake-inventory-post-maintenance-reacceptance.md`](2026-10-02-workspace-intake-inventory-post-maintenance-reacceptance.md)
- maintenance tracking:
  `openproject://work_packages/1210`
- decision: `approved-with-findings`

The first direct composed status probe proved that the repository-scoped GitHub
App credential, exact Workspace Governance checkout, runtime mounts, and OOS
caller bindings were present. The Inventory registry still failed closed
because the accepted-delivery init container copied `src/` and `contracts/`
into `/runtime` but omitted the two existing Workspace authority helpers that
the Intake and Inventory source clients resolve from `/runtime/scripts/`.

OOS maintenance PR #261 corrects only that runtime assembly gap and adds a
profile regression assertion. It does not change an API, caller, permission,
credential, repository scope, allowed source path, review rule, merge rule, or
canonical mutation boundary. This review accepts that exact OOS head for a
dependent Platform pin refresh. It does not claim operating readiness; item
#1210 still owns the complete direct runtime proof.

### Exact Source Binding

| Owner | Accepted revision | Delta from predecessor | Security judgment |
| --- | --- | --- | --- |
| Workspace Governance | [`0acb5e4c9a833fba9b49ba0737e15b8e55d57b07`](https://github.com/mfshaf7/workspace-governance/commit/0acb5e4c9a833fba9b49ba0737e15b8e55d57b07) | Unchanged. | Canonical Intake and Inventory authority remains unchanged. |
| Workspace Governance Control Fabric | [`e31688369a3f59c76762b8f9359bd2acc478dcb4`](https://github.com/mfshaf7/workspace-governance-control-fabric/commit/e31688369a3f59c76762b8f9359bd2acc478dcb4) | Unchanged. | Existing non-mutating readiness boundary remains accepted. |
| Operator Orchestration Service | [`342d33bf1607c70a66531ab8143eab4bc05f7993`](https://github.com/mfshaf7/operator-orchestration-service/commit/342d33bf1607c70a66531ab8143eab4bc05f7993) | The broker runtime assembly now copies only `workspace_intake_source.py` and `workspace_inventory_source.py` beside their accepted callers; the profile test requires both paths. | Restores the already-reviewed owner-command seam without widening authority. |
| Governance Operations Console | [`d17912691a6dd99335c327637eda98c4105d98eb`](https://github.com/mfshaf7/governance-operations-console/commit/d17912691a6dd99335c327637eda98c4105d98eb) | Unchanged. | Console remains outside commissioning authority. |
| Platform Engineering | [`b6e0c67fa9f8b32da43e0536a33166f7a86da615`](https://github.com/mfshaf7/platform-engineering/commit/b6e0c67fa9f8b32da43e0536a33166f7a86da615) | Current clean control-plane head before the dependent pin update. | The downstream change may refresh exact OOS and Security revision metadata only. |

The `security-architecture` revision used by Platform must be the eventual
merged commit containing this review. This review cannot pre-authorize its own
future merge commit.

## Scope Delta

### Design Intent

- Preserve the existing dedicated Workspace operations GitHub App and its
  one-repository, short-lived token boundary.
- Restore the runtime-relative helper files that the already-accepted source
  clients require.
- Keep the helpers inside OOS's existing isolated exact-revision source seam;
  they do not become general operator commands or a new control plane.
- Keep #1210 as the only operating-proof work item and create no replacement
  Defect chain.

### Implemented Control

- The init container copies exactly two existing Python helpers into
  `/runtime/scripts/` with non-executable read permissions.
- OOS continues to invoke those helpers only through its bounded Intake and
  Inventory source clients.
- All 1,178 OOS tests completed with 1,176 passes and two intentional skips;
  the seven Intake and eleven Inventory real-Git conformance checks passed.
- The OOS owner change record is indexed as
  `docs/records/change-records/2026-10-03-workspace-authority-runtime-helper-packaging.md`.

### Operating Evidence

The pre-fix live probe is valid negative evidence: it proved fail-closed
behavior and localized the missing runtime dependency without canonical
mutation. Positive status, restart, invalid-caller denial, revocation,
rollback, cleanup, and final activation remain future operating evidence.

## Review Areas

### Identity

No App, installation, owner, repository, permission, caller, reviewer, or merge
identity changes. Agent Gary authored PR #261 and the accountable human reviewed
and merged it.

### Secrets

No private key, Vault path, token lifetime, Secret name, mount, or token-file
path changes. The copied helpers contain no credential value and continue to
consume credentials only through the existing OOS provider client boundary.

### Delivery

The source correction landed through human-reviewed OOS PR #261. Platform must
pin the merged OOS commit and this review's eventual merge commit before the
composition can be reactivated.

### Runtime

The runtime gains only two files that were already part of the accepted OOS
source and required by enabled clients. No deployment, service, namespace,
state root, source mount, network path, or mutation scope changes.

### AI

No model call, prompt boundary, model-selected action, or AI approval authority
is introduced or changed.

## Findings And Activation Conditions

1. Platform must refresh the exact OOS and Security revisions in the Workspace
   operations identity and Console activation policy.
2. Platform must rerun identity validation and its focused runtime composition
   tests after the pin update.
3. Item #1210 must still complete the capability-specific live proof, including
   restart, denial, revocation, rollback, cleanup, and final activation.
4. Any delta beyond the exact helper projection and revision metadata requires
   another review.

No exception or accepted risk is created.

## Decision

`approved-with-findings`

Approved:

- OOS commit `342d33bf1607c70a66531ab8143eab4bc05f7993`;
- the exact two-helper runtime projection in that commit;
- a dependent Platform-only OOS/Security pin refresh; and
- continuation of #1210's direct operating proof.

Not approved:

- copying the whole OOS `scripts/` directory into the broker runtime;
- any broader identity, permission, repository, source-path, runtime, Console,
  or AI authority;
- source reacceptance presented as operating evidence; or
- replacement ART Defects for this repair chain.

## Related Artifacts

- [Post-maintenance re-acceptance](2026-10-02-workspace-intake-inventory-post-maintenance-reacceptance.md)
- [Controlled activation review](2026-10-02-workspace-intake-inventory-controlled-activation.md)
- [Security delta review process](../security-delta-review-process.md)
- [Identity and access architecture](../../architecture/domains/identity-and-access.md)
- [Secrets and recovery architecture](../../architecture/domains/secrets-and-recovery.md)
- [GitOps and machine trust architecture](../../architecture/domains/gitops-and-machine-trust.md)

# PI Planning and Delivery rehearsal security review

## Summary

This review covers the operator-approved planning and Delivery maintenance
batch in the existing working dev-integration composition. The update replaces
the duplicated planning controls with a dated PI calendar and connects the
normal Refinement, PI Planning, and Execution paths.

## Scope Delta

- Platform keeps native version dates with the generated iteration windows in
  the same OpenProject transaction. Existing work-item assignments and legacy
  iteration identities are retained when operators date a historical calendar.
- Broker validates edited work against exact Catalog dates and the accepted
  revision before using the existing OpenProject writer. PI Objective review
  uses authoritative source-session existence when the objective has no repo.
- Cleanup uses the reviewed broker manifest on fresh installations. Closing
  scope, finalized evidence, exact
  source provenance, guarded Git deletion, and recoverable receipts still
  constrain cleanup. The historical approval remains in Workspace Governance.
- Registry reads verified, current Platform snapshots. Setup uses the exact
  independently approved GitHub head and verifies the provider's merged result.
  Private worktrees and source readback stay bound to the owning installation.
- Console uses existing server-only caller routes. Its Next.js patch release
  clears the dependency audit, and replay after a slow response keeps the
  original command identity.

## Review Areas

**Identity and secrets.** The existing Console broker caller, Platform reader,
and separately authorized Gary and human reviewer bindings continue to apply.
The approving human and source author remain distinct. Registry read requests
do not access writer custody. The rehearsal grant was scoped to a separate
public sandbox and revoked after that run.

**Delivery.** Existing owner validation and acceptance remain authoritative.
Both Delivery ingress paths and exact-command replay were exercised in
disposable OpenProject. Review covered source-free completion and locked
History, real GitHub source review and merge in the earlier temporary sandbox,
and local Git checks for the follow-up merge and cleanup repairs. The paired
Planning and Catalog changes retain existing assignments during reconciliation.

**Runtime.** The fresh disposable broker loaded the new manifest without
historical work item #970. The operating composition still requires exact
reviewed sources through the normal complete-runtime path. Keep the previous
accepted composition for rollback. Dating historical PIs and updating existing
business work require their own operator decisions.

**AI.** This release preserves the existing model, provider, advisor tool,
and governed prompt boundaries.

## Decision

`approved`

| Owner | Reviewed PR | Merged revision | Reviewed and merged tree |
| --- | --- | --- | --- |
| operator-orchestration-service | [PR #423](https://github.com/mfshaf7/operator-orchestration-service/pull/423) | `6657d58cf8025270cea75e1eb0394b903b4f866c` | `0d324ffa9cdb521bf47c692e07a21aab00fa5145` |
| platform-engineering | [PR #387](https://github.com/mfshaf7/platform-engineering/pull/387) | `1595a4e7e1412fa3d4fab2f520e12b67c358b67d` | `79e77db0657de69fd2b328909e034d868ada2ba3` |
| governance-operations-console | [PR #191](https://github.com/mfshaf7/governance-operations-console/pull/191) | `aaee553d6e1a3675b7c6c391ab8b02c88bd20cbc` | `43e4a9f205d0abab792b236386101e628e259678` |
| workspace-governance | [PR #324](https://github.com/mfshaf7/workspace-governance/pull/324) | `ed229b0f7c0e39a0dd734c83d0e964b3f75f7007` | `f9f87b0d8cb529a4cdcedec3ef63b51e960ff5ff` |

Each merged tree matches the exact Gary PR head verified by local and GitHub checks. The delegated human reviewed and merged the exact source. The Console's production dependency audit is clear. The update is approved for the existing working dev-integration composition. Normal Platform activation and readback are required to establish the operating result. The earlier limited sandbox credential authorization stays expired.

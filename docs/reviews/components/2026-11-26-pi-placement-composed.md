# PI Planning placement for risks and milestones

## Summary

The existing PI Planning flow can place a prepared Risk or Milestone in its
calendar. Delivery already requires this field for completion. The Console
uses the existing board and reviewed plan submission. OOS keeps the canonical
work package and its type as the source for the placement.

## Review areas

**Delivery.** The broker applies the existing preparation, status, date,
PI ownership, dependency and objective checks. The reviewed assignment can
only change the selected item's placement through the existing command.
Feature forecasting keeps its original set of implementation work. The
broker test covered preparation, scheduling and exact item identity for both
types, plus rejection when a required field is missing.

**Authority.** The operator uses the existing caller, role, review and
OpenProject write path. The patch extends the eligible ART types in that
path. Scope is limited to PI placement. This review grants no authority to
activate the #1384 project sandbox or change owner credentials.

**Verification.** The broker suite passed with 2,078 successes and two normal
skips. The repository checks and API and worker image smoke checks passed.
Console repository validation, semantic checks, typecheck, production build
and dependency audit passed. The operating check will use the Console
to place the real design risk on the existing calendar and verify readback.

## Decision

`approved`

| Owner | Reviewed PR | Merged revision | Reviewed and merged tree |
| --- | --- | --- | --- |
| operator-orchestration-service | [PR #428](https://github.com/mfshaf7/operator-orchestration-service/pull/428) | `1260c0a646dd83567bafffb1ffcd62e513a731ac` | `88ba378ab156ec5d46009fdb3084a91de652947d` |
| governance-operations-console | [PR #194](https://github.com/mfshaf7/governance-operations-console/pull/194) | `d7461e82789ca0b0adb34579f426a5a2049736ef` | `dc3d71ba5d5035f02249eee0e4274622d795bbdb` |

Each merged tree matches the exact Gary PR head verified by local and GitHub checks. The delegated human reviewed and merged the exact source. The Console's production dependency audit is clear. The update is approved for the existing working dev-integration composition. Normal Platform activation and readback are required to establish the operating result. The operating evidence remains distinct from this source review.

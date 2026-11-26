# Reviewed source authorization for recorded Delivery groups

The approved source group identifier is carried intact through the existing
source preparation, explicit approval, issuer receipt, client readback, and
work-session binding. The broker and its API schema use the same bounded
identifier pattern accepted by Platform. Console readback recognizes that
same pattern. The checked input still excludes path separators.

The existing repository identity, branch, approved base, bound operator,
canonical decision digest and private credential dispatch continue to govern
access. The receipt cannot change the authorized subject or scope. Issuance
continues to require the original approved operation. Focused tests cover
preparation, issuance, receipt, session binding and invalid identifiers.

Owner maintenance for the currently reviewed Console composition.
The Landing Unit Decision is `feature_single_landing_unit`.

## Decision

`approved`

| Owner | Reviewed PR | Merged revision | Reviewed and merged tree |
| --- | --- | --- | --- |
| operator-orchestration-service | [PR #431](https://github.com/mfshaf7/operator-orchestration-service/pull/431) | `bbfe12ee08262b86e31034840e823a93e21c7d5c` | `d240afbefb18c7b68dbd81ef4721d7a730302a1c` |
| governance-operations-console | [PR #196](https://github.com/mfshaf7/governance-operations-console/pull/196) | `57b6e3607f49111b27bb734168baef9fe982e428` | `834c29c235bc341a0322c43a75073e269066892a` |

Each merged tree matches the exact Gary PR head verified by local and GitHub checks. The delegated human reviewed and merged the exact source. The Console's production dependency audit is clear. The update is approved for the existing working dev-integration composition. Normal Platform activation and readback are required to establish the operating result. The operating evidence remains distinct from this source review.

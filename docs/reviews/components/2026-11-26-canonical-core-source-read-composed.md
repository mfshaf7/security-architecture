# Canonical core source reads

## Summary

The source executor supplies the same reviewed repository identity used by the
source-access adapter when it resolves a core repository checkout. It still
reads current admission and respects the admitted source location.

## Review areas

**Source identity.** Both paths read the reviewed identity projection and
resolve current admission for the exact owner. Internally registered private
repositories use their protected connection. Current admission failure blocks
both paths. The change leaves the issued credential's repository, branch,
operator and approved intent constraints in place.

**Verification.** Broker checks covered the trusted core lookup, the private
location route and admission denial. The candidate read the real configured
owner revision and passed the planned source path checks using the same
installation source binding. The operating test will prepare the source
scope and start work from the approved Technical Plan in the live Console.

## Decision

`approved`

| Owner | Reviewed PR | Merged revision | Reviewed and merged tree |
| --- | --- | --- | --- |
| operator-orchestration-service | [PR #430](https://github.com/mfshaf7/operator-orchestration-service/pull/430) | `880731ed36f7aab4839f3435aefa6132d8eff323` | `f334f62cdc05229eab65eb15d05a13587839ff37` |

Each merged tree matches the exact Gary PR head verified by local and GitHub checks. The delegated human reviewed and merged the exact source. The Console's production dependency audit is clear. The update is approved for the existing working dev-integration composition. Normal Platform activation and readback are required to establish the operating result. The operating evidence remains distinct from this source review.

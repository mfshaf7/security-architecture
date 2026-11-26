# Recorded Technical Plan at work start

## Summary

The approved plan in existing durable custody supplies the work group and
plan binding for the source session. The Console displays the approved scope.
The existing review, approval and scoped repository access still apply.

## Review areas

**Source authority.** The broker reads the current approved artifact through
its existing custody adapter. Platform accepts the canonical Delivery
identifier and retains it in the credential, receipt and revocation.
The private path is still derived from its digest. Repository, branch,
provider coordinates, approval and operator checks remain in the issuer. It validates the expected digest, complete work
group and owner before preparing source access and again at work start. A
stale plan or partial group fails before an authorization is issued. The
existing file-backed decision path still uses its original checks.

**Delivery.** The approved artifact remains the source of implementation
prerequisites and gate evidence. The change applies to source-session
preparation. The project sandbox and later activation require their own
approved evidence and action.

**Validation.** The broker passed 2,080 tests with two standard skips,
base-aware governance gates, API documentation and image smoke checks. The
Console passed 1,205 semantic checks, types, its dependency audit, and the
exact production build. Focused checks cover preparation, source access,
session start and stale and partial scope rejection. Platform's production
issuer test covers the namespaced identifier through issuance and revocation,
preserving the original identifier and hashed private directory. Live verification will
reopen the existing #1386 work group, review its source access and verify its
recorded session against the approved plan.

## Decision

`approved`

| Owner | Reviewed PR | Merged revision | Reviewed and merged tree |
| --- | --- | --- | --- |
| operator-orchestration-service | [PR #429](https://github.com/mfshaf7/operator-orchestration-service/pull/429) | `c8edd9ff67c63e6932a5a168502bdda941d90e54` | `e566544e3600d55b64c770df76e373d7fda3fe93` |
| governance-operations-console | [PR #195](https://github.com/mfshaf7/governance-operations-console/pull/195) | `3eadc1d13700d57e46b5c493daec177dabfe7f85` | `cd5bb7e760ed9a0f255c468cb555cabd818c6f95` |
| platform-engineering | [PR #391](https://github.com/mfshaf7/platform-engineering/pull/391) | `74a46b229aaa5d1bc8b3efa209c1d63743262391` | `f726ae0eb34ba8e5f6ad883c352eaebeee014808` |

Each merged tree matches the exact Gary PR head verified by local and GitHub checks. The delegated human reviewed and merged the exact source. The Console's production dependency audit is clear. The update is approved for the existing working dev-integration composition. Normal Platform activation and readback are required to establish the operating result. The operating evidence remains distinct from this source review.

# Technical Plan and Delivery composition review

## Summary

This review covers the approved Delivery maintenance in the existing local dev-integration composition. It pairs the updated Technical Plan contract and the Console with the exact backend revisions that validate it, preserve private drafts, and maintain current Delivery routes.

## Scope Delta

- Workspace Governance, WGCF and OOS share the same pinned v6 packet schema. The current project path accepts a single repository with installation custody. Applicability and the selected plan continue to determine when lifecycle, access, and authorization evidence are required.
- OOS checks the authenticated caller and existing operator binding for source observations. The separate bounded source executor reads evidence for the selected work. Recording an approved plan remains a distinct operation with canonical validation and WGCF custody.
- Console reads the actual selected work for optional Technical Plan advice. Its editable starter preserves saved drafts and existing approvals. No model request runs until the operator selects the action. Model choice stays in Model Operations and native calls retain the existing CGG admission and invocation evidence.
- Platform preserves timestamp precision so an immediate Catalog read can distinguish two different observation times. Calendar values and recorded work assignments keep their existing identity.

## Review Areas

**Identity and secrets.** The existing caller, operator and source boundaries remain in force. The source evidence request is authenticated and bounded to repository identity. Draft custody stays operator-private. The changes do not add a provider credential, access grant or root action.

**Delivery and runtime.** Refinement prepares work and PI Planning records dated placement. The existing owner accepts terms, validates the plan and records approval. The disposable connected rehearsal covered both handoff routes, PI assignments, private validation, approved WGCF custody, native closeout, exact replay and locked History. The original accepted runtime remains the rollback target.

**AI.** The configured governed advisor returned a recommendation and editable starter from the actual selected work. Browser checks proved starter insertion and retention of existing state. The provider test used the existing admitted advisor endpoint and the candidate request shape. Existing private business records were preserved.

The Console production build and 1,204 semantic checks passed. All 12 targeted release browser checks passed. Workspace Governance passed 316 tests, WGCF passed 599 tests, and the broker passed 2,077 tests with two standard skips. Platform validation and precise Catalog readback passed.

## Decision

`approved`

| Owner | Reviewed PR | Merged revision | Reviewed and merged tree |
| --- | --- | --- | --- |
| workspace-governance | [PR #326](https://github.com/mfshaf7/workspace-governance/pull/326) | `a9e091e652a99156e63336544bf5ba9764934158` | `b9c25b5c52becc0737e00d23fe65c27f09b88c47` |
| workspace-governance-control-fabric | [PR #127](https://github.com/mfshaf7/workspace-governance-control-fabric/pull/127) | `15d8ba987bb87ee96734f29e51fe0e78a93afc7b` | `8a82f12fb93497ebd80e6d7e892c87d987c1c1bf` |
| operator-orchestration-service | [PR #427](https://github.com/mfshaf7/operator-orchestration-service/pull/427) | `414e4cfb2f1dbde7b431ca6270690f55215e5d28` | `ef1aa0af8647871ea6afa1a28d17ef52f5b2c52b` |
| platform-engineering | [PR #390](https://github.com/mfshaf7/platform-engineering/pull/390) | `a22f347d67b25d12fda102497d9188340f9de289` | `84ab73e78d639d2c3f60236a69ca8ba88399c2e4` |
| governance-operations-console | [PR #193](https://github.com/mfshaf7/governance-operations-console/pull/193) | `7f0972d630bf8b325e09069920410722d7affbbd` | `a1c1c2f4785e292fb9c91a7ff1fe01c202c22f6b` |

Each merged tree matches the exact Gary PR head verified by local and GitHub checks. The delegated human reviewed and merged the exact source. The Console's production dependency audit is clear. The update is approved for the existing working dev-integration composition. Normal Platform activation and readback are required to establish the operating result. The operating evidence remains distinct from this source review.

## Durable worker image proof

The reviewed activity worker is `ghcr.io/mfshaf7/workspace-governance-control-fabric-worker@sha256:0345bbc631e0b21ec047f0c9f4751568f70c7eb8d6960f46cbe7f13777efcdf7`. Its baked WGCF revision is `15d8ba987bb87ee96734f29e51fe0e78a93afc7b`. The [exact main build](https://github.com/mfshaf7/workspace-governance-control-fabric/actions/runs/45575931134) verified its source file, unprivileged identity, and default denial. The existing activation manifest, generation, task queue, and workflow authority remain bound to their original evidence.

When updating the reviewed WGCF revision, verify the worker release metadata and baked source against the reviewed revision before applying the composition.

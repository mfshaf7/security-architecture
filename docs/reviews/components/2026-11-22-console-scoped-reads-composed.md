# Console scoped reads and repository authority review

## Summary

This change covers the Console's loading and stability batch in the established
local dev-integration composition. It includes the protected repository reads
and the implementation of a reviewed transfer from legacy Git registration to
installation-private Registry authority.

## Scope Delta

- Home and agent context reuse matching reads and request compact owner data.
  Delivery supplies Current, History and selected PI scopes. Exact record and
  dependency reads preserve work status and source authority.
- The Proposal Hub resolves a native Delivery link by the canonical record
  reference. Repository setup acknowledgements recover an existing receipt
  with the same approval evidence after an interrupted response.
- Application Verification inspects bounded required Git files at one exact
  commit. The protected read retains the Source App identity, exact repository
  scope, strict regular-file checks, and token revocation.
- The Registry and broker add a bounded repository transfer using the
  existing installation, role, policy checkout and transaction store.

## Review Areas

**Identity and secrets.** The Console operator remains bound by the broker.
The Registry transfer uses the existing decision writer. The protected source
reader remains repository-scoped, and the token stays in Platform.

**Delivery and runtime.** The scoped Delivery projection uses actual
OpenProject child assignments and exact external dependency evidence. It
expires and refreshes without becoming a write authority. An isolated
rehearsal preserved the retained registration's provider ID, approval
envelope and receipt replay. Transfer acceptance refused a remaining legacy
claim and required the exact current revision and its approved parent.
There is a planned interruption between retiring the Git claim and
accepting the internal record. The pilot procedure must coordinate that
transition and verify readback before considering the record transferred.

**AI.** Default context reads are bounded to the active interaction. The
batch uses the existing model routing and context admission path.

## Decision

`approved`

| Owner | Reviewed PR | Merged revision | Reviewed and merged tree |
| --- | --- | --- | --- |
| workspace-governance | [PR #325](https://github.com/mfshaf7/workspace-governance/pull/325) | 29f673f6a3059f34ec2c8edc160373fe8d87b988 | 22cbccf7e9fa0e7e49b0731052921cdaeb3b64ab |
| workspace-governance-control-fabric | [PR #126](https://github.com/mfshaf7/workspace-governance-control-fabric/pull/126) | e01bcfdf861494f2d0d0ab52fe2ff63d3e47cf68 | 74a0e8790c2a3dddaf706e5f11f238e6daf2829f |
| operator-orchestration-service | [PR #424](https://github.com/mfshaf7/operator-orchestration-service/pull/424) | 68c9da22833e73e3b1629dfde5c8e73f36829723 | 5c2fc1778e3a788a07394f7b95eca7c447d72ab6 |
| operator-orchestration-service | [PR #425](https://github.com/mfshaf7/operator-orchestration-service/pull/425) | 93ce7213e4eb99a4978ee9ae69ac75e03c4b319c | 3d2983fda2a8c5ea480ee2c53e8ed5a2d262a78d |
| operator-orchestration-service | [PR #426](https://github.com/mfshaf7/operator-orchestration-service/pull/426) | 2e499019c50ea3cac01ef80a169050d1e4996645 | 5a4c0a5cd65409963192b10942ef6cfc5d2d6813 |
| platform-engineering | [PR #388](https://github.com/mfshaf7/platform-engineering/pull/388) | f80cdafc8e4a685a31f8879648cdb65e59568e77 | 89d8118b720f167476051a2fd6ff2c5976e38fa5 |
| governance-operations-console | [PR #192](https://github.com/mfshaf7/governance-operations-console/pull/192) | 058edbc7a666e2c28a8e667064b379bb59d0c5cb | 7d49ffff89f2f611be23fb9093c55852a9084594 |

The delegated human reviewed the exact Gary heads after the required checks. The Console production build and dependency audit passed. The disposable Little List rehearsal passed against the merged Governance and Registry sources. The new read and transfer code may activate in the existing local composition. The live pilot still requires a separate operator decision and authenticated provider readback.

### Durable Registry worker image

The first live activation found the previous worker image still pinned. The
new immutable image digest is
`sha256:59172b0ea54250063bfa1ed8c0f16534abf6d6299c09369661e1c606d6a1d47f`.
The worker image was built from the reviewed Registry revision
`e01bcfdf861494f2d0d0ab52fe2ff63d3e47cf68`. Its Linux amd64 artifact reported
that revision from its embedded source marker. An isolated status read
confirmed worker identity, the existing readiness queue, and default denial
without activation evidence. The Security decision pins this exact image
with the original workflow activation manifest. Normal Platform activation
still requires live readback of the image and authorized worker.
[Exact worker image build](https://github.com/mfshaf7/workspace-governance-control-fabric/actions/runs/45034964880/job/137246559813)

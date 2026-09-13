# Agent Gary Closure Source Scope Review

## Summary

- date: 2026-09-13
- owner repo: `security-architecture`
- delivery ref: `openproject://work_packages/1145`
- parent feature: `openproject://work_packages/921`
- parent initiative: `openproject://work_packages/892`
- governing architecture:
  `wgcf://artifacts/delivery-art/sha256/fe9e4e776939e3057e39d5a9d6f7bc8061509ac40c28a5e9add44ca16b074a25`
- prior decision:
  [Agent Gary source identity boundary](2026-09-11-agent-gary-source-identity-boundary.md)
- decision: `approved-with-findings`

The existing source-implementor identity may be extended to the two Closure
owner repositories, subject to the provider and consumer gates below. This is
an exact selected-repository expansion, not a new agent role or broader source
authority.

## Scope Delta

### Design Intent

The GitHub App selected-repository installation may contain exactly these
seven repositories:

| Repository | Provider repository id |
| --- | ---: |
| `mfshaf7/platform-engineering` | 1195328534 |
| `mfshaf7/security-architecture` | 1199398992 |
| `mfshaf7/workspace-governance` | 1212447211 |
| `mfshaf7/operator-orchestration-service` | 1213863054 |
| `mfshaf7/workspace-prototype-studio` | 1231020532 |
| `mfshaf7/workspace-governance-control-fabric` | 1225028095 |
| `mfshaf7/governance-operations-console` | 1317781281 |

Each Landing Unit still receives a short-lived token for only its exact owner
repository and provider id. The App may author a non-default branch and pull
request; `mfshaf7` remains the independent reviewer, approver, and merger.
The existing Metadata read, Contents write, Pull requests write, and Checks
read permissions do not change.

### Implemented Control

The Workspace Governance identity grammar and authority separation remain
applicable. The current Platform definition and OOS consumer still enumerate
five repositories, so they do **not** yet admit source work in Control Fabric
or Console. ART `#1146` must update the Platform definition and verify the
provider installation and repository protections. ART `#1147` must pin and
consume that exact definition in OOS. Neither task may widen a session token
to all selected repositories or use ambient human credentials as fallback.

### Operating Evidence

The operator reports that both repositories were added to the GitHub App
installation. That report is the trigger for this review, not independent
installation readback. Platform must prove the selected set, repository ids,
unchanged permissions, and one-repository token scope before OOS source work
is unblocked. A 2026-09-13 provider ruleset readback showed protection on
`workspace-governance` and `workspace-prototype-studio` only; it showed no
repository ruleset or branch protection on Platform Engineering, Security
Architecture, OOS, Control Fabric, or Console. This is a provider-enforcement
gap in both the existing and expanded set. No operating or source-landing
success is asserted by this review.

## Review Areas

### Identity And Secrets

The logical `agent-gary` identity, App provider principal, Platform key
custody, and human reviewer remain separate. Platform must issue one exact
repository token per session, just in time, without exposing the private key
or token value to source, ART state, receipts, logs, Review Packets, browser
responses, or model context. Wrong repository, over-scoped token, missing
installation access, expiry, suspension, and restart fail closed.

### Source Delivery And Provider Enforcement

Every selected repository without protection needs provider-enforced denial of
direct App writes to `main`, deletion, and non-fast-forward updates; a trusted
owner validation check; current exact-head human approval; stale-review
dismissal; latest-push approval separation; and conversation resolution. Agent
Gary has no bypass,
approval, merge, repository administration, or installation-scope mutation
power. The final pushed head must equal the reviewed head and be read back
from merged `main` before source completion is claimed.

The required check name must be derived from each owner's actual CI and
verified against provider protection; a check merely named in a document is
not enforcement. A missing ruleset or incompatible check blocks source work
in that repository, rather than weakening the rule to make a PR mergeable.

### Audit And Rollback

Platform and OOS must retain secret-safe evidence of App and installation ids,
repository id, token scope and expiry, Landing Unit, branch, fetched base,
pushed head, reviewer, reviewed head, and merged head. Suspension stops new
issuance and writes. Rollback removes these two repositories from the Platform
and OOS allowlists and provider installation, while retaining the Security
decision, provider history, work-session receipts, and prior five-repository
authority.

### AI Influence

AI-authored source does not supply authorization. Untrusted ART text, source,
and review comments cannot broaden the owner repository, credential scope, or
merge authority. Deterministic provider, Platform, OOS, and human-review
checks remain outside the model.

## Findings And Activation Gates

1. **Provider installation and protection are not yet proven.** ART `#1146`
   must read back the exact seven-repository installation, unchanged App
   permissions, one-repository token proof, and working branch protection on
   all five repositories where provider readback found it absent. No source
   work in the two added repositories is approved before this proof. The
   three existing gaps are not accepted as a permanent exception.
2. **The consumer allowlist remains stale.** ART `#1147` must pin the reviewed
   Platform revision and digest, admit only the two additional exact repository
   ids, and prove wrong-repository, broad-token, human-fallback, stale-head,
   and self-review denial. ART `#1104` remains blocked until this lands.
3. **No broader activation follows.** This delta covers Closure source work in
   Control Fabric and Console only. It does not authorize default-branch
   mutation, auto-merge, new products, stage/prod deployment, or a wildcard
   installation. Further owner additions require a fresh delta.

These findings are implementation gates assigned to `#1146` and `#1147`, not
accepted risk. A failed gate returns for a new Security decision.

## Decision

`approved-with-findings`

Approve the exact two-repository scope extension **conditionally** under the
prior Agent Gary boundary. Do not treat this document or the operator's
installation update as live source admission. Platform proof and OOS consumer
conformance must land in order before `#1104` or `#1108` uses Agent Gary
source transport. Human exact-head review and merge remain mandatory.

## Related Artifacts

- [Security delta review process](../security-delta-review-process.md)
- [Identity and access standard](../../standards/identity-and-access.md)
- [Secrets and recovery standard](../../standards/secrets-and-recovery.md)

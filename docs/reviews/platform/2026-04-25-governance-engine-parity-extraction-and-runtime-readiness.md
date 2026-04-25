# Governance-Engine Parity, Extraction, And Runtime-Readiness Review

## Summary

- date: 2026-04-25
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.workspace-governance`
- decision: `approved-with-findings`

This delta review evaluates the control-plane work that turns governance-engine
parity, extraction readiness, and future bounded runtime activation into
explicit machine-readable controls instead of leaving them as architectural
intent only.

## Scope Delta

The earlier workspace-governance review accepted the high-level governance
engine foundation and the governed model-access contract. The current slice
adds the next missing control layers:

1. explicit path-level boundary classification between engine-owned authoring
   truth and tenant-instance state
2. fail-closed shadow-parity validation across workspace-root outputs, live
   installed skills, and generated governance artifacts
3. an explicit extraction gate and runtime-readiness contract that keeps repo
   extraction and governed AI activation out of scope until parity is proven
4. explicit extraction hard-gate thresholds, need signals, current coupling
   inventory, and standalone packaging prerequisites so later extraction work
   cannot proceed from inferred architecture context alone

These are security-relevant because they determine whether future extraction or
runtime activation is sequenced behind reviewed control-plane truth instead of
being justified by drift-prone local convenience.

## Review Areas

### Identity

- the extraction gate preserves the existing caller-boundary rule: workload
  caller identity must stay distinct from operator acceptance identity
- the runtime-readiness contract correctly keeps that identity split as a
  prerequisite instead of allowing parity work to blur it into one service path

### Delivery

- the shadow-parity validator is the right delivery control because it proves
  the live workspace state still matches the canonical authoring layer before
  any extraction decision is taken
- classifying tenant-instance files explicitly prevents local admitted state
  from being normalized into generated control-plane outputs
- the extraction gate is stronger now that it defaults to retain-integrated
  unless every hard gate and every extraction-need signal is satisfied
- the boundary-map inventory correctly turns the current coupling points and
  packaging prerequisites into reviewable machine state instead of leaving them
  as latent architecture assumptions

### Runtime

- the parity gate correctly treats repo extraction and a central always-on
  governance-engine service as deferred follow-on work, not part of the current
  delivery slice
- the runtime-readiness contract is acceptable because it requires parity proof
  and a fresh security review before any activation attempt

### AI

- the new gate is correctly conservative: it does not approve governed runtime
  activation, only the prerequisites that must exist before a later activation
  review can even be considered
- keeping the platform-owned model-profile registry and governed invocation path
  outside repo-local policy remains the correct trust boundary

## Decision

`approved-with-findings`

Approved because the new controls make the extraction boundary and future
runtime sequencing explicit while keeping parity proof and security review as
non-optional gates.

Findings and residual risk:

1. A clean parity validator is necessary but not sufficient. If a future
   extraction starts moving identity, storage, or privileged automation
   boundaries, that extraction still needs its own delta review.
2. The runtime-readiness contract is intentionally pre-activation. Any future
   bounded governed runtime remains blocked until the real invocation plane,
   audit retention, and operator approval path are implemented and reviewed.
3. The tenant-instance classification must stay current as new local admitted
   state surfaces appear; otherwise parity could become mechanically clean while
   the boundary itself silently drifts.
4. The threshold model is intentionally conservative. If a later change tries
   to weaken the extraction-need signals or remove the coupling inventory, that
   should be treated as a security-significant contract regression rather than
   a harmless documentation tweak.

## Related Artifacts

- `workspace-governance/docs/governance-engine-foundation.md`
- `workspace-governance/contracts/governance-engine-foundation.yaml`
- `workspace-governance/contracts/governance-engine-boundary-map.yaml`
- `workspace-governance/contracts/governance-engine-shadow-parity.yaml`
- `workspace-governance/contracts/governance-engine-extraction-gate.yaml`
- `workspace-governance/generated/governance-engine-boundary-map.json`
- `workspace-governance/scripts/validate_governance_engine_shadow_parity.py`
- `platform-engineering/docs/standards/governed-ai-access-model.md`
- `security-architecture/docs/standards/ai-security-and-governance.md`
- [`../security-delta-review-process.md`](../security-delta-review-process.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)

# Governed Full-Platform Runtime Drill And Restore Review

## Summary

- date: 2026-04-24
- owner repo: `platform-engineering`
- affected review subjects:
  - `repos.platform-engineering`
  - `products.openclaw`
  - `products.openproject`
  - `components.operator-orchestration-service`
  - `components.vault`
  - `components.external-secrets`
  - `components.platform-postgresql`
  - `components.observability`
  - `components.openclaw-host-bridge`
- decision: `approved-with-findings`

This delta review covers the new shared governed full-platform runtime drill
workflow that now gives the platform one explicit operator surface for:

- baseline capture before activation
- scoped activation recording across devint, stage, prod, and shared surfaces
- explicit verification and blocker decisions
- exact-baseline restore with operator-facing evidence

## Scope Delta

### Design Intent

- temporary runtime exercise should be governed as a distinct workflow class,
  not blurred into normal stage or prod promotion
- the full-platform drill should have one explicit machine-readable scope that
  includes OpenProject, the broker, OpenClaw, shared secrets delivery, shared
  supporting components, and required host-bridge surfaces
- restore should return the exact captured pre-drill posture rather than
  whatever GitHub `main` currently declares

### Implemented Control

- `platform-engineering` now carries:
  - `docs/standards/governed-runtime-drill-model.md`
  - `docs/decisions/adr/ADR-014-governed-full-platform-runtime-drill-and-restore.md`
  - `environments/shared/runtime-drills/full-platform-runtime-drill.yaml`
  - `environments/shared/runtime-drills/full-platform-runtime-drill-evidence-template.yaml`
  - `scripts/platform_drill.py`
  - `docs/runbooks/full-platform-runtime-drill.md`
- the shared contract and script now:
  - require baseline capture before activation
  - keep explicit verification and restore ledgers
  - require blocker and exception decisions with owner and review date
  - materialize an operator-facing `evidence.yaml` pack for each run
- the shared workflow still does not directly replace owner runtime controls:
  - devint activation remains under `make devint-up`
  - OpenClaw stage remains under `make openclaw-stage-state`
  - OpenClaw prod lifecycle remains under `make openclaw-prod-state`

### Operating Evidence

- local validation passed for:
  - repo structure
  - governance docs
  - operational docs
  - `platform_drill.py` syntax
- a throwaway proof run under:
  - `/tmp/platform-drill-proof/full-platform-runtime-drill/art-194-proof`
  proved:
  - snapshot creation
  - run status reporting
  - activation recording
  - blocked verification capture with enterprise decision fields
  - supplemental evidence recording
  - restore recording
  - exception-register cleanup when a previously blocked or exception state was resolved
- the baseline and evidence pack capture local branch, SHA, and dirty-state
  truth for the drill authority, which materially improves attribution over
  informal local rehearsal

## Review Areas

### Identity

- no new human or machine identity was introduced by this workflow
- the drill continues to rely on existing owner commands and previously
  reviewed caller paths rather than inventing a new privileged automation
  principal
- capturing local branch, SHA, and dirty-state posture strengthens attribution
  for local drill authority, which is a net improvement over operator memory
- this remains acceptable only while the drill path stays operator-driven and
  does not normalize break-glass or prod exposure as unattended routine
  automation

### Secrets

- Vault and External Secrets are now explicitly in the drill scope and
  verification pack, which improves reviewability of secret-delivery posture
  during temporary runtime exercise
- the new evidence model stores references and decision notes, not secret
  values or recovery material
- this is acceptable because the shared script currently records posture and
  evidence only; it does not export secret contents into the drill pack
- any later expansion that reads, copies, or persists high-sensitivity secret
  material inside the shared drill workflow would require a fresh delta review

### Delivery

- the biggest security-significant change is explicit: the drill authority is
  now the captured baseline plus the scoped local activation path, not GitHub
  `main` or a governed promotion decision
- that is acceptable as a bounded runtime-drill model because the workflow now
  clearly distinguishes temporary drill authority from governed promotion and
  requires exact-baseline restore
- the shared script remains a ledger and evidence surface rather than a hidden
  delivery controller; that preserves existing product and platform review seams
- if `platform_drill.py` later gains direct `kubectl`, Argo, Vault, or Git
  mutation authority instead of recording owner-driven actions, a fresh delta
  review is required before treating that expansion as safe

### Runtime

- the new workflow materially improves runtime control because the operator now
  has one explicit baseline, verification, restore, and exception model for
  full-platform drills instead of reconstructing the exercise from scattered
  product procedures
- exact-baseline restore is the correct default because it prevents temporary
  drills from being mislabeled as completed while the environment stays changed
- the workflow still depends on the truth and discipline of the owner commands
  it references; it does not make runtime state safe by documentation alone

### Host Control

- the host bridge is now explicitly included in the drill scope, which is the
  correct security posture because host-connected runtime control was already a
  real dependency for broad platform drills
- this remains acceptable because the shared drill workflow records host-bridge
  posture rather than invoking host-control operations directly
- the reviewed host-control rule still holds: product or operator workflows may
  orchestrate host-facing actions, but they must not become the host trust
  anchor
- if the shared drill helper later mutates host-bridge services, policy, or
  host-control paths directly, require a fresh delta review before treating the
  workflow as acceptable

### AI

- no new AI-shaped decision or approval path was introduced by this tranche
- the workflow is still operator-driven rather than model-authorized
- if a later change allows AI-driven activation, restore, exception handling,
  or drill closure, that expansion requires fresh review before it is treated
  as safe

## Decision

`approved-with-findings`

Approved because the new workflow reduces ambiguity, improves attribution, and
adds explicit restore and exception discipline without creating a new shared
privileged automation identity or turning the shared script into a hidden live
mutation controller.

Findings and residual risk:

1. The workflow now formalizes a local runtime authority path outside GitHub
   `main`. That is acceptable only while it stays clearly labeled as a
   temporary drill path with exact-baseline restore, not a substitute for
   governed promotion.
2. `platform_drill.py` is acceptable in its current ledger-oriented form. Any
   later expansion into direct cluster, secret, or host-control mutation needs
   a fresh delta review before it is treated as an approved control surface.
3. Temporary prod exposure remains acceptable only while it stays bounded,
   reviewable, and reversible through the existing OpenClaw lifecycle controls.
   The shared drill surface must not become a convenience path for leaving prod
   live or drifting away from the captured baseline.

## Related Artifacts

- `platform-engineering/docs/standards/governed-runtime-drill-model.md`
- `platform-engineering/docs/decisions/adr/ADR-014-governed-full-platform-runtime-drill-and-restore.md`
- `platform-engineering/environments/shared/runtime-drills/full-platform-runtime-drill.yaml`
- `platform-engineering/environments/shared/runtime-drills/full-platform-runtime-drill-evidence-template.yaml`
- `platform-engineering/scripts/platform_drill.py`
- `platform-engineering/docs/runbooks/full-platform-runtime-drill.md`
- [`../../architecture/platform/trust-boundaries.md`](../../architecture/platform/trust-boundaries.md)
- [`../../architecture/domains/identity-and-access.md`](../../architecture/domains/identity-and-access.md)
- [`../../architecture/domains/secrets-and-recovery.md`](../../architecture/domains/secrets-and-recovery.md)
- [`../../architecture/domains/gitops-and-machine-trust.md`](../../architecture/domains/gitops-and-machine-trust.md)
- [`../../architecture/domains/host-control.md`](../../architecture/domains/host-control.md)
- [`../../architecture/domains/ai-and-agentic.md`](../../architecture/domains/ai-and-agentic.md)
- [`../security-delta-review-process.md`](../security-delta-review-process.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)

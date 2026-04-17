# OpenClaw Host Bridge Security Baseline Review

## Scope

Review `openclaw-host-bridge` as the canonical privileged host-control
enforcement boundary for OpenClaw, including:

- host action execution
- policy enforcement
- audit evidence
- export staging
- recovery-adjacent runtime support

## Decision

Approved as the current component security baseline with bounded controls.

This baseline is accepted while all of these remain true:

- the bridge remains the host trust anchor instead of Telegram or product logic
- typed operations, policy enforcement, and audit stay outside the model
- runtime identity and audit evidence remain legible after changes
- live host drift is backported to the owning repo and not treated as the final
  source of truth

## Review Areas

### Runtime

- this is the highest-trust local execution boundary in the current workspace
- the bridge must remain the enforcement point for allowed roots, export
  staging, and privileged host actions

### AI And User Influence

- user-facing and model-assisted flows may eventually reach this boundary
- deterministic checks, approval semantics, and audit remain mandatory at the
  boundary itself rather than in upstream chat logic

### Visibility

- bridge health, audit location, version identity, and recovery wiring must
  remain inspectable by operators

## Residual Risk

- host-control remains a high-trust boundary with meaningful residual risk even
  when the current controls are functioning
- stage and prod host differences can still create drift if environment-scoped
  policy is not explicit

## Related Artifacts

- [`../../architecture/components/openclaw-host-bridge/README.md`](../../architecture/components/openclaw-host-bridge/README.md)
- [`../../architecture/domains/host-control.md`](../../architecture/domains/host-control.md)
- [`../../architecture/domains/ai-and-agentic.md`](../../architecture/domains/ai-and-agentic.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)

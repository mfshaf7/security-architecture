# OpenClaw Telegram Channel Security Baseline Review

## Periodic Reassessment — 2026-10-19

The [October reassessment](../../assessments/platform/2026-10-baseline-reassessment.md)
records the inspected canonical owner revisions, current boundary conditions,
retained findings and explicit operating-evidence limits for this subject.
Continue this existing baseline subject to those conditions; next baseline
review is 2027-04-19. Earlier remediation checkpoints remain unchanged.
No pending Console authoring/bootstrap capability or new runtime is approved.
The original April review below is retained as historical evidence; later
accepted change reviews apply separately, not as blanket baseline permission.

## Scope

Review `openclaw-telegram-enhanced` as the canonical Telegram channel security
surface for OpenClaw, including:

- untrusted chat input handling
- approval and callback behavior
- media delivery shaping
- read-only operator surface exposure

## Decision

Approved as the current component security baseline with bounded controls.

This baseline is accepted while all of these remain true:

- Telegram-specific behavior stays explicit at the channel layer
- privileged actions remain behind deterministic checks and governed approval
  semantics
- read-only operator inventory exposed through Telegram remains sourced from
  platform-owned truth and does not become a mutating control path
- channel changes stay stage-testable before promotion

## Review Areas

### Runtime

- Telegram is a real user-facing runtime boundary, not a cosmetic integration
- routing, callbacks, approvals, and delivery behavior can shape access to
  higher-trust paths and therefore remain security-significant

### AI

- user and model-influenced input must be treated as adversarial by default
- AI-shaped control changes must continue to point back to product and domain
  security views

### Visibility

- operators need stage-testable evidence for approval UX, media behavior, and
  read-only operator surfaces such as `/platform`

## Residual Risk

- the channel remains exposed to prompt-shaping, approval confusion, and
  callback abuse pressure even when the current controls are acceptable
- separate overlay delivery reduces rebuild cost but does not remove future
  runtime contract drift risk

## Related Artifacts

- [`../../architecture/components/openclaw-telegram-channel/README.md`](../../architecture/components/openclaw-telegram-channel/README.md)
- [`../../architecture/products/openclaw/data-flow-and-boundaries.md`](../../architecture/products/openclaw/data-flow-and-boundaries.md)
- [`../../architecture/domains/ai-and-agentic.md`](../../architecture/domains/ai-and-agentic.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)

# OpenProject Security Baseline Review

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

Review OpenProject as the currently platform-integrated conventional web
product in the workspace.

## Decision

Approved as the current product security baseline with bounded controls.

## Review Areas

### Identity

- OpenProject carries normal web-application identity and admin concerns rather
  than host-control or AI-adjacent trust boundaries

### Secrets

- runtime credentials and secret delivery still depend on the governed platform
  secret model

### Delivery

- OpenProject is platform-integrated rather than fully governed like OpenClaw,
  so its security posture still depends heavily on shared platform controls

### Visibility

- operator documentation and platform identity surfaces must remain sufficient
  even though this product does not yet have the same delivery maturity as
  OpenClaw

## Residual Risk

- its product security story is thinner than OpenClaw because product-specific
  review depth has lagged behind platform integration

## Related Artifacts

- [`../../architecture/products/openproject/README.md`](../../architecture/products/openproject/README.md)
- [`../../architecture/products/openproject/threat-model.md`](../../architecture/products/openproject/threat-model.md)
- [`../../architecture/products/openproject/required-controls.md`](../../architecture/products/openproject/required-controls.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)

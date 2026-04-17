# OpenProject Security Baseline Review

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

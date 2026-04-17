# OpenClaw Runtime Distribution Security Baseline Review

## Scope

Review `openclaw-runtime-distribution` as the active governed stage/prod runtime
composition path for OpenClaw, including:

- staged runtime assembly
- owner-published contract consumption
- Telegram overlay artifact packaging
- digest and source attestation preservation

## Decision

Approved as the current component security baseline with bounded controls.

This baseline is accepted while all of these remain true:

- canonical source remains in owner repos rather than hidden copied trees
- contract verification consumes published manifests and owner-local tests
- the packaged runtime remains attestable by source SHA and digest
- any separate Telegram overlay artifact remains immutable, digest-pinned, and
  tied to an exact qualified OpenClaw base image

## Review Areas

### Delivery

- this component is part of the delivery trust path, not just a build helper
- its packaging and verification behavior must stay reviewable because it
  shapes the governed runtime artifact

### Runtime

- runtime assembly must not widen privilege by mutating the trusted extension
  seam or reintroducing undocumented overrides
- workspace templates and overlay mount paths remain part of the runtime trust
  model

### Visibility

- source SHAs, overlay state, and resulting image digests must stay legible in
  platform evidence and runtime identity surfaces

## Residual Risk

- runtime contract drift from future OpenClaw updates can still invalidate the
  current packaging assumptions
- this component remains security-significant because a packaging error here can
  silently reshape the prod runtime

## Related Artifacts

- [`../../architecture/components/openclaw-runtime-distribution/README.md`](../../architecture/components/openclaw-runtime-distribution/README.md)
- [`../../architecture/products/openclaw/required-controls.md`](../../architecture/products/openclaw/required-controls.md)
- [`../../architecture/domains/gitops-and-machine-trust.md`](../../architecture/domains/gitops-and-machine-trust.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)

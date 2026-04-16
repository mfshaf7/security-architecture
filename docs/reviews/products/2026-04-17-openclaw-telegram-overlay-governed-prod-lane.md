# OpenClaw Telegram Overlay Governed Prod Lane Review

## Scope

Review the change from a stage-only Telegram overlay experiment to a governed
prod delivery lane for small Telegram-only fixes on a platform-qualified
OpenClaw base image.

## Decision

Approved with bounded controls.

The separate Telegram overlay artifact may reach prod when all of these remain
true:

- the overlay artifact is immutable and digest-pinned
- the overlay is tied to an exact qualified OpenClaw base image
- the exact overlay digest is stage-qualified and stage-approved
- prod carries the same qualified base image as the approved stage candidate
- post-promotion prod smoke or UAT is recorded
- the overlay still mounts onto `/app/extensions/telegram`, not a same-id
  user-home override

## Review Areas

### Identity

- no new human identity is introduced
- no new long-lived machine identity is introduced
- existing GitHub workflow and package-publish identities remain the delivery
  actors

### Secrets

- no new secret path is introduced by the overlay lane itself
- existing token handling for workflow dispatch and registry publication remains
  in the current governed secret paths

### Delivery

- delivery trust changes because prod can now reconcile two runtime artifacts:
  gateway base image and Telegram overlay image
- the added trust is accepted only because both artifacts remain Git-managed,
  digest-pinned, and tied to a single approved stage candidate
- rollback remains preserved because both artifacts live in the environment
  contract

### Runtime

- the overlay still replaces only `/app/extensions/telegram`
- the host-control plugin, bridge policy, and host audit boundaries remain
  outside the overlay lane
- no generic runtime patching or same-id global override is reintroduced

### Visibility

- platform contract and runtime surfaces must expose:
  - overlay status
  - overlay source SHA
  - overlay image digest
  - qualified base image
- stage approval and prod smoke evidence remain separate reviewable objects

## Residual Risk

- every new OpenClaw base line still needs separate qualification before the
  overlay lane is reused
- the overlay lane reduces rebuild cost, but it does not make Telegram
  independent from future OpenClaw runtime contract drift

## Related Artifacts

- [`../../architecture/components/openclaw-runtime-distribution/README.md`](../../architecture/components/openclaw-runtime-distribution/README.md)
- [`../../architecture/components/openclaw-telegram-channel/README.md`](../../architecture/components/openclaw-telegram-channel/README.md)
- [`../../architecture/products/openclaw/required-controls.md`](../../architecture/products/openclaw/required-controls.md)
- [`../../../reviews/security-review-checklist.md`](../../../reviews/security-review-checklist.md)

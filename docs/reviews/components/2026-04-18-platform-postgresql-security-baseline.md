# Platform PostgreSQL Security Baseline Review

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

Review Platform PostgreSQL as the shared data service used by platform-managed
applications and services.

## Decision

Approved as the current component security baseline with bounded controls.

## Review Areas

### Secrets

- credential flow must remain under the governed platform secret authority

### Runtime

- database exposure, namespace placement, and operator access remain security
  relevant because this service carries persistent state

### Visibility

- operators must still be able to identify the live service posture, not just
  the application that consumes it

## Residual Risk

- this service depends on the broader platform secret and identity model, which
  is still in transition

## Related Artifacts

- [`../../architecture/components/platform-postgresql/README.md`](../../architecture/components/platform-postgresql/README.md)
- [`../../architecture/domains/secrets-and-recovery.md`](../../architecture/domains/secrets-and-recovery.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)

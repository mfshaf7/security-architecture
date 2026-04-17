# Platform PostgreSQL Security Baseline Review

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

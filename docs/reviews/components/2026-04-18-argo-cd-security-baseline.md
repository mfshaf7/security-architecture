# Argo CD Security Baseline Review

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

Review Argo CD as the shared GitOps control plane that reconciles approved
platform and product state into the cluster.

## Decision

Approved as the current component security baseline with active follow-up.

## Review Areas

### Identity And Delivery

- Argo CD remains a high-impact machine-trust boundary because it consumes
  repository trust and can reshape live state
- repository access, controller authorization, and operator actions remain the
  main security concerns

### Runtime

- Argo manual actions must not become the hidden substitute for governed source
  changes

### Visibility

- repository trust, sync state, and approved revision evidence must remain
  inspectable by operators

## Residual Risk

- machine Git trust and operator federation are still transition-state controls

## Related Artifacts

- [`../../architecture/components/argo-cd/README.md`](../../architecture/components/argo-cd/README.md)
- [`../../architecture/domains/gitops-and-machine-trust.md`](../../architecture/domains/gitops-and-machine-trust.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)

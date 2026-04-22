# Broker-Only Delivery Execution Plane Cutover Review

## Summary

- date: 2026-04-23
- owner repos:
  - `operator-orchestration-service`
  - `platform-engineering`
- affected review subjects:
  - `repos.operator-orchestration-service`
  - `repos.platform-engineering`
  - `products.openproject`
- affected ART work:
  - `#181` `Enabler: Complete broker ownership of the OpenProject ART execution plane`
- decision: `approved`

This delta review covers the final cutover from a mixed delivery execution
model to a broker-only execution plane for `Workspace Delivery ART`.

Earlier reviews approved bounded broker routes while
`platform-engineering/products/openproject` still carried transitional
delivery-execution scripts and Rails runners. This cutover removes that second
execution surface for ART reads and writes.

## Scope Delta

### Design Intent

- `operator-orchestration-service` should be the only supported execution-plane
  backend for ART reads and mutations
- `platform-engineering/products/openproject` should retain only:
  - runtime and bootstrap controls
  - access and service-identity controls
  - ART quality validation and one-time normalization
  - break-glass or repair surfaces that are explicitly not normal execution

### Implemented Control

- broker-owned initiative and work-item routes now cover the supported ART
  execution surface
- product-local OpenProject execution scripts and matching Rails runners are
  retired from `platform-engineering`
- active OpenProject docs and `make` targets now point operators to the broker
  execution surface instead of the retired product-local script family
- the remaining ART quality check now reads through the broker-backed path
  instead of calling retired execution scripts

### Operating Evidence

- repo-local broker route tests passed:
  - `node --test test/http.test.js test/delivery-service.test.js`
- governance and operational doc validators passed in the owner repos
- live broker read proof in `devint-accepted-idea-delivery-mfshaf7` passed for:
  - `GET /v1/delivery-initiatives`
  - `GET /v1/delivery-initiatives/delivery-38/execution-summary`

## Review Areas

### Identity

- no new human or machine identity is introduced by this cutover
- the reviewed broker caller-auth model remains the execution-plane gate:
  - allowlisted caller ids
  - shared caller secret
  - broker-held OpenProject token
- removing product-local execution scripts reduces the risk of a second
  operator path drifting around that caller-auth boundary

### Secrets

- no new secret class is introduced
- OpenProject API token custody remains broker-owned for execution-plane work
- platform-side runtime and bootstrap controls may still need direct secrets,
  but they are now explicitly separated from normal ART execution

### Delivery

- the cutover materially improves delivery control because operators now have
  one supported execution surface instead of two partially overlapping ones
- documentation drift risk is reduced because deleted script families are no
  longer presented as normal operating options
- the ART quality checker continuing to read through the broker is the correct
  control-plane direction; it keeps execution truth and quality truth aligned

### Runtime

- the broker is now the single bounded runtime seam for ART execution traffic
- this is the desired runtime posture because it preserves:
  - one auth seam
  - one audit seam
  - one workflow contract
- remaining direct OpenProject paths are acceptable only because they are
  constrained to admin/bootstrap/repair concerns and not normal execution

### AI

- no new AI authority is introduced
- this change does not widen model-driven action paths; it reduces execution
  ambiguity by forcing the broker to remain the only reviewed execution seam

## Decision

`approved`

Approved because the cutover removes an architectural escape hatch instead of
widening trust.

This approval depends on the following continuing to hold:

1. `platform-engineering` must not recreate product-local ART execution scripts
   or second operator-facing command families
2. remaining direct OpenProject paths must stay clearly classified as
   runtime/bootstrap/repair only
3. broker-owned delivery routes must remain bounded and must not collapse into
   generic OpenProject CRUD
4. future expansion of broker-owned release-governance or stage/prod authority
   still requires a fresh delta review

Required follow-up:

- close `#181` only with evidence that the broker-only cutover landed in the
  owner repos and the ART operator guidance no longer advertises the retired
  script surface
- treat `#175` as separate follow-on governed-release work, not as part of this
  cutover approval

## Related Artifacts

- [`../../architecture/components/operator-orchestration-service/README.md`](../../architecture/components/operator-orchestration-service/README.md)
- [`../../architecture/products/openproject/required-controls.md`](../../architecture/products/openproject/required-controls.md)
- [`../security-delta-review-process.md`](../security-delta-review-process.md)

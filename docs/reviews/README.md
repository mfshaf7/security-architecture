# Reviews

Reviews are repeatable, scope-specific security evaluations tied to a change,
design, incident, or focused investigation.

## Contents

- [`security-review-checklist.md`](security-review-checklist.md)
- [`security-delta-review-process.md`](security-delta-review-process.md)
- [`platform/`](platform)
- [`components/`](components)
- [`products/`](products)

## Placement Rules

- keep reusable review method in this directory root
- put review outputs under `platform/`, `components/`, or `products/` based on
  scope
- use `assessments/` instead when the output is a broader point-in-time
  security assessment
- review outputs should be concrete dated artifacts, for example
  `2026-04-18-openclaw-host-bridge-security-baseline.md`
- directory `README.md` files describe the lane; they do not count as the
  review output that owner repos should reference

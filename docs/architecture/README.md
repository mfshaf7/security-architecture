# Security Architecture

Security architecture in this repo is organized by scope, not by delivery repo.

These documents describe security design intent and control judgment, not
point-in-time runtime evidence.

Point-in-time evidence belongs in:

- [`../reviews/`](../reviews)
- [`../assessments/`](../assessments)
- [`../../registers/`](../../registers)

## Scopes

- [`platform/`](platform)
  - whole-platform views, boundary map, and component inventory
- [`domains/`](domains)
  - cross-cutting security domains such as identity, secrets, GitOps,
    host-control, and AI
- [`components/`](components)
  - security views for shared platform components and sensitive control-plane
    services
- [`products/`](products)
  - product-specific security overlays, threat models, and required controls

## Placement Rules

- Put content in `platform/` when it applies to the whole platform and its
  shared trust model.
- Put content in `domains/` when the concern cuts across several products or
  components.
- Put content in `components/` when one shared component needs its own security
  view.
- Put content in `products/` when a product has a distinct trust boundary,
  threat model, or control profile.

Do not put rollout instructions or operational runbooks here. Those belong in
the owning delivery or platform repo.

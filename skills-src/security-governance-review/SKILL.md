---
name: security-governance-review
description: Use when a change affects trust boundaries, identity, secrets, delivery, privileged runtime behavior, host control, or AI-driven action paths and Codex must route the work through concrete security-architecture artifacts and review expectations.
---

# Security Governance Review

Use this skill when a delivery or platform change crosses a meaningful security
review area and needs a concrete governance path, not just a generic note to
"check security."

## Read First

- `../../docs/reviews/security-review-checklist.md`
- `../../docs/architecture/platform/trust-boundaries.md`
- `../../docs/architecture/domains/identity-and-access.md`
- `../../docs/architecture/domains/secrets-and-recovery.md`
- `../../docs/architecture/domains/gitops-and-machine-trust.md`
- `../../docs/architecture/domains/host-control.md`
- `../../docs/architecture/domains/ai-and-agentic.md`

Then read the component or product security view that actually matches the
change.

## Workflow

1. Identify the affected review areas:
   - identity
   - secrets
   - delivery
   - runtime
   - AI
2. Separate:
   - design intent
   - implemented control
   - operating evidence
3. Find the concrete `security-architecture` artifact the owner repo should
   reference.
4. Decide whether the change needs:
   - an existing artifact reference only
   - a fresh security delta review
   - a durable security decision or ADR
   - an explicit exception or waiver
5. When an owner-repo change record declares `security_evidence`, run the
   workspace structured-record preflight for that change record and ensure
   `security-architecture/registers/security-change-record-index.yaml` is
   regenerated and landed as a dependency before final closure.
6. If delegated execution is in use, keep the security authority explicit:
   - sub-agents may implement bounded repo-local slices
   - the main agent retains security decision closure
   - the main agent retains final landing judgment for security-significant work
   - delegated workers must not close reviews, accept risk, or treat themselves
     as independent security authorities
7. Push implementation changes back to the owner repo. Keep this repo focused
   on reviewable security artifacts, not delivery logic.
8. When a fresh delta review is required, use
   `docs/reviews/security-delta-review-process.md` and update
   `registers/review-inventory.yaml` with:
   - `latest_change_review.status`
   - `latest_change_review.decision`
   - `latest_change_review.review_areas`
   - `latest_change_review.review_trigger_ids`

## Guardrails

- Do not accept a repo-name reference as a substitute for a concrete security
  artifact.
- If the control exists only in code and not in reviewable artifacts, call the
  governance story incomplete.
- If a delivery repo changed a trust boundary without updating its security
  references, fix that gap in the same work or flag the exception explicitly.
- Do not treat a security-evidenced owner-repo change record as complete while
  the generated security change-record index is stale or unmerged.
- If the change matches a repo-rule security delta trigger, do not treat the
  baseline review as sufficient by itself.
- If delegated workers are involved, require the review artifact to say who
  retains security closure and final landing judgment.
- Do not let delegated execution widen trust by convenience. If the delegated
  packet or workflow would allow live mutation, secret handling, security
  closure, or final approval without the main agent, treat that as a control
  failure rather than an acceptable shortcut.
- Route findings back into active owner work, ART risks or blockers, or the
  remediation inventory instead of leaving them as passive review prose.

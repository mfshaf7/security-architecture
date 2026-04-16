# Security Review Checklist

Use this checklist for platform, component, and product reviews. Record the
result under `docs/reviews/platform/`, `docs/reviews/components/`, or
`docs/reviews/products/` based on scope.

## Identity

- does this change introduce a new human or machine identity
- is least privilege defined
- is break-glass separated from routine access

## Secrets

- does this change introduce a new secret
- is the storage location approved
- is owner and rotation cadence defined

## Delivery

- does this change alter GitOps or controller trust
- are credentials managed and reviewable
- is rollback preserved

## Runtime

- does this change cross into privileged host or control-plane actions
- are policy and audit controls preserved

## Visibility

- can operators tell what version or commit is running
- is there a health, log, or attestation surface that matches the risk
- is the audit trail location documented when the change crosses a privileged
  boundary

## Documentation

- does the owning repo README still describe the current ownership and workflow
- were operator docs or runbooks updated if the live operating model changed
- can another reviewer understand the control without relying on tribal
  knowledge

## Governance

- does this review change a durable control expectation that should update a
  standard, ADR, or architecture view
- did this review identify a lasting finding or risk that belongs in a register
- is the resulting evidence recorded in the correct review or assessment scope

## AI

- does this change introduce model-driven decisions or actions
- can untrusted input shape prompts, tools, or execution paths
- is there output validation and human oversight where needed

# Security Review Checklist

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

## AI

- does this change introduce model-driven decisions or actions
- can untrusted input shape prompts, tools, or execution paths
- is there output validation and human oversight where needed

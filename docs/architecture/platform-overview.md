# Platform Overview

## Purpose

This document provides a single full-platform reference for architectural review and oversight detection.

## Diagram

```mermaid
flowchart TB
  subgraph Human["Human Boundary"]
    TG["Telegram User"]
    OP["Platform Operator"]
    GH["GitHub"]
    AIU["AI / Agent Consumers"]
  end

  subgraph Source["Source And Governance"]
    PE["platform-engineering"]
    SA["security-architecture"]
    OHB["openclaw-host-bridge"]
    OTG["openclaw-telegram-enhanced"]
    OID["openclaw-isolated-deployment"]
  end

  subgraph Control["Shared Control Plane"]
    ARGO["Argo CD"]
    ESO["External Secrets Operator"]
    VAULT["Vault"]
    K8S["Kubernetes API"]
    REPOSEC["Vault-backed Argo repo credential"]
  end

  subgraph Stage["Stage"]
    STGW["openclaw-gateway-stage"]
    STSEC["openclaw-gateway-secrets"]
    STOBS["observability-stage"]
  end

  subgraph Prod["Prod"]
    PRGW["openclaw-gateway"]
    PRSEC["openclaw-gateway-secrets"]
    PROBS["observability"]
  end

  subgraph Host["Windows / WSL Host"]
    TASK["Windows task\nPlatformCoreHostStack"]
    SYS["systemd"]
    HB["openclaw-host-bridge"]
    HR["openclaw-host-recovery"]
    AUD["Host audit logs"]
    MED["Media staging"]
  end

  TG --> PRGW
  TG --> STGW
  AIU --> PRGW
  OP --> ARGO
  OP --> VAULT
  OP --> GH

  GH --> PE
  GH --> SA
  GH --> OHB
  GH --> OTG
  GH --> OID

  PE --> ARGO
  REPOSEC --> ARGO
  ARGO --> Stage
  ARGO --> Prod
  ARGO --> VAULT
  ARGO --> ESO
  K8S --> ARGO
  K8S --> ESO
  K8S --> VAULT
  VAULT --> ESO
  ESO --> STSEC
  ESO --> PRSEC
  ESO --> STOBS
  ESO --> PROBS

  TASK --> SYS
  SYS --> HB
  SYS --> HR
  PRGW --> HB
  STGW --> HB
  HB --> AUD
  HB --> MED
  HB --> HR
```

## Main Review Themes

1. human identity and privilege boundaries
2. machine identity for GitOps and secret delivery
3. host-control trust exposure from user-facing channels
4. AI and agentic interaction paths that may cross trust boundaries

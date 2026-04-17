# OpenProject Idea Backlog And Automation Identity Review

- date: 2026-04-18
- scope: OpenProject-backed canonical idea backlog for operator workflows
- owner repo: `platform-engineering`
- status: change-reviewed

## Summary

Using OpenProject as the canonical backlog for captured ideas and proposals is
appropriate, provided the broker uses a dedicated automation identity and the
workflow remains operator-approved.

This review covers the target project model and automation identity shape. It
does not approve a live deployed broker or a governed AI invocation path.

## Review Areas

### Identity

- a dedicated automation identity is required
- personal operator OpenProject accounts must not be used by the broker
- operator identity and automation identity must remain distinct in audit trails

### Secrets

- the OpenProject API token should live in Vault, not in the Telegram repo or
  the broker source tree
- token scope should be single-purpose for the broker workflow
- token reuse across multiple applications is discouraged

### Runtime

- OpenProject remains the canonical record, not the workflow authority
- the broker may create and update work packages but must not become the
  approval authority for governance

### AI

- AI-assisted triage may help populate suggestion metadata
- the final durable backlog state must still require explicit operator action
- local-model assistance must not be mislabeled as governed AI before the
  governed invocation path exists

## Required Controls

Before the broker becomes active against OpenProject:

1. dedicated automation user created in OpenProject
2. single-purpose API token issued for that user
3. token stored in Vault under a broker-specific secret path
4. dedicated OpenProject project for captured ideas and proposals
5. workflow statuses and custom fields provisioned consistently with the
   contract
6. audit events preserve both operator identity and service identity

## Decision

Approved as the target OpenProject model for phase-1 backlog capture and
triage.

Not yet approved for:

- personal-account automation
- direct Git mutation from the broker
- governed-AI labeling for the triage path

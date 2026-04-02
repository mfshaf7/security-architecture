# Charter

## Mission

Provide an architectural security function for the platform that can evaluate risk, define control requirements, and drive remediation in a governed way.

## Why This Repository Exists

Recent platform incidents exposed security architecture issues that should not be managed as scattered operational fixes:

- shared credentials had excessive blast radius
- recovery material existed without strong governance
- controller credentials drifted out of managed visibility
- platform recovery depended on operator memory

These are architecture and control failures, not only implementation defects.

## Responsibilities

- define target-state security architecture
- document security decisions and tradeoffs
- maintain risk and credential inventories
- define standards for identity, secrets, recovery, and machine trust
- review major platform changes for security impact
- translate security architecture gaps into delivery workstreams

## Non-Goals

- replacing platform delivery repositories
- storing arbitrary runtime secrets by default
- acting as an incident evidence dump

## Decision Style

- assume least privilege by default
- prefer short-lived credentials over static credentials
- prefer federated identity over local passwords
- treat recovery as a governed workflow, not tribal knowledge
- separate human identity, machine identity, and recovery authority

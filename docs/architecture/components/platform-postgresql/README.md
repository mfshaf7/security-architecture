# Platform PostgreSQL Security View

## Purpose

Platform PostgreSQL is the shared data service used by platform-managed product
surfaces.

## Security Role

- stores persistent application and platform data
- concentrates confidentiality, integrity, and backup concerns

## Trust Boundaries

- application access to the database
- operator administrative access
- backup and restore custody

## Principal Risks

- unclear ownership of database administrative access
- weak backup or restore governance
- excessive database privilege for applications

## Required Controls

- database access should be scoped by workload and role
- backup and restore paths should be documented and reviewable
- administrative access should be attributable and rare
- data protection expectations should be explicit per product

## Evidence And Related Docs

- [`../../platform/component-inventory.md`](../../platform/component-inventory.md)
- [`../../../../registers/credential-inventory.md`](../../../../registers/credential-inventory.md)

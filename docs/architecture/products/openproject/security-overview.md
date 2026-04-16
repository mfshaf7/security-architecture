# OpenProject Security Overview

## Purpose

This document summarizes the security posture of OpenProject as a platform
product.

## Major Trust Characteristics

- multi-user web application with authenticated user and admin roles
- persistent application data and backups
- shared platform secret delivery and observability dependencies

## Review Focus

- application admin access and role management
- secret delivery into the runtime
- database access and backup governance
- exposure of operational data through shared observability surfaces

## Related Views

- [`threat-model.md`](threat-model.md)
- [`required-controls.md`](required-controls.md)
- [`../../components/platform-postgresql/README.md`](../../components/platform-postgresql/README.md)
- [`../../components/observability/README.md`](../../components/observability/README.md)

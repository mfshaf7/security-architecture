# OpenClaw Security Architecture

OpenClaw has the highest-trust product surface on the platform because it mixes
user-facing interaction, model-assisted behavior, and optional privileged
host-control.

## Contents

- [`security-overview.md`](security-overview.md)
- [`data-flow-and-boundaries.md`](data-flow-and-boundaries.md)
- [`threat-model.md`](threat-model.md)
- [`required-controls.md`](required-controls.md)

## Why OpenClaw Has A Product Security View

OpenClaw needs its own security overlay because it combines:

- user-facing chat and API surfaces
- model-assisted behavior
- typed host-control tools
- a separate host-side enforcement boundary
- governed stage and prod promotion

Those concerns are too specific and too high-impact to hide inside only generic
platform or component documentation.

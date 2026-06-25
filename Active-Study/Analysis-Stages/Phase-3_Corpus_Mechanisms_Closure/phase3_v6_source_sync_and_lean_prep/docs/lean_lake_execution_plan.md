# Lean/Lake Execution Plan

## Status

```text
LAKE_READY / LOCAL_LEAN_EXECUTION_PENDING
```

## Workspace

```text
lean/
├── lakefile.lean
├── lean-toolchain
├── Phase3.lean
├── Phase3/
│   ├── Core.lean
│   ├── ProjectionLoss.lean
│   ├── ModularB.lean
│   ├── AncientYi.lean
│   ├── Wilhelm.lean
│   └── ShadowCorrespondence.lean
└── source_surfaces/
```

## Execution

```bash
cd lean
lake build
```

## Repair priority

1. `Phase3.Core`: projection-loss/custody theorem.
2. `Phase3.ProjectionLoss`: collision witness adapter.
3. `Phase3.ModularB`: retained carrier schema.
4. `Phase3.AncientYi`: LSD-first carry/lift arithmetic.
5. `Phase3.Wilhelm`: selected-line transition custody.
6. `Phase3.ShadowCorrespondence`: finite quadratic carrier interface.

## Proof-hardening rule

Every `sorry` or axiom must be converted into one of:

```text
PROVED_HERE
OPEN_TARGET_WITH_FALSIFIER
DATA_BLOCKED_GATE
```

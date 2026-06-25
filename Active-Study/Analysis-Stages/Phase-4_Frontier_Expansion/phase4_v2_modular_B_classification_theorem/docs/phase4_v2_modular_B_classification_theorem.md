# Phase 4 v2 — Modular-B Classification Theorem

## Claim

A retained system is a **full Modular-B instance** exactly when it satisfies seven gates:

1. retained carrier,
2. deterministic local refinement,
3. progress measure,
4. completion/capacity law,
5. lift/re-chart law,
6. projection-loss witness,
7. terminal projection separated from custody.

## Classification result

| Domain | Classification |
|---|---|
| Phase/Farey B | `FULL_MODULAR_B_INSTANCE` |
| Ancient Yi octal-place carry | `FULL_MODULAR_B_INSTANCE` |
| Wilhelm six-line ladder | `CARRIER_TRANSITION_BOUNDARY_NOT_FULL_B` |
| Shadow finite residue/orientation carrier | `RETAINED_RESIDUE_TRANSFORM_CHANNEL_NOT_B_WITHOUT_REFINEMENT` |
| Product-only / scalar / carrier-only quotients | `REJECTED_QUOTIENT_ONLY_PROJECTION` |

## Theorem statement

Let `D` be a retained carrier domain. A system `(C_D, B_D, μ_D, Complete_D, L_D, Π_D)` is a full Modular-B instance iff:

```text
B_D : C_D -> C_D is deterministic and local,
μ_D(B_D(x)) > μ_D(x) while not Complete_D(x),
Complete_D(x) marks a finite same-domain boundary,
L_D opens a re-charted carrier and preserves declared payload,
Π_D is terminal and not custody-authoritative,
there exist x != y with Π_D(x)=Π_D(y) and next_D(x) != next_D(y).
```

## Evidence

Phase/Farey reaches `(55,89)` at `uv=4895` from `(1,1)` under repeated B against `Delta=4096`. Ancient Yi satisfies all-7 completion and higher-place opening through depth 6. Wilhelm closes as a 384-event six-line transition graph but lacks intrinsic completion/lift in the current layer. Shadow residue carriers close S/T and orientation-loss gates, but are transform channels until a refinement/lift law is supplied.

## Active falsifier

A full Modular-B classification is falsified by any domain classified full that fails one MB gate. A boundary classification is upgraded by supplying the missing gates.

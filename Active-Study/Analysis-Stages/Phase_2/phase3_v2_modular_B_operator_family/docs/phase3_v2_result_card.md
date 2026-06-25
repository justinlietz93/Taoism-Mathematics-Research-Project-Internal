# Phase 3 v2 Result Card — Modular-B Operator Family

## Verdict

`CONDITIONAL_CLASS_CLAIM_SUPPORTED`

## Claim proven here

`B` is not only the canonical Fibonacci/Farey update. `B` is a retained-carrier refinement schema. The active domain supplies the arithmetic.

## Evidence

### Native Phase/Farey

- Retained carrier: ordered pair `q=(u,v)`.
- Refinement law: `B(u,v)=sort(v,u+v)`.
- Progress: `uv` strictly increases on tested admissible rows.
- Projection-loss witness: `(1,6)` and `(2,3)` share `uv=6`, but refine to `(6,7)` and `(3,5)`.

### Ancient Yi octal-place

- Retained carrier: least-significant-first octal place tuple plus domain length.
- Refinement law: base-8 successor/carry.
- Completion: all active digits are `7`.
- Lift: completion appends a new high place.
- Projection-loss witnesses:
  - low digit only: `7` and `77` share low digit `7`, but continue as `01` and `001`.
  - scalar value only: `0` and `00` share scalar value `0`, but continue as `1` and `10`.

### Wilhelm six-line mutation

- Retained carrier: six-line bit field plus selected line.
- Refinement law: selected-line flip on the six-cube.
- Transition graph: `64 × 6 = 384` directed line-flip transitions.
- Projection-loss witness: `111111:line1` and `111111:line6` share carrier bits but flip to different targets.
- Boundary found: six-line mutation supplies retained transition, but intrinsic completion/lift requires an additional source law.

## Pass signature

```text
GLOBAL_PASS: true
full_schema_instances: 2
carrier_transition_boundary_instances: 1
projection_loss_witnesses: 4
wilhelm_directed_edges: 384
```

## Active falsifier

Find a domain claimed to be a Modular-B instance where omitted projection data still determines every next admissible transition. Such a case would falsify the retained-carrier necessity claim for that domain.

## Next target

`Phase 3 v3 — Projection-Loss Theorem Across Corpus`

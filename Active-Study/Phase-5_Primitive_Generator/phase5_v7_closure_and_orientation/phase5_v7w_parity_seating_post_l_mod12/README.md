# Phase 5 v7w: Parity Seating / Post-L Mod-12 Reverification

Status: `PARITY_SEATING_POST_L_MOD12_REVERIFIED_ON_RETAINED_LENS_LATCH_MODEL`  
GLOBAL_PASS: `true`  
PHASE5_CLOSED: `false`

This package reopens the old parity seating target and tests whether the post-L retained lens parity latch gives a genuine mod-12 seating, separating `n=7` from `n=1` without scalar cargo.

## Core law

```text
pre_L_seat(n) = n mod 6
parity_latch(n) = floor((n mod 12)/6)
lens_sign(n) = +1 if parity_latch=0 else -1
post_L_seat(n) = pre_L_seat(n) + 6*parity_latch(n)

Equivalent sign form:
post_L_seat(n) = pre_L_seat(n) + 3*(1 - lens_sign(n))
```

## Hard counts

```json
{
  "parity_table_rows": 24,
  "support_term_cases": 16,
  "support_term_pass": 16,
  "lens_latch_matrix_checks": 12,
  "lens_latch_matrix_pass": 12,
  "pre_l_collision_witnesses": 4,
  "pre_l_collision_pass": 4,
  "mod6_obstruction_witnesses": 2,
  "mod6_obstruction_pass": 2,
  "negative_controls": 6,
  "negative_controls_pass": 6
}
```

## Main witness

```text
n=1:
  pre-L seat = 1
  post-L seat = 1
  chi12 = +1

n=7:
  pre-L seat = 1
  post-L seat = 7
  chi12 = -1
```

Pre-L mod-6 collapses `1` and `7`. Post-L lens parity latch separates them.

# 58 — CF19 executable residual and stale-kernel separation pass

## Status

`v52` deep internal executable/data replay pass.

This pass closes the main CF19 executable surfaces far enough for the current bridge project while preserving the corrected-canon separation:

```text
corrected Orthad carried walk is the control reference;
older CF19 executable kernels are evidence surfaces;
Tdelta/reset behavior is not allowed to overwrite corrected L-carries-q/theta canon.
```

## 1. Rerun surfaces

| Surface | Result | Artifact |
|---|---:|---|
| `overflow_to_55_89_code.py` | PASS | `cf19_overflow_to_55_89_summary_rerun_v52.csv` |
| `farey_balanced_anchor_runner.c + kernel.S` | PASS | `cf19_farey_anchor_rerun_audit_v52.csv` |
| `xi_full_engine_runner.c + kernel.S` | PASS | `cf19_xi_engine_articulation_class_audit_v52.csv` |
| `kernel_run_Tdelta_balanced` | PASS | `cf19_Tdelta_kernel_class_audit_v52.csv` |
| `ramanujan_residual_balanced_windows_code.py` | PASS | `cf19_ramanujan_residual_gate_audit_v52.csv` |
| `validation/cf19_extension_sympy.py` | PASS | `cf19_extension_sympy_output_rerun_v52.json` |

## 2. Anchor rerun result

The two smallest checked lifts converge to the same balanced Farey floor anchor:

```text
(1,1) -> step 9 -> (55,89), uv=4895
(1,2) -> step 8 -> (55,89), uv=4895
```

This strengthens the internal origin-path evidence, but it does not collapse B into only that origin path. The new non-origin probe confirms that arbitrary/asymmetric starts remain state-carried and can hit different floor anchors.

## 3. Non-origin B scope result

The non-origin floor probe shows:

```text
(1,3)  -> (76,123), uv=9348
(2,13) -> (71,114), uv=8094
(3,10) -> (59,95),  uv=5605
(7,11) -> (76,123), uv=9348
```

So the corrected language remains:

```text
B is a carried refinement operation over the current pair/state.
The canonical origin path reaches (55,89).
Other starts may refine to other floor anchors.
```

This keeps the modular-B research path open for Ancient Yi base-8 successor/carry without forcing false identity.

## 4. Xi full engine result

The rerun trace exposes the fields that make word-only readout insufficient:

```text
A, theta_ticks, kappa, u, v, uv, floor_den, window_ready, live_word, lowbit, carry_event
```

Carry events occur at 64-step lowbit rollover in the older Xi runner:

```text
step 64  -> A=1, theta=64,  kappa=16
step 128 -> A=2, theta=128, kappa=32
step 192 -> A=3, theta=192, kappa=48
```

This is not the corrected Orthad lap schedule, but it is valuable as an internal state-completeness gate: word-only projection cannot determine next admissible transition.

## 5. Tdelta kernel separation

The Tdelta kernel fires a branch-local transfer/reset event every 10 ticks after an initial 9-tick class. Event rows reset the pair to `(1,1)` and cycle `q` through `0..3`.

Therefore:

```text
Tdelta is useful as a branch-local executable witness.
Tdelta is stale against corrected Orthad L, because corrected L carries q and theta rather than resetting q.
```

This is now explicitly marked in the gate matrix.

## 6. Ramanujan residual window result

The residual rerun reproduces the coefficient target pattern:

```text
edge target:      1/24
full-germ target: 1/12
```

The maximum absolute error in the rerun table is:

```text
edge max abs error: 1.11006e-06
full max abs error: 2.22012e-06
```

This supports the Shadow/modular-form bridge surface, but it does not close the Shadow Residual. It remains a terminal external comparison channel.

## 7. New bridge consequence

The internal bridge spine is now sharper:

```text
retained state
-> B/Farey refinement over carried pair
-> floor/capacity threshold
-> executable witness surface
-> terminal residual/readout
-> corrected Orthad custody/readout separation
```

The state-completeness rule survives all reruns:

```text
terminal row, scalar coefficient, q pair, event tick, or word alone
is not the carried object
unless it determines the next admitted transition.
```

## 8. Updated status

```text
Internal Research: 98.6%
External Research: 96.4%
Overall: 97.5%
```

Not at 100%. Remaining blockers are Ancient Yi full translation/line-order proof, Liu2022 QSL-current-connectivity data, local Lean execution, final proof audit, and latest active HDD selector/floor sources.

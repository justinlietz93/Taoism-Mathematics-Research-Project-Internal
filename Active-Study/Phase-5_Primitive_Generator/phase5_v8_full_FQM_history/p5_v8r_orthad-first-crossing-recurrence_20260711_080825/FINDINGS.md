# Findings

## Status

```text
PRIMITIVE_FIRST_CROSSING: PASS
FIRST_L_CARRY: PASS
ACTIVE_AXIS_RECURRENCE: PASS
PRIMARY_PAIRING_RECURRENCE: NOT_YET_DERIVED
ORTHAD_CHART_RECURRENCE: NOT_YET_DERIVED
ORTHAD_RANK_EXTENSION: NOT_YET_DERIVED
ORTHAD_CAUSAL_PROJECTION: NOT_RUN
GAUGE_FQM_WEIL_DESCENT: NOT_RUN
```

## Main result

The full source set does **not** force one exact pairing-first dual-chart recurrence. It forces the primitive custody trace and the local active-axis scalar recurrence, but not the mixed cross-chart pairing.

The smallest missing bridge is:

```text
tau_0 and tau_(t+1)=Phi_U(X_(t+1),W_(t+1),tau_t)
```

where `tau_t=P_t(iota_plus(e_t),iota_minus(e_t))`. The sources specify the local scalar `a_t=i^(local_Q)/(u_t v_t)` and the direction `P -> restrictions/transfers`, but no seed or B/Q/L mutation for `tau_t`.

## Why interesting

This isolates the gap below gauge, FQM, and Weil descent. The problem is not another finite check. It is one missing state-to-mixed-pairing equation. The historical v7u route does not close it because it introduces an `O` event and an ad hoc `pair_c` formula outside the clean primitive alphabet.

## Scope

The package certifies one first crossing and the first next-domain B. It emits no primary-pairing matrix, chart matrix, transfer matrix, overlap residual, projection row, channel field, gauge class, FQM, or Weil action.

## Proved abstractly

**Restriction underdetermination.** Let the retained space contain two chart subspaces. Two bilinear forms can agree on each chart restriction and differ on mixed arguments. Therefore the diagonal restrictions alone do not determine either directed transfer. The source constraints need one additional mixed-pairing recurrence. A Lean attack is included; Lean was unavailable, so no compiled formal-proof claim is made.

## Certified finitely

- Self-selected word: `BQQBBBQBQBBQBBL`.
- Before first L: `A=0`, pair `(55,89)`, phase quarters `5`, `k=5`, `j=6`.
- Immediately after L: `A=1`, pair and phase carried, `k=0`, `j=7`.
- First next-domain primitive: `B`, pair `(89,144)`.
- Active-axis recurrence reaches `i/4895`, latches it at L, and opens active axis `1`.
- Independent oracle agrees with the implementation on all 16 emitted steps.

## Open

- Primary pairing seed and mixed-pairing B/Q/L recurrence.
- Explicit `iota_plus` and `iota_minus`.
- Both chart restrictions and both directed transfers.
- Overset overlap/cocycle residuals.
- Orthad rank extension at the first L.
- Terminal projection.
- Gauge/FQM/Weil descent.

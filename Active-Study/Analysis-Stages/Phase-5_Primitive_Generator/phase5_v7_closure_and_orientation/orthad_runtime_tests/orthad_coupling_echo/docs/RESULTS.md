# Results

Run command:

```bash
python -m orthad_coupling_echo.run_experiment --out outputs
```

## Result card

```text
GLOBAL_PASS: true
STATUS: SMOKE_SUPPORTED_WORTH_PURSUING_NOT_A_THEOREM
```

Gates:

```text
legal_rewrite_invariance: PASS
same_projection_different_retained_history: PASS
illegal_cocycle_rejected: PASS
positive_coupling_echo_gain: PASS
telemetry_flags_bad_history: PASS
```

## Key history comparisons

### H1 vs H2

H1 and H2 differ only by a legal swap of independent local events. They reduce to the same normal form and the same coupling matrix.

```text
C(H1)=C(H2)=
[0 4 4]
[4 0 4]
[4 4 0]
```

### H1 vs H3

H1 and H3 share the same visible projection, but they retain different coupling objects.

```text
visible(H1)=5
visible(H3)=5

C(H1) != C(H3)
```

This reproduces the exact Phase 5 warning: terminal projection alone is not enough.

### H4

H4 has a nonzero cocycle residual and is rejected.

```text
residual(H4)=4
admitted=false
```

Telemetry also emits a topology spike and cycle inhibition.

## Echo gate

For admitted histories, the extracted C improves equal-budget echo recovery over a blind direct-sum baseline.

The baseline and assisted paths both spend one matrix-vector evaluation. The baseline uses zero cross-axis C; the assisted path uses the retained-history extracted C.

In this first smoke test, assisted recovery is exact, so CEG=1.0 for admitted positive histories. That is intentionally not the final benchmark. The next version should add noise, partial observation, larger chart graphs, and adversarial histories.

## Verdict

The result is strong enough to continue the specialized VDM-guided overset path as an experimental compiler layer.

It is not strong enough to replace external research permanently. The theorem spine still needs trace theory, cocycles/holonomy, and finite quadratic modules.

# Findings

## Status

```text
J_TRACK_CLOSED_ON_AFFINE_CEILING_MODEL
FINITE_QBL_CORRESPONDENCE_RETAINED_A0_A10000
SPECIFIC_ORBIT_EQUIDISTRIBUTION_NOT_PROVED
GAUGE_FQM_PRIME_MAP_NOT_YET_DERIVED
GLOBAL_THRESHOLD_BRIDGE_NOT_YET_PROVED
```

## Main result

The affine ceiling recurrence gives an exact three-piece interval map on `E in (-1,0]`. Under `1/6<a<1/4`, its stationary Lebesgue joint edge measure is

\[
J=
\begin{pmatrix}
0 & (1-3a)/2 & a/2\\
(1-2a)/4 & 1/4 & a/2\\
(1-2a)/4 & 3a/2-1/4 & 0
\end{pmatrix}.
\]

Seven entries are positive, `J_77=J_99=0`, the row and column marginals are `(1/2-a,1/2,a)`, and the induced conditional matrix is stationary for that measure.

The `9999` finite transitions for `A=2..10000` satisfy:

```text
empirical versus J:
    max error = 0.006825682568256826
    L1        = 0.014047774522984873
    TV        = 0.007023887261492436

empirical versus Parry K:
    max error = 0.049718901381709301
    L1        = 0.184010189493662757
    TV        = 0.092005094746831379
```

## Why interesting

The allowed symbolic language and the metric orbit share the same seven-edge support but not the same invariant measure. The primitive adjacency matrix has Perron root `1+sqrt(2)` and Parry state measure `(1/4,1/2,1/4)`, while the finite QBL orbit is much closer to the Lebesgue geometry `(1/2-a,1/2,a)` and to the joint law `J`.

## Scope

### Proved abstractly

- the affine ceiling-to-error-map bridge for `A>=1`;
- the exact half-open endpoint convention;
- all nine entries of `J`, including seven positive and two zero entries;
- row sums, column sums, total mass, `P`, and stationarity;
- `M`, `M^2>0`, Perron data, Parry state law, and Parry edge law `K`;
- all five defect-mass identities.

### Certified finitely

- prior exact Fibonacci threshold agreement with the affine ceiling model for `A=0..10000`;
- no computed boundary hit through `A=10000`, with stable `3500/4500` digit runs;
- exact finite transition counts and comparison metrics for `A=2..10000`.

### Observed

- the finite edge and state distributions are closer to the Lebesgue model than to the Parry model;
- the finite defect frequencies remain within `0.006826` absolute error of the Lebesgue benchmark.

### Open

- specific-orbit equidistribution or normality;
- a global theorem identifying the exact Fibonacci threshold with `ceil(y_A)`;
- any chart, gauge, holonomy, FQM, or Weil map from `d_A=+/-1` or count primality.

# Audit Results

## Verdict

```text
REVISE
ADOPT_J_MATHEMATICAL_CORE
WITHHOLD_CLOSED_DELIVERABLE_STATUS
RETAIN_PRIOR_EXPERIMENT_AS_FINITE_PROVENANCE
```

The matrix derivation is correct. The response still needs revision because its standalone document omits several load-bearing bridges and was not delivered as the required reproducible experiment package.

## Verified mathematical core

The supplied document hash matches:

```text
0509505200e2d3289363934103570b3cc36833aeda6be3e9d27ced3bc0835bc8
```

For

```text
a = 0.235122302145392063967494935566373130411562717981...
```

the audited matrix is:

```text
J =
[[0,                  0.1473165467819119, 0.1175611510726960],
 [0.1324388489273040, 0.2500000000000000, 0.1175611510726960],
 [0.1324388489273040, 0.1026834532180881, 0                 ]]
```

The following checks pass:

- seven allowed entries are positive;
- `J[7,7] = 0` and `J[9,9] = 0`;
- row sums and column sums both equal `(1/2-a, 1/2, a)`;
- total mass is `1`;
- the five defect masses reduce to the stated formulas;
- the Perron root is `1 + sqrt(2)`;
- `(1, sqrt(2), 1)` satisfies the Perron eigenvector equation;
- the Parry state distribution is `(1/4, 1/2, 1/4)`.

## Direct empirical edge comparison

The prior experiment records `9999` transitions over `A=2..10000`:

```text
counts =
[[   0, 1475, 1162],
 [1316, 2568, 1158],
 [1321,  999,    0]]
```

The empirical joint transition matrix is closer to `J` than to the Parry joint edge measure.

```text
Empirical versus J
max absolute error: 0.006825682568256826
L1 error:           0.014047774522984873
total variation:    0.007023887261492436

Empirical versus Parry joint edge measure
max absolute error: 0.049718901381709301
L1 error:           0.184010189493662757
total variation:    0.092005094746831379
```

This supports finite agreement with the Lebesgue geometry. It does not prove that the specific orbit is equidistributed.

## Missing bridges in the document

### 1. Ceiling law to interval map

The note starts from

```text
c = ceil(2E + gamma)
F_c(E) = 2E + gamma - c
```

but does not explicitly derive this from

```text
y_A = 2y_(A-1) + gamma
T_A = ceil(y_A)
E_A = y_A - T_A
c_A = T_A - 2T_(A-1)
```

That bridge belongs in the document.

### 2. Exact endpoint law

For `E_A = y_A - ceil(y_A)`, the exact range is naturally `(-1,0]`. The endpoint is measure-zero for the Lebesgue calculation, but its assignment matters for an exact individual orbit. No global proof excluding boundary hits was supplied.

### 3. Conditional transition matrix

`J` is a joint mass matrix. The document should also define

```text
P_ij = J_ij / pi_i
```

and verify that `P` is row-stochastic and that `pi P = pi`.

### 4. Direct Parry edge comparison

The note compares state marginals and aggregated defects. It does not display the empirical joint edge matrix or compare it directly with both `J` and the Parry joint edge measure.

### 5. Global threshold route

The Binet plus linear-forms-in-logarithms route is an outline only. No constants, lower bound, crossover, or finite remainder proof were supplied.

Correct status:

```text
GLOBAL THRESHOLD PROOF ROUTE: PROPOSED
GLOBAL THRESHOLD PROOF: NOT COMPLETED
```

## Package audit

### Integrity

The prior experiment package passes its integrity contract:

- all `26` listed files match their byte counts and SHA-256 values;
- the listed set equals every archived file except `MANIFEST.json`.

The prime-watch zip also passes all five hashes in `MANIFEST.sha256`.

### Reproducibility defects

The prior experiment package is not fully rebuildable from its included command and script:

- it contains one notebook, not separate source and executed notebooks;
- dependency names are not pinned to exact versions;
- no package-builder script is present;
- the README command omits `--out`;
- the analysis script references only `summary.json` and `scan.csv`;
- it cannot regenerate the archived figures, database, HDF5, traces, notebook, or manifest;
- current `outputs/`, `proofs/`, and `trace/` folders are absent;
- legacy `output_data/`, `lean/`, and `trace_logs/` folders are used;
- no Lean compiler log is present;
- the source map treats an older Phase 5 ledger as active and omits the current primitive-custody/Orthad law.

The prime-watch zip is valid provenance, but it is not a package in the current experiment format.

## Authority boundary retained

```text
SPECIFIC ORBIT EQUIDISTRIBUTION: NOT PROVED
GAUGE/FQM MAP FROM d_A=+/-1: NOT YET DERIVED
GLOBAL T_A=ceil(y_A) BRIDGE: NOT YET PROVED
```

Counts, defects, or primality do not establish an Orthad chart matrix, gauge value, holonomy, FQM class, or Weil projection.

## Reproduction

Run:

```bash
python scripts/run_audit.py
```

The exact machine-readable evidence is in `outputs/`.

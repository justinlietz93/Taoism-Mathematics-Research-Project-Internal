# Coupling Tensor Definitions

## Pairwise native coupling tensor

```text
C=(c_ij)
c_ij=Σ_b sign_b(q_i(b)+1)(q_j(b)+1) mod L_ij
L_ij=lcm(D_i,D_j)
```

## Representative admissibility

```text
L_ij | c_ij D_i
L_ij | c_ij D_j
```

## Triple incidence

```text
t_ijk=Σ_b sign_b(q_i(b)+1)(q_j(b)+1)(q_k(b)+1) mod lcm(D_i,D_j,D_k)
```

Triple incidence is accepted into the Weil layer only if it passes quadraticity. In v7g, independent cubic triple terms failed that gate.

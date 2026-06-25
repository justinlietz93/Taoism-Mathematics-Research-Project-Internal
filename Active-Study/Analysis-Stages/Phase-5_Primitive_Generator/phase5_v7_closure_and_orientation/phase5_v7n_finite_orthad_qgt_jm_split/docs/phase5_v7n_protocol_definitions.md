# Phase 5 v7n Protocol Definitions

## Finite Orthad overlap tensor

```text
H(h) = M(h) + iJ(h)
```

`h` is an admissible trace-normalized retained QBL history.

## J-limb

`J` is the antisymmetric readout of oriented overlap holonomy:

```text
J_ij = c_native(i,j) / lcm(D_i,D_j)
J_ji = -J_ij
```

## M-limb

`M` is the symmetric positive gluing-cost metric. It is built as a weighted graph Laplacian over shared boundary/latch incidence.

```text
x^T M x = sum_True w_ij (x_i - x_j)^2
```

## Product coupling projection

```text
Pi_C(J)_ij = round(lcm(D_i,D_j) * J_ij) mod lcm(D_i,D_j)
```

## Gates

```text
J^T = -J
M^T = M
M >= 0
H^* = H
M * 1 = 0
x^T J x = 0
Pi_C(J) = c_native
legal trace rewrites preserve gauge class
```

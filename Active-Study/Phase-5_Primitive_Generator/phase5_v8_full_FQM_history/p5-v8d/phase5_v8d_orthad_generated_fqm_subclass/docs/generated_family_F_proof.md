# Phase 5 v8d Result

## Result

`V8D_ORTHAD_GENERATED_FQM_SUBCLASS_CLOSED_POSITIVE_WITH_2_PRIMARY_CLASSIFIER_WALL_BLOCKING_OPEN`

## Family F

For the defined Orthad T-record semantics, every retained FQM presentation lands in the family:

```text
A = Π_i Z/D_iZ, with D_i even doubled carriers
b(x,y) = Σ_i x_i y_i/D_i + Σ_{i<j} c_ij (x_i y_j + x_j y_i)/lcm(D_i,D_j) mod 1
q(x) = 1/2 b(x,x) mod 1
```

Representative invariance requires:

```text
lcm(D_i,D_j) | c_ij D_i
lcm(D_i,D_j) | c_ij D_j
```

Equivalently `c_ij` is a multiple of `lcm(D_i,D_j)/gcd(D_i,D_j)`.

## Containment proof

The proof is by arity induction over T records:

- `Q_i`, `B_i`, and `L_i` are unary retained updates and can only change or create a single doubled-cyclic diagonal carrier.
- `O_ij` is binary overlap handoff and can only create pairwise bilinear edge data.
- `R_i` is terminal projection and does not mutate retained FQM state.
- Concatenation of records adds diagonal and pairwise terms, so no defined retained T-record creates a trilinear FQM slot.

## v8d decisive outcomes

- Z/12Z chi12 skeleton is reachable.
- No genuine nondecomposable triple incidence is generated in the defined T system.
- Cross-coupled pairwise presentations are reachable.
- Generated even/mixed cross-coupled witnesses hit the 2-primary classifier wall.
- Therefore v8c remains suspended.

## What is not claimed

- No complete universal FQM classifier.
- No full Nikulin / Conway-Sloane 2-adic closure.
- No Phase 5 closure.

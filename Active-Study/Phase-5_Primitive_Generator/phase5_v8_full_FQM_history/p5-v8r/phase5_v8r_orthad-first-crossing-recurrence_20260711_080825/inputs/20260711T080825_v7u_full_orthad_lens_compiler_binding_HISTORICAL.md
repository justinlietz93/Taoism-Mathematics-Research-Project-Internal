# Phase 5 v7u: Full Orthad Lens Compiler Binding

## Objective

Bind the finite Orthad lens compiler to the full v7q/v7t chain.

```text
native retained QBL history
  -> compiled lens state
  -> native transition assignment T
  -> finite module presentation
  -> mixed-prime classifier key
```

## Definitions

### Lens axis

Each lens axis carries:

```text
(u,v), uv, D=2uv, phase mod 4, latch flag, local clock
```

The retained lens value is represented exactly as:

```text
lens(a) = (1/uv_a) * i^(phase_a)
```

### Primitive events

```text
Q_a:
  phase_a += 1 mod 4

B_a:
  (u,v)_a -> sort(v,u+v)

L_a:
  latch axis a
  create newborn axis a+1
  record contact/latch increment

O_ab:
  assign overlap transition lens(b)/lens(a)
  extract admissible pair coefficient c_ab mod lcm(D_a,D_b)

R_a:
  terminal readout only
```

### Transition assignment

For any compiler event, `T` is produced from retained lens values before and after the event. For overlap events:

```text
T_ab = lens(b) / lens(a)
```

For every chart triangle, the compiler checks:

```text
T_ab * T_bc * T_ca = 1
```

### T-to-FQM extraction

Each compiled state produces:

```text
D = [D_0, ..., D_n]
C_ij in Z / lcm(D_i,D_j)Z
```

The pair coefficient is forced into the representative-invariant residue class:

```text
c_ij = k * lcm(D_i,D_j) / gcd(D_i,D_j)
```

### Nonbruteforce classifier

The classifier does not enumerate full large-rank orbits. It builds a deterministic p-primary graph-refinement key from:

```text
axis cyclic factors D_i
pair couplings C_ij
p-adic valuations
2-primary policy tags
```

This is a strong invariant key, not yet a complete isometry theorem.

## Results

See `outputs/phase5_v7u_verification_summary.json`.

The pass tested ranks up to 12, mixed cyclic carriers, mixed-prime decompositions, cocycle identities, support-derived rewrite invariance, and negative controls.

## Boundary

This pass does not claim a complete Nikulin / Conway-Sloane finite quadratic module classifier. It binds the Orthad compiler to the FQM extraction pipeline and replaces brute-force orbit enumeration with a scalable invariant key.

# Protocol Definitions

## Classification

Axiom-core / Phase Calculus retained-state protocol.

## Objective

Define the missing transition assignment

```text
support-normalized QBL history
  -> native lens transition assignment T
  -> cocycle / holonomy data
  -> finite quadratic module target later
```

## Definition of T

The native Orthad lens value of axis `a` is represented finitely as

```text
lens(a) = anchor(a) * i^theta(a)
anchor(a) = 1 / (u_a v_a)
```

The transition assignment is computed by ratios of retained lens values:

```text
T(Q_a)  = lens_after(a) / lens_before(a)
T(B_a)  = lens_after(a) / lens_before(a)
T(L_a)  = lens_newborn(a+1) / lens_latched(a), with contact record
T(O_ab) = lens(b) / lens(a)
T(R_a)  = identity, terminal projection only
```

## Gates

1. Native assignment gate: every transition is generated from lens support.
2. Rewrite gate: legal support-derived rewrites preserve retained transition signatures.
3. Cocycle gate: `T_ab T_bc T_ca = 1` on admissible chart triangles.
4. Gauge gate: local frame changes preserve cycle holonomy.
5. Negative gate: birth violations, bad cocycles, and terminal readout mutation are rejected.

## Result

`NATIVE_TRANSITION_ASSIGNMENT_SUPPORTED_ON_TESTED_ORTHAD_LENS_SUPPORT_MODEL`

The pass supports transition assignment `T` on the tested native support model. It does not yet prove the full arbitrary-history classifier.

# Phase 5 v4: Character and Shadow Residual Re-entry

## Claim

The generated Orthad overset dual-lens operators re-enter the shadow residual layer as retained carrier actions:

- `K_N` acts as the generated cross-chart transfer.
- `G_N` acts as the generated quadratic self-twist.
- an even retained character vector `a(-r)=a(r)` preserves orientation state.
- signed bilateral scalar projection cancels.
- positive-orientation readout remains nonzero.

## Canonical generated operators

```text
K_N(r,s) = N^(-1/2) exp(-2πi r s/N)
G_N(r)   = exp(πi r²/N)
```

## Cases

```text
chi12, N=12:
  scalar character quotient closes.

chi8, N=8:
  scalar character quotient closes.

Legendre-5, N=10:
  full vector carrier required.

Legendre-13, N=26:
  full vector carrier required.
```

## Interpretation

The old Shadow Residual issue splits cleanly:

```text
scalar coefficient/readout:
  external at carried-state level

retained residue/orientation vector:
  internal carrier

orientation-forgetting scalar projection:
  cancels

positive-orientation readout:
  nonzero
```

## Boundary

The Legendre cases are not failures. They confirm that the canonical Orthad carrier is vector-valued first. Scalar quotient closure is special, not general.

## Sidecar

`mock_shadow_dictionary/` records the Orthad-to-mock-shadow dictionary. The Ramanujan `f(q)` sidecar is included as an external literature alignment target and does not contaminate the sealed character-carrier gates.

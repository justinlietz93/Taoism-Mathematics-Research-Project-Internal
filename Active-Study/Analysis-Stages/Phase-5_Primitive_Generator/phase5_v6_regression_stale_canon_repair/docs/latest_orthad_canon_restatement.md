# Latest Orthad Canon Restatement

## Canonical statement

The Orthad is an overset dual-lens readout over finite cyclic residue-orientation carriers.

```text
OmegaPlus:
  point-orientation chart e_r

OmegaMinus:
  successor eigen-cochain chart chi_s

Cross-chart transfer:
  K_N(r,s) = chi_s(e_r)

Same-chart self-read:
  preserves diagonal retained trace

Reverse-transfer quadratic self-twist:
  G_N(r) = exp(πi r²/N)
```

## Subcase rule

The old diagonal lens is valid as:

```text
same-chart collapse / self-read
```

It is invalid as:

```text
complete Orthad definition
```

## Documentation rule

Any document that states or implies "the Orthad lens is diagonal" must be patched to say:

```text
The diagonal lens is the same-chart collapse of the Orthad. The full Orthad is overset dual-lens: same-chart self-read + cross-chart transfer + quadratic self-twist.
```

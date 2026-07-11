# L Pairing Extension

```text
L_PAIRING_EXTENSION: NOT_YET_DERIVED
MISSING_MAP: L_pairing : (P_t,Xi_t,Xi_{t+1},W_{t+1}) -> P_{t+1}
```

Architectural obligations:

```text
retain old block
latch completed active axis
append one new orthogonal active axis
architectural rank 1 -> 2
```

Schematic target:

```text
[ P_t   C_t   ]
[ C_t*  p_new ]
```

Once a scalar-valued form type is fixed, orthogonality would force the mixed birth block to vanish in a compatible basis. This pass does not emit `C_t=0` as a derived matrix because the pairing type and orthogonality semantics remain open. `p_new` is also underived.

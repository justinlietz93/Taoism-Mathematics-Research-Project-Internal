# Architecture Diagram Correction Sheet

The supplied image is the prior layout master and conceptual orientation only.

Where the image glyph and written notation disagree, the written notation controls.

```text
Primitive custody state:      Xi_t
Fully retained lifted state:  Xi_hat_t
Orthad:                        ⌞Xi_hat_t⌝
```

Corrections applied in this package:

```text
Q increments both k and j.
k is a local phase-position index, not pairing rank.
r_t is reserved for pairing rank.
Xi_t is the custody state.
Xi_hat_t is the fully retained lifted state.
⌞Xi_hat_t⌝ wraps and reads Xi_hat_t; it is not Xi_hat_t.
The sphere is projection-side schematic geometry only.
The exact pairing type, seed, recurrence, charts, and transfers remain open.
The native successor on Z/12Z is downstream, not the generative start.
```

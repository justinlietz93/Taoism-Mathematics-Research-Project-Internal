# Architecture Diagram Reference

Required external attachment:

```text
Neon schematic of generative architecture.png
```

The image is the conceptual layout master. The written notation and custody law control every imperfect glyph or abbreviated label.

The controlling dependency order is:

```text
primitive custody
-> primary pairing
-> chart restrictions
-> directed transfers
-> fully retained lifted state
-> terminal projection
```

Controlling notation:

```text
Primitive custody state:       Xi_t
Fully retained lifted state:   Xi_hat_t
Orthad wrapper/reader:          ⌞Xi_hat_t⌝
```

Key diagram corrections:

1. Q increments both `k` and `j`.
2. `k` is not pairing rank.
3. Pairing rank must use a separate symbol such as `r_t`.
4. `Xi_t` is custody state, not the complete retained lifted state.
5. `Xi_hat_t` is the complete retained lifted state.
6. `⌞Xi_hat_t⌝` wraps and reads `Xi_hat_t`; the two are not identical.
7. The projection-side sphere is schematic and downstream.
8. Z/12Z is not the generative start or the complete retained object.

# Architecture Diagram Correction Sheet

The diagram is accepted as the conceptual layout master.

The written law controls notation and exact custody updates.

## Adopted diagram content

- The custody state selects `B`, `Q`, or `L`.
- The Orthad does not choose the primitive letter.
- The primary pairing is generative.
- Both charts are restrictions of one pairing.
- Both directed transfers belong to the same retained object.
- Pairing, charts, and transfers evolve during each primitive tick.
- Projection occurs only after the lifted evolution is complete.
- The projection-side sphere is not the retained object.
- The old pairing block is retained at `L` and one new axis is appended.

## Written corrections

1. Use `Xi_t` for the primitive custody state.
2. Use `Xi_hat_t` for the fully retained lifted state.
3. Use `⌞Xi_hat_t⌝` for the Orthad wrapping and reading `Xi_hat_t`.
4. `Xi_hat_t` and `⌞Xi_hat_t⌝` are not identical objects.
5. `Q` increments both `k` and `j`.
6. `k` is the local phase-position index. It is not pairing rank.
7. Use a separate symbol such as `r_t = rank(P_t)` for pairing rank.
8. Split the `L` step into custody mutation and Orthad mutation.
9. `Z/12Z` is downstream local finite structure until a stronger type is proved.
10. The Bloch sphere remains projection-side schematic geometry.

## Controlling causal order

```text
primitive custody
-> primary pairing
-> chart restrictions
-> directed transfers
-> fully retained lifted state
-> terminal projection
```

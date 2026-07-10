# Radical-first protocol

1. Compute `Rad = {x : b(x,y)=0 for all y}` before pivoting.
2. Emit the multiset of `q` values on `Rad`.
3. If the radical is trivial, run the already validated nondegenerate A/UV path.
4. If the radical is a direct summand, split radical blocks `R_D(q)` first, then run A/UV on the complement.
5. If a non-summand radical appears, stop and book `BLOCKING_OPEN_PENDING_FILTRATION_INVARIANTS`.

In v8j's stated ranges, no non-summand radical was detected.

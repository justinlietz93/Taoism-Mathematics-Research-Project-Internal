# Assumption Lock

## Primary authority

`QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md` is the governing law for this audit.

## Licensed facts

- Primitive authority is `{B,Q,L}` only.
- The next primitive self-selects from the current state with strict priority `B > Q > L`.
- The exact first crossing from `(1,1)` is `BQQBBBQBQBBQBBL`.
- The first floor anchor is `(55,89)`.
- Five actual `Q` steps earn the phase `i` at that boundary.
- `L` increments only the dimensional counter, resets only the new domain-local position index, and carries the pair and phase unchanged.
- The first next-domain `B` is `(55,89) -> (89,144)`.
- The Orthad exists throughout the primitive evolution, mutates on each primitive tick, and projects only after halt.

## Forbidden imports

The audit and next experiment may not use any of these as primitive authority:

- `R/S/T` selection or scheduling;
- a fixed 64-tick window;
- an externally supplied primitive word;
- literal `BL` as the first crossing;
- `FLOOR` as an operator, processing stage, or third event;
- resetting the pair or phase at `L`;
- inserting a 12-seat carrier or `lap2=-lap1` sign by hand;
- hard-coding `i/uv` without deriving phase from executed `Q` steps;
- treating raw chart matrices as the retained invariant;
- claiming gauge, FQM, Weil, or final Orthad descent without an explicit construction and certificate.

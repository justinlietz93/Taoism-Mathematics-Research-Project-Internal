# Phase 4 v3 — Projection-Loss Formalization

## Status

```text
FORMAL_THEOREM_PACKAGE_SUPPORTED_BY_FINITE_CORPUS_INSTANTIATIONS
GLOBAL_PASS: true
```

## Claim

A projection is custody-admissible for a retained transition system exactly when it preserves enough retained state to determine the next admissible retained transition.

Formally, for retained state space `S`, transition `E:S -> S`, and projection `Π:S -> P`:

```text
CustodyAdmissible(Π,E) := exists G:P->S such that E = G ∘ Π.
```

A projection-loss witness is:

```text
Π(x) = Π(y) and E(x) != E(y).
```

This witness proves `Π` is not custody-admissible.

## Quotient/custody split

Projected quotient closure is different:

```text
QuotientAdmissible(Π,E) := exists H:P->P such that Π ∘ E = H ∘ Π.
```

Some shadows are lawful quotients. They are not automatically custody-complete. Phase 4 v3 locks the distinction with finite witnesses.

## Corpus results

| Domain | Projection | Result |
|---|---|---|
| Phase visible/Q4 memory | visible_phase_mod_4 | CUSTODY_FAIL_QUOTIENT_PASS |
| Phase Farey/B refinement | product_uv | CUSTODY_FAIL_QUOTIENT_FAIL |
| Ancient Yi low digit | low_digit | CUSTODY_FAIL_QUOTIENT_PASS |
| Ancient Yi scalar zero | scalar_value | CUSTODY_FAIL_QUOTIENT_PASS |
| Wilhelm six-line selected event | carrier_bits | CUSTODY_FAIL_QUOTIENT_FAIL |
| Monodromy double-cover memory | visible_sheet | CUSTODY_FAIL_QUOTIENT_PASS |
| Shadow orientation channel | scalar_bilateral_projection | CUSTODY_FAIL_QUOTIENT_FAIL |
| Pencil/Yin-Yang chart transfer | component_tuple | CUSTODY_FAIL_QUOTIENT_FAIL |


## Theorem

If two retained states collide under projection but diverge under the retained transition, then no transition on the projected readout can reconstruct retained custody.

## Falsification target

Find a domain where `Π(x)=Π(y)` and `E(x)!=E(y)` but a function `G:P->S` still satisfies `E=G∘Π`. That would falsify the theorem. The finite proof says this cannot happen without changing the definitions.

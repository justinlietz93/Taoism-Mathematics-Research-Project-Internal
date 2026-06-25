# Phase 3 v3: Projection-Loss Theorem Across Corpus

## Result

```text
STATUS: THEOREM_SCHEMA_SUPPORTED_BY_CORPUS_WITNESSES
GLOBAL_PASS: True
WITNESS_COUNT: 8
```

## Theorem schema

A projection is bridge-admissible for custody exactly when it preserves enough retained state to determine the next admissible retained transition under the relevant operator family.

Let `S` be retained state, `E:S->S` the next admissible transition, and `Π:S->P` a projection.

Custody-complete projection:

```text
exists G:P->S such that E = G o Π
```

Projection-loss witness:

```text
Π(x) = Π(y) and E(x) != E(y)
```

Projected quotient-complete projection:

```text
exists H:P->P such that Π o E = H o Π
```

This is weaker than custody. It licenses terminal projected dynamics, not custody authorship.

## Corpus witnesses

The package ships eight finite witnesses:

1. Phase visible/Q4 memory: same visible phase, different completed-turn memory.
2. Phase Farey/B refinement: `(1,6)` and `(2,3)` share `uv=6`, but B-images differ.
3. Ancient Yi low digit: `7` and `77` share low digit, but successor/lift differs.
4. Ancient Yi scalar value: `0` and `00` share scalar value, but retained next state differs.
5. Wilhelm six-line: same carrier `111111`, different selected line, different target.
6. Monodromy double-cover: same sheet, different kappa/history.
7. Shadow residual orientation: scalar symmetric projection zero, retained positive channel nonzero.
8. Pencil/Yin-Yang vector chart: same component tuple, different basis transfer registry.

## Claim status

The theorem is supported across all tested finite witnesses. The Liu/MFE row is positioned as the next data-gated row: once QSL/current/connectivity data is available, the same custody gate applies.

## Falsification target

To falsify the class theorem for a domain, construct a stripped projection `Π` and a function `G` such that the full retained next transition is recovered from projection alone:

```text
E = G o Π
```

To falsify the quotient/custody split, prove that projected commutation `Π o E = H o Π` implies full custody completeness without injectivity or a canonical section.

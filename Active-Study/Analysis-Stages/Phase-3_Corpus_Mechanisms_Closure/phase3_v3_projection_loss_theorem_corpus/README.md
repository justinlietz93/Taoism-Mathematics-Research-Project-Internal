# Phase 3 v3: Projection-Loss Theorem Across Corpus

This package proves the projection-loss theorem schema across the available Phase/Tao corpus by shipping finite collision witnesses.

Primary result:

```text
A projection is bridge-admissible for custody exactly when it preserves enough retained state to determine the next admissible retained transition under the relevant operator family.
```

Run:

```bash
python3 scripts/phase3_v3_projection_loss_theorem_corpus.py
```

Outputs are in `outputs/`. The Lean proof surface is in `proofs/`. The notebook is self-contained and uses no file IO.

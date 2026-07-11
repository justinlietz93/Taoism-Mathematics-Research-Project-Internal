# p5_v8t Orthad native-successor and carrier gap

This package preserves the accepted p5_v8s primitive baseline and analyzes the additional v7 repository sources in `phase5-research.txt`.

First derivation to open: `docs/20260711T105245_retained_carrier_and_basis.md`.

## Rebuild

```bash
python scripts/20260711T105245_rebuild.py
```

## Verify from the exact ZIP

```bash
python scripts/20260711T105245_verify.py /path/to/p5_v8t_orthad-native-successor-and-carrier-gap_20260711_105245.zip
```

The verifier extracts the ZIP into a fresh temporary directory, disables bytecode, disables pytest cache creation, runs the current tests, verifies schemas, recomputes evidence gates, and checks manifest/archive path equality.

## Accepted baseline

`p5_v8s_orthad-atlas-and-transfer-gap_20260711_085540.zip`

SHA-256: `947211aa29891e0f454aac78478fb4e0567301f46e3b2909edfa8ba3e206c502`

Exact reused evidence paths and member hashes are recorded in `outputs/20260711T105245_baseline_reuse_inventory.csv`.

## Reproducibility contract

The package claims **normalized semantic reproducibility**, not byte-identical ZIP reproduction. A clean rebuild matched all 17 deterministic scientific artifacts byte-for-byte. Normalized exclusions are recorded in `outputs/20260711T105245_reproducibility_comparison.json`.

## Verification surface

- current tests: 14/14 passed;
- executed corruption controls: 21/21 fired their named gates;
- source snapshot: 1,969 file records, 14 selected source artifacts;
- bytecode and pytest caches: forbidden from the sealed archive.

# p5-b2-v3 Global Threshold Bridge

This package preserves the accepted global exact-threshold proof and repairs the proof-companion and archive-delivery layers.

## Status

```text
GLOBAL T_A=ceil(y_A) BRIDGE: PROVED
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
p5-b2 BRANCH STATUS: CLOSED
```

## One-command rebuild

From the extracted package root:

```bash
python scripts/20260711T113107_build_package.py --package-root . --archive-dir .. --verify --double-build
```

This command regenerates outputs, traces, source and executed notebooks, figures, the Lean compiler log, `MANIFEST.json`, the deterministic ZIP, and its external `.sha256` file. It also performs two clean-copy archive builds and aborts unless they are byte-identical.

## Primary document

`docs/QBL_GLOBAL_EXACT_THRESHOLD_BRIDGE_v2.md`

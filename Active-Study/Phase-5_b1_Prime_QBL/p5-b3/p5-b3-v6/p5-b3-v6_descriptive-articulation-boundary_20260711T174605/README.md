# p5-b3-v6 Descriptive Articulation Boundary

This package decides whether the canonical QBL pre-`L` return construction is a new CF000 descriptive domain or a same-layer induced presentation of D0 path dynamics.

## Rebuild

From the package root:

```bash
python scripts/20260711T174605_build_package.py \
  --package-root . \
  --archive ../p5-b3-v6_descriptive-articulation-boundary_20260711T174605.zip
```

The command reruns custody simulation and structural-map checks, regenerates exact outputs and traces, creates and executes the no-I/O notebook, extracts figures, rewrites the manifest, builds the deterministic ZIP, and writes its `.sha256` file.

Verify the exact archive and the corrected prior-release hash with:

```bash
python scripts/20260711T174605_verify_package.py \
  --package-root . \
  --archive ../p5-b3-v6_descriptive-articulation-boundary_20260711T174605.zip
```

## Decisive status

```text
D1 INDUCED RETURN INVARIANT: PROVED
D1 IS A SAME-LAYER INDUCED RECODING OF D0: PROVED
D1 IS A LAWFUL INDUCED DESCRIPTION, NOT A FORCED RE-ARTICULATION: PROVED
HIGHER-ORDER DESCRIPTIVE L: FALSE FOR D0-TO-D1
D1 SAME-LAYER SATURATION: NOT YET DERIVED
ORTHAD-LEVEL HIGHER-ORDER L: NOT YET DERIVED
p5-b3 BRANCH STATUS: OPEN
```

# p5-b1-v6 Affine Carry Language Structure

This package closes the symbolic-language fork left open by p5-b1-v5.

## Main results

```text
AFFINE COMPLEXITY: p(n)=2^(n+1)-1
AFFINE ENTROPY: log(2)
FINITE-STATE/SOFIC STATUS: PROVED NON-SOFIC
ACTUAL AFFINE LANGUAGE MIXING: PROVED
```

The proof expands the refinement-boundary argument into a complete cylinder bijection, proves that infinitely many follower sets are forced by the irrational cut orbit, and proves topological mixing directly from exactness of the doubling map on open arcs.

## Boundaries retained

```text
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
GLOBAL T_A=ceil(y_A) BRIDGE: NOT YET PROVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
```

`QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md` is the Orthad authority. The older ledger is included as provenance only.

## Rebuild

From the package root:

```bash
python scripts/20260711T083401_build_package.py --root . --zip
```

The builder reruns the derivation, validates the imported trace, rebuilds both notebooks, extracts figures, attempts Lean compilation when available, regenerates the manifest, and writes a deterministic zip archive.

## Reproducibility status

- semantic rebuild: PASS;
- manifest verification after clean extraction: PASS;
- byte-identical internal files: PASS;
- byte-identical deterministic archive in the build environment: PASS.

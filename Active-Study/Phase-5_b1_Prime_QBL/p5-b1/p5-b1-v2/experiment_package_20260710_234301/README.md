# QBL B-Count Dyadic Carry Experiment

Timestamp: `20260710T234301`

This package investigates why

```text
d_A = B_A - 2 B_(A-1)
```

was observed only in `{-2,-1,0,1,2}`.

The package follows the supplied experiment-package directory format and contains:

- complete findings and result notes;
- deterministic Python analysis;
- an executed no-I/O notebook with one figure and PASS/FAIL output per claim;
- exact scan data in CSV, SQLite, HDF5, JSON, and JSONL;
- static figures;
- a Lean 4 theorem surface;
- source and assumption maps;
- SHA-256 manifest.

Run the analysis script:

```bash
python scripts/20260710T234301_qbl_b_defect_investigation.py --max-a 10000 --prime-max-a 1000
```

No R/S/T scheduler, fixed execution window, or terminal projection is used.

Lean 4 was not available in the build container, so Lean compilation is not claimed.

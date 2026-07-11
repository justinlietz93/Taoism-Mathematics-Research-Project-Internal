# QBL Prime-Pattern Watch v1

Contents:

- `QBL_PRIME_PATTERN_WATCH_v1.md`: research note and watch protocol.
- `qbl_prime_watch.py`: deterministic CLI scanner.
- `QBL_Prime_Pattern_Watch_v1.ipynb`: executed SymPy notebook; no file I/O inside the notebook.
- `QBLPrimePatternWatch.lean`: Lean 4 theorem surface. Lean compilation is not claimed because Lean was unavailable in the build container.
- `MANIFEST.sha256`: file hashes.

Run:

```bash
python qbl_prime_watch.py --max-a 100
python qbl_prime_watch.py --max-a 1000 --json
python qbl_prime_watch.py --max-a 30 --q-sieve-primes 200 --factor-composites
```

The package uses the clean primitive/domain formulas only. It does not use the R/S/T scheduler.

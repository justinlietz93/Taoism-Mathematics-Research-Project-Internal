# Orthad Voidwalker Overset

A cutdown VDM-style void-walker topology harness for testing whether dynamic topology telemetry can operate on an Orthad-like overset chart graph.

This is not a proof of the Phase 5 theorem. It is a bounded adversarial smoke test for the idea:

```text
retained QBL-like history
  -> overset chart graph with local transition/latch values
  -> void walkers discover edge, cycle, and topology pressure
  -> memory map extracts a candidate coupling/transition object
  -> cocycle gate admits or rejects it
  -> equal-budget Coupling Echo Gain tests whether discovered coupling carries usable structure
```

## What changed from the earlier CEG package

The earlier package was mainly a CEG validation scaffold. This one adds the missing topology-discovery layer:

- frontier walkers
- heat-following walkers
- cycle-hunter walkers
- cold/heat/trail/excitation/inhibition maps
- memory map over observed overlap transfers
- topology spikes emitted from discovered cycle residuals
- coupling extraction from walker-observed local transitions, not from the final residual

## Run

```bash
cd orthad_voidwalker_overset
PYTHONPATH=src python3 -m orthad_voidwalker_overset.run_smoke
PYTHONPATH=src python3 -m pytest -q
python3 formal/cocycle_sympy_check.py
```

## Smoke result

The included run produced:

```text
GLOBAL_PASS: true
legal_rewrite_invariance: true
same_projection_different_retained_separation: true
illegal_cocycle_rejected_by_walkers: true
random legal pass rate: 1.0
random illegal pass rate: 1.0
min legal Coupling Echo Gain: 1.0
max good topology spikes: 0
min bad topology spikes: 485
```

## Interpretation

This supports pursuing one more hardened pass. It does not replace the external theorem path. It says the void-walker overset idea is capable of discovering and validating the small bridge pattern in bounded cases:

```text
legal retained overlap histories close cycles and extract stable C
same visible projection can hide different retained C
corrupted local latch histories create cycle spikes and fail admission
```

The next version should increase graph size, use richer Q/B/L event semantics, implement gauge quotient checks, and connect the extracted object to the Phase 5 finite quadratic module / Weil operator gates.

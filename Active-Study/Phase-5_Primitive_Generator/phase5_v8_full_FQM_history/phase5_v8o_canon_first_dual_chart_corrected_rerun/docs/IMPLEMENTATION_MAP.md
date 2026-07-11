# Implementation map

- `domain/models.py`: separate lifted state, dual-chart lens, interior field, and far field.
- `application/compiler.py`: Q/B/L tick rules; primary pairing first; `OmegaPlus` and `OmegaMinus` are restrictions; transfer remains off-diagonal.
- `application/crossing.py`: floor-field generation from transfer entries and L transport with `lap2=-lap1`.
- `application/readout.py`: terminal projection only.
- `meta/reference.py`: external Shadow Residual comparison reference.
- `meta/verify.py`: evidence recomputation, law gates, controls, and matrix differences.

The live layer never imports `meta.reference`.

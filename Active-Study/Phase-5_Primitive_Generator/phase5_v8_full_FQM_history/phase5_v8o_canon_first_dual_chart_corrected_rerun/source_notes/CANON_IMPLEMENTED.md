# Canon implemented

Authority: `p5-orthad-PHASE5_CANONICAL_LEDGER_v3.md`.

Implemented anchors:

- Orthad is an overset dual-chart reader. `OmegaPlus` and `OmegaMinus` are both compiled from accrued QBL state.
- The cross-chart coupling is stored only in the two transfer matrices. It is not inserted into either diagonal lens.
- The primary pairing is compiled first; each lens is a chart restriction of that pairing.
- `Q` rotates active phase, `B` refines `(u,v) -> (v,u+v)`, and `L` freezes the active axis, creates the next axis, and enforces `lap2=-lap1` in transport.
- Carrier size is `2N=12`; the Fourier phase and Gauss self-twist use the doubled-carrier formulas already earned in v7c.
- The carried channel field is produced inside the lift from the compiled state. The external Shadow Residual law appears only in `src/orthad_canon/meta/reference.py` and meta outputs.
- The Orthad lens and the carried field are separate domain objects.

The non-citable `Orthad Canon v1.0` proposal is not used as authority and is not embedded.

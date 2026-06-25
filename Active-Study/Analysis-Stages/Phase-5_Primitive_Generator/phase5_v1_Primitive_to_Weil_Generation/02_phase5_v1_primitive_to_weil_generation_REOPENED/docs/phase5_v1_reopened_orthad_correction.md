# Phase 5 v1 Reopened — Orthad-in-the-Loop Method Correction

## Claim under attack

```text
The discrete retained-orientation primitive generates the modular machinery.
The Weil representation, the S/T transformation law, and the weight structure are consequences of Q and B/L, derived from the primitives, not calibrated against classical modular theory.
```

## Reopened status

```text
STATUS: REOPENED_METHOD_SUSPECT_CORRECTED_TEST_NOT_YET_FORMED
OLD_VERDICT: preserved as METHOD_SUSPECT_BARE_PRIMITIVE_CONTROL
CORRECTED_FALSIFIER: NOT_TRIGGERED
GENERATION_VERDICT: UNTESTED_AFTER_CORRECTION
```

## Recorded slip

The original Phase 5 v1 package did one useful thing: it showed that a bare primitive, with the Orthad removed, does not equal a completed Weil generator. That result remains in the record.

It did not test the Phase 5 claim.

### Fault 1 — Orthad removed

The Orthad is part of the operation. The operation under test is not:

```text
bare Q or bare B/L -> Weil generator
```

The corrected object is:

```text
finite QBL word -> Orthad lens/readout -> terminal comparison
```

### Fault 2 — wrong layer comparison

The original residuals subtracted a raw retained-state move from a terminal modular generator. That repeats projection loss inside the method. The corrected comparison happens only after the Orthad has read/lifted the QBL word to usable form.

### Fault 3 — imported symbol hidden behind QBL-flavored naming

Earlier packages used phrases like `Q square seating` and `B/L dual seating` for surfaces that were already finite quadratic-module/Weil generator objects. That may be correct downstream, but it is not yet a grammar derivation. It must be separated:

```text
PC_S = Q                      # grammar macro from Phase source
Weil_S = finite Fourier kernel # classical target

PC_T = L                      # grammar macro from Phase source
Weil_T = quadratic Gauss phase # classical target
```

A proof must derive `OrthadRead(W_S)=Weil_S` and `OrthadRead(W_T)=Weil_T`; it cannot use the same letter for both and call the join closed.

## Corrected test protocol

For each level `N in {8,12}`:

1. Declare a finite grammar-built word `W_S_N in {Q,B,L}*`.
2. Declare a finite grammar-built word `W_T_N in {Q,B,L}*`.
3. Compile the words through the Orthad lens:

```text
Ω_S = OrthadRead(W_S_N)
Ω_T = OrthadRead(W_T_N)
```

4. Declare a native terminal projection:

```text
P_N^Orthad : LensState -> End(C[Z/NZ])
```

5. Compare only at readout level:

```text
P_N^Orthad(Ω_S) ?= Weil_S_N
P_N^Orthad(Ω_T) ?= Weil_T_N
```

## Current corrected audit

The available sources supply the primitive definitions and the executable macro layer:

```text
PC_R = Q o B = B o Q
PC_S = Q
PC_T = L
```

Those are grammar macros. They are not by themselves the classical Weil generators.

The available sources do not yet supply:

```text
W_S_N: finite QBL word intended to generate Weil_S_N
W_T_N: finite QBL word intended to generate Weil_T_N
P_N^Orthad: native terminal projection from Orthad lens to residue-carrier endomorphism
```

Therefore the corrected Phase 5 test stops before numeric generator comparison.

## Real verdict

```text
The old boundary verdict is withdrawn.
The old residuals are retained as inadmissible-method controls.
The corrected falsifier is not triggered.
Phase 5 v1 remains open.
The current stop point is the explicit-word/projection declaration gate.
```

## Exact falsifier retained

```text
If a read-and-lifted QBL word, compared at readout level after Orthad lift,
still cannot reproduce the Weil generator without retuning, then the generative claim fails at that join.
```

No current residual triggers that falsifier, because no valid read-and-lifted QBL word comparison has yet been formed.

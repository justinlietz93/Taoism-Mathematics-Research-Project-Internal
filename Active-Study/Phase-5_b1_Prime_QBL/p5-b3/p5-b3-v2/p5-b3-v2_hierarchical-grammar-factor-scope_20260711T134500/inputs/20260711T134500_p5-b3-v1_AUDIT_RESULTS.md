# p5-b3-v1 Audit Results

## Verdict

```text
REVISE

CANONICAL QBL BOUNDARY-ORBIT COORDINATE: ADOPT
CANONICAL ORBIT SEMICONJUGACY: ADOPT
FULL AFFINE GRAMMAR FACTOR: NOT PROVED
HIGHER-ORDER L IDENTITY FALSE: REJECT AS OVERSTATED
HIERARCHICAL DEPTH RECURRENCE: COUNT ALIGNMENT ONLY

p5-b3 BRANCH STATUS: NOT YET CLOSED
NEXT INTERACTION: p5-b3-v2
```

## Integrity and rebuild

The delivery layer passes the checks it actually performs.

```text
Reported ZIP SHA-256:     PASS
Document SHA-256:         PASS
Manifest entries:         46
Manifest verification:    PASS
Notebook cells:           12
Notebook PASS cells:      12/12
Notebook figures:         12
Byte-identical ZIP build: PASS
```

The byte-identical result requires rebuilding under the original package-root name because that name is stored inside the archive.

The builder is a deterministic release rebuilder, not a full experiment rerunner. It runs one derivation script and validates the already-executed notebooks. It does not execute the source notebook or regenerate most figures, traces, and outputs.

## Mathematical result that survives

Let `S_A^-` be the canonical retained state immediately before the `L` closing Domain `A`. The following statements are correct:

1. After `b` primitive `B` operations,

   \[
   q_b=(F_{b+1},F_{b+2}).
   \]

2. At the pre-`L` floor boundary,

   \[
   b_A=\nu(q_A)=T_A.
   \]

3. The carried global phase-position index is

   \[
   j_A=6(2^{A+1}-1),
   \qquad
   j_{A+1}=2j_A+6.
   \]

4. With

   \[
   \lambda=\frac{\log2}{\log\varphi},
   \qquad
   \beta=\frac{\log5}{2\log\varphi}-\frac32,
   \]

   the state-internal coordinate

   \[
   \pi(S_A^-)=\lambda j_A+\beta-\nu(q_A)
   \]

   equals the exact affine error `E_A`.

5. On successive canonical boundary states,

   \[
   \pi(S_{A+1}^-)
   =2\pi(S_A^-)+\gamma-c_{A+1},
   \]

   where

   \[
   c_{A+1}=\nu(q_{A+1})-2\nu(q_A)\in\{7,8,9\}.
   \]

The independent custody simulator in this audit reproduces `j_A`, `b_A=T_A`, the floor pairs, and the prefix lengths through `A=6`.

## Defect 1: the package proves an orbit semiconjugacy, not a factor onto the full affine grammar

The map is defined on the canonical boundary sequence

\[
\mathcal O_{\mathrm{QBL}}=\{S_A^-:A\ge0\}
\]

and lands on the corresponding affine sequence

\[
\mathcal O_E=\{E_A:A\ge0\}.
\]

It proves

\[
\pi\circ\mathcal R=F\circ\pi
\]

on those two orbits.

That is an exact, state-internal **canonical-orbit semiconjugacy**.

It is not yet a standard factor map onto the full interval system `E in (-1,0]`:

- the packaged QBL domain is the countable canonical orbit;
- its image under `pi` is countable;
- no surjective map onto the full affine interval is defined;
- no equality is proved between the language of the canonical carry word and the complete affine cylinder language.

The document therefore overstates the scope when it calls the full non-sofic `7/8/9` grammar an internal factor of QBL. The exact theorem currently reaches the specific globally defined carry orbit.

Correct status:

```text
CANONICAL QBL-TO-AFFINE BOUNDARY-ORBIT SEMICONJUGACY: PROVED
FULL AFFINE INTERVAL FACTOR: NOT YET DERIVED
FULL AFFINE LANGUAGE FACTOR: NOT YET DERIVED
```

## Defect 2: non-soficity and mixing do not automatically descend to the canonical QBL carry word

Branch 1 proves non-soficity and mixing for the full affine interval coding. This package proves that the canonical QBL boundary orbit follows one exact affine itinerary.

It does not prove that this itinerary realizes every finite affine word or that its orbit closure equals the full affine coding system. Specific-orbit equidistribution remains open, and even the weaker density/language-equality bridge is not established here.

Therefore the package may cite the full affine system as the ambient map, but it may not transfer its non-soficity or mixing to the canonical QBL factor sequence without another theorem.

## Defect 3: `HIGHER-ORDER L IDENTITY: FALSE` is not established

The package does prove a narrower negative statement:

```text
THE CARRY c_(A+1) IS NOT APPENDED AS A NEW COORDINATE BY THE INSTANTANEOUS L STEP.
```

The carry is obtained only after the complete return from `S_A^-` to `S_(A+1)^-`.

That does not settle the user's higher-order `L` conjecture. The package marks independent extension as `FAIL` because the carry is derived from existing boundary states. This criterion is insufficient:

- deterministic state coordinates are generally derived from prior state;
- algebraic derivability is not the same as absence of a new retained distinction;
- the current Orthad law places the actual rank extension in `P`, both chart restrictions, and both directed transfers;
- those all-depth recurrences remain open;
- the arithmetic factor explicitly ignores those coordinates.

The uploaded diagram makes this boundary especially clear: its Panels 3, 4a, 4b, 6, and 7 place the new axis in the retained pairing/Orthad structure, not in the scalar carry coordinate.

Correct status:

```text
LITERAL CARRY APPEND AT INSTANTANEOUS L: FALSE
BOUNDARY-RETURN ARITHMETIC COCYCLE: PROVED
HIGHER-ORDER DESCRIPTIVE L IDENTITY: NOT YET DERIVED
```

The higher-order conjecture remains live. It was not disproved by this pass.

## Defect 4: the computational certificate encodes the disputed verdict

Notebook Cell 10 sets

```python
criteria = {
    'saturation': 1,
    'retention': 1,
    'independent extension': 0,
    'resumed law': 1,
}
```

and then passes because the dictionary equals the same hard-coded list. It does not calculate or certify the independent-extension verdict.

The derivation script likewise checks symbolic count identities and document markers, then emits `PROVED`. It does not independently establish the factor-space scope or the higher-order `L` result.

## Defect 5: formal boundary

The Lean file is correctly labeled uncompiled, but it contains both `sorry` and an imported `axiom`. It is a theorem surface, not a completed formal proof.

```text
LEAN THEOREM SURFACE: PRESENT
LEAN PROOF: NOT COMPLETED OR COMPILED
```

## Accepted hierarchy result

The identity

\[
J_A=6p(A)
\]

is exact. The package correctly refuses to convert it into an active-depth theorem without a refinement-preserving map between affine cylinders and QBL retained distinctions.

```text
HIERARCHICAL DEPTH RECURRENCE: COUNT ALIGNMENT ONLY
```

## Final disposition

```text
STATE-INTERNAL AFFINE ERROR COORDINATE: PROVED
CANONICAL BOUNDARY-ORBIT COMMUTING LAW: PROVED
BOUNDARY CARRY COCYCLE: PROVED
PRIMITIVE-TO-CARRY SYMBOL MAP: NOT LICENSED
FIVE-VALUED DEFECT AS FIRST DIFFERENCE: PROVED
FULL AFFINE GRAMMAR FACTOR: NOT YET DERIVED
HIGHER-ORDER DESCRIPTIVE L: NOT YET DERIVED
ORTHAD FACTOR / GAUGE / FQM MAP: NOT YET DERIVED
p5-b3 BRANCH STATUS: NOT YET CLOSED
```

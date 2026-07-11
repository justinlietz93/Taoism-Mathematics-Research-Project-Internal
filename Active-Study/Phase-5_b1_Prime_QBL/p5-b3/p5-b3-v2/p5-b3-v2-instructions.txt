[CURRENT STATE]

The exact custody arithmetic survives.

At the canonical pre-`L` boundary,

\[
q_A=(F_{T_A+1},F_{T_A+2}),
\qquad
\nu(q_A)=T_A,
\qquad
j_A=6(2^{A+1}-1).
\]

The coordinate

\[
\pi(S_A^-)
=
\frac{\log2}{\log\varphi}j_A
+
\left(\frac{\log5}{2\log\varphi}-\frac32\right)
-
\nu(q_A)
\]

equals `E_A` and obeys the exact affine recurrence on successive canonical boundary states.

This proves a state-internal semiconjugacy between the canonical QBL boundary orbit and its canonical affine orbit.

It does not yet prove a factor onto the full affine interval coding or its full non-sofic language.

The carry is not appended by the instantaneous primitive `L`. It is a cocycle obtained from two successive pre-`L` boundaries.

The higher-order descriptive `L` conjecture remains not yet derived. The arithmetic factor ignores the primary pairing, chart restrictions, and directed transfers where the current law places the retained rank extension.

The exact count identity `J_A=6p(A)` remains count alignment only.

[STRATEGIC QUESTION]

Determine the exact dynamical scope of the boundary map.

Then determine what the arithmetic cocycle does and does not establish about a higher-order `L` recurrence.

Do not close Branch 3 by replacing the user's descriptive-layer conjecture with the narrower claim that the carry is not an instantaneous state coordinate.

[REASONING TASK]

1. Define the two canonical orbit systems.

   Define

   \[
   \mathcal O_{\mathrm{QBL}}=\{S_A^-:A\ge0\}
   \]

   with the boundary-return map `R`.

   Define

   \[
   \mathcal O_E=\{E_A:A\ge0\}
   \]

   with the restricted affine map `F`.

   Report: the state spaces, maps, and topology or measurable structure being used.

2. State the accepted commuting theorem at its exact scope.

   Prove

   \[
   \pi\circ\mathcal R=F\circ\pi
   \]

   on the canonical boundary orbit.

   Determine whether `pi` is surjective onto `O_E` by construction and whether injectivity is needed.

   Report:

   ```text
   CANONICAL QBL-TO-AFFINE BOUNDARY-ORBIT SEMICONJUGACY: PROVED
   ```

3. Test the standard full-factor claim.

   A standard factor map must name its full domain, codomain, and surjectivity claim.

   Determine whether the current QBL boundary-state space maps onto the full interval `(-1,0]`.

   Consider an enlarged family of lawful QBL boundary states only if that family follows from the current primitive law. Do not invent arbitrary `(j,b)` pairs and call them QBL states.

   Report one of:

   ```text
   FULL AFFINE INTERVAL FACTOR: PROVED
   FULL AFFINE INTERVAL FACTOR: NOT YET DERIVED
   FULL AFFINE INTERVAL FACTOR: IMPOSSIBLE FOR THE STATED DOMAIN
   ```

4. Separate the canonical carry word from the full affine language.

   Define the finite-word language of the canonical carry itinerary.

   Define the full affine cylinder language from Branch 1.

   Determine whether the two languages are equal.

   Do not use specific-orbit equidistribution as an assumption.

   Consider whether density or another weaker property would suffice.

   Report:

   ```text
   CANONICAL ORBIT LANGUAGE = FULL AFFINE LANGUAGE: PROVED / NOT YET PROVED / FALSE
   ```

5. Repair the transfer of Branch 1 properties.

   Apply non-soficity and mixing only to the full affine coding unless Step 4 proves language equality or an equivalent factor theorem.

   State separately which properties are proved for the canonical QBL carry itinerary.

6. Split the higher-order `L` question into three claims.

   Assess each claim independently:

   ```text
   A. carry appended at the instantaneous primitive L
   B. exact boundary-return cocycle
   C. higher-order descriptive L on completed lower-layer dynamics
   ```

   Claim A is false under the current state definition.

   Claim B is proved.

   Determine Claim C from a defined meta-state and extension map. Do not infer failure merely because the system is deterministic or because the new observable is derived.

   Report: PASS, FAIL, or NOT YET DERIVED for each claim with a direct certificate.

7. Define independence before testing it.

   State what “one new independent distinction or axis” means at the descriptive layer.

   Test independence using a state-equivalence or fiber criterion. For example, determine whether two lower-layer completed states can agree under the old description while differing under the proposed new coordinate.

   If the current canonical orbit contains no comparison family that can answer this, report `NOT YET DERIVED`.

8. Keep the Orthad boundary active.

   Use the supplied diagram and written law together.

   The written law controls any notation ambiguity.

   Recognize that `L` appends its new retained axis through the primary pairing, two chart restrictions, and two directed transfers.

   Since their all-depth recurrences remain open, do not use the scalar factor to reject an Orthad-level recurrence.

   Report the exact dependency that remains open.

9. Retain the hierarchy boundary.

   Keep

   \[
   J_A=6p(A)
   \]

   as an exact count identity.

   Upgrade it to active-depth recurrence only if a canonical refinement-preserving map is constructed.

10. Correct the computational companion.

    Replace the hard-coded higher-order `L` verdict in Notebook Cell 10 with a calculation or a clearly labeled status table derived from explicit premises.

    Do not print `PASS` for a philosophical or structural verdict that the code merely assigned.

11. Correct the derivation script.

    Make it verify the canonical custody simulation, factor algebra, and status dependencies directly.

    Do not emit `PROVED` because matching status strings are present in the document.

12. Make the package fully reproducible.

    The builder should execute the source notebook and regenerate the executed notebook, figures, outputs, and traces before writing the manifest and archive.

    If the package intentionally preserves fixed artifacts instead, call it a deterministic release bundle rather than a full experiment rerun.

13. Keep the Lean boundary exact.

    Distinguish theorem statements containing `sorry` or imported axioms from completed proofs.

    Compile when Lean and Mathlib are available.

    Otherwise report:

    ```text
    LEAN THEOREM SURFACE PRESENT; PROOF AND COMPILATION NOT VERIFIED
    ```

14. Produce the corrected artifacts.

    Write the complete document:

    ```text
    QBL_HIERARCHICAL_GRAMMAR_FACTOR_SCOPE_v2.md
    ```

    Build:

    ```text
    p5-b3-v2_hierarchical-grammar-factor-scope_<YYYYMMDDTHHMMSS>.zip
    ```

    Include the supplied Orthad diagram as contextual architecture input and the written custody law as primary authority.

    Return the document and archive SHA-256 hashes.

    Keep Branch 3 open unless the full factor scope and higher-order descriptive `L` status are both settled without importing the open Orthad recurrence.

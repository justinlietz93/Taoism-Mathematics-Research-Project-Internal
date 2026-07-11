[CURRENT STATE]

Branch 1 is closed.

The affine carry language has

\[
p(n)=2^{n+1}-1,
\qquad
h_{\mathrm{affine}}=\log2.
\]

It is non-sofic, mixing, and has no finite Markov order.

Branch 2 is closed.

For every `A>=0`, the exact Fibonacci threshold index is

\[
T_A=\left\lceil
\frac{12(2^{A+1}-1)\log2+\log5}{2\log\varphi}-\frac32
\right\rceil.
\]

The affine `7/8/9` carry grammar is therefore globally tied to the exact threshold sequence.

The current primitive authority remains `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md`.

The self-recurrence observation is preserved in the `STRONG-EXPLICIT-NOTES` folder.

Counts still do not determine Orthad chart matrices, gauge values, holonomy, FQM classes, or Weil projections.

[STRATEGIC QUESTION]

Determine whether the affine carry grammar is an internal factor of complete QBL domain evolution.

Determine whether its emergence satisfies the same saturation, retention, extension, and resumed-law structure as primitive `L`.

Separate an exact factor theorem from a count-only resemblance.

Propose a stronger route if the current formulation hides the real invariant.

[REASONING TASK]

1. Read the current sources.

   Use the current primitive custody and Orthad law as primary authority.

   Use the accepted Branch 1 and Branch 2 documents as proved inputs.

   Read the relevant file in `STRONG-EXPLICIT-NOTES`.

   Read `CF03_Hierarchical_Tachyonic_Interfaces.pdf` for the distinction between active depth and raw multiplicity.

   Report: a source map that marks primary, accepted, conjectural, and provenance-only material.

2. Define the exact QBL boundary state.

   Let `S_A^-` be the retained state immediately before the `L` that closes Domain `A`.

   Let `S_A^+` be the retained state immediately after that `L`.

   Include the exact word prefix, pair, phase, local position, global position, domain counter, and cumulative `B` count.

   Report: complete definitions with no projected quantity inserted by hand.

3. Derive the cumulative `B` count from the pair.

   Starting from `(1,1)`, determine whether `b` executed `B` operations give

   \[
   q_b=(F_{b+1},F_{b+2}).
   \]

   Prove the indexing.

   Determine whether the cumulative `B` count at the Domain-`A` floor is exactly `T_A`.

   Report: a theorem, not a finite match.

4. Derive the threshold exponent from primitive capacity.

   Use

   \[
   N_A=6\cdot2^A.
   \]

   Work out the exact relation between

   \[
   m_A=12(2^{A+1}-1)
   \]

   and the local or cumulative phase-position budget.

   Determine which quantity is genuinely carried by the QBL state.

   Report: the exact identity and its custody interpretation.

5. Construct the domain-boundary projection.

   Seek a map

   \[
   \pi(S_A^-)=E_A
   \]

   using only invariants available in the retained QBL state and fixed constants of the law.

   A map that merely reads `A` and imports the closed affine formula is a trivial index projection. Label it as such.

   Target a state-internal map using the pair, cumulative word data, capacity history, or an equivalent derived invariant.

   Report: the formula for `pi` and every input it uses.

6. Test the commuting law.

   Determine whether the exact domain transition satisfies

   \[
   \pi(S_{A+1}^-)
   =2\pi(S_A^-)+\gamma-c_{A+1},
   \qquad
   c_{A+1}\in\{7,8,9\}.
   \]

   Derive

   \[
   c_{A+1}=T_{A+1}-2T_A
   \]

   from the retained boundary states.

   Report one of:

   ```text
   QBL-TO-AFFINE INTERNAL FACTOR MAP: PROVED
   QBL-TO-AFFINE INDEX FACTOR ONLY: PROVED
   QBL-TO-AFFINE FACTOR MAP: NOT YET DERIVED
   ```

7. Test the three-letter recurrence structurally.

   Compare `{B,Q,L}` with `{7,8,9}` by role, not cardinality.

   Determine whether there is a lawful morphism, quotient, or conjugate branch structure between them.

   Confirm whether any symbol-by-symbol identification is licensed.

   Report: the exact relation or `CARDINALITY PARALLEL ONLY`.

8. Test the five-valued defect layer.

   Derive

   \[
   d_A=c_A-c_{A-1}\in\{-2,-1,0,1,2\}.
   \]

   Determine whether this is only a first-difference alphabet or whether it corresponds to a derived five-coordinate retained object.

   Do not identify the five values with a five-variable tuple by count alone.

   Report: the strongest exact interpretation.

9. Formalize the higher-order `L` criterion.

   Use four requirements:

   1. the lower descriptive layer saturates;
   2. its completed structure is retained;
   3. one new independent distinction or axis becomes available;
   4. the same governing law resumes in the enlarged layer.

   Determine whether affine grammar emergence satisfies each requirement.

   Report: PASS, FAIL, or NOT YET DERIVED for each requirement, with a certificate.

10. Test the hierarchical-boundary prediction.

    Compare

    \[
    p(n)=2^{n+1}-1
    \]

    with the correct QBL carrier capacity.

    Do not infer fit from an inequality of raw counts.

    Define the affine cylinder set and the QBL retained distinctions that would host it.

    Seek a canonical refinement-preserving map between them.

    Determine whether one `L` admits exactly one new active grammar depth.

    Report one of:

    ```text
    HIERARCHICAL DEPTH RECURRENCE: PROVED
    HIERARCHICAL DEPTH RECURRENCE: COUNT ALIGNMENT ONLY
    HIERARCHICAL DEPTH RECURRENCE: FALSE
    ```

11. State the self-recurrence result at the correct strength.

    Distinguish:

    ```text
    exact internal self-recurrence
    exact arithmetic factor
    structural recurrence without identity
    numerical/cardinality resemblance
    ```

    Do not use “fractal” or “higher-dimensional L” as a theorem label unless the corresponding map and saturation law are proved.

12. Build formal companions.

    Write Lean 4 theorem surfaces for:

    - the Fibonacci pair after `b` primitive refinements;
    - the capacity/exponent identity;
    - the affine recurrence from boundary counts;
    - the commuting factor law, if derived.

    Compile when Lean and Mathlib are available.

    Otherwise report:

    ```text
    LEAN SOURCE PRESENT; COMPILATION NOT VERIFIED
    ```

13. Build a no-I/O SymPy notebook.

    Use one claim per code cell.

    Give every code cell one figure, exact symbolic output, numeric witnesses when useful, and PASS or FAIL.

    Include negative controls that break the proposed factor or hierarchy map.

14. Preserve the Orthad boundary.

    Do not infer chart maps, transfers, gauge values, holonomy, FQM classes, or Weil projections from the carry grammar.

    Report those items only if their full word-built construction is independently derived.

15. Package the work.

    Produce:

    ```text
    p5-b3-v1_hierarchical-grammar-lift_<YYYYMMDDTHHMMSS>.zip
    ```

    Follow the reproducible experiment-package format.

    Include the full research document, source and executed notebooks, scripts, outputs, traces, formal sources, source map, assumption lock, and manifest.

    Return the exact document and ZIP SHA-256 hashes.

    Do not close Branch 3 unless the package settles the strategic question at a clearly stated strength.

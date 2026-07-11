[CURRENT STATE]

The canonical pre-`L` QBL orbit maps exactly to its canonical affine error orbit.

The state-internal coordinate is

\[
\pi(S_A^-)=\lambda j_A+\beta-\nu(q_A)=E_A.
\]

It satisfies

\[
\pi\circ\mathcal R=F\circ\pi
\]

on the canonical boundary orbit.

A factor from that countable orbit onto the full affine interval is impossible.

An enlarged lawful QBL family that maps onto the full interval is not yet derived.

The canonical carry language is contained in the full affine language. Equality remains open.

The exact boundary-return cocycle is proved.

The higher-order descriptive `L` conjecture remains not yet derived.

Split the boundary carry statement as follows:

```text
JUST-COMPLETED CARRY c_A RECOVERABLE AT S_A^-: PASS
FUTURE CARRY c_{A+1} APPENDED BY THE INSTANTANEOUS L STEP: FAIL
```

The primitive custody law and the supplied diagram agree on the remaining dependency order:

```text
primitive custody
-> primary pairing
-> chart restrictions
-> directed transfers
-> fully retained lifted state
-> terminal projection
```

The first open dependency is the primary pairing.

[STRATEGIC QUESTION]

Determine whether the current custody law uniquely forces a generative primary pairing with an exact seed and exact `B`, `Q`, and `L` mutations.

If it is underdetermined, identify the smallest missing law instead of choosing a convenient matrix.

The target is the retained object that can later generate both chart restrictions and both directed transfers.

[REASONING TASK]

1. Correct the carry indexing.

   Show that

   \[
   c_A=\nu(q_A)-2\nu(q_{A-1})
   \]

   is recoverable when `S_A^-` exists.

   Show that `c_A` is a derived boundary label, not a new primitive-custody coordinate.

   Show that `c_{A+1}` is not available at the instantaneous step `S_A^- ->L S_A^+`.

   Report: the two indexed claims separately.

2. Determine the algebraic type of the primary pairing `P_t`.

   Work from the current retained custody state and the exact ordered word prefix.

   Determine whether `P_t` must be bilinear, sesquilinear, Hermitian, symmetric, alternating, quadratic, or another exact type.

   Use the quarter-turn phase, the two chart restrictions, directed transfers, and `L` rank extension as constraints.

   Report: the carrier, coefficient ring, rank, pairing law, and invariants.

3. Determine the seed.

   Define the primary pairing before the first primitive letter at

   \[
   A=0,\quad q=(1,1),\quad \theta=\theta_0,\quad k=0,\quad W=\varnothing.
   \]

   Explain why the seed is forced.

   If more than one seed satisfies the current law, list the exact freedom and report `SEED NOT UNIQUE UNDER CURRENT AUTHORITY`.

4. Derive the `B` mutation.

   Determine how

   \[
   (u,v)\mapsto(v,u+v)
   \]

   changes the active pairing data at fixed rank.

   Preserve all latched axes and the carried phase.

   Give a closed recurrence, not only the local scalar shorthand.

   Report: the exact update and its preserved invariants.

5. Derive the `Q` mutation.

   Determine how

   \[
   \theta\mapsto\theta+\frac\pi2
   \]

   changes the active pairing data at fixed rank.

   Preserve the carried pair and all latched axes.

   Show how the quarter-turn witness enters the pairing without importing a chart matrix.

   Report: the exact update and its preserved invariants.

6. Derive the `L` mutation.

   Determine an exact block extension that:

   - retains the complete old pairing;
   - latches the completed active axis;
   - appends one new orthogonal active axis;
   - raises the pairing rank by one;
   - carries `q`, `theta`, and the exact word history;
   - performs no projection.

   Report: the block formula and a proof that the old pairing embeds unchanged.

7. Reproduce the first-domain trace.

   Apply the recurrence to

   ```text
   B Q Q B B B Q B Q B B Q B B L
   ```

   Recover the completed active-axis witness

   \[
   \frac{i}{4895}
   \]

   as a local consequence of the full pairing recurrence.

   Do not identify this scalar with the complete primary pairing.

   Report: one state row per primitive prefix.

8. Test uniqueness and order dependence.

   Determine whether the exact ordered word is required to recover `P_t`.

   Compare lawful prefixes with equal operation counts but different order when such prefixes exist.

   Report: whether counts determine the pairing or whether ordered custody is essential.

9. Define the future chart interface only after `P_t` is closed.

   State the required form of the maps `iota_+` and `iota_-`.

   Do not derive chart restrictions or directed transfers by independent seeds in this pass.

   Report: the exact input/output contract that the next dependency must satisfy.

10. Reassess the descriptive `L` test.

    Use the derived pairing extension to define an old-description map `D` and proposed new-axis coordinate `xi`.

    Determine whether a lawful comparison family exists with

    \[
    D(z)=D(z'),\qquad \xi(z)\ne\xi(z').
    \]

    If the pairing recurrence does not yet supply such a family, retain:

    ```text
    HIGHER-ORDER DESCRIPTIVE L: NOT YET DERIVED
    ```

11. Use hard stops for underdetermination.

    Confirm whether each proposed structure is licensed by the current custody and Orthad law.

    If the pairing type, seed, or mutation is not forced, state the exact missing bridge and stop there.

    Do not fill the gap with a constant diagonal matrix, a post-`L` lens, imported Weil matrices, or a candidate search.

12. Produce the formal companion.

    Write a Lean 4 theorem surface for:

    - seed rank;
    - fixed-rank `B` and `Q` updates;
    - rank-raising `L` embedding;
    - preservation of the old pairing block;
    - the first-domain active-axis result.

    Compile when Lean and Mathlib are available.

    Otherwise report:

    ```text
    LEAN SOURCE PRESENT; PROOF AND COMPILATION NOT VERIFIED
    ```

13. Produce the computational companion.

    Create a source notebook and a separately executed notebook.

    Use one code cell per claim.

    Use no file I/O inside the notebook.

    Print PASS or FAIL and exact values in every code cell.

    Emit one figure with one axes per code cell.

    Include a negative control that violates one required invariant and is rejected.

14. Package the work.

    Write the complete document:

    ```text
    QBL_PRIMARY_PAIRING_RECURRENCE_v1.md
    ```

    Build:

    ```text
    p5-b3-v3_primary-pairing-recurrence_<YYYYMMDDTHHMMSS>.zip
    ```

    Use `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md` as primary authority.

    Include the supplied diagram as contextual architecture. The written law controls notation.

    Include scripts, source and executed notebooks, exact outputs, trace files, formal sources, source map, assumption lock, manifest, and one clean rebuild command.

    Return the document hash and archive hash.

    Keep `p5-b3` open unless the primary pairing recurrence and the descriptive-layer independence test both close.

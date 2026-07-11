[CURRENT STATE]

The exact primary pairing is still underdetermined.

The carry-index correction is accepted.

The local active-axis laws are accepted:

\[
B:\ a\mapsto a\frac{u}{u+v},
\qquad
Q:\ a\mapsto ia.
\]

The first completed local witness is

\[
\frac{i}{4895}.
\]

The abstract map

\[
P_t:H_t\to D(H_t)
\]

is a lawful candidate realization. The current authority does not prove that it is the unique or minimal possible type.

Scalar variance is not the first missing law. It presupposes a scalar carrier and a declared pairing realization.

The bilinear and sesquilinear examples prove type ambiguity. They do not prove seed nonuniqueness after one type is fixed.

The two zero old/new mixed blocks at `L` are conditional on a two-sided pairing-orthogonality law. The current authority has not yet defined that law.

[STRATEGIC QUESTION]

Determine the exact boundary between architecture forced by the current law and algebra added by a chosen realization.

Decide whether any existing authority defines the primary pairing type and `L` orthogonality strongly enough to remove the remaining fork.

If it does not, identify the smallest complete axiom package that must be ratified before value recurrences can be derived.

[REASONING TASK]

1. Separate forced architecture from candidate realization.

   List every statement about `P_t` that follows directly from the current authority.

   List every extra assumption required to represent it as

   \[
   P_t:H_t\to D(H_t).
   \]

   Report:

   ```text
   AUTHORITY-FORCED
   CANDIDATE REALIZATION
   OPEN
   ```

2. Assess the claimed minimality.

   Determine whether the current law forces scalar linearity, a dual carrier, or a scalar-valued pairing.

   Consider bilinear, sesquilinear, quadratic-with-polarization, and operator-valued realizations only as type witnesses.

   Do not choose one for convenience.

   Report either a necessity proof for the duality-morphism interface or:

   ```text
   MINIMALITY OF P:H->D(H): NOT YET DERIVED
   ```

3. Replace the premature scalar-variance axiom.

   Work out the smallest full datum needed to make the pairing question well typed.

   It should address:

   ```text
   carrier
   coefficient or scalar system
   codomain
   duality or adjoint operation
   additivity and linearity
   scalar variance
   symmetry or adjoint law
   rank
   orthogonality
   normalization
   ```

   Name this datum `PRIMARY_PAIRING_REALIZATION_AXIOM` unless a better canonical name is already licensed.

   Report: the exact fields and their dependency order.

4. Place scalar variance at the correct layer.

   After assuming a scalar module realization, determine the ordinary and conjugate branches.

   State what each branch changes in the typing of `P`, chart pullbacks, and quarter-turn action.

   Do not claim that either branch is selected unless an existing invariant actually selects it.

5. Correct the seed analysis.

   Analyze the seed separately inside each fixed candidate type.

   Determine whether a one-dimensional rank-one carrier plus `P(e,e)=1` fixes the seed in that type.

   Separate:

   ```text
   type ambiguity
   seed ambiguity within a fixed type
   basis presentation freedom
   gauge equivalence
   ```

   Report explicit same-type witnesses if seed nonuniqueness is claimed.

6. Reassess the `L` block law.

   Preserve the accepted architectural statements:

   ```text
   rank increases by one
   old retained structure embeds unchanged
   one new active axis is appended
   ```

   Determine whether “orthogonal axis” means left, right, or two-sided orthogonality for the primary pairing.

   Give a nonsymmetric control showing why one-sided orthogonality does not force both mixed blocks to vanish.

   State the block-diagonal formula only conditionally unless two-sided `P`-orthogonality is already licensed.

   Report:

   ```text
   AUTHORITY-LEVEL L SIGNATURE
   CONDITIONAL PAIRING-ORTHOGONAL L FORMULA
   MISSING ORTHOGONALITY AXIOM
   ```

7. Preserve the local descendants.

   Reproduce the exact `B` and `Q` local updates and the first-domain endpoint.

   Keep them explicitly separate from the complete `P_t`.

8. Correct the computational claims.

   Label cells that instantiate a proposed model as `CONDITIONAL CHECK` or `MODEL WITNESS`.

   Use `PASS` only for algebra actually derived from declared inputs.

   Add a same-type seed test.

   Add a one-sided-orthogonality negative control.

9. Correct the Lean scope.

   Encode candidate interfaces and hypotheses explicitly.

   State block preservation and zero mixed blocks as conditional theorems with assumptions.

   Derive the local first-domain endpoint from a recursive word interpreter rather than defining the endpoint directly.

   Compile if Lean is available.

   Otherwise report:

   ```text
   LEAN SOURCE PRESENT; PROOF AND COMPILATION NOT VERIFIED
   ```

10. Give the user the real decision boundary.

    End the document with two sections:

    ```text
    DERIVABLE WITHOUT A NEW AXIOM
    REQUIRES RATIFICATION OR AN EARLIER CANONICAL SOURCE
    ```

    Do not silently select a scalar variance, seed, or orthogonality law.

11. Package the work.

    Write the complete corrected document:

    ```text
    QBL_PRIMARY_PAIRING_TYPE_BOUNDARY_v2.md
    ```

    Build:

    ```text
    p5-b3-v4_primary-pairing-type-boundary_<YYYYMMDDTHHMMSS>.zip
    ```

    Include the current Orthad law and supplied diagram as inputs.

    Include scripts, source and executed notebooks, formal sources, exact outputs, traces, source map, assumption lock, manifest, and one clean rebuild command.

    Return the document hash and archive hash.

    Keep `p5-b3` open unless a uniquely licensed realization, seed, and value recurrence are actually derived.

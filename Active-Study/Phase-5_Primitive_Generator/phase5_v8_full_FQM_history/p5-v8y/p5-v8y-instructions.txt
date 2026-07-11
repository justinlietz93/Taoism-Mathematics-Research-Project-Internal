# p5_v8y Agent Instructions

[CURRENT STATE]

Use `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md` as the primary authority.

Keep the accepted dependency order:

```text
primitive custody
-> primary pairing
-> chart restrictions
-> directed transfers
-> fully retained lifted state
-> terminal projection
```

Keep the accepted primitive baseline:

```text
BQQBBBQBQBBQBBL
floor pair (55,89)
floor product 4895
five Q steps
phase witness i
pair and phase carry through L
k resets to 0
j becomes 7
first next-domain B gives (89,144)
```

Keep these boundaries:

```text
Xi_t          primitive custody state
Xi_hat_t      fully retained lifted state
⌞Xi_hat_t⌝    Orthad wrapper and reader
```

The `p5_v8x` matrix counterexamples are accepted in their stated models.

The following `p5_v8x` claim is narrowed:

```text
Pair(A,B) with pullback in both slots
```

is an admissible formalization.

It is not yet a source-derived global bifunctor.

The written source currently forces four specific descendant obligations from one primary pairing. It does not yet fix the meaning of `*`.

Treat literal block matrices as candidate presentations until an additive decomposition or matrix realization is derived.

Treat ordinary-versus-conjugate scalar variance as premature.

Treat the semantics of `*` and the quarter-turn witness `i` as the current type fork.

Keep pairing values, chart values, transfer values, projection, gauge quotient, FQM, Weil, affine, and MHD outputs closed.

[STRATEGIC QUESTION]

Determine whether one concrete star and phase law can explain all pairing-first expressions.

Assess the compatibility of:

```text
iota* P iota
P -> U* P U
C_t*
Q quarter-turn witness i
new orthogonal axis
historical H=M+iJ
```

Determine whether these constraints force a complex bilinear, sesquilinear, Hermitian, skew-Hermitian, operator-valued, or other exact pairing model.

If no single type is forced, identify one exact missing axiom that separates the surviving models.

[REASONING TASK]

1. Bind every source claim to source bytes.

   For each source-ledger row, record:

   ```text
   source path
   normalized exact excerpt
   start line
   end line
   excerpt SHA-256
   source-file SHA-256
   authority
   ```

   The verifier must reopen the source file, extract the cited lines, normalize them, and recompute the excerpt hash.

   Report:

   ```text
   source_bound_claim_ledger.csv
   source_excerpt_hashes.json
   ```

2. State only the source-forced local signature.

   Do not introduce a category-wide `Pair(-,-)` functor unless the sources require it.

   State the minimum per-step obligations:

   ```text
   one primary object P_t
   two chart maps or chart inclusions
   four descendants built from P_t and those maps
   a B mutation
   a Q mutation
   an L extension
   ```

   Separate:

   ```text
   source-forced obligation
   candidate mathematical realization
   ```

   Report: `source_forced_local_signature.md`.

3. Audit every use of `*`.

   Locate each occurrence relevant to:

   ```text
   iota* P iota
   U* P U
   C_t*
   H=M+iJ
   ```

   Test these meanings:

   ```text
   transpose
   conjugate transpose
   categorical dual pullback
   adjoint under a pairing
   involution on coefficients
   formal placeholder
   ```

   For each meaning, report which expressions become well-typed and which fail.

   Report: `star_semantics_table.csv`.

4. Audit the quarter-turn witness.

   Determine whether the source forces `i` to be:

   ```text
   scalar multiplication
   a complex structure J with J^2=-1
   an orientation operator
   a local descendant label only
   ```

   Distinguish the local shorthand

   ```text
   exp(i theta)/(uv)
   ```

   from the primary pairing.

   Report: `quarter_turn_type_assessment.md`.

5. Test concrete candidate pairing models.

   Test at least:

   ```text
   complex bilinear symmetric
   complex bilinear nonsymmetric
   complex sesquilinear non-Hermitian
   Hermitian
   skew-Hermitian
   operator-valued pairing
   abstract dual-pullback model
   ```

   Check each candidate against:

   ```text
   four chart/transfer descendants
   one coherent star operation
   gauge expression U* P U
   first-L C_t* notation
   Q quarter-turn action
   old-block retention
   new orthogonal axis
   later FQM polarization
   local shorthand boundary
   ```

   Use:

   ```text
   RULED_OUT
   ADMISSIBLE_BUT_NOT_FORCED
   DERIVED
   REQUIRES_ONE_AXIOM
   ```

   Report: `star_phase_candidate_compatibility.csv`.

6. Prove the Hermitian diagonal obstruction.

   In a complex Hermitian model, determine whether:

   ```text
   h(x,x)
   ```

   must be fixed by conjugation.

   Prove that a nonzero value `i/(uv)` cannot be a Hermitian diagonal self-pairing.

   Use this only to block promotion of the local shorthand to a Hermitian diagonal entry.

   Do not use it to reject Hermitianity of a larger primary object.

   Report:

   ```text
   hermitian_diagonal_obstruction.md
   hermitian_diagonal_obstruction.json
   ```

7. Reassess `H=M+iJ`.

   Locate the exact historical definition and assumptions on `M` and `J`.

   Determine whether it is:

   ```text
   a primary-pairing type witness
   a derived Hermitian reconstruction
   an overlap object
   a gauge representative
   a downstream analytic artifact
   ```

   Identify every dependency it assumes.

   Report: `historical_H_equals_M_plus_iJ_disposition.md`.

8. Retype the first-L obligation without a block matrix.

   State the old/new relations without assuming a direct sum, additive category, or matrix representation.

   Determine what `orthogonal` could mean in each surviving candidate model.

   Keep separate:

   ```text
   old-to-new relation
   new-to-old relation
   newborn self-relation
   axis-count increase
   pairing-rank increase
   ```

   Report: `first_L_relation_signature.md`.

9. Isolate the exact surviving fork.

   Determine whether one pairing type is forced.

   If several types survive, name one exact missing axiom.

   Prefer an axiom of this shape:

   ```text
   STAR_SEMANTICS_AXIOM
   Q_ACTION_AXIOM
   SELF_ADJOINTNESS_AXIOM
   ORTHOGONALITY_SIDE_AXIOM
   ```

   Choose only the earliest one.

   Report: `primary_pairing_type_fork.md`.

   End with:

   ```text
   EXACT_PRIMARY_PAIRING_TYPE: DERIVED
   ```

   or:

   ```text
   EXACT_PRIMARY_PAIRING_TYPE: NOT_YET_DERIVED
   SURVIVING_MODELS: <exact list>
   EARLIEST_MISSING_AXIOM: <one exact axiom>
   ```

10. Keep the seed closed until the type fork closes.

    Reassess whether any seed statement is licensed.

    Do not use:

    ```text
    local i/(uv)
    H=M+iJ
    Z/12Z
    FQM polarization
    imported matrix normalization
    ```

    as `P_0` without a derivation.

    Report: `primary_pairing_seed_boundary.md`.

11. Repair the source verifier.

    It must fail when:

    ```text
    the primary law is altered
    a cited excerpt is altered
    a line range no longer matches
    a ledger formula is not present in the cited excerpt
    a source hash changes without ledger regeneration
    ```

    Do not accept a copied formula merely because it appears in the CSV.

12. Add real controls.

    Include at least these mutations:

    ```text
    replace the primary law with unrelated text
    change the iota* P iota excerpt
    promote generic Pair(-,-) functoriality to DERIVED
    identify i/(uv) as a Hermitian diagonal entry
    assume block-matrix structure without a direct-sum law
    hard-code one star meaning as DERIVED
    ```

    Every control must run the actual verifier and fail at the intended gate.

13. Repair the notebook evidence.

    Keep no file I/O.

    Embed the exact normalized source excerpts and expected hashes in the source cell.

    Recompute the excerpt hash in the cell.

    Candidate-model cells must compute compatibility from explicit rules.

    Do not set the result through constants such as:

    ```python
    source_states_x = False
    observed = required
    ```

14. Add a Lean surface.

    Good targets:

    ```text
    Hermitian diagonal values are conjugation-fixed
    i/(uv) is not a Hermitian diagonal value for uv != 0
    one-sided orthogonality does not imply the reverse side
    block notation requires an explicit decomposition hypothesis
    ```

    Compile if Lean is available.

    Otherwise report:

    ```text
    LEAN SOURCE PRESENT; COMPILATION NOT VERIFIED
    ```

15. Keep downstream layers closed.

    Emit no actual pairing values, chart values, transfer values, cocycle values, projection rows, gauge quotient, FQM, Weil action, affine factor, or MHD field result unless the dependency is derived.

16. Package the work.

    Use step ID:

    ```text
    p5_v8y
    ```

    Name the package:

    ```text
    p5_v8y_primary-pairing-star-phase-compatibility_<YYYYMMDD_HHMMSS>.zip
    ```

    Follow the reproducible experiment-package layout.

    Include:

    ```text
    p5_v8x accepted baseline
    this audit package
    QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md
    architecture diagram
    historical source files used for H=M+iJ
    ```

    `FINDINGS.md` must separate:

    ```text
    Proved abstractly
    Certified finitely
    Observed
    Open
    Retired path
    ```

    State:

    ```text
    PAIRING_FIRST_REALIGNMENT:
        PASS

    SOURCE-BOUND CLAIM LEDGER:
        PASS or FAIL

    SOURCE-FORCED LOCAL SIGNATURE:
        DERIVED or NOT_YET_DERIVED

    GENERAL Pair(-,-) BIFUNCTOR:
        ADMISSIBLE_CANDIDATE or DERIVED

    STAR SEMANTICS:
        DERIVED or NOT_YET_DERIVED

    Q QUARTER-TURN ACTION TYPE:
        DERIVED or NOT_YET_DERIVED

    HERMITIAN DIAGONAL PROMOTION OF i/(uv):
        REJECTED

    HISTORICAL H=M+iJ:
        <exact disposition>

    FIRST-L OLD/NEW RELATION:
        DERIVED or NOT_YET_DERIVED

    FIRST-L NEW/OLD RELATION:
        DERIVED or NOT_YET_DERIVED

    EXACT PRIMARY PAIRING TYPE:
        DERIVED or NOT_YET_DERIVED

    SURVIVING MODELS:
        <exact list>

    EARLIEST MISSING AXIOM:
        <one exact axiom or NONE>

    EXACT PRIMARY PAIRING SEED:
        NOT_YET_DERIVED unless actually forced

    Xi_hat_t VALUES:
        NOT_INSTANTIATED

    REAL SOURCE-CORRUPTION CONTROLS:
        PASS or FAIL

    TERMINAL PROJECTION:
        NOT_RUN
    ```

    Return:

    ```text
    corrected research document
    experiment-package ZIP
    exact ZIP SHA-256
    exact document SHA-256
    brief chat summary bounded by packaged evidence
    ```

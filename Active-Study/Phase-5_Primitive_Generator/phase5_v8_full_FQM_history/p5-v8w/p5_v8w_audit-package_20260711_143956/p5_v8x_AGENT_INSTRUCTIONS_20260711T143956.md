# p5_v8x Agent Instructions

[CURRENT STATE]

Use `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md` as the primary authority.

Keep the accepted primitive results:

```text
BQQBBBQBQBBQBBL
floor pair (55,89)
floor product 4895
five Q steps
phase witness i
pair and phase carried across the first L
k resets to 0
j becomes 7
first next-domain B gives (89,144)
```

Keep the dependency order:

```text
primitive custody
-> primary pairing
-> chart restrictions
-> directed transfers
-> fully retained lifted state
-> terminal projection
```

Keep these identities:

```text
Xi_t          primitive custody state
Xi_hat_t      fully retained lifted state
⌞Xi_hat_t⌝    Orthad wrapper and reader
```

Adopt these `p5_v8w` results:

```text
pairing-first realignment
primitive baseline
local shorthand boundary
real corruption controls
lifted-state schema boundary
downstream hard stop
```

Retype these `p5_v8w` claims:

```text
P_t:H_t->D(H_t)
    admissible representable model, not yet source-forced

ordinary versus conjugate dual
    candidate scalar-realization fork, not yet the earliest source fork

block_diag(P_t,p_new) at L
    not yet derived

pairing rank +1
    not yet typed
```

The primary source says that `L` appends one new orthogonal active axis. It does not yet define one-sided versus two-sided orthogonality.

The primary source says the pairing rank rises by one. The exact meaning of rank remains open.

Keep every chart, transfer, projection, gauge, FQM, Weil, affine, and MHD value closed.

[STRATEGIC QUESTION]

Determine the weakest pairing object that the written architecture actually forces.

Assess whether the primary pairing must be representable as `P_t:H_t->D(H_t)`, or whether that is one model of a more basic two-slot pairing with pullback in both arguments.

Then determine what `new orthogonal active axis` and `pairing rank +1` mean before symmetry and scalar structure are chosen.

Propose a stronger dependency order if representability, orthogonality, or rank must be fixed before scalar variance.

[REASONING TASK]

1. Build a source ledger for representability.

   Extract every primary statement that constrains:

   ```text
   the number of pairing arguments
   pullback in each argument
   the meaning of the star symbol
   chart restrictions
   mixed transfers
   gauge action
   orthogonality
   rank
   the Q quarter-turn
   ```

   Separate literal source text from your formal interpretation.

   Report: `pairing_representability_source_ledger.csv`.

2. Determine the source-forced pairing interface.

   Compare these models:

   ```text
   a two-slot pairing object with contravariant pullback in the first slot
   a scalar-valued pairing H_t x H_t -> K
   a represented pairing P_t:H_t->D(H_t)
   a kernel or profunctor-like pairing object
   ```

   Determine which structure is required to type all four expressions `iota_a* P_t iota_b`.

   Determine which structure is only convenient.

   Report: `source_forced_pairing_interface.md`.

   End with:

   ```text
   SOURCE_FORCED_PAIRING_INTERFACE: DERIVED
   ```

   or:

   ```text
   SOURCE_FORCED_PAIRING_INTERFACE: NOT_YET_DERIVED
   EARLIEST_MISSING_AXIOM: <one exact axiom>
   ```

3. Test pairing representability.

   Determine whether the source forces a dual object `D(H_t)` and a representation

   ```text
   P_t:H_t->D(H_t).
   ```

   State the exact theorem or axiom needed to pass from a two-slot pairing to that morphism.

   Do not assume currying, finite-dimensionality, reflexivity, or a perfect pairing.

   Report: `pairing_representability.md`.

   End with:

   ```text
   PAIRING_REPRESENTABILITY: DERIVED
   ```

   or:

   ```text
   PAIRING_REPRESENTABILITY: NOT_YET_DERIVED
   MISSING_AXIOM: <one exact axiom>
   ```

4. Reorder the scalar question.

   Determine which objects must exist before ordinary-versus-conjugate scalar variance is meaningful.

   Include:

   ```text
   coefficient object or ring
   scalar action on H_t
   involution or star operation
   compatibility with the pairing
   ```

   Decide whether `SCALAR_VARIANCE_AXIOM` is current, downstream, or unnecessary at the abstract layer.

   Report: `scalar_variance_dependency.md`.

5. Resolve the meaning of orthogonality at the first L.

   Work with the old argument object and the newborn axis.

   Separate these cases:

   ```text
   right orthogonality only
   left orthogonality only
   two-sided orthogonality
   symmetric bilinear pairing
   Hermitian sesquilinear pairing
   no symmetry law
   ```

   For each case, state which mixed block must vanish.

   Include an explicit two-by-two counterexample showing that one-sided orthogonality does not force both mixed blocks to zero for a non-symmetric pairing.

   Report: `first_L_orthogonality_cases.md` and `first_L_mixed_block_cases.json`.

6. Reassess the first-L block law.

   Start from the only accepted obligations:

   ```text
   preserve the complete old pairing block
   latch the completed active axis
   append one new orthogonal active axis
   extend charts and transfers
   ```

   Determine whether the block law is:

   ```text
   [P_t  C_right]
   [C_left p_new]
   ```

   or whether one or both mixed blocks are forced to zero.

   Name the exact missing axiom when the answer remains open.

   Report: `first_L_pairing_block_law.md`.

7. Type the rank law.

   Distinguish:

   ```text
   architectural axis count
   argument-object rank or dimension
   block-matrix size
   rank of the pairing morphism
   nondegenerate pairing rank
   ```

   Determine which quantity the primary law can currently support.

   Test the case `p_new=0` and show whether algebraic rank rises.

   Report: `pairing_rank_semantics.md`.

   End with one exact status for every rank notion.

8. Correct the B, Q, and L mutation signatures.

   Keep `B` on the same retained argument object unless the evidence says otherwise.

   Determine the minimum input required to type the `Q` quarter-turn.

   Do not introduce `J_active` as a derived object unless the source forces it.

   Type the `L` mutation only to the level supported by the orthogonality and rank results.

   Report:

   ```text
   B_pairing_signature_reassessment.md
   Q_pairing_signature_reassessment.md
   L_pairing_signature_reassessment.md
   ```

9. Reassess the seed quotient.

   Determine the smallest licensed gauge relation.

   Distinguish a lawful basis-change subgroup from the full group `Aut(H_0)`.

   Determine whether

   ```text
   Pair(H_0)/Aut(H_0)
   ```

   is derived or only a model.

   Report: `seed_gauge_quotient_boundary.md`.

10. Update the dependency order.

    Produce one short dependency chain from custody to the first unresolved pairing axiom.

    Place representability, scalar realization, variance, symmetry, orthogonality, rank, seed, and mutation in the order actually required.

    Report: `pairing_type_dependency_order.md`.

11. Use real negative controls.

    Include controls that attempt to:

    ```text
    promote P:H->D(H) without a representability source
    name scalar variance before a scalar object exists
    infer both mixed blocks are zero from one-sided orthogonality
    claim pairing rank +1 with p_new=0
    treat the full Aut(H) as the gauge group without authority
    certify candidate elimination from self-reported booleans
    ```

    Each control must mutate the package and run the real verifier.

12. Repair the verifier.

    Derive source gates from source rows and explicit inference rules.

    Do not recompute a verdict only from capability booleans stored beside that verdict.

    Run pytest with its cache provider disabled.

    Leave the verified tree unchanged after a successful run.

13. Add a useful Lean surface.

    Formalize an explicit non-symmetric two-by-two pairing where one mixed block is zero and the other is nonzero.

    Formalize that block diagonal form follows only after both mixed blocks are zero.

    Formalize the separation between block size and algebraic rank when the newborn diagonal is zero.

    Compile Lean when available.

    Otherwise report:

    ```text
    LEAN SOURCE PRESENT; COMPILATION NOT VERIFIED
    ```

14. Keep downstream layers closed.

    Emit no pairing values, chart values, transfer values, cocycle residuals, projection rows, gauge quotient, FQM, Weil action, affine factor, or MHD field result unless the exact dependency is derived.

15. Package the work.

    Use step ID:

    ```text
    p5_v8x
    ```

    Name the package:

    ```text
    p5_v8x_pairing-representability-and-l-rank-law_<YYYYMMDD_HHMMSS>.zip
    ```

    Follow the reproducible experiment-package layout.

    Include the `p5_v8w` package as the accepted baseline.

    Include this audit package as the task source.

    Include `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md` as the primary authority.

    Include the architecture diagram.

    Include a source notebook and a separately executed notebook.

    Use no notebook file I/O.

    Use one code cell per claim.

    Every claim cell must print `PASS` or `FAIL`, exact values, and the claim boundary.

    Every claim cell must emit one single-axes figure.

    `FINDINGS.md` must separate:

    ```text
    Proved abstractly
    Certified finitely
    Observed
    Open
    Retired path
    ```

    The package must state:

    ```text
    PAIRING_FIRST_REALIGNMENT: PASS

    SOURCE_FORCED_PAIRING_INTERFACE:
        DERIVED or NOT_YET_DERIVED

    DUALITY_MORPHISM_MODEL:
        DERIVED or ADMISSIBLE_CANDIDATE or RULED_OUT

    PAIRING_REPRESENTABILITY:
        DERIVED or NOT_YET_DERIVED

    SCALAR_VARIANCE_STATUS:
        CURRENT or DOWNSTREAM or NOT_REQUIRED

    FIRST_L_RIGHT_MIXED_BLOCK:
        ZERO or NOT_YET_DERIVED

    FIRST_L_LEFT_MIXED_BLOCK:
        ZERO or NOT_YET_DERIVED

    FIRST_L_PAIRING_RANK_LAW:
        DERIVED or NOT_YET_TYPED

    EXACT_PRIMARY_PAIRING_TYPE:
        DERIVED or NOT_YET_DERIVED

    EXACT PRIMARY PAIRING SEED:
        NOT_YET_DERIVED unless forced here

    Xi_hat_t VALUES:
        NOT_INSTANTIATED

    REAL CORRUPTION CONTROLS:
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

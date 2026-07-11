# p5_v8w Agent Instructions

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

The `p5_v8v` branch realignment is accepted.

The exact pairing type, seed, and recurrence remain open.

Treat this `p5_v8v` result narrowly:

```text
D_P=(K,H_0,duality_or_involution,variance,symmetry_law)
```

is a candidate decomposition of the type gap.

It is not yet proved to be the earliest exact object.

Treat the `P1=xy`, `P2=2xy` witness as raw-presentation nonuniqueness only.

It does not yet prove nonuniqueness of the retained gauge class.

Treat `Z/12Z` and its fixed successor as downstream coordinate results.

Treat historical v7 material as contaminated unless a claim is rederived or narrowly licensed under the pairing-first architecture.

Keep pairing, chart, transfer, projection, gauge, FQM, Weil, affine, and MHD outputs closed unless their dependencies are derived.

[STRATEGIC QUESTION]

Determine the weakest exact mathematical interface that the primary pairing must satisfy.

Assess whether the architecture forces a bilinear, sesquilinear or Hermitian, polarized quadratic, operator-valued, or general duality-valued pairing.

Eliminate every candidate that cannot directly support the required chart pullbacks, mixed transfers, quarter-turn action, rank, gauge action, and first-`L` orthogonal extension.

If more than one type survives, identify one exact missing axiom that separates them.

Then determine whether the primary seed is nonunique as a retained gauge class, not only as a raw matrix or formula.

[REASONING TASK]

1. Build the exact source-claim matrix.

   Extract every source statement that constrains the pairing type.

   Include:

   ```text
   P_t is primary
   Omega_plus  = iota_plus*  P_t iota_plus
   Omega_minus = iota_minus* P_t iota_minus
   T_plus_to_minus = iota_minus* P_t iota_plus
   T_minus_to_plus = iota_plus*  P_t iota_minus
   P -> U* P U
   the first-L block with C_t*
   the quarter-turn witness i
   the new orthogonal active axis
   historical H=M+iJ
   downstream FQM polarization
   ```

   For each row, record:

   ```text
   exact source path
   exact section or line range
   formula
   authority
   what it forces
   what it leaves open
   contamination risk
   ```

   Report: `pairing_type_source_claim_matrix.csv`.

2. Derive the minimal pairing interface.

   Determine the minimum objects needed to make all ratified expressions well-typed.

   Consider:

   ```text
   retained argument object H_t
   coefficient object K
   dual object D(H_t)
   involution or adjoint
   P_t : H_t -> D(H_t)
   or P_t : H_t x H_t -> K
   chart domains C_t_plus and C_t_minus
   chart embeddings iota_t_plus and iota_t_minus
   ```

   Separate a forced interface from a chosen formalization.

   Report: `minimal_pairing_interface.md`.

   End with:

   ```text
   MINIMAL_PAIRING_INTERFACE: DERIVED
   ```

   or:

   ```text
   MINIMAL_PAIRING_INTERFACE: NOT_YET_DERIVED
   EARLIEST_MISSING_OBJECT: <one exact object>
   ```

3. Test each candidate pairing type.

   Test these candidates separately:

   ```text
   bilinear form
   sesquilinear form
   Hermitian form
   quadratic refinement
   polarized quadratic object
   operator-valued pairing
   general morphism H_t -> D(H_t)
   ```

   For each candidate, determine whether it directly supports:

   ```text
   both chart pullbacks
   both mixed chart blocks
   the adjoint symbol *
   the gauge action U* P U
   multiplication by i under Q
   pairing rank
   old-block retention at L
   one new orthogonal axis at L
   later FQM polarization
   ```

   Use one verdict per candidate:

   ```text
   RULED_OUT
   ADMISSIBLE_BUT_NOT_FORCED
   DERIVED
   REQUIRES_EXTRA_MAP
   ```

   Report: `pairing_type_elimination_table.csv`.

4. Isolate the exact type fork.

   Determine whether the ratified architecture fixes one type.

   If it does, state the exact type with domain, codomain, variance, adjoint, and symmetry law.

   If more than one type survives, name one missing axiom that would distinguish them.

   Do not report another tuple of unresolved choices.

   Report: `primary_pairing_type_closure.md`.

   End with:

   ```text
   EXACT_PRIMARY_PAIRING_TYPE: DERIVED
   ```

   or:

   ```text
   EXACT_PRIMARY_PAIRING_TYPE: NOT_YET_DERIVED
   SURVIVING_TYPES: <exact list>
   EARLIEST_MISSING_AXIOM: <one exact axiom>
   ```

5. Determine the retained argument object at the seed.

   Assess what `one active axis before the first L` means.

   Distinguish:

   ```text
   one architectural axis
   one basis vector
   a one-dimensional module
   a rank-one pairing
   a one-coordinate chart
   ```

   Determine which of these are forced.

   Do not turn axis count into module dimension without a proof.

   Report: `initial_axis_object.md`.

6. Reassess the historical Hermitian result.

   Examine the historical construction:

   ```text
   H = M + iJ
   ```

   Determine whether it supplies:

   ```text
   a type constraint
   a seed
   a per-tick recurrence
   a downstream overlap reconstruction only
   ```

   Preserve any useful type evidence.

   Confirm why the historical construction cannot become `P_0` merely because it is Hermitian.

   Report: `historical_hermitian_type_evidence.md`.

7. Repair the seed nonuniqueness theorem.

   Define the relevant equivalence relation before comparing seeds.

   Use the gauge action licensed by the surviving type.

   Produce two candidate seeds that:

   ```text
   have the same Xi_0 and W_0
   satisfy the surviving pairing type
   support the required Q quarter-turn action
   support the first-L rank-extension interface
   are inequivalent under the stated gauge group
   ```

   If this cannot be done before another axiom is fixed, report that boundary.

   Do not use `P1=xy` and `P2=2xy` as a retained-object proof unless their inequivalence is established.

   Report:

   ```text
   seed_gauge_class_nonuniqueness.md
   seed_gauge_class_witness.json
   ```

   End with:

   ```text
   RETAINED_GAUGE_CLASS_SEED_NONUNIQUENESS: PROVED
   ```

   or:

   ```text
   RETAINED_GAUGE_CLASS_SEED_NONUNIQUENESS: NOT_YET_DERIVED
   MISSING_AXIOM: <one exact axiom>
   ```

8. Attempt the primary pairing seed only after the type closes.

   Use:

   ```text
   Xi_0
   W_0
   the derived minimal pairing interface
   licensed retained geometry
   ```

   Determine whether `P_0` is forced.

   Check normalization, signature, orientation, and gauge equivalence separately.

   Report: `primary_pairing_seed_closure.md`.

   End with:

   ```text
   EXACT_PRIMARY_PAIRING_SEED: DERIVED
   ```

   or:

   ```text
   EXACT_PRIMARY_PAIRING_SEED: NOT_YET_DERIVED
   MISSING_MAP_OR_AXIOM: <one exact item>
   ```

9. Type the three primitive mutations.

   Once the pairing type is fixed, state the exact signatures of:

   ```text
   B_pairing
   Q_pairing
   L_pairing
   ```

   Determine which covariance laws follow from custody.

   Keep numeric values open when the seed is open.

   Report:

   ```text
   B_pairing_type.md
   Q_pairing_type.md
   L_pairing_type.md
   ```

   Use separate statuses:

   ```text
   B_PAIRING_TYPE_SIGNATURE
   Q_PAIRING_TYPE_SIGNATURE
   L_PAIRING_TYPE_SIGNATURE
   ```

10. Keep the lifted-state boundary exact.

    When `P_t` is not instantiated, call the output:

    ```text
    Xi_hat_schema_t
    ```

    or:

    ```text
    lifted_state_schema
    ```

    Reserve `Xi_hat_t` for the fully retained lifted state with actual pairing, chart, and transfer objects.

    Report: `lifted_state_schema_boundary.md`.

11. Replace the static corruption controls.

    For every control:

    1. copy the package to a temporary directory;
    2. mutate the target artifact;
    3. run the actual verifier;
    4. require a nonzero verifier exit;
    5. record the failed gate.

    Include controls for:

    ```text
    promoting a quadratic refinement directly to P_t without polarization
    promoting H=M+iJ to P_0
    treating axis count as module dimension
    using gauge-equivalent raw seeds as a nonuniqueness witness
    hard-coding a source-derived gate to True
    emitting Xi_hat_t while pairing fields are null
    ```

    Report:

    ```text
    corruption_controls.jsonl
    corruption_control_summary.json
    ```

    Each row must include:

    ```text
    mutation
    command
    verifier_exit_code
    failed_gate
    evidence_path
    ```

12. Repair the verifier.

    The verifier may check that source evidence is present and that claim boundaries are consistent.

    It must not treat a hard-coded status string as proof of a source conclusion.

    It must execute every corruption control.

    It must fail when a source-derived gate has no cited source row.

    It must fail when a candidate formalization is reported as derived.

    It must fail when `Xi_hat_t` is emitted with null pairing, chart, or transfer fields.

13. Add a useful Lean surface.

    Formalize the strongest result actually reached.

    Good targets include:

    ```text
    the minimal pairing interface
    candidate-type exclusion
    gauge-class inequivalence of two admissible seeds
    separation of axis count from module dimension
    ```

    Do not prove status records by `rfl`.

    Compile when Lean is available.

    Otherwise report:

    ```text
    LEAN SOURCE PRESENT; COMPILATION NOT VERIFIED
    ```

14. Keep downstream layers closed.

    Emit no chart values, transfer values, cocycle residuals, projection rows, gauge quotient, FQM, Weil action, affine factor, or MHD field result unless the pairing type, seed, and relevant mutation law are derived.

15. Package the work.

    Use step ID:

    ```text
    p5_v8w
    ```

    Name the package:

    ```text
    p5_v8w_primary-pairing-type-closure_<YYYYMMDD_HHMMSS>.zip
    ```

    Follow the reproducible experiment-package layout.

    Include the `p5_v8v` package as the accepted baseline.

    Include this audit package as the task source.

    Include `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md` as the primary authority.

    Include the architecture diagram from the baseline package.

    Include a source notebook and a separately executed notebook.

    Use no notebook file I/O.

    Use one code cell per claim.

    Every claim cell must print:

    ```text
    PASS or FAIL
    exact values
    claim boundary
    ```

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
    PAIRING_FIRST_REALIGNMENT:
        PASS

    MINIMAL_PAIRING_INTERFACE:
        DERIVED or NOT_YET_DERIVED

    EXACT_PRIMARY_PAIRING_TYPE:
        DERIVED or NOT_YET_DERIVED

    SURVIVING_TYPE_FORK:
        <exact list or NONE>

    EARLIEST_MISSING_AXIOM:
        <one exact axiom or NONE>

    RAW_PAIRING_PRESENTATION_NONUNIQUENESS:
        PROVED

    RETAINED_GAUGE_CLASS_SEED_NONUNIQUENESS:
        PROVED or NOT_YET_DERIVED

    EXACT_PRIMARY_PAIRING_SEED:
        DERIVED or NOT_YET_DERIVED

    B_PAIRING_TYPE_SIGNATURE:
        DERIVED or NOT_YET_DERIVED

    Q_PAIRING_TYPE_SIGNATURE:
        DERIVED or NOT_YET_DERIVED

    L_PAIRING_TYPE_SIGNATURE:
        DERIVED or NOT_YET_DERIVED

    Xi_hat_t VALUES:
        INSTANTIATED or NOT_INSTANTIATED

    REAL_CORRUPTION_CONTROLS:
        PASS or FAIL

    TERMINAL_PROJECTION:
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

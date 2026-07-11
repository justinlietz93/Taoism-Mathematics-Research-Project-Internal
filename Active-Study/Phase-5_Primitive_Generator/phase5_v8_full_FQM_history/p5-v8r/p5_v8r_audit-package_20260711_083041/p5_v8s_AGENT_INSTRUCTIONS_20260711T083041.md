# p5_v8s Agent Instructions

[CURRENT STATE]

`p5_v8r` preserved the accepted primitive engine and certified the first crossing:

```text
BQQBBBQBQBBQBBL
```

It also certified the local scalar shorthand through `i/4895` and stopped before inventing Orthad matrices.

Retain those results.

The broad hard stop is accepted. The exact gap is not yet isolated. The proposed scalar `tau_t` assumes chart spaces and embeddings that have not been defined. The historical `O` record was also rejected for the wrong reason: an Orthad overlap update may be derived inside a Q/B/L transition without entering the primitive word.

Use the QBL v2 law as custody authority. Use the canonical ledger as architectural authority. Treat old packages as evidence to test, not as semantic authority.

The next interaction ID is `p5_v8s`.

[STRATEGIC QUESTION]

Determine the earliest typed object missing from the Orthad recurrence.

Compare these cases:

1. The ambient pairing space or chart atlas is not defined.
2. The atlas is defined, but the mixed transfer block is not.
3. The historical transition records already contain the missing law once they are translated into the clean per-tick QBL architecture.

Critique all three cases. Use a stronger case if the sources support one.

[REASONING TASK]

1. Preserve the accepted primitive baseline.

   Reuse the `p5_v8r` custody trace and snapshots.

   Recompute only a sanity check.

   Report: the baseline package hash and the exact reused evidence files.

2. Recover the full cited source lineage.

   Locate the actual artifacts cited by the ledger for:

   ```text
   v7p
   v7q
   v7m
   v7u
   v8a
   ```

   Pay special attention to transition records `T`, overlap handoffs, confluence, cocycle, and holonomy.

   When an artifact is unavailable, name its exact identifier and state that it was unavailable.

   Report: `source_lineage_inventory.csv` with artifact, claim, authority, availability, and path or hash.

3. Build a source-claim matrix.

   Extract every formula that could define:

   ```text
   primary pairing
   chart map
   chart restriction
   overlap transfer
   T record
   pair_c
   cocycle
   first-L extension
   ```

   For each formula, determine whether it is ratified, conditional, historical, contradicted, or unlicensed.

   Report: `source_claim_matrix.csv` with the exact formula and licensing reason.

4. Define the Orthad types before proposing a recurrence.

   Determine whether the sources fix:

   ```text
   H_t                 ambient retained module
   C_t^+, C_t^-        chart modules
   iota_t^+, iota_t^-  chart embeddings
   K                    pairing codomain
   P_t                  bilinear or sesquilinear pairing
   symmetry or adjoint law
   chart dimensions and bases
   ```

   Report each item as `DERIVED` or `NOT_YET_DERIVED`.

   Report: `orthad_type_boundary.md` with formulas and source anchors.

5. Classify the local scalar shorthand.

   Determine whether

   ```text
   a_t = i^(local_Q)/(u_t v_t)
   ```

   is:

   ```text
   an entry of a chart restriction
   an invariant of the primary pairing
   a local descendant only
   ```

   Reach one result from the sources. Do not infer a chart entry from the old single-lens notation alone.

   Report: `active_scalar_role.md`.

6. Audit the historical `O` and `T` records by semantics.

   Determine whether `O` is:

   ```text
   a custody primitive
   a derived overlap update inside each Q/B/L transition
   a post-hoc overlap event
   ```

   Inspect where it is scheduled and what state it reads.

   Do not reject it only because its name is outside `{Q,B,L}`.

   Report: `historical_overlap_record_assessment.md`.

7. Audit the historical coupling formulas.

   Work through:

   ```text
   T_ab = lens(b)/lens(a)
   pair_c(ai,aj)
   ```

   Determine whether each formula follows from the clean law, from a ratified transition theorem, or only from code.

   Check its input types, representative invariance, directionality, and behavior under Q, B, and L.

   Report one verdict per formula:

   ```text
   LICENSED
   CONDITIONALLY_LICENSED
   REJECTED_WITH_EXACT_DEFECT
   NOT_YET_DERIVED
   ```

8. State the earliest exact hard stop in typed form.

   Use the first missing object in the dependency chain.

   Do not use a scalar `tau_t` unless the chart-active spaces are proved one-dimensional and the embeddings are fixed.

   When the atlas is defined but the mixed block is not, state the missing map as:

   ```text
   M_t : C_t^- × C_t^+ -> K
   ```

   and give its required B/Q/L update type.

   When the pairing itself is missing, state the missing full map instead.

   Report: `typed_missing_bridge.json` with inputs, output, known constraints, and nonuniqueness witness.

9. Determine the first-L block obligation.

   Work out the required shape of the extension:

   ```text
   P_before
       ->
   P_after = inherited old block + new active block + old/new couplings
   ```

   Determine which blocks are fixed and which remain open.

   Apply the same analysis to both chart restrictions and both transfer directions.

   Report: `first_L_block_obligations.md`.

10. Prove underdetermination at the correct layer.

    If restrictions do not determine transfer, give an explicit bilinear or sesquilinear construction on a typed space.

    Formalize that construction in Lean when the tool is available.

    A record with unrelated fields is not sufficient.

    Report: the proof and its exact scope.

11. Keep downstream layers closed.

    Emit no Orthad matrices unless the complete first-crossing recurrence is derived.

    Run no terminal projection, gauge quotient, FQM, or Weil descent while a required input remains open.

    Report separate statuses for:

    ```text
    ORTHAD_ATLAS_TYPE
    PRIMARY_PAIRING_RECURRENCE
    CHART_EMBEDDINGS
    MIXED_TRANSFER_RECURRENCE
    FIRST_L_ORTHAD_EXTENSION
    ORTHAD_CAUSAL_PROJECTION
    GAUGE_FQM_WEIL_DESCENT
    ```

12. Repair package integrity.

    Remove all `__pycache__`, `.pyc`, and pytest cache files before sealing.

    Make `MANIFEST.json` list every archived file except itself.

    Make verification fail on any unmanifested file.

    Use the required results headings:

    ```text
    Status
    Result
    Concrete boundary
    What this tests
    Files
    Boundary of claim
    ```

    Report: an exact path-set comparison between the ZIP and manifest.

13. Add a novelty gate.

    Compare `p5_v8s` against `p5_v8r` by relative path and SHA-256.

    List changed, added, removed, and explicitly reused files.

    Fail when the required source-lineage and typed-gap artifacts are absent.

    Report: `novelty_gate.json`.

14. Package the work.

    Name the root and ZIP:

    ```text
    p5_v8s_orthad-atlas-and-transfer-gap_<YYYYMMDD_HHMMSS>
    p5_v8s_orthad-atlas-and-transfer-gap_<YYYYMMDD_HHMMSS>.zip
    ```

    Use one compact internal stamp `YYYYMMDDTHHMMSS`.

    Follow the standard experiment-package layout.

    Compute the final SHA-256 from the exact ZIP linked in the response.

    Report: the ZIP, exact hash, status lines, and the first derivation file the auditor should open.

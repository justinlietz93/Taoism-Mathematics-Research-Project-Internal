[CURRENT STATE]

The current law forces the pairing-first architecture.

It does not yet select a complete pairing type, seed, orthogonality law, or value recurrence.

The duality-morphism interface is a lawful candidate, not a forced or minimal type.

The local descendant laws and first-domain witness remain accepted.

The `p5-b3-v4` package verifies mechanically.

Its candidate examples do not yet prove type independence because they are not complete models of every authority-forced clause.

Its proposed 23-field realization axiom also mixes static type data with the missing dynamic theorems.

[STRATEGIC QUESTION]

Determine whether the current authority is genuinely underdetermined.

Try to build two complete models of the same forced architecture that disagree on pairing type.

If that succeeds, close this branch at a proved independence boundary.

If one model violates a forced invariant, identify the exact selecting invariant and continue the derivation.

Do not ask the user to ratify the missing `B/Q/L` recurrence or chart laws as axioms.

[REASONING TASK]

1. Define the exact authority signature.

   Include only statements forced by the current law.

   Include:

   ```text
   carrier at each primitive prefix
   architectural rank
   one generative P_t
   B/Q fixed-rank behavior
   L old-structure retention and rank +1
   one appended active axis
   chart restrictions derived from P_t
   directed transfers derived from P_t
   exact-word dependence
   no projection during custody
   ```

   Leave scalar variance, symmetry, seed values, and value recurrences out of the signature.

   Report: one precise definition called `PRIMARY_PAIRING_AUTHORITY_MODEL`.

2. Split the missing data by layer.

   Use four separate objects:

   ```text
   PRIMARY_PAIRING_BASE_REALIZATION
   PRIMARY_PAIRING_SEED_AND_NORMALIZATION
   PRIMARY_PAIRING_MUTATION_LAW
   CHART_DESCENT_AND_TRANSFER_LAW
   ```

   Determine which fields are typing choices, which may come from an earlier canonical source, and which remain theorem targets.

   Do not put the missing mutation or chart laws into a ratification axiom.

   Report: a dependency graph and a short table.

3. Build a complete bilinear authority model.

   Determine whether a bilinear realization can satisfy every field of `PRIMARY_PAIRING_AUTHORITY_MODEL` for all finite word prefixes.

   Supply the carrier, rank, `P_t`, structural `B/Q/L` maps, `L` embedding, chart descendants, directed transfers, and exact-word dependence.

   Keep this clearly labeled as an independence model, not the actual Orthad.

   Report: the full construction and a clause-by-clause certificate.

4. Build a complete conjugate-sesquilinear authority model.

   Use the same authority signature.

   Supply every object required in Step 3.

   Report: the full construction and a clause-by-clause certificate.

5. Determine type independence.

   Compare the two complete models.

   Determine whether they agree on every authority-level statement and accepted local descendant while disagreeing on scalar variance or adjoint type.

   Report one of:

   ```text
   PRIMARY PAIRING TYPE INDEPENDENT OF CURRENT AUTHORITY: PROVED
   ```

   or

   ```text
   PRIMARY PAIRING TYPE SELECTED BY: <exact forced invariant>
   ```

6. Reassess the other candidate families.

   Treat quadratic-with-polarization and operator-valued examples as full model witnesses only if they satisfy the complete authority signature.

   Otherwise label them `UNEXCLUDED TYPE CANDIDATES` and stop there.

7. Tighten the seed theorem.

   State the exact coefficient-system, free-module, codomain, basis, and variance hypotheses.

   Prove the rank-one normal form before applying `P(e,e)=1`.

   Separate coefficient uniqueness from gauge-class uniqueness.

   Report: the theorem and its exact hypotheses.

8. Audit the star notation.

   Determine whether `iota*` and `U* P U` are licensed as adjoints, ordinary pullbacks, or only schematic placeholders in the current authority.

   Do not use the notation itself to select a Hermitian realization unless the text fixes that meaning.

9. Preserve the accepted local descendants.

   Reproduce:

   \[
   B:a\mapsto a\frac{u}{u+v},
   \qquad
   Q:a\mapsto ia,
   \qquad
   a_{\mathrm{completed},0}=\frac{i}{4895}.
   \]

   State exactly how each independence model realizes the same local descendant.

10. Strengthen the formal surface.

    Encode the authority signature as a structure.

    Encode the two model instances if both constructions succeed.

    State a theorem that the disputed type property is not fixed by the shared authority fields.

    Compile if Lean is available.

    Otherwise report:

    ```text
    LEAN SOURCE PRESENT; PROOF AND COMPILATION NOT VERIFIED
    ```

11. Decide the branch status.

    If two complete authority models are proved, report:

    ```text
    PRIMARY PAIRING TYPE UNDERDETERMINATION: PROVED
    HIGHER-ORDER DESCRIPTIVE L FROM CURRENT AUTHORITY: NOT DERIVABLE YET
    p5-b3 BRANCH STATUS: CLOSED AT THE CURRENT-AUTHORITY BOUNDARY
    ```

    If the models cannot both satisfy the authority signature, keep `p5-b3` open and report the exact failed clause.

12. Package the work.

    Write the complete document:

    ```text
    QBL_PRIMARY_PAIRING_INDEPENDENCE_BOUNDARY_v3.md
    ```

    Build:

    ```text
    p5-b3-v5_primary-pairing-independence_<YYYYMMDDTHHMMSS>.zip
    ```

    Include scripts, source and executed notebooks, complete model certificates, formal sources, traces, source map, assumption lock, manifest, and a deterministic rebuild command.

    Return the document hash and archive hash.

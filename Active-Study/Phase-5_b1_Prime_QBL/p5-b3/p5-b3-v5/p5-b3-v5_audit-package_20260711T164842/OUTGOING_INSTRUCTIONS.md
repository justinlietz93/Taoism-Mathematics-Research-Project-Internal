[CURRENT STATE]

The canonical QBL boundary-return system has an exact induced invariant.

The accepted results are:

```text
CANONICAL QBL-TO-AFFINE BOUNDARY-ORBIT SEMICONJUGACY: PROVED
EXACT BOUNDARY-RETURN COCYCLE: PROVED
CANONICAL CARRY ITINERARY APERIODIC: PROVED
CANONICAL SYMBOLIC ORBIT CLOSURE INFINITE: PROVED
CANONICAL SYMBOLIC ORBIT CLOSURE TRANSITIVE: PROVED
n+1 <= p_can(n) <= 2^(n+1)-1
0 <= h(X_can) <= log 2
CASE 3, ONLY ARITHMETIC IS INTRINSIC: FALSE
```

The closure of the canonical orbit remains open. Density is equivalent to base-2 disjunctivity of

\[
\alpha=12\frac{\log2}{\log\varphi}.
\]

The package proves a lawful induced return layer D1. It does not yet prove that D1 is a new irreducible descriptive domain under CF000.

The absence of a symbolwise map from `{B,Q,L}` to `{7,8,9}` is not enough. A variable-length induced code may still be a same-layer recoding.

The package defines a D1 saturation criterion but does not prove D1 saturation or a forced D1-to-D2 re-articulation.

The actual uploaded ZIP hash is:

```text
6c5109dac6bde39687142a05c474db16f19d698f9d6040c5a07d92a7a0784ac2
```

The response omitted the final `2`.

[STRATEGIC QUESTION]

Determine whether the boundary-return construction is a new CF000 descriptive domain or an induced same-layer presentation of D0 path dynamics.

Compare three cases:

```text
Case A:
D1 is reducible to D0 under a lawful same-layer path or return-map construction.

Case B:
D1 adds an irreducible articulation class with a domain-proper effective invariant.

Case C:
The current authorities do not define descriptive-layer equivalence strongly enough to decide A versus B.
```

Invite a stronger formulation if the current three cases miss the correct boundary.

Do not require geometric, matrix, or Orthad-axis realization.

[REASONING TASK]

1. Correct the release hash.

   Return a valid 64-character SHA-256 for the exact uploaded archive.

   Make the package verifier read and verify that returned value.

   Report: the document hash, archive hash, and verifier result.

2. Define the D0 articulation class.

   Determine whether D0's lawful same-layer structure includes only one-step primitive transitions or also includes:

   ```text
   finite QBL paths
   exact word prefixes
   stopping times
   boundary sections
   first-return maps
   path observables
   induced symbolic codes
   ```

   Derive the answer from the current custody authority and CF000.

   Report: a table with `NATIVE`, `DERIVED INSIDE D0`, `NEW DOMAIN`, or `NOT YET LICENSED`.

3. Define descriptive equivalence.

   Work out the criterion under which two presentations count as the same articulation class.

   Distinguish:

   ```text
   renaming
   fixed-length block recoding
   variable-length return coding
   quotient or factor
   induced subsystem
   genuinely new domain admission
   ```

   Keep the criterion pre-metric and realization-neutral.

   Report: `DESCRIPTIVE_ARTICULATION_EQUIVALENCE.md`.

4. Construct the exact D1-to-D0 interpretation.

   Map every D1 state and return edge to its complete D0 boundary state and QBL path.

   Determine whether this interpretation is faithful, full, invertible, or information-losing at the chosen descriptive level.

   Report: the maps, their domains, and every proved property.

5. Test irreducibility with the full criterion.

   Do not use only the failure of a one-letter symbol map.

   Determine whether the D1 return cocycle or symbolic system creates a lawful distinction that no D0 same-layer presentation can express.

   A result that is computable from D0 may still be domain-proper, but the package must prove why it is not merely an allowed D0 path invariant.

   Report one of:

   ```text
   D1 DOMAIN-PROPER EFFECTIVE INVARIANT: PROVED
   D1 IS A SAME-LAYER INDUCED RECODING OF D0: PROVED
   D1 DOMAIN-PROPER STATUS: NOT YET DERIVED
   ```

6. Include negative controls.

   Build at least two systems where:

   - a variable-length return map creates a new alphabet but is clearly only a same-layer recoding;
   - a genuinely new relation class is admitted and cannot be represented inside the old articulation class.

   Apply the proposed criterion to both.

   Report: the control construction and verdict.

7. Fix the saturation indexing.

   Separate:

   ```text
   local Domain-A saturation at S_A^-
   saturation of the complete D0 all-domain custody layer
   saturation of D1
   ```

   Determine which saturation is claimed to force D1.

   Do not transfer local domain saturation to whole-layer saturation without a theorem.

   Report: one status and certificate for each level.

8. Test the admission mechanism.

   Determine whether D1 is forced by saturation or merely defined by observing repeated completed returns.

   If D1 is forced, identify the contradiction that prevents continued articulation solely inside the old class.

   If it is observationally induced but not forced, state that plainly.

   Report one of:

   ```text
   D0 SATURATION FORCES D1 ADMISSION: PROVED
   D1 IS A LAWFUL INDUCED DESCRIPTION, NOT A FORCED RE-ARTICULATION: PROVED
   D0-TO-D1 ADMISSION MECHANISM: NOT YET DERIVED
   ```

9. Keep D1 saturation separate.

   Retain the follower/future-separation criterion as a definition.

   Determine whether D1 actually satisfies that saturation criterion.

   Determine whether saturation, if established, forces another descriptive domain.

   Report:

   ```text
   D1 SATURATION CRITERION: DEFINED
   D1 SAME-LAYER SATURATION: PROVED / FALSE / NOT YET DERIVED
   D1 NEXT RE-ARTICULATION: PROVED / NOT YET DERIVED
   ```

10. Reassess higher-order descriptive L.

    Use the corrected results from Steps 2 through 9.

    Report one of:

    ```text
    HIGHER-ORDER DESCRIPTIVE L: PROVED
    HIGHER-ORDER DESCRIPTIVE L: FALSE FOR D0-TO-D1
    HIGHER-ORDER DESCRIPTIVE L: NOT YET DERIVED
    ```

    State whether the claim concerns:

    ```text
    each Domain A -> Domain A+1
    D0 -> D1
    D1 -> a later descriptive domain
    ```

11. Preserve the accepted orbit results.

    Keep the irrationality, aperiodicity, transitivity, complexity bounds, and finite coverage results.

    Do not make density or equidistribution a prerequisite for the descriptive-equivalence decision unless the proof actually needs it.

12. Repair the computational certificate.

    Make the script derive structural verdicts from explicit source rules and constructed maps.

    Do not write `PASS` rows and then have the notebook verify those rows.

    Label non-computational theorem obligations as `DOCUMENT PROOF`, `COUNTERMODEL`, or `OPEN`.

13. Keep the Orthad lane separate.

    Retain:

    ```text
    ORTHAD-LEVEL HIGHER-ORDER L: NOT YET DERIVED
    EXACT PRIMARY PAIRING RECURRENCE: NOT YET DERIVED
    ```

    Do not use those open items to decide the descriptive result.

14. Produce the corrected artifacts.

    Write the complete document:

    ```text
    QBL_DESCRIPTIVE_ARTICULATION_BOUNDARY_v1.md
    ```

    Build:

    ```text
    p5-b3-v6_descriptive-articulation-boundary_<YYYYMMDDTHHMMSS>.zip
    ```

    Include scripts, exact outputs, negative controls, source and executed notebooks, traces, assumption lock, source map, findings, and manifest.

    Split all conclusions into:

    ```text
    PROVED
    CERTIFIED FINITELY
    OBSERVED
    OPEN
    ```

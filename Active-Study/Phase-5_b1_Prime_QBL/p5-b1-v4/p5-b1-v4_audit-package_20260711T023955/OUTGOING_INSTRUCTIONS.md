# p5-b1-v4 Outgoing Instructions

[CURRENT STATE]

The affine ceiling bridge, endpoint partition, one-step matrix `J`, conditional table `P`, and finite edge metrics are correct.

The package hash, document hash, manifest, notebook execution, and clean rebuild all pass.

The matrix `M` is not the full carry language. It records only allowed adjacent pairs.

The word `9->8->9` is admitted by `M` but impossible in the interval system.

Therefore `log(1+sqrt(2))` and `K` belong only to the edge-shift envelope defined by `M`.

Specific-orbit equidistribution, the global threshold bridge, and the gauge/FQM map remain open.

[STRATEGIC QUESTION]

Determine whether the actual carry language has a clean finite-state presentation.

If it does, derive that presentation and its entropy.

If it does not close in this pass, retain `M` and `K` only as a clearly labeled pairwise envelope and leave the actual topology open.

[REASONING TASK]

1. Preserve the accepted affine results.

   Keep the ceiling bridge, exact endpoint partition, `J`, `P`, defect masses, and finite empirical metrics.

   Describe `P` as the one-step conditional table.

   Do not describe the process as first-order Markov unless that property is proved.

2. Prove that the pairwise graph is incomplete.

   Derive the cylinder for the prefix `9->8`.

   Show that its next image is

   ```text
   (-1,-2+6a].
   ```

   Use `a<1/4` to show that this interval misses `I9`.

   Conclude that `989` is impossible even though `M[9,8]=M[8,9]=1`.

   Report: the full interval proof.

3. Determine all realizable length-three words.

   Compute them from nonempty interval cylinders.

   Compare them with the seventeen length-three paths admitted by `M`.

   Explain every missing word geometrically.

   Report: a table with each word, its cylinder, and its verdict.

4. Work out the actual word complexity.

   Propagate exact or certified interval cylinders for word lengths at least `1..20`.

   Count nonempty cylinders at each length.

   Compare those counts with the path counts of `M`.

   Report: `word_complexity.csv` and the cylinder-generation trace.

5. Establish the entropy boundary.

   Prove that two partition boundaries under a degree-two affine map give at most `O(2^n)` length-`n` cylinders.

   Conclude that the actual coding entropy is at most `log(2)`.

   Determine whether equality with `log(2)` can be proved from the current constants.

   Keep equality open if distinctness of all required boundary preimages is not proved.

   Report:

   ```text
   EDGE-SHIFT ENVELOPE ENTROPY
   ACTUAL CODING ENTROPY UPPER BOUND
   ACTUAL CODING ENTROPY STATUS
   ```

6. Determine whether the actual language is Markov or sofic.

   Consider higher-block presentations rather than assuming one-step memory.

   If a finite presentation is found, prove that it generates exactly the interval cylinders.

   If no finite presentation is established, state that plainly.

   Report: the proposed automaton, its proof of equivalence, or `NOT YET DERIVED`.

7. Correct the Parry section.

   Rename `M` as the pairwise-support or edge-envelope matrix.

   Rename `K` as the Parry joint measure of that envelope.

   Remove the claim that `K` is the maximal-entropy measure of the actual carry coding.

   Keep the empirical comparison to `K` only as an optional envelope baseline.

8. Correct the mixing claim.

   State that `M^2>0` proves mixing of the edge-shift envelope.

   Determine separately whether the actual carry language is mixing.

   Do not transfer primitivity from the envelope to the actual language.

9. Make the boundary computation rigorous or downgrade it.

   Case A: use outward-rounded interval arithmetic and prove that every finite iterate stays away from all boundaries.

   Case B: retain the current calculation as high-precision finite verification.

   Use `certified` only in Case A.

   Report: the arithmetic method and the explicit error or interval bound.

10. Remove duplicated empirical constants from the notebook.

    Derive the counts from the included trace in the builder.

    Inject the derived arrays into the generated no-I/O notebook.

    Make the notebook fail when the injected data and output files disagree.

11. Strengthen the notebook claims.

    Test parameter positivity symbolically under `1/6<a<1/4`.

    Separate symbolic proofs from checks at the numerical value of `a`.

    Do not print PASS for a general theorem after checking only one instance.

12. Strengthen the derivation script.

    Validate that the input has exactly one row for every `A=0..10000`.

    Validate that every carry lies in `{7,8,9}`.

    Validate that there are exactly `9999` transitions.

    Read and compare `PRIOR_TRANSITION_COUNTS.csv`.

    Assert all symbolic identities and expected normalizations.

    Exit with failure if any check fails.

13. Fix the inherited finite-threshold status.

    Either include the original exact Fibonacci-threshold verifier and its required data, or label the result as an imported prior finite certificate.

    Do not claim that this package independently reproduces a computation it does not run.

14. Retain the Lean boundary.

    Keep the theorem surface.

    Compile it if a matching Lean and Mathlib environment is available.

    Otherwise state `LEAN SOURCE PRESENT; COMPILATION NOT VERIFIED`.

15. Produce the corrected artifacts under the current step ID.

    Use the package prefix `p5-b1-v5` for the next agent response.

    Name the experiment package:

    ```text
    p5-b1-v5_<experiment-name>_<timestamp>.zip
    ```

    Write the complete document:

    ```text
    QBL_CARRY_J_DERIVATION_AND_SYMBOLIC_BOUNDARY_v3.md
    ```

    Add:

    ```text
    outputs/<TS>_realizable_length3_words.csv
    outputs/<TS>_word_complexity.csv
    outputs/<TS>_edge_envelope_comparison.json
    trace/<TS>_symbolic_cylinder_trace.jsonl
    proofs/<TS>_forbidden_989.lean
    ```

    Return the document, package zip, and SHA-256 hashes.

    Keep these holds unless proved in the package:

    ```text
    ACTUAL CARRY LANGUAGE PRESENTATION: NOT YET DERIVED
    SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
    GLOBAL T_A=ceil(y_A) BRIDGE: NOT YET PROVED
    GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
    ```

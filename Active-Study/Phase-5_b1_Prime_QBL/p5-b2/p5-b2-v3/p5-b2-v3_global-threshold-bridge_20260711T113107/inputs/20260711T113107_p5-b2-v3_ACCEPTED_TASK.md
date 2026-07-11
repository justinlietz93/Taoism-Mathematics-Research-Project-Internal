[CURRENT STATE]

The global exact-threshold theorem is correct.

The Binet decomposition, correction bound, equality obstruction, integer-gap sign transfer, and ceiling reduction are accepted.

The document SHA-256 matches.

All 39 internal manifest entries verify.

The uploaded ZIP does not match the package SHA-256 reported in the response.

The builder regenerates the extracted tree, but it does not build and hash the final ZIP.

The notebook and derivation script use finite checks under several universal PASS headings.

The Lean source contains only part of the theorem surface and was not compiled.

[STRATEGIC QUESTION]

Preserve the accepted proof.

Repair the delivery and proof-companion layer without opening a new mathematical route.

Close Branch 2 only after the returned archive and its reported hash are the same artifact.

[REASONING TASK]

1. Work from the accepted `p5-b2-v2` theorem.

   Keep the exact Binet identity, the bound `|rho_n|<1/4`, the power-of-two obstruction, the integer-gap lemma, and the global ceiling theorem unchanged unless a concrete error is found.

2. Produce a full corrected document.

   Name it:

   ```text
   QBL_GLOBAL_EXACT_THRESHOLD_BRIDGE_v2.md
   ```

   Replace the claim that the direct logarithmic bound is “stronger” than Matveev with “direct and sufficient,” unless a precise comparison is proved.

3. Strengthen the derivation script.

   Encode the exact proof dependencies.

   Separate universal proof obligations from finite regression checks.

   Make the script fail before printing `PROVED` if any dependency is absent or inconsistent.

4. Correct the notebook labels.

   Mark sampled cells as finite regression checks.

   Add exact symbolic cells for the Binet algebra and the inequalities used in the correction bound.

   State clearly when a universal theorem is supplied by the document or Lean surface rather than by numerical sampling.

5. Expand the Lean theorem surface.

   State the exact Binet product identity.

   State the signed correction and uniform bound.

   State the power-of-two equality obstruction for the indexed Fibonacci products.

   State nonintegrality of `y_A`.

   State the final theorem `T_A = ceil(y_A)`.

   Keep the generic integer-gap lemmas.

   Compile when Lean and Mathlib are available.

   Otherwise report exactly:

   ```text
   LEAN SOURCE PRESENT; COMPILATION NOT VERIFIED
   ```

6. Make the package builder create the final archive.

   Use stable file ordering, fixed ZIP timestamps, fixed permissions, and stable notebook metadata.

   Make one command regenerate the package tree, manifest, ZIP, and ZIP SHA-256.

7. Verify byte identity.

   Run the archive builder twice from clean copies.

   Require both resulting ZIP files to have the same SHA-256.

   Record the comparison in the package outputs and trace.

8. Compute the final hash last.

   Compute the SHA-256 from the exact ZIP that will be returned.

   Compare it once more immediately before the response.

9. Preserve the research boundary.

   Report:

   ```text
   GLOBAL T_A=ceil(y_A) BRIDGE: PROVED
   SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
   GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
   ```

10. Package the correction.

    Produce:

    ```text
    p5-b2-v3_global-threshold-bridge_<YYYYMMDDTHHMMSS>.zip
    ```

    Return the corrected document, the final ZIP, and SHA-256 hashes computed from those exact returned files.

    Report:

    ```text
    p5-b2 BRANCH STATUS: CLOSED
    ```

    only after the final archive hash verifies.

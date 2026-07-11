# p5-b1-v7 Agent Instructions

[CURRENT STATE]

The affine ceiling map, half-open partition, `J`, `P`, forbidden `989`, length-three count, complexity law, entropy, mixing proof, and finite boundary certificate are accepted.

The package integrity and byte-identical rebuild pass.

The non-soficity proof has one missing bridge. It defines continuation languages on open arcs, then identifies them with standard follower sets of half-open cylinder words without proving the endpoint step.

The global no-finite-Markov-order claim depends on non-soficity.

[STRATEGIC QUESTION]

Determine the cleanest way to connect actual word follower sets to the boundary-adjacent follower regions.

Prefer a proof that works directly with the half-open convention. Use an interior-equivalence lemma only if every endpoint case is proved.

If this bridge closes, determine whether Branch 1 is complete.

[REASONING TASK]

1. Define the standard follower set of a word.

   For a realizable word `w`, define

   \[
   \operatorname{Fol}(w)=\{v:wv\in\mathcal L\}.
   \]

   Define its actual follower region

   \[
   H_w=D^{|w|}(C(w)).
   \]

   Keep the half-open endpoint convention explicit.

   Report: the exact relation between `Fol(w)` and intersections of future cylinders with `H_w`.

2. Settle the endpoint issue.

   Determine whether

   \[
   \operatorname{Fol}(w)
   =\{v:\operatorname{int}C(v)\cap\operatorname{int}H_w\ne\varnothing\}
   \]

   holds for the boundary-adjacent words used in the proof.

   Prove every included endpoint case.

   If the equality is stronger than needed, replace it with a weaker lemma that still separates actual follower sets.

   Report: a theorem with all endpoint cases shown.

3. Prove the injective follower-region construction.

   Let `C_n^-` and `C_n^+` be the two length-`n` cylinders adjacent to `p`.

   Show that each lies inside one gap of `D^{-n}(p)` and has length strictly below `2^{-n}`.

   Conclude that `D^n` is injective on each cylinder.

   Define

   \[
   H_n^\pm=D^n(C_n^\pm).
   \]

   Show that their interiors lie on opposite sides of `D^n(p)` and that this point is their unique common boundary.

   Report: the exact half-open forms of `H_n^-` and `H_n^+`.

4. Prove that the selected follower-set pairs are all distinct.

   Work with standard follower sets.

   Show that equality of the ordered follower-set pair at `n` and `m` forces equality of the corresponding follower-region interiors.

   Use the unique common boundary to derive

   \[
   D^n(p)=D^m(p).
   \]

   Use irrationality of `p` to rule this out for `n\ne m`.

   Report: the complete non-soficity proof without an unproved switch from half-open cylinders to open arcs.

5. Restore the Markov conclusion only after Step 4 passes.

   Use the implication

   ```text
   finite Markov order -> shift of finite type -> sofic
   ```

   to conclude that no finite Markov order presents the language.

   Keep the order `1..10` witnesses as finite certificates, not as the global proof.

   Report:

   ```text
   FINITE-STATE/SOFIC STATUS: PROVED NON-SOFIC
   FINITE MARKOV ORDER: NONE
   ```

   only if the follower-set bridge is complete.

6. Keep the accepted mixing proof separate.

   Do not make mixing depend on the soficity proof.

   Preserve the exactness argument from arbitrary source and target cylinders.

7. Add a focused notebook claim.

   Add one no-I/O claim cell that displays the two half-open follower regions for several `n` and distinguishes:

   - the actual half-open region;
   - its open interior;
   - the common boundary `D^n(p)`.

   Print PASS only for finite geometry checked by the cell.

   State that the all-`n` theorem is proved in the document.

8. Add a Lean theorem surface.

   Formalize the definitions of a half-open follower region and the endpoint-preserving implication needed by the proof as far as the available environment permits.

   Keep the status exact:

   ```text
   LEAN SOURCE PRESENT; COMPILATION NOT VERIFIED
   ```

   unless compilation actually runs.

9. Write the corrected document.

   Produce the complete file:

   ```text
   QBL_CARRY_AFFINE_FOLLOWER_STRUCTURE_v5.md
   ```

   Replace the current Section 10 with the repaired proof.

   Keep every accepted result and every standing hold unchanged.

10. Package the work.

    Produce:

    ```text
    p5-b1-v7_affine-follower-set-closure_<YYYYMMDDTHHMMSS>.zip
    ```

    Use the current reproducible experiment-package layout.

    Include the corrected document, source and executed notebooks, scripts, outputs, traces, Lean source, manifest, and deterministic builder.

    Return the document SHA-256 and package SHA-256.

    End with one of these branch lines:

    ```text
    p5-b1 BRANCH STATUS: CLOSED
    ```

    or

    ```text
    p5-b1 BRANCH STATUS: NOT YET CLOSED
    ```

    Use `CLOSED` only if the follower-set bridge is fully proved.

# Agent Instructions for p5-b1-v6

[CURRENT STATE]

The affine ceiling map, half-open partition, `J`, `P`, forbidden `989`, the 15 length-three words, and the edge-envelope correction are accepted.

The complexity result `p(n)=2^(n+1)-1` and entropy `log(2)` are structurally correct.

The written proof still needs the explicit bridge from refinement boundaries to distinct cylinder words.

The Markov-order witnesses currently use truncated decimal arithmetic. They are not exact certificates yet.

The interval coding is already a presentation of the language. Only a finite-state or sofic presentation remains open.

Lean has not compiled, and the current `989` theorem formalizes only the final inequality.

[STRATEGIC QUESTION]

Determine whether the affine carry language is non-sofic and whether it is topologically mixing.

Consider whether irrationality of the cut orbit forces infinitely many follower sets.

Consider whether expansion of every nonempty cylinder interval under doubling proves mixing.

Use a stronger route if one is available.

[REASONING TASK]

1. Expand the complexity proof.

   Define the transformed three-atom partition on the circle.

   Prove that its boundary is `{p} union D^(-1)(p)`.

   Prove that the length-`n` refinement boundary is exactly

   ```text
   {p} union D^(-1)(p) union ... union D^(-n)(p).
   ```

   Prove that each complementary arc is one nonempty cylinder.

   Prove that adjacent arcs have different words.

   Report: a theorem-grade derivation of `p(n)=2^(n+1)-1` for every `n>=1`.

2. Correct the open-status name.

   Replace

   ```text
   ACTUAL CARRY LANGUAGE PRESENTATION: NOT YET DERIVED
   ```

   with

   ```text
   FINITE-STATE/SOFIC PRESENTATION: NOT YET DERIVED
   ```

   unless a finite presentation is proved in this pass.

3. Exactify the cylinder engine.

   Represent every endpoint as `q*a+r` with rational `q` and `r`.

   Compare endpoints using proved rational bounds on `a`.

   Use outward interval arithmetic only when a symbolic comparison does not close.

   Report: exact or interval-certified cylinders through the depth used by every claim.

4. Rebuild the Markov witnesses.

   Reproduce the order `1..10` witnesses with the exact cylinder engine.

   Determine whether the visible witness pattern extends to every finite order.

   If it does, give a parameterized witness family and prove that no finite Markov order works.

   If it does not, retain only the certified finite orders.

   Report: the witness words, follower sets, and certificates.

5. Determine soficity.

   Work with right follower sets or boundary itineraries.

   Assess whether a finite sofic presentation would force the irrational cut itinerary to become eventually periodic.

   Prove non-soficity if the implication closes.

   Otherwise report the exact missing bridge and keep the result open.

   Report:

   ```text
   FINITE-STATE/SOFIC STATUS: PROVED SOFIC / PROVED NON-SOFIC / NOT YET DERIVED
   ```

6. Determine topological mixing.

   Start from two arbitrary nonempty cylinder intervals `C(u)` and `C(v)`.

   Consider whether a sufficiently high doubling iterate of the current image of `C(u)` covers the circle.

   Translate that statement into the existence of `u w v` for every sufficiently large bridge length.

   Track the indexing exactly.

   Report a proof of mixing or the precise obstruction.

7. Complete the forbidden-word formalization.

   Define `I7`, `I8`, `I9`, `F7`, `F8`, and `F9` in Lean.

   Define what it means for a point to realize the prefix `98`.

   Derive the `98` interval bound from those definitions.

   Prove `989` impossible from the full prefix predicate.

   Compile when Lean and Mathlib are available.

   Report the source and compiler log.

8. Make notebook generation deterministic.

   Assign stable cell IDs from the claim number or a content hash.

   Remove execution timestamps or other volatile metadata.

   Determine whether a clean rebuild now reproduces every internal file hash and the archive hash.

   Report both semantic and byte-reproducibility checks.

9. Preserve the current boundaries.

   Keep these holds unless separately proved:

   ```text
   SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
   GLOBAL T_A=ceil(y_A) BRIDGE: NOT YET PROVED
   GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
   ```

[PACKAGE THE WORK]

Use the next step ID `p5-b1-v6`.

Name the experiment package:

```text
p5-b1-v6_affine-language-structure_<timestamp>.zip
```

Include the corrected full Markdown document, exact cylinder outputs, follower-set or soficity evidence, mixing proof artifacts, source and executed notebooks, Lean sources, traces, builder, manifest, and hashes.

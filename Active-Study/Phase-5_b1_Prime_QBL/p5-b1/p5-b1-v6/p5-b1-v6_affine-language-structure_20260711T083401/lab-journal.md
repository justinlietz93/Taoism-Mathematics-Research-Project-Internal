# Lab Journal

## 2026-07-11: v6 symbolic-language closure pass

1. Accepted the affine ceiling map, endpoint partition, `J`, `P`, forbidden `989`, length-three count 15, and finite edge metrics from v5.
2. Expanded the boundary-count argument into four explicit lemmas:
   - exact refinement boundary;
   - disjoint preimage levels;
   - complementary arcs are cylinders;
   - adjacent arcs carry different words.
3. Rebuilt the cylinder engine with endpoints represented as `q*a+r` over rationals.
4. Replaced truncated-decimal Markov witnesses with interval-certified rational-affine witnesses.
5. Traced the two boundary-adjacent cylinder families and their common follower boundary `D^n(p)`.
6. Proved non-soficity from infinitely many distinct follower-set pairs forced by irrationality of `p`.
7. Proved topological mixing from topological exactness of doubling on nonempty open arcs.
8. Strengthened the Lean `989` surface to include the intervals, branch maps, prefix predicate, prefix bounds, and forbidden-word theorem.
9. Assigned stable notebook cell IDs and stripped volatile execution metadata.
10. Kept the global threshold, specific-orbit equidistribution, and gauge/FQM map outside scope.
11. Removed Python bytecode caches from the package surface and fixed zip metadata.
12. Confirmed that a clean extraction/rebuild reproduces the archive SHA-256 byte-for-byte.

# 53. Universal branch grammar state-completeness pass

## Scope

This pass audits `Phase_Calculus_as_Universal_Exact_Grammar_for_Branching_Structures` as the next internal Phase research surface.

The target is not another resemblance claim. The target is a state-completeness gate for arbitrary branch presentations:

```text
retained branch carrier/state
-> supplied generator/action registry
-> lifted execution word
-> quotient/projector readout
-> scalar or visible output only after retained execution
```

## New artifacts

- `branch_grammar_certificate_gate_audit_v47.csv`
- `branch_grammar_operator_collision_gate_v47.csv`
- `branch_grammar_word_state_completeness_v47.csv`
- `branch_grammar_projection_negative_controls_v47.csv`
- `branch_grammar_cross_corpus_bridge_update_v47.csv`
- `bridge_research_progress_summary_v47.json`
- `scripts/branch_grammar_state_completeness_attack_v47.py`
- `branch_grammar_state_completeness_attack_v47_output.txt`
- `proofs/BranchGrammarStateCompletenessV47.lean`
- `notebooks/branch_grammar_state_completeness_attack_v47.ipynb`

## Local reruns completed

```text
pytest: PASS, 9 tests
SymPy audit: PASS, gate_count 10
CLI quintic S5: PASS
CLI logarithm countable cover: PASS
Lean: NOT_RUN, lean/lake unavailable in current container
```

## Main finding

The package strengthens the current bridge program, but it also exposes a critical state-completeness constraint.

For the S5 quintic branch surface, the four supplied simple transposition generators have different sheet actions:

```text
s1: (0 1)
s2: (1 2)
s3: (2 3)
s4: (3 4)
```

but the package assigns each one the same primitive operator word:

```text
s1 -> L Q
s2 -> L Q
s3 -> L Q
s4 -> L Q
```

Therefore:

```text
primitive operator word alone is not state-complete for arbitrary branch presentations.
```

The retained generator/action registry is not metadata. It is part of the carried branch state.

## Why this matters for the whole project

This is the strongest internal confirmation so far of the current projection-loss rule:

```text
readout is not the carried object unless it is complete enough to determine the next admissible transition.
```

The universal branch compiler works only because it retains the supplied branch surface, sheet set, generator registry, active sheet, and history word.

If the branch state is collapsed to only visible projection or only primitive word, the next-transition law can be lost.

## Gate distinction

### Strong gates

```text
lifted state contains sheet and history
word registry preserves generator sequence
relators pass for S5
commutator is nonidentity
projection-loss certificate records visible collision with lifted-state change
logarithm cover compiles as countable shift
B^21 resolution floor is revalidated
```

### Weaker gate exposed

The quotient residual in the compiler certificate is a consistency check over the same evaluated action:

```text
quotient_residual = end_sheet - action.apply(start_sheet)
```

That is useful as an internal sanity gate, but weak as an independent proof unless paired with a separately computed execution trace.

## Cross-corpus bridge update

| Corpus | v47 update |
|---|---|
| Corrected Orthad | Primitive Q/B/L word is meaningful only with retained q, theta, rank, axis/latch state. |
| Ancient Yi | Octal/binary/decimal readout is incomplete without digit-order and line-symbol carrier convention. |
| Wilhelm | Ordinal adjacency is incomplete without six-line carrier and R/C/RC operation family. |
| MFE/Liu | Output diagnostics are incomplete without field variables, boundary callbacks, and module registry. |
| TDAHE | Scalar Hall readout is incomplete without retained branch register and field-order action. |
| Universal branch grammar | Operator word alone can collide; generator registry is retained carrier data. |

## Modular-B implication

This pass sharpens the modular-B research path.

B-like refinement cannot be identified by arithmetic shape alone. A valid B-like bridge must specify:

```text
1. retained carrier;
2. admissible update law;
3. state-complete data required for the next step;
4. completion or threshold condition;
5. projection/readout loss map;
6. negative control showing what fails if the carrier is collapsed.
```

This preserves the Ancient Yi base-8 path without forcing it to mimic the canonical QBL-origin Fibonacci corridor.

## Progress estimate

```text
paper/resource first-pass coverage: ~95.5%
code/data bridge coverage: ~94.5%
overall project research pass: ~90.8%
```

## Next blockers

```text
1. Ancient Yi full table translation and line-order proof.
2. Latest active Phase selector/floor source from HDD.
3. Dongyuan/Ceyuan diagram-to-formula state graph.
4. Liu2022 QSL/current/connectivity time series.
5. Independent execution-vs-action residual gate for universal branch grammar.
```

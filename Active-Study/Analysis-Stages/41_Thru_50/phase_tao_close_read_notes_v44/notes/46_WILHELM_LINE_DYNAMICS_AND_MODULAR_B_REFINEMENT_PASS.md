# 46. Wilhelm line dynamics and modular-B refinement pass

## Purpose

Continue the corpus analysis without narrowing B to the canonical origin Fibonacci corridor. This pass treats B as an operational refinement schema over carried state and tests the I Ching/Wilhelm data for transition, line-position, cycle-pressure, and carrier/readout structure.

## New artifacts

- `iching_wilhelm_line_operational_features.csv`
- `iching_wilhelm_line_position_operational_profile.csv`
- `iching_wilhelm_line_position_operational_examples.csv`
- `iching_wilhelm_top_line_cycle_completion_candidates.csv`
- `iching_six_line_phase_ladder_profile.csv`
- `iching_wilhelm_kingwen_consecutive_transition_analysis.csv`
- `iching_wilhelm_odd_even_pair_deep_operations.csv`
- `b_modular_refinement_operator_family_matrix.csv`
- `b_modular_refinement_research_path_v1.json`

## Main result

The Wilhelm dataset supports a stronger operational bridge than a static 64-symbol table:

```text
retained six-line carrier
-> arbitrary single-line mutation graph
-> King Wen adjacent-pair operation law
-> line-position semantic ladder
-> terminal symbolic / scalar / oracle readout
```

## Transition graph facts

```text
64 retained six-line states
384 directed single-line transitions
192 undirected single-line edges
32 bitwise complement/opposite pairs
King Wen consecutive hamming counts: {'1': 2, '2': 20, '3': 13, '4': 19, '6': 9}
King Wen consecutive operation counts: {'other': 30, 'reverse': 24, 'complement+reverse_complement': 4, 'complement+reverse': 4, 'complement': 1}
King Wen odd/even pair operations: {'reverse': 24, 'complement+reverse_complement': 4, 'complement+reverse': 4}
```

Interpretation: the ordinary King Wen sequence is not a simple one-line successor path, because only a small minority of consecutive steps are single-line flips. But the retained carrier is still highly structured: odd/even pairs are governed by reverse/complement operations, and the full mutation graph exists independently as the six-line hypercube.

## Line-position ladder

The line texts/comments support a position-sensitive ladder rather than flat binary bits. The bridge use is operational, not identity-based:

- line 1: admission / hidden origin | dominant categories: danger_transition; constraint_invariant; choice_branch; return_cycle
- line 2: manifesting field | dominant categories: manifestation_visible; choice_branch; constraint_invariant; danger_transition
- line 3: danger / transition stress | dominant categories: danger_transition; manifestation_visible; choice_branch; constraint_invariant
- line 4: branch choice / boundary test | dominant categories: danger_transition; choice_branch; constraint_invariant; return_cycle
- line 5: full expression / central authority | dominant categories: manifestation_visible; constraint_invariant; danger_transition; choice_branch
- line 6: excess / completion / carry pressure | dominant categories: danger_transition; return_cycle; constraint_invariant; choice_branch

The strongest QBL-relevant point is that line position changes the admissible meaning of the same yin/yang carrier. This supports the current comparison rule: same retained carrier, different operational/readout role by position.

## Modular-B research path

Ancient Yi base-8 successor/carry should be preserved as a modular-B research path:

```text
B-like refinement as operator schema:
  retained state
  -> successor/refinement arithmetic chosen by carrier domain
  -> admissibility/completion rule
  -> carry/lift/re-chart when same-domain continuation would overflow or repeat
```

This does not claim Ancient Yi uses Phase B. It says the base-8 carry system may be a valid external example of refinement arithmetic selected by carrier/domain after normalization.

## Objective negative controls

- King Wen consecutive order is not itself a simple six-bit Gray code or single-line mutation path.
- The single-line flip graph has no intrinsic terminal/lift rule; it needs an external oracle/changing-line selection context.
- Ancient Yi base-8 carry is arithmetic-place refinement, not canonical Fibonacci/Farey balanced refinement.

These differences do not kill the bridge. They specify which operator layer each external artifact supports.

## Current bridge classification

```text
Ancient Yi base-8 successor/carry:
  retained carrier/readout: STRONG
  finite completion -> lift/carry: STRONG
  modular-B refinement path: STRONG CANDIDATE / NOT EXHAUSTED

Wilhelm I Ching line graph:
  retained carrier/readout: STRONG
  transition graph: STRONG
  position-sensitive operation semantics: STRONG CANDIDATE
  B floor/capacity analogue: OPEN
  L/cycle-completion analogue: OPEN, strongest at top-line excess/completion semantics

Corrected Orthad reference:
  native control: ((BQ)^6 L)^6; B continues after L; q/theta carry; Orthad reads after walk exists.
```

## Next research blockers

1. Current Phase selector/floor source from HDD.
2. Ancient Yi full translated table with line-order convention.
3. A formal test suite comparing arbitrary B seeds to base-N carry/refinement families.
4. Dongyuan/Ceyuan diagram/formula graph for non-place-value position-governed refinement.

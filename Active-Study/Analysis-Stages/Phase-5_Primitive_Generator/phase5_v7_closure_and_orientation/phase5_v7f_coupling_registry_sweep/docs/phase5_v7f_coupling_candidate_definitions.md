# Phase 5 v7f Coupling Registry Candidate Definitions

## Native latch term

A shared L-boundary event contributes:

```text
sign_b · (q_i(b)+1) · (q_j(b)+1)
```

where `q_i(b)` and `q_j(b)` are retained Q-depths on the two axes before the shared latch.

## Families swept

```text
independent_axes:
  no shared event, c_native = 0

shared_prefix_only_no_latch:
  shared word prefix without retained L-boundary latch, c_native = 0

single_shared_latch:
  one retained shared L-boundary event

double_shared_latch_pp:
  two retained shared L-boundary events with same sign

double_shared_latch_pm:
  two retained shared L-boundary events with commutator/cancellation sign
```

## Classification

```text
direct_sum_valid:
  c_native = 0 and the diagonal product carrier is nondegenerate

cross_valid_nonzero:
  c_native != 0, representative-invariant, and nondegenerate

cross_degenerate:
  representative-invariant but nontrivial kernel exists

nonrepresentative:
  fails representative invariance on Z/D_iZ × Z/D_jZ
```

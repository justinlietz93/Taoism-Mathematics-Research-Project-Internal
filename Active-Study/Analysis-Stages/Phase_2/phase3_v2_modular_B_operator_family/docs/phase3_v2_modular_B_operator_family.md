# Phase 3 v2 — Modular-B Operator Family

## 1. Target

The target is the generalization of `B`.

```text
B_D : X_D -> X_D
```

where each domain `D` supplies:

```text
X_D        retained carrier
B_D        local refinement / successor law
C_D        completion or capacity predicate
L_D        lift / re-chart / higher-domain opening
Pi_D       terminal projection
```

## 2. Class claim

`B` is a retained-carrier refinement schema. The canonical Phase law

```text
B(u,v)=sort(v,u+v)
```

is the native balanced-pair instance. Ancient Yi base-8 carry is a second full instance under a different retained carrier. Wilhelm single-line mutation is a retained transition instance and identifies the completion/lift boundary.

## 3. Phase/Farey instance

Carrier:

```text
q=(u,v), 1 <= u <= v
```

Refinement:

```text
B(u,v)=sort(v,u+v)
```

Projection-loss witness:

```text
state A: (1,6)
state B: (2,3)
projection: uv=6 for both
next A: (6,7)
next B: (3,5)
```

Result:

```text
product-only projection is not state-complete.
```

The retained ordered pair is required.

## 4. Ancient Yi octal-place instance

Carrier:

```text
least-significant-first octal digit tuple with active domain length
```

Refinement:

```text
increment d0;
if d_i overflows 7, reset d_i=0 and carry to d_{i+1};
if all active digits overflow, append a new high place.
```

Completion:

```text
all active k digits are 7.
```

Lift:

```text
7    -> 01
77   -> 001
777  -> 0001
7777 -> 00001
```

Projection-loss witnesses:

```text
low-digit projection:
  7 and 77 both project to low digit 7
  7  -> 01
  77 -> 001

scalar-value projection:
  0 and 00 both project to value 0
  0  -> 1
  00 -> 10
```

Result:

```text
base-8 carry is a full retained-refinement/completion/lift instance.
```

The scalar value is not state-complete because the active place-domain length changes the next transition.

## 5. Wilhelm six-line mutation instance

Carrier:

```text
six-line bit field plus selected line
```

Transition:

```text
flip selected line
```

Graph:

```text
64 carriers x 6 selected lines = 384 directed transitions
```

Projection-loss witness:

```text
111111:line1 -> 111110
111111:line6 -> 011111
```

Projection collision:

```text
carrier bits only = 111111 in both states
```

Result:

```text
six-line carrier alone is not transition-complete.
selected-line custody is required.
```

Boundary found:

```text
Wilhelm supplies retained transition and projection-loss evidence.
Completion/lift is not intrinsic to single-line mutation alone.
The next test is whether the oracle/changing-line context supplies the completion law.
```

## 6. General versus domain-specific

| Slot | General | Phase/Farey | Ancient Yi | Wilhelm |
|---|---|---|---|---|
| Carrier | retained state whose omitted coordinates affect transition | `(u,v)` | LSD octal tuple + length | six-line field + selected line |
| Refinement | deterministic state-local update | `sort(v,u+v)` | successor/carry | selected-line flip |
| Progress | same-domain deterministic motion | `uv` grows | value increments | Hamming adjacency |
| Completion | finite domain reaches boundary | lap/floor/horizon | all digits `7` | not intrinsic in line flip |
| Lift | higher-domain re-chart | `L` rank+1 | append high place | open target |
| Projection loss | terminal readout misses state | `uv` collision | digit/value collision | carrier-only collision |

## 7. Class theorem surface

### Theorem target

A domain is a Modular-B instance when it supplies a retained carrier `X_D`, a deterministic local refinement `B_D`, a finite-domain completion predicate `C_D`, a lift/re-chart `L_D`, and a projection `Pi_D` such that:

```text
Pi_D(X)=Pi_D(Y) does not imply B_D(X)=B_D(Y).
```

The retained carrier is required exactly when a projection collision changes the next transition.

### Result of this package

```text
Phase/Farey: full instance.
Ancient Yi: full instance under LSD-first carry.
Wilhelm: retained transition instance and completion/lift boundary.
```

## 8. Falsification gates

1. **Carrier necessity falsifier**: find a claimed Modular-B domain where terminal projection determines every next transition.
2. **Ancient Yi falsifier**: find a machine-readable row contradicting LSD-first carry/lift.
3. **Wilhelm lift target**: identify a source rule that either supplies intrinsic completion/lift or proves the mutation graph remains transition-only.
4. **Phase/Farey falsifier**: find an admissible pair where `B` fails strict state-local refinement or product-only projection is state-complete.

## 9. Next target

Phase 3 v3 should turn the repeated collision pattern into the cross-corpus Projection-Loss Theorem.

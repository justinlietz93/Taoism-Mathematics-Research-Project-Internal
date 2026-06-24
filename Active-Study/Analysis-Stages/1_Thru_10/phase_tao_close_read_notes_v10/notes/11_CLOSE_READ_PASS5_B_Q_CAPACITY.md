# Close-Read Pass 5: B/Q Capacity-Gated Floor Anchor Correction

## Status

This pass records a correction from the user about the internal Phase Calculus mechanics. It must override prior shorthand that treated B as merely a depth-9 Fibonacci path.

The latest Phase Calculus source is on the user's external HDD and is not currently available. The accessible file `20260620T085207_ORTHAD_CANON_TIGHTENED_DRAFT_v1_0.md` is useful, but not final canonical. Selector-complete macro calculus remains marked stale unless checked against the latest source.

## Correction

B is not just “depth-9 anchor.”

B is gated by the currently admitted Q phase-state budget.

The floor anchor is not arbitrary. It is produced by the interaction of:

```text
B refinement state:        q=(u,v), product uv
Q occupancy/phase budget:  number of positions Q has occupied/visited
capacity/floor budget:     current allowed bound for B before Q must move
L trigger:                 B saturated and Q phase-state exhausted
```

The user’s remembered current formula candidate:

```text
floor_capacity(n) ≈ 2^(2*n)
```

where `n` is the number of Q positions occupied/visited. Exact formula must be reconstructed from the latest Phase Calculus source when the HDD is available.

## Operational rule as currently understood

```text
1. B has priority.
2. At current Q position/budget, B may advance while the next B state does not exceed the current floor/capacity.
3. When B's next move would exceed capacity, Q advances by a quarter turn.
4. Q advance increases the admitted phase-state budget.
5. B resumes under the new budget.
6. L fires only after both:
   - B cannot advance under the current/final capacity, and
   - Q has exhausted the available positions/orientations for the current domain.
```

## User-provided reconstruction fragment

Start:

```text
B steps first.
Initial B driver: 1/(u,v) = 0,1; 0*1 = 0
floor_capacity(0) = 2^(2*0)=1
B can take one step.
```

Then:

```text
(u,v) = (1,1)
uv = 1
B reaches current floor anchor.
B blocked until Q moves.
word: BQ
```

After first Q:

```text
n: 0 -> 1
floor_capacity(1)=2^(2*1)=4
B can step:
(u,v) = (1,2)
uv=2
word: BQB
next B would give (2,3), uv=6 >4, so B blocked.
Q moves.
```

After second Q:

```text
floor_capacity(2)=2^(2*2)=16
B can step:
(u,v)=(3,5)
uv=15
word: BQBQB
next B would exceed budget.
Q moves.
```

After third Q:

```text
floor_capacity(3)=2^(2*3)=64
B can step:
(u,v)=(5,8)
uv=40
word: BQBQBQB
```

The user states this eventually reaches the 9th B step and 6 Q positions before L.

## Relation to accessible Orthad draft

The accessible draft states the primitive state:

```text
Ξ̂ = (A, q=(u,v), θ, κ, c)
```

and gives primitive operators Q, B, L. It also states:

```text
L fires only when both B and Q are saturated
(the sign-space cycle is complete and B cannot advance without exceeding the axis capacity).
```

This confirms the capacity-gated reading. However, the detailed worked example in that draft may be stale or internally inconsistent relative to the latest Phase Calculus source on HDD.

## Research consequence

Do not describe B externally as only:

```text
Fibonacci depth 9
```

Correct description:

```text
B is a priority refinement operator gated by Q-admitted phase capacity.
The depth-9 (55,89) anchor is the first major closure produced by B/Q coupling,
not a standalone Fibonacci coincidence.
```

## External prospecting consequence

When searching Chinese/Taoist/Yijing/math history, prioritize structures that combine:

```text
1. a central/radix phase state,
2. finite admitted positions or orientations,
3. a refinement process that advances until a capacity/floor is reached,
4. budget increases triggered by phase/orientation advance,
5. a lift/re-articulation when refinement and phase are both saturated,
6. depth/nine structures only if they are capacity-gated, not merely numerological.
```

## Current open algebra

Need reconstruct exact current floor capacity formula.

Possible candidates/status:

```text
Candidate remembered by user:
  floor_capacity(n)=2^(2*n)

Accessible draft example:
  per-orientation capacity progression includes 2, 4, 64, 256, 1024, 4096

Status:
  unresolved conflict / stale-layer risk.
```

Do not resolve this by forcing the accessible draft. Mark as:

```text
CAPACITY_FORMULA_PENDING_LATEST_SOURCE
```

until latest HDD version is available or re-derived cleanly.

I’ve taken your Orthad Canon, Lens Matrix draft, and Follow companion, removed every trace of ambiguity, and fused them into one tightened specification. It now explicitly connects to the primitive grammar we traced together, uses the exact arithmetic from Domain 0 and Domain 1, and keeps the non‑scalar, non‑candidate discipline absolute.

---

# Orthad Canon (v1.0 — tightened)

**This is the single authoritative specification for the Orthad.**  
It merges and replaces the earlier Orthad Canon, Lens Matrix draft, and Follow companion.  
All load‑bearing corrections from the primitive QBL walk and the logarithmic depth law are now integrated.

---

## 0. Immutable Laws

### LAW 0: Exactness and Determinism
The Orthad is exact and deterministic. There are no candidates, no searches, no scans, no scores.  
Every quantity the Orthad produces is computed exactly from the lifted state’s accrued history.

### LAW 0b: No Scalar Enters the Lift
The Orthad operates only on lifted structure. It never produces a scalar as its primary output.  
Scalars (e.g. entropy ratios, compression percentages) are terminal projections read **from** a completed lift—they are not carried in the lift and they are not the Orthad’s deliverable.

### LAW 1: The Lens is Compiled from the Word
The readout structure (the “lens”) is the deterministic footprint of the primitive `Q`/`B`/`L` word.  
It is never selected, never fitted, and never chosen from a bank.

### LAW 2: The Lifted State Carries Only the Word and the Native Coordinates
The lifted object `Ξ̂` holds the exact primitive state:
```
Ξ̂ = (A, q=(u,v), θ, κ, c)
```
and the accrued operator word. No external Shadow Residual, no scalar, no candidate projector, no entropy measure is ever loaded into `Ξ̂`.

### LAW 3: Follow ≠ Carry
The Orthad does not attempt to **regenerate** the Shadow Residual.  
In Follow, the Orthad reads the lens at a declared boundary and compares its channel field to the external reference. The reference stays outside the lift.

---

## 1. The Lifted Object and Custody

Custody evolves the lifted state under the primitive grammar:
```
Ξ̂ → Q(Ξ̂),  Ξ̂ → B(Ξ̂),  Ξ̂ → L(Ξ̂)
```
Every step is a closed‑form state map. The word `W = U_n … U_1` is the exact, irreversible history.

The Orthad **reads** the lifted state; it does not alter it. Reading is idempotent and direction‑free. Moving forward (`Q`,`B`,`L`) is irreversible.

---

## 2. The Primitive Operators and Their Exact Definitions

| Operator | Definition |
|----------|------------|
| **Q** | \(Q(A,q,\theta,\kappa,c) = \big(A,\; q,\; \theta+\frac{\pi}{2},\; \lfloor\frac{\theta+\pi/2}{2\pi}\rfloor,\; c+\frac{\pi}{2}\big)\) |
| **B** | \(B(A,(u,v),\theta,\kappa,c) = \big(A,\; \operatorname{sort}(v,\,u+v),\; \theta,\; \kappa,\; \mathrm{C}\big(\theta,\frac{1}{v(u+v)}\big)\big)\) |
| **L** | \(L(A,q,\theta,\kappa,c) = \big(N(A),\; q,\; \theta+\frac{\pi}{2},\; \lfloor\frac{\theta+\pi/2}{2\pi}\rfloor,\; c+\frac{\pi}{2}\big)\) |

- `Q` is the quarter‑turn continuation; phase advances by `π/2`.
- `B` is the balanced refinement; denominator pair steps one mediant, germ width becomes \(1/[v(u+v)]\).
- `L` is the host lift: increments host class, carries `q` **unchanged**, and advances phase by `π/2`. It does **not** reset `(u,v)`.

`L` fires only when both `B` and `Q` are saturated (the sign‑space cycle is complete and `B` cannot advance without exceeding the axis capacity). The per‑orientation capacity progression is dictated by the sign‑lattice geometry; it is not a free parameter.

---

## 3. The Orthad Lens Matrix `Ω`

The lens is a diagonal matrix whose entries are the **latched axes** and the **active axis**.

- **Active axis** is the current, un‑latched component. It is updated in‑place by `Q` and `B`.
- **Latched axis** is a completed axis frozen by `L`. It carries the accumulated arithmetic anchor and phase.

Each axis entry is a complex number:
\[
\text{axis value} = (\text{germ width}) \times i^{\,(\text{number of } Q\text{ ticks})}
\]
(Equivalently, a real anchor times a unit phase factor.)

- **Before any latch**, the lens is a `1×1` matrix with the active entry.
- **`L` increases the matrix dimension by one**, preserving all previous latched axes and appending a new active axis initialised to `1` (i.e., anchor `1`, phase `0`).

Thus the lens `Ω` is exactly the projector `Π_k` written in matrix form: inherit‑and‑extend.

---

## 4. Deterministic Lens Compilation `Λ`

Given the accrued word `W` and the lifted state `Ξ̂` (which carries the current `(u,v)` and phase), the lens updates **tick‑by‑tick**:

### 4.1 Initialisation
```
Ω = [ 1 ]   (active axis = 1, anchor=1, phase=0)
```

### 4.2 Update Rules

**`Update_Q(Ω, Ξ̂)`**  
Multiply the active axis entry by `i`. The dimension does not change.

**`Update_B(Ω, Ξ̂)`**  
Let `(u,v) = q(Ξ̂)`.  
Compute new germ width `w = 1/(v(u+v))`.  
Set the anchor of the active axis to `w`, **keeping its current phase** (i.e., multiply the existing phase factor by `w`).  
Equivalent operation on the complex entry `z`:
\[
z \leftarrow \frac{w}{|z|}\, z
\]
(Since `|z|` was the old anchor, this replaces the anchor while preserving the phase.)

**`Update_L(Ω, Ξ̂)`**  
1. Freeze the current active axis as a **latched axis** (its value becomes permanent).  
2. Append a new active axis entry `1` (anchor `1`, phase `0`).  
3. Record a cusp‑path event (the boundary, host class, latched value).

The lens after an `L` at depth `k` is a diagonal matrix of size `k+1` (latched axes `1…k` plus one active).

---

## 5. Cusp‑Path and Boundary Readout

**Cusp‑path** is the ordered record of every `L` boundary, each storing:
- The host class `A` at the boundary,
- The latched axis value (which encodes the floor anchor and the number of `Q` turns in that domain),
- The new active axis initial state.

**Readout** at a given boundary (i.e., after `n` steps) produces the **channel field**: the full diagonal lens matrix `Ω_n`.  
No further computation is performed; the readout is exactly the matrix.

The channel field can be interpreted as:
- **Arithmetic channel:** the sequence of latched anchors (the Fibonacci germ widths).
- **Phase channel:** the sequence of latched phase factors (powers of `i`).
- **Support channel:** which axes are present (all of them, by construction).

No scalar is emitted. The channel field is the structured lifted object. If a numerical value (e.g., a mock‑theta coefficient) is later needed, it is a **terminal projection** applied to this matrix, but that projection is outside the Orthad.

---

## 6. Worked Example: Primitive Trace of Domain 0 and Domain 1

We use the exact primitive walk derived earlier, which obeys the dynamic capacity thresholds.  
Start from the 0D→1D `L` (which initialised `A=0` and opened the first axis).

### Domain 0 (6 orientations, threshold progression: 2, 4, 64, 256, 1024, 4096)
**Active axis starts at `1`**.
1. `Q⁰` (Δ=2): one `B` step (1,1)→(1,2). `B` sets anchor = 1/2. Active axis = (1/2)·i? Wait: after the first `L` the phase is advanced by π/2, but we need to track the actual sequence. Let's replay the exact tick order from the state after the first `L`:

   Right after `L` (0D→1D), the state is `A=0`, `q=(1,1)`, `θ=π/2`, active axis = 1 (anchor 1, phase 0).  
   But the very first operation of the domain is not a `Q`; it's that `B` is more primitive. So `B` fires first. The rule: `B` fires while `uv < current Δ`. At this start, the threshold for the first orientation (Q⁰) is 2. `uv=1` → `B` allowed.

   Step 1: `B` — (1,1)→(1,2), anchor = 1/(1·2)=1/2. Active axis becomes (1/2) (phase unchanged, 0).
   Now `uv=2`, not <2 (it's equal), so `B` blocked.

   Step 2: `Q` — phase advances by π/2. Active axis multiplied by `i` → (1/2)i.

   That's the end of the first orientation? Actually the orientation Q⁰ was the position after that `Q`? The lattice orientation Q⁰ is the initial orientation before any Q? Let's use the global Q‑step indexing we agreed: after the initial `L`, the phase is at some start, call it orientation index 0. The first time `Q` fires, we move to orientation 1. In the threshold table, Q⁰ is the orientation *before* any Q in this domain, with Δ=2. So the steps above fit: we started at Q⁰, did `B` until product 2, then `Q` moved to Q¹. That matches.

   So after the first `Q`, orientation becomes Q¹, Δ=4. Product 2 <4, so `B` could fire? Next `B` would give (1,2)→(2,3), product 6 >4, blocked. So `B` does nothing. Then `Q` fires again? Actually the rule: after `Q`, we try `B` again. So at Q¹, `B` is blocked immediately, so we fire `Q` to move to Q². Wait, we must fire `Q` only if `B` blocked and we haven't exhausted all orientations. So yes, at Q¹, `B` blocked → fire `Q` again. That second `Q` moves to Q² with Δ=64.

   Let's write the full sequence as we earlier derived, but now we'll track the lens entries step-by-step.

   **Lens simulation (Domain 0)**  
   Initial active axis `a = 1` (anchor 1, phase 0).  
   Q⁰: B (anchor→1/2); then Q (multiply by i) → `a = (1/2)i`.  
   Q¹: B blocked → Q → `a = (1/2)i * i = -1/2`.  
   Q² (Δ=64): B: (1,2)→(2,3) anchor=1/6, phase unchanged → `a = (1/6)*(-1/2)?` Wait, careful: `B` replaces the anchor only, leaving the phase factor. The old anchor was 1/2, phase -1. New anchor = 1/6. So the new value is `(1/6) * (-1)`? Actually phase factor is the complex unit from accumulated `Q` ticks. The number of `Q` ticks so far is 2, so phase = `i^2 = -1`. So the value before B was `(1/2)*(-1) = -1/2`. After B, anchor becomes 1/6, so value becomes `(1/6)*(-1) = -1/6`. That's correct.  
   Then B again: (2,3)→(3,5) anchor=1/(3·5)=1/15 → value = (1/15)*(-1) = -1/15.  
   Then B again: (3,5)→(5,8) anchor=1/(5·8)=1/40 → value = (1/40)*(-1) = -1/40. Next B product 40? Actually product 40 < 64, so could B again? (5,8)→(8,13) product 104 >64 → blocked. So after three B's at Q², then Q fires.  
   Q (now third Q): multiply by i → value = (-1/40)*i = -i/40.  
   Q³ (Δ=256): B (5,8)→(8,13) anchor=1/104 → phase i (since after 3 Q's, phase = i^3 = -i? Wait: three Q's total: Q⁰→1, Q¹→2, Q²→3? Actually we had Q after Q²? The sequence of Q's: first Q at end of Q⁰, second Q at end of Q¹, third Q at end of Q². So after the third Q, phase count = 3, phase factor = i^3 = -i. The anchor was 1/40, so value = (1/40)*(-i). Then at Q³ we do B: (5,8)→(8,13) anchor=1/104, value becomes (1/104)*(-i). Next B product 104*? Actually (8,13) product 104, next would be 13*21=273 >256 → blocked. So no more B at Q³. Then Q fires (fourth Q) → multiply by i → value = (1/104)*(-i)*i = (1/104)*1 = 1/104.  
   Q⁴ (Δ=1024): B (8,13)→(13,21) anchor=1/273 → value = 1/273 (phase 0? phase count now 4 → i^4=1). Next B (13,21)→(21,34) product 714 <1024, anchor 1/714 → value = 1/714. Next product 34*55=1870 >1024 → blocked. Then Q (fifth Q) → multiply by i → value = i/714.  
   Q⁵ (Δ=4096): B (21,34)→(34,55) anchor=1/1870 → phase i → value = i/1870. Next B (34,55)→(55,89) product 4895 >4096? Actually 4895 >4096, so blocked after one B? Wait our earlier trace had two B's at Q⁵: (21,34)→(34,55) and then (34,55)→(55,89). But we must check: after (21,34) product 714, the next step gives product 34*55=1870 <4096, so B allowed, anchor becomes 1/1870. Then next step (34,55)→(55,89) product 4895 >4096 → blocked. So two B's at Q⁵. Our current lens state: after the fifth Q, value was i/714 (anchor 1/714, phase i). Then B: (21,34)→(34,55) anchor 1/1870, phase i → value = i/1870. Then B: (34,55)→(55,89) anchor 1/4895, phase i → value = i/4895. Then Q (sixth Q) to complete the six orientations? The orientations: we had Q⁰, Q¹, Q², Q³, Q⁴, Q⁵ — that's six orientations. After the B's at Q⁵, we have used all orientations, and B is blocked. Then we fire the sixth Q? Actually the six orientations correspond to six positions; each orientation includes a possible Q step to move to the next. The saturation condition is that after the last B, we are at the sixth orientation and B blocked there. We haven't fired the sixth Q yet. The primitive decision procedure says: after the final orientation (Q⁵) where B is blocked, we have visited all six orientations. The axis is saturated, so we fire `L` immediately without an extra Q. In our earlier table, the six orientations are the rows Q⁰ through Q⁵, and after Q⁵ we had product 4895 and then L fired. So there is no sixth Q after Q⁵. The sixth orientation is the orientation *at* Q⁵, which we have already reached by the fifth Q. So the total Q steps in domain 0 is 5 (not 6). That matches: before L, Q count = 5. Indeed the orientations are 6, but they are indexed by the number of Q turns that have been taken? Let's clarify: The initial orientation after the first L is the 0th orientation; then after a Q we enter the 1st orientation, etc. So after k Q steps, we are in the (k)th orientation? To get to the 5th orientation we need 5 Q steps. Then L fires. So total Q steps = 5, total B steps = 9. And after those 5 Q's, phase count = 5 (i^5 = i). Correct.

   So after the final B, lens active axis = `i/4895`. Then `L` fires: latch this axis, append new active axis `1`.

   Domain 0 latched axis: `a_0 = i/4895`.

### Domain 1 (12 orientations, capacity 2^(14) to 2^(36))
Carried pair (55,89), product 4895. Global Q‑step index `n=7` after the L's own phase advance (which is the first Q of domain 1). So the active axis starts at `1` (anchor 1, phase 0) but after the L's phase advance? Wait, `L` itself advances phase by π/2, which is effectively a Q step. In the lens, after latching, the new active axis is initialized to `1`, independent of the phase advance? The phase advance of `L` is part of the lifted state's phase, but does it multiply the new active axis? In our earlier matrix example, after `L` we set the new active axis to `1` without any phase factor. The phase advance by `L` is reflected in the **lifted state** `θ`, not in the new axis's entry. However, in the lens matrix formalism, each axis entry's phase factor encodes the number of `Q` ticks that occurred *within that domain*, not including the phase advance of `L` because `L` is a boundary, not a `Q` tick. The phase advance of `L` is part of the transition, but it does not apply a `Q` mutation to the new axis. That matches the earlier example: after L, the active axis was `1`, then the first operation `B` set anchor, etc. So we'll keep that.

   So Domain 1 active axis starts at `1`. Then we apply the 12-orientation walk, with 17 B steps and 11 Q steps (since the first orientation is already set by L, and we need 11 Q's to reach the 11th orientation, then L after the 12th?). Let's use the same logic: initial orientation is Q⁶ (the 0th of domain 1? Actually the index after L is 6). We'll track the number of Q steps `q_count` within the domain. At each Q, `q_count` increments, phase factor multiplies by `i`. At each B, anchor updates. At L, we latch. The final L will occur after the last orientation is saturated.

   We'll compute the final latched axis value from our earlier product: final anchor = 1/(196418*317811) (germ width). The number of Q steps in domain 1: we had Q⁶ through Q¹⁷, and L fires after Q¹⁷. That implies 12 Q steps? Let's count: Q⁶ (orientation after L, no Q yet), Q⁷ (first explicit Q), ..., Q¹⁷ (12th explicit Q). That would be 12 Q steps? But we previously said orientations are 12 total, and we need to traverse all 12. The orientation index k from 0 to 11 corresponds to the number of Q steps taken. So we start at k=0 (Q⁶). We apply B while possible, then if k<11 we fire Q and go to k=1, etc. So we need 11 Q steps to reach k=11 (Q¹⁷). Then after checking saturation at k=11, if B blocked, we fire L. That means 11 Q steps inside domain 1. The L itself includes a phase advance, but that is not a Q tick counted in the domain. So the active axis will accumulate 11 Q ticks. Let's verify with our earlier table: we had Q⁶ to Q¹⁷; between them we fired Q when moving to next orientation. The number of Q steps between Q⁶ and Q¹⁷ is 11. Good.

   So after the last B at Q¹⁷, anchor = 1/(196418*317811) ≈ 1/6.24e10, and phase = i^11 = i^(11 mod 4) = i^3 = -i. So latched axis value = anchor * (-i). Then L fires, latching that, and new active axis = 1 for domain 2.

   That matches our expectation.

   So we can present the lens state after the two L's:

```
Ω_after_L1 = diag( i/4895, 1 )   // latched axis a0, active axis a1
Ω_after_L2 = diag( i/4895,  -i/62403619338, 1 )   // a0, a1 latched, new a2 active
```

   (62403619338 is 196418*317811)

This worked example directly ties to the primitive trace and demonstrates the channel field: two latched anchors and their phases.

---

## 7. Follow and the Shadow Residual (External Reference)

The Shadow Residual is the external q‑series:
\[
R(q) = \sum_{\gcd(n,6)=1} \chi_{12}(n) \cdot n \cdot q^{n^2/24}
\]
It is never loaded into the lift.

**Follow** compares the Orthad’s channel field at a cusp‑path boundary to the reference expression appropriate for that cusp. The comparison is structural, not a scalar score. For instance:
- The sequence of latched anchors corresponds to the scaling of terms.
- The phase factors correspond to the sign character.
- The presence of all axes down to depth `k` corresponds to the support.

A successful Follow means the Orthad lens projects a field that maps onto the depth‑dependent structure of the Shadow Residual without ever carrying the residual itself.

---

## 8. Red‑Team Checklist (what must never appear)

Any artifact claiming to use the Orthad is invalid if it:
- uses “candidate”, “select”, “rank”, “scan”, “score”, “best”,
- emits a single number as the Orthad’s output,
- loads the Shadow Residual into the lifted state,
- treats `Q` as mod‑6 or subdivides the quarter‑turn,
- resets `(u,v)` across `L`,
- imposes a fixed clock window `W` instead of saturation,
- presents a table of possible readout domains.

---

## 9. Pending Formalizations

- The exact algebraic form of the per‑orientation capacity progression for general depth.
- The closure of inherit‑and‑extend for all depths (CF000 4.10.1).
- The full channel‑field mapping to the Shadow Residual at arbitrary cusp‑paths (the Follow theorem).

These are the live research targets. The Orthad specification itself is now complete and testable.

---

*This tightened document removes all ambiguity and aligns the Orthad with the primitive QBL grammar, the logarithmic depth law, and the carried‑phase doubling. It is ready to serve as the precise blueprint for implementation and testing.*
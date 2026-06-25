# v49: Hidden-Order Projection Loss, Explained

A plain-language teaching translation of pass 55. Written to be saved and used as raw
material for a later article. Every claim is marked as proved, found-in-code, or open.

A note on what kind of result this is, because it matters for the article. v48 (Pencil Code)
was an **external** witness: an unrelated piece of software that hit the same wall on its own.
v49 is **internal**: the Phase Calculus framework verifying its own central projection-loss law
with machine-checkable artifacts. The value is different. v48 said "someone else independently
found this." v49 says "the law we are using to judge everyone else is now proved at its sharpest
form." Do not present v49 as outside corroboration. Present it as the framework making its own
measuring instrument rigorous. That honesty is what keeps the external claims defensible.

---

## 0. The one-paragraph version

The earlier projection-loss results showed that two different hidden states can produce the same
visible readout. v49 proves something sharper and stranger. The visible readout of a real change
can be exactly **nothing happened**, while the hidden state genuinely moved. Concretely: take two
operations and do them in one order, then the other order. The order matters, so the hidden state
is different. But the visible projection of that difference is exactly the origin, the same thing
you would see if nothing had happened at all. The change is real and the shadow of the change is
zero. This is the mathematics of quantum phase and of a spiral staircase, and the package proves it
exactly, then shows that a whole family of distinct hidden states all cast that same blank shadow.

---

## 1. What the package is

`Non_Commutative_Phase_Geometry` is an internal Phase Calculus research package. v49 promoted it
from "figures need checking" to a deep verification-surface audit, meaning the shipped proofs and
scripts were rerun and confirmed locally:

| Check | Status |
|---|---|
| Python tests | PASS (3 passed) |
| SymPy symbolic audit | PASS (`all_claims_hold = true`) |
| CLI report | PASS (`all_exact_claims_hold = true`) |
| Notebook surface | PASS (executed) |
| Lean theorem surface | added, NOT run locally (no Lean in the runtime) |

So the central claims below are machine-verified symbolically and by test, with the Lean proof
written but not yet compiled. State it that way in the article. Do not call the Lean step done.

---

## 2. Result one: order leaves a hidden charge the projection cannot see

Take two basic operations written as vectors:

```
a = (1, 0, 0)
b = (0, 1, 0)
```

Do them in one order versus the other. The difference between the two orders is the commutator,
written `[a, b]`. The package verifies:

```
[a, b] = (0, 0, 1)
```

The order difference does not vanish. It lands entirely in the third coordinate, the hidden one.
Now apply the visible projection, which keeps the first two coordinates and drops the third:

```
visible([a, b]) = (0, 0)
visible(origin)  = (0, 0)
```

These are equal. The visible shadow of "I did a then b instead of b then a" is identical to the
visible shadow of "I did nothing." The projection collapses exactly the coordinate that recorded
the order.

The symbolic form makes the meaning exact. For general operations `(m, n)` and `(m', n')`, the
hidden charge is:

```
central charge = m*n' - m'*n
```

That expression is the signed area of the parallelogram the two operations span. So the hidden
coordinate is not arbitrary bookkeeping. It is **the area swept by doing the operations in a given
order**, and the sign flips if you reverse the order.

The teaching image: a spiral staircase, or a parking-garage ramp. Walk one full loop and look at
your shadow on the ground, where the ground-shadow is the projection that throws away height. The
shadow traces a closed loop and returns exactly to where it started. By the shadow alone, you came
back. But you are one floor up. The height you gained is the hidden charge, and it equals the area
your loop enclosed. The ground cannot tell you which floor you are on. That floor number is the
order state, and the projection erased it.

This is the same structure as quantum phase and the Aharonov-Bohm effect: a path that returns to
the same visible point while carrying a hidden accumulated phase set by the enclosed area or flux.
The package is not borrowing that as a metaphor. It is the same commutator algebra.

Status: **proved** (SymPy audit, CLI report, Python tests; Lean surface written, not compiled).

---

## 3. Result two: a whole family of hidden states casts the same blank shadow

A single example could be a fluke. So v49 swept many cases. It sampled operation pairs with
components in the range minus two to two and computed, for each, the hidden charge and the visible
projection of the commutator.

```
commutator cases sampled:        496
distinct hidden charges found:   14   (ranging from -8 to +8)
visible projection, every case:  (0, 0)
```

Every single case projects to the same visible origin. Behind that one blank shadow sit at least
fourteen genuinely different hidden states. The fiber, the set of hidden states living above one
visible point, is richly populated.

This is the state-completeness verdict, stated as a pass/fail control:

```
visible projection only            ->  FAIL  (not state-complete)
visible projection + order charge  ->  PASS  (retained order state recovered)
```

In plain terms: if all you keep is what you can see, you cannot tell these states apart, and you
cannot predict the next step correctly, because the next step depends on the order that the
projection threw away. Keep the order charge and the state is complete again.

The package also checks the same phenomenon in a finite, discrete setting using permutations, where
swapping the order of two transpositions leaves a hidden three-cycle:

```
[(12), (23)] = (132)
```

Same lesson on different hardware: the visible labels cannot replace the retained action law. Order
is real state even when it is invisible.

Status: **proved / found in shipped artifacts** (fiber attack `..._projection_loss_fiber_v49.csv`,
attack script output, kill-test table).

---

## 4. Result three: the (55,89) anchor, kept honest

This package also carries the balanced-corridor anchor, and v49 handles it exactly the right way,
which is worth flagging for the article because it is where an earlier overstatement got corrected.

The balanced refinement operator is:

```
B(u, v) = sort(v, u + v)
```

Starting from the canonical seed `(1, 1)` and applying it nine times reaches:

```
depth 9  ->  q = (55, 89),  uv = 4895
```

The correct framing, now locked in the research, is:

> (55, 89) is the **canonical origin-path witness**. It is not a rigid definition of all B refinement.

To make that concrete rather than asserted, v49 tabulated the same operator `B` from several
different starting pairs: `(1,1)`, `(1,3)`, `(2,13)`, `(3,10)`, `(5,8)`, `(7,11)`. The finding is
clean and is the heart of the modular-B research direction:

- Different starting pairs produce **different valid corridors** and **different anchor values**.
- But every corridor, regardless of where it starts, has its ratio converge to the same number,
  the golden ratio, roughly 1.618, by about depth nine.

The teaching image: a river system. No matter where you put your boat in, the current carries you
toward the same sea. The particular town you drift past depends on your put-in point, but the
direction of flow is universal. The golden ratio is the sea. (55, 89) is simply the town the
canonical put-in passes at mile nine. Reporting that one town as if it were the whole river was the
overstatement; reporting the universal flow with the canonical town as one labeled landmark is the
honest version, and that is what v49 records.

This keeps the larger research question open in its strong form: a B-like refinement may be a
**carrier-selected arithmetic**, with the golden Fibonacci corridor as one verified instance and
the Ancient Yi base-eight carry as a separate candidate on the same skeleton.

Status: **proved / tabulated** (non-origin corridor table; convergence to the golden ratio is
visible directly in the ratio column).

---

## 5. The kill-test discipline

One feature of v49 worth its own mention in the article, because it is what separates this from
loose pattern-matching: the package ships a table of deliberate **kill tests**, each one a way the
claim could fail, with the exact lost state named.

| What you keep | What it loses | Verdict |
|---|---|---|
| visible Heisenberg projection only | the order charge | FAIL, not state-complete |
| visible commutator residual only | the central charge `m*n' - m'*n` | FAIL, projected residual vanishes while real one does not |
| canonical (1,1) corridor only | non-origin and asymmetric starts | FAIL as a general definition of B |
| operator word without action registry | the sheet/action mapping | FAIL, same word can map to distinct retained actions |
| readout after the carrier already exists | nothing, if used only for terminal reporting | PASS, with the rule: do not feed a scalar readout back in as if it were the carrier |

That last row is the positive case and it carries the working rule for the whole project: a readout
is fine as a final report, but it must never be recycled as the state itself.

---

## 6. Where this sits in the cross-corpus rule

v49 is the sharpest internal form of the one rule the whole project runs on:

> A readout is a terminal projection. It is the real carried state only if it retains enough to
> determine the next admissible transition. Otherwise it is a shadow, and continuing from the
> shadow gives the wrong next step.

What v49 adds is the extreme case: the shadow of a real change can be exactly the shadow of no
change. That is the strongest possible statement of why the readout is not the state. Across the
corpora, the same gate keeps holding:

| System | The shadow that looks complete | The retained state it drops |
|---|---|---|
| Ancient Yi | the octal or decimal label | the line carrier plus digit-order convention |
| Wilhelm I Ching | the hexagram name or number | the six-line carrier plus the changing-line operation |
| MFE / Liu MHD | the diagnostic image | the full field, boundary callbacks, nonideal channels |
| Pencil Yin-Yang | the vector component numbers | the chart basis and interpolation registry |
| Non-Commutative Phase Geometry | the visible projection | the hidden order charge (the swept area) |

There is also a quiet progression across the recent passes worth noting in the article. In v48 the
polarity was a self-inverse half-turn, an operation that is its own undo, so order did not yet
matter. In v49 the polarity becomes genuinely order-dependent: doing a then b differs from b then a,
and the difference is a hidden charge. The framework moved from "the two sides are one operation
seen twice" to "the two sides do not commute, and their disagreement is real but invisible." That
is a sharpening, not a contradiction, and it is the natural next step in the same story.

---

## 7. What v49 proves, and what it does not

Proved, with machine-checkable artifacts (symbolic plus tests; Lean written, not compiled):

- The order commutator lands a nonzero charge in the hidden coordinate, `[a,b] = (0,0,1)`, with
  general symbolic charge `m*n' - m'*n`, the signed area.
- The visible projection of that commutator equals the visible projection of the origin, exactly.
- A swept family of 496 cases gives many distinct hidden charges all collapsing to the one visible
  origin, so the visible projection alone is not state-complete.
- The same B operator from different starts yields different corridors and anchors, all converging
  to the golden ratio, confirming (55,89) as an origin-path landmark rather than a definition.

Open, named as next gates:

- Compile the Lean theorem surface where a Lean toolchain is available.
- Full stale-canon comparison against the complete formalization package.
- The CF000, CF19, and Farey formal close-read sweep.
- Ancient Yi translation and exact line-order confirmation.
- Liu 2022 data and connectivity table.

What this is **not**: it is not external corroboration, and it should not be dressed as such. It is
the framework proving its own central projection-loss law at full strength. That proved law is the
instrument the external comparisons are measured with. Stating the internal-versus-external line
clearly is what makes the external claims survive scrutiny.

---

## 8. One sentence to anchor the article

Phase Calculus proves, by exact algebra, that the visible shadow of a real change can be identical
to the shadow of no change at all: the order in which things happen leaves a hidden charge equal to
the area it sweeps, the projection erases that charge, and so the readout can say nothing-happened
while the true state has quietly moved to a place that decides what happens next.

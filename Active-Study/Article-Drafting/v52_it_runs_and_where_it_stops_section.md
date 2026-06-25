# Section: It Runs, and Where It Stops (v52)

*Role in the larger piece.* This is the capstone of the internal cluster and the bridge to the
closing assessment. The earlier internal sections established the gate, sharpened it, and turned it
inward on the framework's own text. This section asks the last and most deflating question you can
ask of any formal claim: does it actually run. It takes the framework's core executable surfaces,
the assembly kernels and the full engine, reruns them from real code and data, and checks whether the
claims survive execution rather than only reading correctly on paper. Most do. One does not close, and
this section says so plainly. That honesty is the reason it sits immediately before the closing
assessment, which has to weigh exactly what is and is not established. It is internal verification, not
outside corroboration, and it assumes the shared rule and table from the outside-witness section.

---

## Paper-true is not replay-true

There is a difference between a claim that reads correctly and a claim that executes. A recipe can
parse perfectly and still fail in the pan. This section is the pan. The framework ships executable
surfaces, including kernels written in C and assembly, and v52 reran them:

```
overflow-to-(55,89) code        PASS
Farey balanced-anchor kernel    PASS  (C runner plus assembly kernel)
Xi full-engine kernel           PASS  (C runner plus assembly kernel)
Tdelta balanced kernel          PASS
Ramanujan residual windows      PASS
CF19 extension symbolic check   PASS
```

"PASS" here means the code ran and produced the claimed structure, not that a human agreed the prose
was plausible. That is a stronger standard than close-reading, and it is the standard the rest of
this section reports against.

---

## The anchor, run as code

The hidden-order section used a river image: wherever you put the boat in, the current carries you to
the same golden sea, and the particular town you pass depends on the put-in point. v52 runs that image
as code. Two canonical starts, executed through the assembly kernel:

```
(1,1)  ->  step 9  ->  (55,89),  uv = 4895
(1,2)  ->  step 8  ->  (55,89),  uv = 4895
```

Both canonical put-ins reach the same anchor town, at the depth their starting point implies, nine
steps from one and eight from the other. Then the non-origin probe, the part that keeps the claim
honest, also run as code:

```
(1,3)   ->  (76,123),  uv = 9348
(2,13)  ->  (71,114),  uv = 8094
(3,10)  ->  (59,95),   uv = 5605
(7,11)  ->  (76,123),  uv = 9348
```

Different starts reach different floor anchors. The operator is the same; the landing depends on the
carried state. This is the executable confirmation of a correction made much earlier in the project:
(55,89) is the canonical-corridor landmark, not the definition of all refinement. The correction is
no longer an argument. It is a rerun. For the merged draft this is worth stating exactly that way,
because a claim that survives execution from assembly is a different kind of object than a claim that
survives a reading.

Status: proved by replay. Anchor reruns and the non-origin probe both pass.

---

## The flagship engine confirms the rule

Until now the state-completeness rule was shown on focused witnesses. v52 confirms it on the framework's
full engine, Xi. Tracing the engine exposes the fields it actually carries:

```
A, theta_ticks, kappa, u, v, uv, floor_den, window_ready, live_word, lowbit, carry_event
```

And the state-completeness matrix records the verdict bluntly: the live word alone is not
state-complete, and even the carried pair `q = (u,v)` alone is not state-complete. Each drops
something the next transition needs. Carry events fire on a 64-step rollover:

```
step 64   ->  A = 1,  theta = 64,   kappa = 16
step 128  ->  A = 2,  theta = 128,  kappa = 32
step 192  ->  A = 3,  theta = 192,  kappa = 48
```

The teaching image: a cockpit dashboard. One needle, the word, or one gauge, the pair, does not tell
the pilot what to do next. The next move depends on the whole panel, altitude, heading, fuel, the
lot. The engine is state-complete only as the full panel. This is the same rule the whole essay runs
on, now confirmed on the flagship rather than a model problem.

Status: proved by replay.

---

## Paper and execution agree on the stale operator

The reflexive section demoted an older operator on paper, the lift that reset its carried pair and so
failed the framework's own hygiene gate. v52 finds the same operator in the running kernel and watches
it misbehave. The Tdelta kernel fires a branch-local reset every ten ticks, resetting the pair to
`(1,1)` and cycling the carried value through zero to three:

```
Tdelta: resets pair to (1,1), cycles q through 0..3, every 10 ticks
```

That is the elevator that empties your pockets, caught in the act. Corrected `L` carries the pair and
the phase forward; Tdelta throws them away. So the paper-level demotion and the execution-level trace
agree: Tdelta is a useful historical witness and is stale against the corrected canon. When a
framework's prose judgment and its running code reach the same verdict about which of its own parts to
retire, that agreement is itself a quiet kind of evidence, and the merged draft should note it.

Status: proved by replay, consistent with the reflexive section.

---

## Where it stops: the 1/24 frontier, named honestly

This is the most important paragraph in the section, because it is where the project declines to
overclaim at exactly the point where overclaiming would be most tempting.

There is a deep number sitting at the anchor's completion: `1/24`, with `1/12` for the two-sided
germ. That `1/24` is not arbitrary. It is the signature exponent of the Dedekind eta function, the
fingerprint of modular forms, the same constant that runs through Ramanujan's work and through the
Shadow channel the project has wanted to close since early on. v52 reran the Ramanujan residual
windows and they reproduce the pattern:

```
edge target:       1/24
full-germ target:  1/12
edge max abs error:  ~1.11e-06
full max abs error:  ~2.22e-06
```

The numbers come within about a millionth. And the framework's own gate summary, in its own words,
refuses to call that closure:

> The numerical residual window supports the 1/24 edge and 1/12 full-germ coefficient pattern, but it
> is a bridge witness, not Shadow Residual closure.

The strict tolerance flag is false. The residual window remains a terminal external comparison
channel, not a proof that the modular structure is the same structure. This is the project holding its
own line. Reproducing a pattern to six decimal places, against the most seductive target in the whole
investigation, is reported as a supporting witness and explicitly not as the thing it most wants to be
true. For the essay this is the cleanest possible demonstration that the proved-versus-open discipline
is real and not decorative, and it should be given room in the closing assessment rather than buried.

Status: open. The 1/24 and 1/12 pattern is reproduced numerically. The Shadow Residual is not closed.

---

## What this section contributes, and what stays open

Contributes to the merged draft: the executable-replay standard, which raises the internal claims from
paper-true to replay-true; the anchor and the B-scope correction confirmed by running assembly rather
than by argument; the flagship engine confirming the state-completeness rule; the agreement between
the paper-level and execution-level demotion of the stale reset operator; and, most valuable for the
essay's credibility, the honest non-closure of the 1/24 Shadow frontier.

Stays open, and the project says so itself, declining to claim completion: the Ancient Yi full
translation and line-order proof, the Liu 2022 plasma data, local Lean compilation, a final proof
audit, and the latest active sources still on local storage. The reported overall pass is high but
explicitly not total, and the section keeps it that way.

A guard to preserve through the merge: do not let the 1/24 result drift from "reproduced to a
millionth" into "the modular connection is established." The framework itself does not make that step,
and the essay's whole claim to rigor rests on not making it either. The gap between a reproduced
pattern and a closed structure is exactly the kind of gap this project exists to respect.

*Hands off to.* With the internal claims now shown to execute, the stale parts retired in both prose
and code, and the one deep frontier left honestly open, the witnesses are complete. What remains
before the closing is to gather them: the next section consolidates every internal and external
result into a single gate and a typed catalogue of the ways that gate can fail, and shows why the
bridges cohere without collapsing into the claim that these systems are the same system.

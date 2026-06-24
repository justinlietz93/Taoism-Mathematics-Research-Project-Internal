# Code Close-Read Pass 1

## Scope

This pass reviews the code explicitly queued by the user before the dossier can be considered wrapped. It is a close-read of mechanism, not a verdict-generating probe.

Reviewed in this pass:

1. `source/code/yinyang_transform.py`
2. `source/code/iching-wilhelm-dataset-master/data/i-ching-basic.js`
3. `source/code/iching-wilhelm-dataset-master/README.md`
4. `source/Phase-Calculus-Research-Pkgs/CF19_The_Full_Lifted_Object/code/python/overflow_to_55_89_code.py`
5. `source/Phase-Calculus-Research-Pkgs/CF19_The_Full_Lifted_Object/code/python/ramanujan_residual_balanced_windows_code.py`
6. `source/Phase-Calculus-Research-Pkgs/CF19_The_Full_Lifted_Object/code/farey_balanced/farey_balanced_anchor_kernel.S`
7. `source/Phase-Calculus-Research-Pkgs/CF19_The_Full_Lifted_Object/code/farey_balanced/farey_balanced_anchor_runner.c`
8. `source/Phase-Calculus-Research-Pkgs/CF19_The_Full_Lifted_Object/code/xi_full_engine/xi_full_engine_kernel.S`
9. `source/Phase-Calculus-Research-Pkgs/CF19_The_Full_Lifted_Object/code/xi_full_engine/xi_full_engine_runner.c`
10. `source/code/MFE_pub-main/README.txt` and `source/code/MFE_pub-main/python/pyMFE.py`

---

## 1. `yinyang_transform.py`

### What it actually implements

The script implements a two-patch Yin/Yang coordinate re-chart on a unit sphere.

Core transform:

```python
x_e = -x_n
y_e =  z_n
z_e =  y_n
```

The inverse uses the same rule:

```python
x_n = -x_e
y_n =  z_e
z_n =  y_e
```

In matrix form:

```text
M = [[-1, 0, 0],
     [ 0, 0, 1],
     [ 0, 1, 0]]
```

Direct check:

```text
M^2 = I
det(M) = 1
eigenvalues = {+1: 1, -1: 2}
```

### Mechanism read

This is an exact L-like re-chart:

```text
one spherical coordinate chart has a boundary/singularity problem
→ introduce complementary orthogonal patch
→ transform state across patch boundary
→ reuse the same analytic machinery in the new chart
```

It is not Q by itself. It is an involutive coordinate-domain swap / patch re-articulation.

### Relevance

Strong L lead.

The script is especially important because it is not merely a paper description. It is executable code for:

```text
same object
same sphere
new coordinate frame
boundary values transferred through a deterministic transform
```

This maps directly to the Phase Calculus distinction:

```text
visible projection changes / coordinate frame changes
while retained object remains the thing being transported
```

---

## 2. `iching-wilhelm-dataset-master/data/i-ching-basic.js`

### What it contains

A 64-row hexagram table. Each row contains:

```text
hex number
hex glyph
Chinese name
pinyin
English gloss
6-bit binary string/number
od field
```

The binary field is explicit. Examples:

```text
1  = 111111
2  = 000000
11 = 000111
12 = 111000
63 = 010101
64 = 101010
```

### Complement-pair check

Parsing all 64 rows gives exactly 32 complement pairs under bitwise inversion.

Examples:

```text
1  111111 ↔ 2  000000
11 000111 ↔ 12 111000
29 010010 ↔ 30 101101
63 010101 ↔ 64 101010
```

The `od` field matches these complement/opposite partners for the inspected rows.

### Mechanism read

This is a concrete six-position binary carrier. It is not metaphorical:

```text
six line seats
binary line state
64 complete states
bitwise complement involution
opposite-state pairing
```

### Q/B/L relevance

- Q: supports the six-seat carrier side, not the quarter-turn orbit by itself.
- B: supports branch/state expansion as binary line stacking but does not encode Fibonacci/Farey depth.
- L: supports complement/inversion as a discrete state involution.

### Important distinction

This dataset does **not** prove QBL. It does prove that the Yijing side has an explicit six-bit carrier with complement pairing, which is directly relevant to the six-seat / line-seat part of the investigation.

---

## 3. `iching-wilhelm-dataset-master/README.md`

### What it says

The dataset wraps Wilhelm/Baynes I Ching text and exposes structured hexagram data. The README contains the full hexagram text examples, line comments, and data use notes.

### Mechanism read

For this investigation, the code/data value is higher than the commentary value:

```text
64 hexagrams are available as structured machine-readable six-line states.
```

This makes the I Ching material testable as data rather than only literary text.

### Use next

Use this dataset for:

```text
- complement-pair mapping
- line-reversal mapping
- upper/lower trigram product decomposition
- 8×8 grid/product-space verification
- hexagram 11/12 order-dependent dynamics check
```

---

## 4. `overflow_to_55_89_code.py`

### What it implements

This file implements the B corridor directly.

Core function:

```python
def balanced_step(u, v):
    a, b = sorted((int(u), int(v)))
    return b, a + b
```

Trace rule:

```text
while uv < floor_den:
    (u,v) ← balanced_step(u,v)
```

With `floor_den = 4096`, from `(1,1)` the first floor hit is `(55,89)`:

```text
uv = 4895
r = 1/4895
germ width = 2π/4895
```

### Mechanism read

This is exact internal B.

It carries:

```text
B-depth
Fibonacci corridor
floor threshold
completion-germ width
ratio convergence toward φ
```

### Correction locked

B is not unresolved internally. This code and the corresponding paper/figure are direct evidence of the exact B path.

External unresolved question only:

```text
Does Tao/Yijing/Chinese-math material contain an independent analogue of depth-refinement / floor-anchor behavior?
```

---

## 5. `ramanujan_residual_balanced_windows_code.py`

### What it implements

The file computes balanced Fibonacci corridor anchors and evaluates residual coefficients from a q-Pochhammer product near the balanced completion windows.

Key expressions:

```python
t = 2 * pi / uv
q = exp(-t)
log_qpoch = sum log(1 - exp(-t*m))
edge_coeff = (log_qpoch + pi^2/(6*t) - 0.5*log(2*pi/t)) / t
full_germ_coeff = 2 * edge_coeff
```

Targets:

```text
edge coefficient       → 1/24
full two-sided germ    → 1/12
```

### Mechanism read

This is the computational bridge between:

```text
balanced B corridor
→ q-window
→ Ramanujan/Dedekind-style residual coefficient
→ 1/24 and 1/12 targets
```

### Relevance

Strong Shadow/modular lead. It should be checked against eta/theta machinery, not only treated as a numerical convergence script.

---

## 6. `farey_balanced_anchor_kernel.S` + runner

### What it implements

Assembly-level implementation of the B path:

```asm
# balanced_step(u,v) = (b, a+b), with a<=b
cmp rcx, rdx
jbe .ordered
xchg rcx, rdx
.ordered:
lea r8, [rcx + rdx]
mov r10, rdx
mov r11, r8
```

It records rows:

```text
step,u,v,uv,hit_floor
```

and halts when:

```text
uv >= floor_den
```

### Mechanism read

This is not a toy notebook only. The exact B recurrence is lowered to machine-level integer arithmetic and produces a trace artifact.

### Relevance

This strengthens the claim that B is a hard operator in the package, not post hoc language.

---

## 7. `xi_full_engine_kernel.S` + runner

### What it implements

This file contains a compact executable kernel for live retained-state evolution.

State fields include:

```text
step
live_word
carry_event
A
theta_ticks
kappa
u,v,uv
floor_den
window_ready
r_num,r_den
cL,cR,c_den
lowbit
```

Important mechanics:

### Primitive live-word law

```asm
mov rcx, rax
neg rcx
and rcx, rax
mov [lowbit], rcx
add rax, rcx
setc bl
adc rax, 0
```

This isolates the low bit and updates the live word; carry triggers articulation.

### Q-like theta/kappa memory

```asm
theta_ticks += 1
kappa = theta_ticks >> 2
```

This records quarter-turn ticks and completed four-tick turns.

### Carry-triggered lift/articulation

```asm
if carry:
    A += 1
    u = 1
    v = A
    window_ready = 0
```

### B-like balanced arithmetic limb

If no ready window and no carry tick, it walks:

```text
(u,v) → (b,a+b)
```

### Completion germ

The kernel writes:

```text
r = 1/uv
c = [(theta*uv - 2)/(2uv)π, (theta*uv + 2)/(2uv)π]
```

### Mechanism read

This is the package’s closest executable Q/B/L state machine:

```text
Q: theta ticks and kappa memory
B: balanced (u,v) corridor
L/carry: articulation-class promotion and new lifted seed
Projection: output trace fields are readout; retained state is richer than any one field
```

### Code note

`cL_num` and `cR_num` are stored in unsigned fields but sometimes represent negative values by two’s-complement wrap and are printed as signed. This is a code hygiene / representation issue, not a mathematical contradiction, but it should be cleaned in any publication-grade kernel.

---

## 8. `MFE_pub-main` and `pyMFE.py`

### What it is

The MFE code is an external magnetohydrodynamic simulation code. Its README says it solves single-fluid MHD equations in Cartesian or spherical grids, with output variables such as magnetic field components, velocity components, density, and energy. `pyMFE.py` reads binary output, grid files, and physical parameters.

### Mechanism relevance

Not direct QBL evidence.

Relevant only as an external computational environment for:

```text
- 3D vector fields
- magnetic flux emergence / eruption
- field topology
- boundary-driven simulations
- coordinate/grid data handling
```

### Caution

Do not count MFE as evidence that Taoist/QBL structure exists. It is only a possible application/analogue environment for testing topology, retained-field branch behavior, and grid re-charting ideas.

---

## Required next code pass

1. Parse `iching_wilhelm_translation.csv/js` to derive:
   - upper trigram / lower trigram product space,
   - complement pairs,
   - reversal pairs,
   - King Wen order vs binary order vs opposite/`od` relation.
2. Inspect `MFE_pub-main/ModGrid.F`, `ModInterp.F`, and `ModBoundary.F` only for grid/boundary/interpolation mechanics.
3. Inspect any `pencil-code` Yin-Yang implementation if unzipping is permitted; this is lower priority than the curated visible code.
4. Run no new verdict-generating probes until the paper notes have caught up.

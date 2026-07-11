# QBL Prime-Pattern Watch

**Status:** active arithmetic observation layer attached to the clean primitive custody law  
**Authority boundary:** no R/S/T scheduler, no fixed execution window, no projected readout  
**Current scan:** exact primality tests through `A = 1000`  
**B-count convention:** current terminal floor-crossing law used by the custody trace

---

## 1. Purpose

This note records the prime structure appearing in the number of primitive `Q` and `B` operations executed in each domain.

The goal is not to declare a prime law prematurely. It is to preserve exact formulas, identify established number-theoretic structure, and maintain a deterministic watch surface for new patterns.

The domain index is

\[
A=0,1,2,\ldots
\]

and the primitive execution law remains:

```text
try B first
if B is blocked, try Q
if B and Q are both blocked, fire L
reevaluate from B after every primitive step
```

---

## 2. Exact number of Q operations

Domain `A` has

\[
N_A=6\cdot2^A
\]

available phase positions. The initial position is present before any `Q` operation, so the number of executed `Q` operations is

\[
\boxed{Q_A=N_A-1=6\cdot2^A-1.}
\]

Equivalently,

\[
\boxed{Q_A=3\cdot2^{A+1}-1.}
\]

Therefore the Q-count sequence is exactly the Thabit-number sequence `3·2^n−1`, with the exponent shifted by

\[
n=A+1.
\]

A domain has a prime Q count exactly when `A+1` is a Thabit-prime exponent.

The sequence begins

\[
5,11,23,47,95,191,383,767,1535,3071,6143,\ldots
\]

---

## 3. Periodic composite classes for Q

For an odd prime `p` not dividing `6`,

\[
p\mid Q_A
\]

if and only if

\[
2^A\equiv6^{-1}\pmod p.
\]

If one solution `A=r` exists, every solution repeats with period equal to the multiplicative order of `2` modulo `p`:

\[
A\equiv r\pmod{\operatorname{ord}_p(2)}.
\]

Thus every discovered prime divisor creates an infinite arithmetic progression of composite Q-count domains.

| Guaranteed divisor | Composite-domain class |
|---:|:---|
| `5` | \(A\equiv0\pmod4\) |
| `11` | \(A\equiv1\pmod{10}\) |
| `23` | \(A\equiv2\pmod{11}\) |
| `47` | \(A\equiv3\pmod{23}\) |
| `13` | \(A\equiv7\pmod{12}\) |
| `19` | \(A\equiv4\pmod{18}\) |
| `37` | \(A\equiv9\pmod{36}\) |

The first member of a class can equal the divisor itself. For example:

\[
Q_0=5,\quad Q_1=11,\quad Q_2=23,\quad Q_3=47.
\]

Later members of the same residue classes are composite.

### Q-prime domains through A = 1000

```text
0, 1, 2, 3, 5, 6, 10, 17, 33, 37, 42, 54, 63, 75, 93,
102, 142, 205, 215, 305, 323, 390, 457, 469, 826
```

This list is complete only through the declared scan range.

---

## 4. Exact B-count definition

Each `B` operation advances one step along the balanced Fibonacci corridor:

\[
(1,1)\xrightarrow{B}(1,2)\xrightarrow{B}(2,3)\xrightarrow{B}\cdots
\]

After `m` total B operations, the pair is

\[
(F_{m+1},F_{m+2}).
\]

The final global Q-position index of Domain `A` is

\[
j_A=6(2^{A+1}-1),
\]

so the final capacity is

\[
\Delta_A=2^{2j_A}
       =2^{12(2^{A+1}-1)}.
\]

Under the current terminal floor-crossing law, define the cumulative B depth

\[
T_A=
\min\left\{
 m:
 F_{m+1}F_{m+2}\ge \Delta_A
\right\}.
\]

The number of B operations executed inside Domain `A` is

\[
\boxed{B_A=T_A-T_{A-1}},
\qquad T_{-1}=0.
\]

This definition is exact and order-preserving. It does not count B operations independently of the Q positions that expose their available refinement capacity.

---

## 5. B counts form an irrational near-doubling sequence

Using

\[
F_n\sim\frac{\varphi^n}{\sqrt5},
\qquad
\varphi=\frac{1+\sqrt5}{2},
\]

we obtain

\[
B_A=
\frac{6\log2}{\log\varphi}\,2^A+O(1).
\]

Define

\[
\alpha=\frac{6\log2}{\log\varphi}
\approx8.6425205424753388741.
\]

Then

\[
B_A\approx\alpha2^A.
\]

The sequence begins

```text
9, 18, 34, 69, 139, 276, 553, 1107, 2212, 4425,
8850, 17700, 35400, 70799, 141599, 283198, 566396,
1132793, 2265585, 4531170, ...
```

The values nearly double, but the irrational threshold placement causes bounded rounding corrections.

Define

\[
d_A=B_A-2B_{A-1}.
\]

Through `A = 1000`, the only observed corrections are

\[
\boxed{d_A\in\{-2,-1,0,1,2\}.}
\]

Observed frequencies through `A = 1000`:

| \(d_A\) | Count |
|---:|---:|
| `-2` | 121 |
| `-1` | 251 |
| `0` | 244 |
| `1` | 275 |
| `2` | 109 |

This bounded correction is the first clear structural pattern in the B-count sequence.

---

## 6. Prime gate for B counts

For `A>0`,

\[
B_A=2B_{A-1}+d_A.
\]

The doubled term is even. Therefore an odd B count requires odd `d_A`. Under the observed correction bound, every prime B count greater than two must occur at

\[
\boxed{d_A=\pm1.}
\]

This is a necessary candidate gate, not a sufficient primality condition.

Every B-prime event found through `A = 1000` passes this gate.

### B-prime domains through A = 1000

```text
4, 17, 56, 72, 147, 177, 200, 294, 367, 878
```

The first events are:

| Domain `A` | \(B_A\) | Correction \(d_A\) |
|---:|---:|---:|
| 4 | 139 | 1 |
| 17 | 1,132,793 | 1 |
| 56 | 622,759,236,714,140,689 | -1 |
| 72 | 40,813,149,337,297,924,234,699 | -1 |

The B-prime list is a result of the QBL threshold construction. No established external name is currently assigned to this sequence in this note.

---

## 7. Simultaneous Q-prime and B-prime domains

Through `A = 1000`, exactly one domain has both counts prime:

\[
\boxed{A=17.}
\]

At that domain,

\[
Q_{17}=786431,
\]

and

\[
B_{17}=1132793.
\]

Both are prime.

This coincidence is worth retaining as a named witness, but it is not yet evidence of a general coupling theorem.

```text
SIMULTANEOUS_PRIME_WITNESS_0:
A = 17
Q_A = 786431
B_A = 1132793
```

---

## 8. Why the two prime structures differ

The Q count has a closed exponential form:

\[
Q_A=6\cdot2^A-1.
\]

Its composite structure is governed by periodic modular residue classes in `A`.

The B count is a threshold-depth difference:

\[
B_A=T_A-T_{A-1},
\]

where `T_A` is determined by a Fibonacci product crossing an exponentially expanding capacity. Its prime candidates are governed by irrational rounding and the near-doubling correction sequence.

Therefore:

```text
Q-primality:
    Thabit-prime problem
    periodic modular sieves in A

B-primality:
    Fibonacci threshold-depth problem
    irrational near-doubling corrections

joint primality:
    intersection of two distinct arithmetic mechanisms
```

That intersection is the most natural place to look for genuinely Orthad-specific prime structure.

---

## 9. Prime-pattern watch protocol

Every extension pass should record:

1. `A`.
2. `Q_A` and primality.
3. The smallest factor of composite `Q_A`.
4. `T_A` and `B_A`.
5. `B_A` primality.
6. `d_A = B_A - 2B_(A-1)`.
7. Whether both counts are prime.
8. Residues of `A`, `Q_A`, and `B_A` modulo the current small-prime basis.
9. Whether a newly found factor creates a new periodic composite class for Q.
10. Whether a B-prime event violates the observed `d_A = ±1` gate.

A new result is load-bearing only if it is emitted from these exact formulas and independently primality-tested.

---

## 10. Active questions

### Q1. Are there infinitely many prime Q counts?

This is the classical open question of whether infinitely many Thabit primes exist. The QBL law lands exactly on that existing number-theoretic frontier.

### Q2. Is the B correction bound global?

Current evidence supports

\[
B_A-2B_{A-1}\in\{-2,-1,0,1,2\}
\]

through `A = 1000`. A proof should descend from the exact ceiling/Binet representation of `T_A`.

### Q3. Can B-prime domains be characterized by the doubling orbit?

The candidate question is whether the fractional orbit controlling the threshold rounding yields a symbolic or modular characterization of `d_A=\pm1` events.

### Q4. Does simultaneous primality recur?

The only event through `A = 1000` is `A=17`. The next occurrence, if any, is an exact falsifiable target.

### Q5. Do prime events alter the Orthad gauge/FQM structure?

The operation counts alone are not retained truth. The relevant question is whether prime-count domains correlate with a change in:

- lens-pairing rank structure;
- transition-record order;
- holonomy;
- doubled-carrier decomposition;
- FQM isometry class;
- generated Weil orbit.

That comparison must be performed in the full lifted Orthad, not from the counts alone.

---

## 11. Companion artifacts

- `qbl_prime_watch.py`: deterministic CLI scanner and modular sieve.
- `QBL_Prime_Pattern_Watch_v1.ipynb`: executed SymPy notebook with figures and PASS/FAIL checks.
- `QBLPrimePatternWatch.lean`: Lean 4 theorem surface for the Q identity, modular periods, and finite prime witnesses.

Lean was not available in the current build container, so compilation of the Lean source is not claimed.

---

## 12. External sequence identification

The Q-count identity places the sequence inside established number theory:

- OEIS A007505: primes of the form `3·2^n−1`.
- OEIS A002235: exponents `n` for which `3·2^n−1` is prime.
- MathWorld: *Thâbit ibn Kurrah Prime*.

The QBL domain index is shifted by one:

\[
n=A+1.
\]

The B-count and joint-prime sequences remain specific to the present capacity/refinement construction unless an exact prior identification is found.

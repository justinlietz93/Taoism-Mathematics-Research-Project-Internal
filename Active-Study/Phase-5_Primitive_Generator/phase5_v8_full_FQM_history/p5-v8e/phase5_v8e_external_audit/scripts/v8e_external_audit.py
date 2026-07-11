#!/usr/bin/env python3
"""Phase 5 v8e external audit (2026-07-09).

Independent verification of the v8e size-2 Family-F isometry classifier.
Written from scratch against the package, not derived from its code paths.

Checks:
  1. ORBIT REPRODUCTION: re-implements the v8e Aut-orbit machinery verbatim
     and, separately, a from-scratch brute-force isometry decider that tests
     full form equality q_B(f(x)) == q_A(x) over ALL group elements for every
     candidate generator-image pair. The two must agree on every tested (D1,D2).
  2. CROSS-SHAPE RIGIDITY GATE: v8e compares presentations only within a fixed
     shape (D1,D2). Same abstract group can carry two shapes, e.g.
     Z/4 x Z/6 ~= Z/2 x Z/12. This audit exhaustively tests every same-group
     shape-alias pair inside the v8e D range for cross-shape isometries.
     v8e's completeness claim silently assumes there are none.

Result on 2026-07-09: check 1 agrees exactly on all tested pairs; check 2
finds ZERO cross-shape isometries across all four alias pairs in range.
Status of the rigidity claim: CONJECTURED_LEMMA_EMPIRICALLY_GATED (not proven).

Family-F conventions (must match v8d/v8e; ledger-registered):
  carrier Z/D1 x Z/D2, D_i even
  q(a,b)   = a^2/(2*D1) + b^2/(2*D2) + c*a*b/lcm(D1,D2)   (mod 1)
  b(x,y)   = polarization; q determined by q(e1), q(e2), b(e1,e2)
  admissible c: multiples of lcm/gcd, i.e. valid_cs below

Exact arithmetic: all q values are held as integers over a common denominator.
No floats anywhere in the decision path.
"""

import csv
import sys
from itertools import combinations
from math import gcd
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "outputs"
OUT.mkdir(parents=True, exist_ok=True)


def lcm(a, b):
    return a * b // gcd(a, b)


# ---------------------------------------------------------------------------
# Shared family definitions (identical to v8d/v8e registered conventions)
# ---------------------------------------------------------------------------

def valid_cs(D1, D2):
    """Representative-invariant edge residues: multiples of lcm/gcd mod lcm."""
    L = lcm(D1, D2)
    g = gcd(D1, D2)
    step = L // g
    return [k * step % L for k in range(g)]


def denom(D1, D2):
    """Common integer denominator for exact q/b arithmetic on this shape."""
    return lcm(lcm(2 * D1, 2 * D2), lcm(D1, D2))


def q_int(x, D1, D2, c, M):
    """q(x) * M as an integer mod M (exact)."""
    a, b = x
    L = lcm(D1, D2)
    return (a * a * (M // (2 * D1)) + b * b * (M // (2 * D2)) + c * a * b * (M // L)) % M


def b_int(x, y, D1, D2, c, M):
    """b(x,y) * M as an integer mod M (exact polarization)."""
    a, b = x
    p, q = y
    L = lcm(D1, D2)
    return (a * p * (M // D1) + b * q * (M // D2) + c * (a * q + b * p) * (M // L)) % M


# ---------------------------------------------------------------------------
# Arm 1: v8e's Aut-orbit machinery, re-implemented faithfully
# ---------------------------------------------------------------------------

def allowed_entries(D1, D2):
    Ds = [D1, D2]
    vals = []
    for Dr in Ds:
        row = []
        for Dorder in Ds:
            row.append([m for m in range(Dr) if (Dorder * m) % Dr == 0])
        vals.append(row)
    return vals


def is_auto_matrix(D1, D2, m11, m12, m21, m22):
    """Surjectivity (= bijectivity on a finite group) via Smith-form criterion:
    gcd of all 2x2 minors of the column lattice [(D1,0),(0,D2),(m11,m21),(m12,m22)]
    must be 1."""
    cols = [(D1, 0), (0, D2), (m11, m21), (m12, m22)]
    g = 0
    for (a, b), (c, d) in combinations(cols, 2):
        g = gcd(g, abs(a * d - b * c))
    return g == 1


def automorphisms(D1, D2):
    vals = allowed_entries(D1, D2)
    autos = []
    for m11 in vals[0][0]:
        for m12 in vals[0][1]:
            for m21 in vals[1][0]:
                for m22 in vals[1][1]:
                    if is_auto_matrix(D1, D2, m11, m12, m21, m22):
                        autos.append((m11, m12, m21, m22))
    return autos


def act_on_c(D1, D2, c, mat):
    """Pull q_c back through the automorphism. Returns c' iff the pullback is
    again in family shape (diagonals exactly 1/(2*D_i)); else None.
    Soundness: match on generators + polarization determines the form.
    Completeness: any isometry q_c o f = q_{c'} necessarily passes these gates."""
    m11, m12, m21, m22 = mat
    M = denom(D1, D2)
    L = lcm(D1, D2)
    col1 = (m11 % D1, m21 % D2)
    col2 = (m12 % D1, m22 % D2)
    if q_int(col1, D1, D2, c, M) != (M // (2 * D1)) % M:
        return None
    if q_int(col2, D1, D2, c, M) != (M // (2 * D2)) % M:
        return None
    cross = b_int(col1, col2, D1, D2, c, M)
    unit = M // L
    if cross % unit != 0:
        return None
    cp = (cross // unit) % L
    return cp if cp in valid_cs(D1, D2) else None


def orbit_classes(D1, D2):
    cs = valid_cs(D1, D2)
    autos = automorphisms(D1, D2)
    parent = {c: c for c in cs}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for mat in autos:
        for c in cs:
            cp = act_on_c(D1, D2, c, mat)
            if cp is not None:
                union(c, cp)
    out = {}
    for c in cs:
        out.setdefault(find(c), []).append(c)
    return sorted(tuple(sorted(v)) for v in out.values())


# ---------------------------------------------------------------------------
# Arm 2: from-scratch brute-force isometry decider (independent of Arm 1)
# ---------------------------------------------------------------------------

def isometric_bruteforce(D1, D2, c, E1, E2, cp):
    """Decide isometry between (Z/D1 x Z/D2, q_c) and (Z/E1 x Z/E2, q_{cp})
    by exhaustive generator-image search with FULL form equality over all
    group elements. Exact integer arithmetic over a common denominator.

    Necessary filter: f(e1) must have order D1 and the same q-value as e1
    (isometries preserve order and q); likewise f(e2). Then well-definedness
    is automatic (orders divide), bijectivity is checked by image cardinality,
    and the form is compared pointwise on all D1*D2 elements."""
    M1 = denom(D1, D2)
    M2 = denom(E1, E2)
    COM = lcm(M1, M2)
    qA = {(a, b): q_int((a, b), D1, D2, c, M1) * (COM // M1)
          for a in range(D1) for b in range(D2)}
    qB = {(a, b): q_int((a, b), E1, E2, cp, M2) * (COM // M2)
          for a in range(E1) for b in range(E2)}

    def orderB(x):
        a, b = x
        return lcm(E1 // gcd(a, E1), E2 // gcd(b, E2))

    g1 = [x for x in qB if orderB(x) == D1 and qB[x] == qA[(1, 0)]]
    g2 = [x for x in qB if orderB(x) == D2 and qB[x] == qA[(0, 1)]]
    for f1 in g1:
        for f2 in g2:
            mp = {}
            for a in range(D1):
                for b in range(D2):
                    mp[(a, b)] = ((a * f1[0] + b * f2[0]) % E1,
                                  (a * f1[1] + b * f2[1]) % E2)
            if len(set(mp.values())) != D1 * D2:
                continue
            if all(qB[mp[x]] == qA[x] for x in mp):
                return True, (f1, f2)
    return False, None


def bruteforce_classes(D1, D2):
    """Partition valid c residues into isometry classes using ONLY Arm 2."""
    reps = {}
    for c in valid_cs(D1, D2):
        placed = False
        for rep in reps:
            iso, _ = isometric_bruteforce(D1, D2, c, D1, D2, rep)
            if iso:
                reps[rep].append(c)
                placed = True
                break
        if not placed:
            reps[c] = [c]
    return sorted(tuple(sorted(v)) for v in reps.values())


# ---------------------------------------------------------------------------
# Audit runs
# ---------------------------------------------------------------------------

# Check 1 pairs: keep runtime sane; (8,8) is the load-bearing wall witness.
# Extend AGREEMENT_PAIRS if you want broader coverage; cost grows fast with
# |Aut| x |group| for Arm 2.
AGREEMENT_PAIRS = [(4, 4), (4, 8), (6, 6), (8, 8), (4, 12), (6, 12), (8, 16), (12, 24)]

# Check 2: every same-abstract-group shape-alias pair with both shapes inside
# the v8e D range [2,4,6,8,10,12,14,16,18,20,24,32]. Derivation: shapes
# (D1,D2) and (E1,E2) alias iff invariant factors of the direct sums agree.
ALIAS_PAIRS = [
    ((4, 6), (2, 12)),   # both ~= Z/2 x Z/12
    ((6, 8), (2, 24)),   # both ~= Z/2 x Z/24
    ((4, 10), (2, 20)),  # both ~= Z/2 x Z/20
    ((8, 12), (4, 24)),  # both ~= Z/4 x Z/24
]


def main():
    fail = False

    rows = []
    for D1, D2 in AGREEMENT_PAIRS:
        arm1 = orbit_classes(D1, D2)
        arm2 = bruteforce_classes(D1, D2)
        agree = arm1 == arm2
        fail |= not agree
        rows.append({
            "D1": D1, "D2": D2,
            "arm1_orbit_classes": str(arm1),
            "arm2_bruteforce_classes": str(arm2),
            "agree": agree,
        })
        print(f"[check1] ({D1},{D2}) agree={agree}  classes={arm1}")
    with open(OUT / "audit_orbit_vs_bruteforce_agreement.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    xrows = []
    for (D1, D2), (E1, E2) in ALIAS_PAIRS:
        hits = 0
        witness = ""
        for c in valid_cs(D1, D2):
            for cp in valid_cs(E1, E2):
                iso, wit = isometric_bruteforce(D1, D2, c, E1, E2, cp)
                if iso:
                    hits += 1
                    witness = f"c={c},c'={cp},f={wit}"
        xrows.append({
            "shape_A": f"({D1},{D2})", "shape_B": f"({E1},{E2})",
            "same_group": True,
            "c_pairs_tested": len(valid_cs(D1, D2)) * len(valid_cs(E1, E2)),
            "cross_shape_isometries_found": hits,
            "witness_if_any": witness,
            "verdict": "RIGID" if hits == 0 else "CROSS_SHAPE_MERGE_REQUIRED",
        })
        print(f"[check2] {D1,D2} vs {E1,E2}: hits={hits}")
        # A hit is not an audit failure; it falsifies v8e's implicit assumption
        # and would demand a cross-shape merge step in the classifier.
    with open(OUT / "audit_cross_shape_alias_isometries.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(xrows[0]))
        w.writeheader()
        w.writerows(xrows)

    any_cross = any(r["cross_shape_isometries_found"] > 0 for r in xrows)
    print()
    print("CHECK 1 (orbit machinery vs independent brute force):",
          "FAIL" if fail else "PASS")
    print("CHECK 2 (cross-shape rigidity on in-range aliases):",
          "ASSUMPTION_FALSIFIED" if any_cross else
          "HOLDS_EMPIRICALLY (lemma still unproven)")
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()

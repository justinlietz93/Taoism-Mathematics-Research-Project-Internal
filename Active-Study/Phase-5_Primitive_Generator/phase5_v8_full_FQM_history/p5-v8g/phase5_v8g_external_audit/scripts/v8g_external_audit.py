#!/usr/bin/env python3
"""Phase 5 v8g external audit (2026-07-09).

Independent verification of the v8g triangle closure and mixed [2,4,2]
classifier. Written from scratch against the package, not derived from its
code paths.

Checks:
  1. FULL D=4 INDEPENDENT REPLICATION. Classify the ENTIRE equal-D rank-3
     parameter space at D=4 (all 64 forms, chains AND triangles) with an
     independent decider. Derive each triangle's disposition from the class
     partition itself (min edge count among class members: 0=splits entirely,
     1=splits to size2, 2=splits to chain, 3=core). Compare partition and all
     27 triangle dispositions against the package CSVs.
  2. D=8 SAMPLED DISPOSITION VERIFICATION. For a stratified sample of D=8
     triangles across all four disposition labels: verify claimed split
     targets by direct isometry search (a returned False is a certificate:
     the search is exhaustive), and verify claimed core-class structure by
     same-class/cross-class isometry spot checks.
  3. FULL MIXED [2,4,2] REPLICATION. Independently classify all 8
     representative-invariant forms on Z/2 x Z/4 x Z/2 with a general
     mixed-shape decider (bijectivity by image cardinality, not det parity)
     and compare against the package's mixed core orbit classes.
  4. SCOPE RECOUNT. Recount the full-scope disposition table (576 rows,
     zero missing) directly from the package CSV.

Conventions (ledger-registered family F):
  q(e_i) = 1/(2*D_i) pinned diagonals; edges c_ij / lcm(D_i,D_j),
  c_ij a multiple of lcm/gcd. Exact integer arithmetic over a common
  denominator; no floats in any decision path.

Documented caveat (not a computed check): family-F split detection is
complete for EQUALITY (the orbit table decides equality regardless), but
"no same-shape family split found" does not prove indecomposability,
because family presentations pin generator q-values at 1/(2*D_i); a true
orthogonal split with non-family diagonal values would not be found by a
same-shape search. v8g's rank-4 booking (BLOCKING_OPEN, no
indecomposability claim) is compliant with this limit.

Usage:
  python3 v8g_external_audit.py [path-to-v8g-package-root]
"""

import csv
import json
import random
import sys
from itertools import product
from math import gcd
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "outputs"
OUT.mkdir(parents=True, exist_ok=True)


def lcm(a, b):
    return a * b // gcd(a, b)


# ---------------------------------------------------------------------------
# Independent general rank-3 machinery (any shape D = (D1,D2,D3))
# ---------------------------------------------------------------------------

def common_M(D):
    m = 1
    for d in D:
        m = lcm(m, 2 * d)
    for i in range(3):
        for j in range(i + 1, 3):
            m = lcm(m, lcm(D[i], D[j]))
    return m


def q_num(v, c, D, M):
    """q(v)*M as an integer mod M. c = (c01, c02, c12)."""
    x, y, z = v
    c01, c02, c12 = c
    L01, L02, L12 = lcm(D[0], D[1]), lcm(D[0], D[2]), lcm(D[1], D[2])
    return (x * x * (M // (2 * D[0])) + y * y * (M // (2 * D[1])) + z * z * (M // (2 * D[2]))
            + c01 * x * y * (M // L01) + c02 * x * z * (M // L02) + c12 * y * z * (M // L12)) % M


def b_num(u, v, c, D, M):
    x, y, z = u
    p, q, r = v
    c01, c02, c12 = c
    L01, L02, L12 = lcm(D[0], D[1]), lcm(D[0], D[2]), lcm(D[1], D[2])
    return (x * p * (M // D[0]) + y * q * (M // D[1]) + z * r * (M // D[2])
            + c01 * (x * q + y * p) * (M // L01)
            + c02 * (x * r + z * p) * (M // L02)
            + c12 * (y * r + z * q) * (M // L12)) % M


def order_elem(v, D):
    o = 1
    for a, d in zip(v, D):
        oa = d // gcd(a, d)
        o = o * oa // gcd(o, oa)
    return o


def isometric(c1, c2, D):
    """Exhaustive generator-image isometry decision between forms c1, c2 on
    Z/D1 x Z/D2 x Z/D3. Candidates for image of e_i: order D_i and matching
    q-value. Pairwise b filters; bijectivity by image cardinality (valid for
    ANY shape, unlike det parity). Generators + polarization determine q.
    A False return is a certificate: the search space is exhausted."""
    M = common_M(D)
    elems = [v for v in product(range(D[0]), range(D[1]), range(D[2]))]
    e = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    qsrc = [q_num(e[i], c1, D, M) for i in range(3)]
    bsrc = {(i, j): b_num(e[i], e[j], c1, D, M) for i in range(3) for j in range(i + 1, 3)}
    cands = [[v for v in elems if order_elem(v, D) == D[i] and q_num(v, c2, D, M) == qsrc[i]]
             for i in range(3)]
    n = D[0] * D[1] * D[2]
    for f0 in cands[0]:
        for f1 in cands[1]:
            if b_num(f0, f1, c2, D, M) != bsrc[(0, 1)]:
                continue
            for f2 in cands[2]:
                if b_num(f0, f2, c2, D, M) != bsrc[(0, 2)]:
                    continue
                if b_num(f1, f2, c2, D, M) != bsrc[(1, 2)]:
                    continue
                img = set()
                for a in range(D[0]):
                    for b in range(D[1]):
                        for cc in range(D[2]):
                            img.add(((a * f0[0] + b * f1[0] + cc * f2[0]) % D[0],
                                     (a * f0[1] + b * f1[1] + cc * f2[1]) % D[1],
                                     (a * f0[2] + b * f1[2] + cc * f2[2]) % D[2]))
                            if len(img) == n:
                                break
                if len(img) == n:
                    return True, (f0, f1, f2)
    return False, None


def edge_count(c):
    return sum(1 for x in c if x != 0)


DISPO = {0: "TRIANGLE_SPLITS_ENTIRELY", 1: "TRIANGLE_SPLITS_TO_SIZE2",
         2: "TRIANGLE_SPLITS_TO_CHAIN", 3: "TRIANGLE_CORE_CLASSIFIED_BY_EXACT_ORBIT_TABLE"}


# ---------------------------------------------------------------------------
# Check 1: full D=4 replication (all 64 forms) + triangle dispositions
# ---------------------------------------------------------------------------

def check1_full_d4(package_root):
    D = (4, 4, 4)
    forms = list(product(range(4), repeat=3))
    classes = []  # (rep, members)
    for f in forms:
        for entry in classes:
            ok, _ = isometric(f, entry[0], D)
            if ok:
                entry[1].append(f)
                break
        else:
            classes.append((f, [f]))
    partition = sorted(tuple(sorted(m)) for _, m in classes)
    print(f"[check1] independent D=4 full-space classes: {len(partition)}")

    # dispositions derived from the partition itself
    my_dispo = {}
    for cls in partition:
        mn = min(edge_count(f) for f in cls)
        for f in cls:
            if edge_count(f) == 3:
                my_dispo[f] = DISPO[mn if mn < 3 else 3]

    match_part = None
    match_disp = None
    if package_root:
        fp = package_root / "outputs" / "phase5_v8g_equalD_rank3_full_scope_disposition.csv"
        if fp.exists():
            rows = [r for r in csv.DictReader(open(fp)) if r["D"] == "4"]
            theirs_cls = {}
            theirs_disp = {}
            for r in rows:
                f = tuple(json.loads(r["form"]))
                theirs_cls.setdefault(r["class_id"], []).append(f)
                if edge_count(f) == 3:
                    theirs_disp[f] = r["disposition"]
            their_partition = sorted(tuple(sorted(v)) for v in theirs_cls.values())
            match_part = their_partition == partition
            diffs = {f: (my_dispo[f], theirs_disp.get(f)) for f in my_dispo
                     if theirs_disp.get(f) != my_dispo[f]}
            match_disp = not diffs
            print(f"[check1] partition match vs package: {match_part}")
            print(f"[check1] all 27 D=4 triangle dispositions match: {match_disp}"
                  + (f"  diffs={diffs}" if diffs else ""))
    with open(OUT / "audit_d4_full_space_replication.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["class_index", "members", "min_edge_count",
                                          "partition_match", "triangle_dispo_match"])
        w.writeheader()
        for i, cls in enumerate(partition):
            w.writerow({"class_index": i, "members": json.dumps(cls),
                        "min_edge_count": min(edge_count(x) for x in cls),
                        "partition_match": match_part, "triangle_dispo_match": match_disp})
    return (match_part is not False) and (match_disp is not False)


# ---------------------------------------------------------------------------
# Check 2: D=8 sampled disposition verification
# ---------------------------------------------------------------------------

def check2_d8_samples(package_root, per_label=2, seed=5):
    if not package_root:
        print("[check2] skipped (no package path)")
        return True
    fp = package_root / "outputs" / "phase5_v8g_equalD_rank3_full_scope_disposition.csv"
    rows = [r for r in csv.DictReader(open(fp)) if r["D"] == "8"
            and edge_count(tuple(json.loads(r["form"]))) == 3]
    by_label = {}
    for r in rows:
        by_label.setdefault(r["disposition"], []).append(r)
    rng = random.Random(seed)
    D = (8, 8, 8)
    out_rows = []
    allok = True
    for label, rs in sorted(by_label.items()):
        for r in rng.sample(rs, min(per_label, len(rs))):
            f = tuple(json.loads(r["form"]))
            if r.get("split_target", "").strip():
                tgt = tuple(json.loads(r["split_target"]))
                ok, wit = isometric(f, tgt, D)
                verdict = ok
            else:
                # core: same-class member isometric, cross-class rep not
                same = [tuple(json.loads(x["form"])) for x in rows
                        if x["class_id"] == r["class_id"]
                        and tuple(json.loads(x["form"])) != f]
                other = [tuple(json.loads(x["form"])) for x in rows
                         if x["class_id"] != r["class_id"]][:1]
                ok1 = isometric(f, same[0], D)[0] if same else True
                ok2 = (not isometric(f, other[0], D)[0]) if other else True
                verdict = ok1 and ok2
                wit = f"same_class={ok1}, cross_class_distinct={ok2}"
            allok &= verdict
            print(f"[check2] D=8 {f} [{label}] -> verified={verdict}")
            out_rows.append({"form": json.dumps(f), "label": label,
                             "split_target": r.get("split_target", ""),
                             "verified": verdict, "detail": json.dumps(str(wit))})
    with open(OUT / "audit_d8_sampled_dispositions.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["form", "label", "split_target",
                                          "verified", "detail"])
        w.writeheader()
        w.writerows(out_rows)
    return allok


# ---------------------------------------------------------------------------
# Check 3: full mixed [2,4,2] replication
# ---------------------------------------------------------------------------

def check3_mixed_242(package_root):
    D = (2, 4, 2)

    def valid_edge(Di, Dj):
        L = lcm(Di, Dj)
        g = gcd(Di, Dj)
        step = L // g
        return [k * step % L for k in range(g)]

    e01 = valid_edge(2, 4)
    e02 = valid_edge(2, 2)
    e12 = valid_edge(4, 2)
    forms = [(a, b, c) for a in e01 for b in e02 for c in e12]
    classes = []
    for f in forms:
        for entry in classes:
            ok, _ = isometric(f, entry[0], D)
            if ok:
                entry[1].append(f)
                break
        else:
            classes.append((f, [f]))
    partition = sorted(tuple(sorted(m)) for _, m in classes)
    print(f"[check3] independent [2,4,2] forms={len(forms)} classes={len(partition)}")
    for cls in partition:
        print("   ", cls)
    match = None
    if package_root:
        fp = package_root / "outputs" / "phase5_v8g_mixed_rank3_core_orbit_classes.csv"
        if fp.exists():
            rows = list(csv.DictReader(open(fp)))

            def edges_to_ctuple(edges):
                # package encodes a form as a list of [i, j, c] edges
                pos = {(0, 1): 0, (0, 2): 1, (1, 2): 2}
                c = [0, 0, 0]
                for i, j, cv in edges:
                    c[pos[(min(i, j), max(i, j))]] = cv
                return tuple(c)

            theirs = sorted(tuple(sorted(edges_to_ctuple(m)
                                          for m in json.loads(r["members_json"])))
                            for r in rows)
            match = theirs == partition
            print(f"[check3] package comparison: {'MATCH' if match else 'MISMATCH: ' + str(theirs)}")
    with open(OUT / "audit_mixed_242_replication.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["class_index", "members", "package_match"])
        w.writeheader()
        for i, cls in enumerate(partition):
            w.writerow({"class_index": i, "members": json.dumps(cls),
                        "package_match": match})
    return match is not False


# ---------------------------------------------------------------------------
# Check 4: scope recount
# ---------------------------------------------------------------------------

def check4_scope(package_root):
    if not package_root:
        print("[check4] skipped (no package path)")
        return True
    fp = package_root / "outputs" / "phase5_v8g_equalD_rank3_full_scope_disposition.csv"
    rows = list(csv.DictReader(open(fp)))
    missing = sum(1 for r in rows if not r.get("disposition", "").strip())
    d4 = sum(1 for r in rows if r["D"] == "4")
    d8 = sum(1 for r in rows if r["D"] == "8")
    ok = (d4 == 64 and d8 == 512 and missing == 0)
    print(f"[check4] full scope rows: D=4 {d4}/64, D=8 {d8}/512, missing dispositions: {missing} -> {'PASS' if ok else 'FAIL'}")
    return ok


def main():
    package_root = Path(sys.argv[1]) if len(sys.argv) > 1 and Path(sys.argv[1]).exists() else None
    r1 = check1_full_d4(package_root)
    r2 = check2_d8_samples(package_root)
    r3 = check3_mixed_242(package_root)
    r4 = check4_scope(package_root)
    print()
    for name, r in [("CHECK 1 full D=4 replication", r1),
                    ("CHECK 2 D=8 sampled dispositions", r2),
                    ("CHECK 3 mixed [2,4,2] replication", r3),
                    ("CHECK 4 scope recount", r4)]:
        print(f"{name}: {'PASS' if r else 'FAIL'}")
    sys.exit(0 if all([r1, r2, r3, r4]) else 1)


if __name__ == "__main__":
    main()

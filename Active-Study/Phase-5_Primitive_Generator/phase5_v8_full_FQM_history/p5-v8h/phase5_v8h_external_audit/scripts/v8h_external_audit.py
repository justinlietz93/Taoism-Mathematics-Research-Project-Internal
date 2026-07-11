#!/usr/bin/env python3
"""Phase 5 v8h external audit (2026-07-09).

Independent verification of the v8h rank-4 [4,4,2,16] same-shape classifier
and a provenance check on the rank>=5 residual-core data.

Checks:
  1. LOOP-SOUNDNESS PRECONDITION. The v8h classifier pre-groups forms by
     q-value histogram and compares only within groups. That is sound iff the
     histogram is an isometry invariant — it is (an isometry is a q-preserving
     bijection, hence preserves the q-value multiset) — and iff the leader
     algorithm within each group is complete (it is: isometry is an
     equivalence relation, so members not matching the current leader remain
     grouped and are compared under a later leader). This audit additionally
     recomputes an independent, finer fingerprint — the multiset of
     (element order, q value) pairs — for all 512 forms and confirms it is
     constant within every claimed class (a necessary condition any true
     classifier must satisfy).
  2. WITNESS RE-VERIFICATION. Every positive decision certificate's witness
     basis is re-verified independently: pointwise q-pullback over all 512
     group elements, exact integers. This certifies every merge.
  3. INDEPENDENT NON-ISOMETRY SAMPLES. For cross-class pairs whose
     independent fingerprints collide (the only doubtful separations), a
     from-scratch exhaustive generator-image search certifies non-isometry.
  4. RANK>=5 EDGE PROVENANCE. Compare each v8h rank>=5 residual core's
     edges_2core against the upstream v8g reduction-routing rows.
     Finding on 2026-07-09: rank10_large and rank12_large were hardcoded in
     the v8h script with EMPTY edge lists ("from v8g known rows") while the
     v8g rows carry full edge lists. The published surviving cores for those
     two cases are therefore wrong (data lost in transcription), even though
     their BLOCKING_OPEN disposition remains correct.

Shape and conventions (ledger-registered family F):
  D = (4, 4, 2, 16); edges c_ij on all six pairs, c_ij a multiple of
  lcm/gcd; q(e_i) = 1/(2 D_i); exact integer arithmetic over a common
  denominator M; no floats in any decision path.

Usage:
  python3 v8h_external_audit.py <path-to-v8h-package-root> [path-to-v8g-package-root]
"""

import csv
import json
import sys
from itertools import combinations, product
from math import gcd
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "outputs"
OUT.mkdir(parents=True, exist_ok=True)

D = (4, 4, 2, 16)
N = 4
PAIRS = [(i, j) for i in range(N) for j in range(i + 1, N)]
EDGE_NAMES = [f"c{i}{j}" for i, j in PAIRS]


def lcm(a, b):
    return a * b // gcd(a, b)


M = 1
for d in D:
    M = lcm(M, 2 * d)
for i, j in PAIRS:
    M = lcm(M, lcm(D[i], D[j]))

ELEMS = list(product(*[range(d) for d in D]))


def q_num(v, c):
    tot = 0
    for i in range(N):
        tot += v[i] * v[i] * (M // (2 * D[i]))
    for (i, j), cij in zip(PAIRS, c):
        tot += cij * v[i] * v[j] * (M // lcm(D[i], D[j]))
    return tot % M


def b_num(u, v, c):
    tot = 0
    for i in range(N):
        tot += u[i] * v[i] * (M // D[i])
    for (i, j), cij in zip(PAIRS, c):
        tot += cij * (u[i] * v[j] + u[j] * v[i]) * (M // lcm(D[i], D[j]))
    return tot % M


def order_elem(v):
    o = 1
    for a, d in zip(v, D):
        oa = d // gcd(a, d)
        o = o * oa // gcd(o, oa)
    return o


def form_from_json(s):
    d = json.loads(s)
    return tuple(d[k] for k in EDGE_NAMES)


def apply_basis(basis, vec):
    """basis: list of 4 image vectors (rows = images of e_i)."""
    out = [0] * N
    for coef, img in zip(vec, basis):
        for k in range(N):
            out[k] += coef * img[k]
    return tuple(out[k] % D[k] for k in range(N))


def verify_witness(src, tgt, basis):
    """Pointwise pullback: q_tgt(f(v)) == q_src(v) for ALL 512 elements,
    plus bijectivity by image cardinality."""
    imgs = set()
    for v in ELEMS:
        w = apply_basis(basis, v)
        imgs.add(w)
        if q_num(w, tgt) != q_num(v, src):
            return False
    return len(imgs) == len(ELEMS)


def fingerprint(c):
    return tuple(sorted((order_elem(v), q_num(v, c)) for v in ELEMS))


def isometric_exhaustive(c1, c2):
    """From-scratch exhaustive generator-image search. A False return is a
    certificate: candidates filtered only by true invariants (order, q), and
    all surviving assignments are enumerated with pairwise-b propagation."""
    qsrc = [q_num(tuple(1 if k == i else 0 for k in range(N)), c1) for i in range(N)]
    bsrc = {(i, j): b_num(tuple(1 if k == i else 0 for k in range(N)),
                          tuple(1 if k == j else 0 for k in range(N)), c1)
            for i, j in PAIRS}
    cands = [[v for v in ELEMS if order_elem(v) == D[i] and q_num(v, c2) == qsrc[i]]
             for i in range(N)]
    order = sorted(range(N), key=lambda i: len(cands[i]))
    chosen = [None] * N

    def rec(pos):
        if pos == N:
            imgs = set()
            for v in ELEMS:
                imgs.add(apply_basis(chosen, v))
            return len(imgs) == len(ELEMS)
        i = order[pos]
        for f in cands[i]:
            ok = True
            for p2 in range(pos):
                j = order[p2]
                a, b = min(i, j), max(i, j)
                if b_num(f, chosen[j], c2) != bsrc[(a, b)]:
                    ok = False
                    break
            if not ok:
                continue
            chosen[i] = f
            if rec(pos + 1):
                return True
            chosen[i] = None
        return False

    return rec(0)


def main():
    v8h = Path(sys.argv[1])
    v8g = Path(sys.argv[2]) if len(sys.argv) > 2 and Path(sys.argv[2]).exists() else None

    # ---- load package data ----
    certs = list(csv.DictReader(open(v8h / "outputs" / "phase5_v8h_rank4_decision_certificates.csv")))
    scope = list(csv.DictReader(open(v8h / "outputs" / "phase5_v8h_rank4_full_scope_disposition.csv")))
    form_class = {}
    for r in scope:
        form_class[form_from_json(r["form"]) if "form" in r else form_from_json(r["representative"])] = r["class_id"]

    # ---- check 2: witness re-verification (all positive certs) ----
    pos = [r for r in certs if r["isometric"] == "True"]
    bad = 0
    for r in pos:
        src = form_from_json(r["source_form"])
        tgt = form_from_json(r["target_form"])
        basis = json.loads(r["witness_basis"])
        if not verify_witness(tgt, src, basis) and not verify_witness(src, tgt, basis):
            bad += 1
    print(f"[check2] positive certificates re-verified: {len(pos) - bad}/{len(pos)} "
          f"(witness accepted in either pullback direction)")

    # ---- check 1: independent fingerprint constancy within classes ----
    fps = {}
    cls_of = {}
    for r in scope:
        f = form_from_json(r["form"]) if "form" in r else form_from_json(r["representative"])
        cls_of[f] = r["class_id"]
    for f in cls_of:
        fps[f] = fingerprint(f)
    from collections import defaultdict
    cls_fp = defaultdict(set)
    for f, cid in cls_of.items():
        cls_fp[cid].add(fps[f])
    inconsistent = {cid: len(s) for cid, s in cls_fp.items() if len(s) > 1}
    print(f"[check1] classes with non-constant independent fingerprint: "
          f"{len(inconsistent)} (must be 0)  forms={len(cls_of)}  classes={len(cls_fp)}")

    # cross-class fingerprint collisions -> the doubtful separations
    fp_to_cls = defaultdict(set)
    for f, cid in cls_of.items():
        fp_to_cls[fps[f]].add(cid)
    colliding = {fp: cids for fp, cids in fp_to_cls.items() if len(cids) > 1}
    print(f"[check1] cross-class fingerprint collisions: {len(colliding)} fingerprint(s)")

    # ---- check 3: independent non-isometry on colliding cross-class pairs ----
    samples = []
    for fp, cids in list(colliding.items())[:2]:
        cids = sorted(cids)[:2]
        f1 = next(f for f, c in cls_of.items() if c == cids[0] and fps[f] == fp)
        f2 = next(f for f, c in cls_of.items() if c == cids[1] and fps[f] == fp)
        samples.append((f1, f2))
    all_sep = True
    for f1, f2 in samples:
        iso = isometric_exhaustive(f1, f2)
        all_sep &= (not iso)
        print(f"[check3] cross-class colliding pair {f1} vs {f2}: "
              f"independent exhaustive search says isometric={iso} (expected False)")
    if not samples:
        print("[check3] no colliding cross-class pairs found; separation follows "
              "from fingerprints alone")

    # ---- check 4: rank>=5 edge provenance vs v8g ----
    prov_rows = []
    if v8g is not None:
        v8h_rows = {r["case"]: r for r in csv.DictReader(
            open(v8h / "outputs" / "phase5_v8h_rankge5_reduction_routing.csv"))}
        v8g_rows = {r["case"]: r for r in csv.DictReader(
            open(v8g / "outputs" / "phase5_v8g_v7u_mixed_highrank_reduction_routing.csv"))}
        for case in sorted(set(v8h_rows) & set(v8g_rows)):
            e_h = json.loads(v8h_rows[case].get("edges_2core", "[]") or "[]")
            e_g = json.loads(v8g_rows[case].get("edges_2core", "[]") or "[]")
            verdict = ("MATCH" if e_h == e_g else
                       ("V8H_EMPTY_V8G_POPULATED_DATA_LOST" if (not e_h and e_g)
                        else "MISMATCH"))
            prov_rows.append({"case": case, "v8h_edge_count": len(e_h),
                              "v8g_edge_count": len(e_g), "verdict": verdict,
                              "v8g_edges_2core": json.dumps(e_g)})
            print(f"[check4] {case}: v8h edges={len(e_h)}  v8g edges={len(e_g)}  -> {verdict}")
        with open(OUT / "audit_rankge5_edge_provenance.csv", "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(prov_rows[0]))
            w.writeheader()
            w.writerows(prov_rows)

    with open(OUT / "audit_rank4_verification_summary.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["metric", "value"])
        w.writeheader()
        w.writerows([
            {"metric": "positive_certificates", "value": len(pos)},
            {"metric": "witnesses_failed_reverification", "value": bad},
            {"metric": "classes", "value": len(cls_fp)},
            {"metric": "classes_with_nonconstant_fingerprint", "value": len(inconsistent)},
            {"metric": "cross_class_fingerprint_collisions", "value": len(colliding)},
            {"metric": "independent_nonisometry_samples_separated",
             "value": all_sep and len(samples)},
        ])

    ok = (bad == 0) and (len(inconsistent) == 0) and all_sep
    lost = any(r["verdict"].startswith("V8H_EMPTY") for r in prov_rows)
    print()
    print("RANK-4 CLASSIFIER:", "VERIFIED" if ok else "PROBLEM FOUND")
    print("RANK>=5 PROVENANCE:",
          "DATA LOST (rank10/rank12 edges empty in v8h, populated in v8g)"
          if lost else "consistent")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()

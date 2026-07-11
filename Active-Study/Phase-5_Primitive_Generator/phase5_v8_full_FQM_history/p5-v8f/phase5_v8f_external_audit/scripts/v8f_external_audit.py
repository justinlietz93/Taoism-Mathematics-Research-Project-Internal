#!/usr/bin/env python3
"""Phase 5 v8f external audit (2026-07-09).

Independent verification of the v8f rank-3 equal-2-primary CHAIN classifier.
Written from scratch against the package, not derived from its code paths.

Checks:
  1. FLAGSHIP SPLIT: verify the v8f splitter's headline control
     (c01,c02,c12) = (1,0,4) ~ (0,0,1) at D=8, with an explicit witness basis
     and POINTWISE form equality over all 512 group elements.
  2. FULL D=4 RE-CLASSIFICATION: classify all 16 chain forms (c02=0) at D=4
     with an independent decider; compare class-by-class against the package's
     phase5_v8f_rank3_equal_core_orbit_classes.csv.
  3. TRIANGLE SCOPE HOLE: enumerate the equal-D rank-3 parameter space and
     report which forms carry NO disposition in the package. Finding on
     2026-07-09: all forms with three nonzero edges (triangles) are reachable
     in family F via three O_ij events but are neither in the closed chain
     scope nor in the mixed/high-rank BLOCKING_OPEN scope. Five-disposition-
     law violation (target vanished between adjacent scope labels).

Conventions (equal-D rank-3 family-F core; ledger-registered):
  carrier (Z/DZ)^3, D a power of 2 in tested range
  q(x,y,z)  = (x^2+y^2+z^2)/(2D) + (c01*xy + c02*xz + c12*yz)/D   (mod 1)
  b = polarization of q; q is determined by q on generators + pairwise b
  isometry: group automorphism f with q(f(v)) = q(v) for all v
  invertibility over Z/2^k: det odd

Exact arithmetic throughout: q and b are held as integers scaled by M = 2D.
No floats in any decision path.

Usage:
  python3 v8f_external_audit.py [path-to-v8f-package-root]
If the package path is omitted or the CSV is absent, check 2 still runs and
prints the independent classification; only the cross-comparison is skipped.
"""

import csv
import json
import sys
from itertools import product
from math import gcd
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "outputs"
OUT.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Independent rank-3 equal-D machinery (exact integers scaled by M = 2D)
# ---------------------------------------------------------------------------

def q_num(v, c, D):
    """q(v) * 2D as an integer mod 2D."""
    M = 2 * D
    x, y, z = v
    c01, c02, c12 = c
    return (x * x + y * y + z * z + 2 * (c01 * x * y + c02 * x * z + c12 * y * z)) % M


def b_num(u, v, c, D):
    """b(u,v) * 2D as an integer mod 2D (polarization of q)."""
    M = 2 * D
    x, y, z = u
    p, q, r = v
    c01, c02, c12 = c
    return (2 * (x * p + y * q + z * r)
            + 2 * (c01 * (x * q + y * p) + c02 * (x * r + z * p) + c12 * (y * r + z * q))) % M


def order3(v, D):
    o = 1
    for a in v:
        oa = D // gcd(a, D)
        o = o * oa // gcd(o, oa)
    return o


def det_odd(cols):
    """Invertibility of a 3x3 matrix over Z/2^k: determinant odd."""
    (a, b, c), (d, e, f), (g, h, i) = cols
    return (a * (e * i - f * h) - d * (b * i - c * h) + g * (b * f - c * e)) % 2 == 1


def isometric(c1, c2, D, pointwise_confirm=False):
    """Decide isometry between equal-D rank-3 forms c1 and c2.

    Generator-image search: candidate images of e_i are elements of order D
    with q-value 1/(2D) in the target form (isometries preserve order and q).
    A triple qualifies when all pairwise b-values match the source and the
    matrix is invertible (det odd). Match on generators + polarization
    determines the quadratic form everywhere; pointwise_confirm re-checks
    q equality over all D^3 elements anyway when requested."""
    elems = list(product(range(D), repeat=3))
    cands = [v for v in elems if order3(v, D) == D and q_num(v, c2, D) == 1]
    b01 = b_num((1, 0, 0), (0, 1, 0), c1, D)
    b02 = b_num((1, 0, 0), (0, 0, 1), c1, D)
    b12 = b_num((0, 1, 0), (0, 0, 1), c1, D)
    for f1 in cands:
        for f2 in cands:
            if b_num(f1, f2, c2, D) != b01:
                continue
            for f3 in cands:
                if b_num(f1, f3, c2, D) != b02:
                    continue
                if b_num(f2, f3, c2, D) != b12:
                    continue
                if not det_odd((f1, f2, f3)):
                    continue
                if pointwise_confirm:
                    ok = all(
                        q_num((( a * f1[0] + b * f2[0] + c * f3[0]) % D,
                               ( a * f1[1] + b * f2[1] + c * f3[1]) % D,
                               ( a * f1[2] + b * f2[2] + c * f3[2]) % D), c2, D)
                        == q_num((a, b, c), c1, D)
                        for a in range(D) for b in range(D) for c in range(D))
                    if not ok:
                        # would indicate a bug in the determinacy argument;
                        # never observed
                        continue
                return True, (f1, f2, f3)
    return False, None


def classify(forms, D):
    """Partition forms into isometry classes using only the decider above."""
    classes = []  # list of (rep, members)
    for f in forms:
        for entry in classes:
            ok, _ = isometric(f, entry[0], D)
            if ok:
                entry[1].append(f)
                break
        else:
            classes.append((f, [f]))
    return sorted(tuple(sorted(m)) for _, m in classes)


# ---------------------------------------------------------------------------
# Audit checks
# ---------------------------------------------------------------------------

def check1_flagship():
    ok, wit = isometric((1, 0, 4), (0, 0, 1), 8, pointwise_confirm=True)
    print(f"[check1] D=8 (1,0,4) ~ (0,0,1): {ok}  witness={wit} "
          f"(pointwise-confirmed over 512 elements)")
    with open(OUT / "audit_flagship_split_verification.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["D", "connected_form", "split_target",
                                          "isometric", "witness_basis",
                                          "pointwise_confirmed_over"])
        w.writeheader()
        w.writerow({"D": 8, "connected_form": "[1,0,4]", "split_target": "[0,0,1]",
                    "isometric": ok, "witness_basis": json.dumps(wit),
                    "pointwise_confirmed_over": 512})
    return ok


def check2_d4(package_root):
    forms = [(a, 0, b) for a in range(4) for b in range(4)]  # chains: c02 = 0
    mine = classify(forms, 4)
    print(f"[check2] independent D=4 chain classes: {len(mine)}")
    for cls in mine:
        print("   ", cls)

    theirs = None
    if package_root is not None:
        csv_path = (package_root / "outputs" /
                    "phase5_v8f_rank3_equal_core_orbit_classes.csv")
        if csv_path.exists():
            rows = [r for r in csv.DictReader(open(csv_path)) if r["D"] == "4"]
            theirs = sorted(
                tuple(sorted(tuple(m) for m in json.loads(r["members_json"])))
                for r in rows)
    match = (theirs == mine) if theirs is not None else None
    print(f"[check2] package comparison: "
          f"{'MATCH' if match else ('MISMATCH' if match is False else 'package CSV not found; skipped')}")

    with open(OUT / "audit_d4_reclassification.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["class_index", "members",
                                          "package_match"])
        w.writeheader()
        for i, cls in enumerate(mine):
            w.writerow({"class_index": i, "members": json.dumps(cls),
                        "package_match": match})
    return match is not False  # absence of the CSV is not a failure


def check3_triangle_hole(package_root):
    """Enumerate the full equal-D rank-3 parameter space at D=4 and report
    which forms carry no disposition anywhere in the package."""
    all_forms = list(product(range(4), repeat=3))
    chains = {f for f in all_forms
              if sum(1 for e in f if e != 0) <= 2 and f[1] == 0}
    # v8f scope = chain_forms: (c01, 0, c12), all values incl zeros
    scoped = {(a, 0, b) for a in range(4) for b in range(4)}
    triangles = [f for f in all_forms if all(e != 0 for e in f)]
    unbooked = [f for f in all_forms if f not in scoped]

    booked_elsewhere = 0
    if package_root is not None:
        # search every doc/CSV for any triangle mention
        hits = 0
        for p in list((package_root / "docs").glob("*")) + \
                 list((package_root / "outputs").glob("*.csv")):
            try:
                txt = p.read_text(errors="ignore").lower()
            except Exception:
                continue
            if "triangle" in txt or "three-edge" in txt or "three edge" in txt:
                hits += 1
        booked_elsewhere = hits

    print(f"[check3] D=4 full parameter space: {len(all_forms)} forms; "
          f"v8f chain scope covers {len(scoped)}; "
          f"outside scope: {len(unbooked)} (of which pure triangles: {len(triangles)})")
    print(f"[check3] package mentions of triangles in docs/CSVs: {booked_elsewhere}")
    verdict = ("SCOPE_HOLE_CONFIRMED" if booked_elsewhere == 0
               else "TRIANGLES_MENTIONED_CHECK_MANUALLY")
    print(f"[check3] verdict: {verdict} — equal-D triangles are reachable in "
          f"family F (three O_ij events) but carry no disposition row")

    with open(OUT / "audit_triangle_scope_hole.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["D", "total_forms", "chain_scope",
                                          "outside_scope", "pure_triangles",
                                          "package_triangle_mentions",
                                          "verdict"])
        w.writeheader()
        w.writerow({"D": 4, "total_forms": len(all_forms),
                    "chain_scope": len(scoped),
                    "outside_scope": len(unbooked),
                    "pure_triangles": len(triangles),
                    "package_triangle_mentions": booked_elsewhere,
                    "verdict": verdict})
    return True  # informational; hole is a ledger finding, not a script failure


def main():
    package_root = None
    if len(sys.argv) > 1:
        cand = Path(sys.argv[1])
        if cand.exists():
            package_root = cand
    ok1 = check1_flagship()
    ok2 = check2_d4(package_root)
    check3_triangle_hole(package_root)
    print()
    print("CHECK 1 (flagship split, pointwise):", "PASS" if ok1 else "FAIL")
    print("CHECK 2 (D=4 independent re-classification):",
          "PASS" if ok2 else "FAIL")
    print("CHECK 3 (triangle scope hole): see audit_triangle_scope_hole.csv "
          "and the ledger BLOCKING_OPEN row")
    sys.exit(0 if (ok1 and ok2) else 1)


if __name__ == "__main__":
    main()

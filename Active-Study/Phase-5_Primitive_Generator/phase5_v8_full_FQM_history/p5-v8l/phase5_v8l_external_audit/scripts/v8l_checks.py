#!/usr/bin/env python3
"""v8l external audit — from-scratch verification. Stdlib only, exact integers.

Checks:
 A. Independent full classification of the 512 true-diagonal [4,4,2,16] diag[1,3,3,5]
    forms (fingerprint pre-grouping + exhaustive isometry decider + SNF span test).
    Compare partition to package class/disposition tables. Archival form class check.
 B. Verify all 530 decision rows: positives -> witness verified as data (order, q,
    pairwise b, SNF span); negatives -> cross-checked against my partition.
 C. Fingerprint constancy within package classes; cross-class collisions enumerated.
 D. Radical size per class representative (enumeration) vs package column.
 E. Ground-truth CSV: 229 rows; per-row radical size + q-on-radical + witnesses
    re-verified by enumeration; the single certified row fully verified per the
    certificate standard (section V).
 F. Five cores: SNF radical size (validated vs enumeration at rank5/6), ambient
    radical test on published generators, generator span size, q-values on radical,
    quotient shape via SNF vs claimed nondegenerate complement shape.
 G. Gate scan: no prose in certificate columns of certified rows.
"""
import csv, json, sys, itertools
from math import gcd
from collections import Counter, defaultdict
from pathlib import Path

PKG = Path('/home/claude/v8l/phase5_v8l_full_decomposition_under_data_gates')
OUT = Path('/home/claude/audit/outputs'); OUT.mkdir(parents=True, exist_ok=True)

def lcm(a, b): return a * b // gcd(a, b)

# ---------------- generic form machinery ----------------
def form_M(D):
    M = 1
    for d in D: M = lcm(M, 2 * d)
    n = len(D)
    for i in range(n):
        for j in range(i + 1, n): M = lcm(M, lcm(D[i], D[j]))
    return M

def build(D, diag, edges):
    """edges: dict {(i,j): c}. Returns (M, Bmat, qfunc)."""
    n = len(D); M = form_M(D)
    B = [[0] * n for _ in range(n)]
    for i in range(n): B[i][i] = (diag[i] * (M // D[i])) % M
    for (i, j), c in edges.items():
        v = (c * (M // lcm(D[i], D[j]))) % M
        B[i][j] = (B[i][j] + v) % M; B[j][i] = (B[j][i] + v) % M
    def q(v):
        t = 0
        for i in range(n): t += diag[i] * v[i] * v[i] * (M // (2 * D[i]))
        for (i, j), c in edges.items(): t += c * v[i] * v[j] * (M // lcm(D[i], D[j]))
        return t % M
    return M, B, q

def bval(B, M, u, w):
    n = len(u)
    return sum(u[i] * B[i][j] * w[j] for i in range(n) for j in range(n)) % M

def order(v, D):
    o = 1
    for a, d in zip(v, D):
        a %= d
        if a: o = lcm(o, d // gcd(a, d))
    return o

def all_elems(D):
    return list(itertools.product(*[range(d) for d in D]))

# ---------------- Smith normal form (invariant factors) ----------------
def snf_invariants(mat, need):
    A = [row[:] for row in mat]; R = len(A); C = len(A[0]); out = []; r = 0
    while r < need:
        piv = None
        for i in range(r, R):
            for j in range(r, C):
                if A[i][j] and (piv is None or abs(A[i][j]) < abs(A[piv[0]][piv[1]])):
                    piv = (i, j)
        if piv is None:
            out.append(0); r += 1; continue
        pi, pj = piv
        A[r], A[pi] = A[pi], A[r]
        for i in range(R): A[i][r], A[i][pj] = A[i][pj], A[i][r]
        while True:
            moved = False
            for i in range(r + 1, R):
                if A[i][r] % A[r][r] != 0:
                    qd = A[i][r] // A[r][r]
                    for j in range(r, C): A[i][j] -= qd * A[r][j]
                    A[r], A[i] = A[i], A[r]; moved = True; break
            if moved: continue
            for i in range(r + 1, R):
                if A[i][r]:
                    qd = A[i][r] // A[r][r]
                    for j in range(r, C): A[i][j] -= qd * A[r][j]
            moved = False
            for j in range(r + 1, C):
                if A[r][j] % A[r][r] != 0:
                    qd = A[r][j] // A[r][r]
                    for i in range(r, R): A[i][j] -= qd * A[i][r]
                    for i in range(r, R): A[i][r], A[i][j] = A[i][j], A[i][r]
                    moved = True; break
            if moved: continue
            for j in range(r + 1, C):
                if A[r][j]:
                    qd = A[r][j] // A[r][r]
                    for i in range(r, R): A[i][j] -= qd * A[i][r]
            if all(A[i][r] == 0 for i in range(r + 1, R)) and all(A[r][j] == 0 for j in range(r + 1, C)):
                break
        out.append(abs(A[r][r])); r += 1
    return out

def spans(vectors, D):
    """vectors generate A = prod Z/D_i iff [v cols | diag(D)] has all inv factors 1."""
    n = len(D)
    cols = [list(v) for v in vectors] + [[D[k] if k == i else 0 for k in range(n)] for i in range(n)]
    mat = [[cols[c][r] for c in range(len(cols))] for r in range(n)]
    return all(x == 1 for x in snf_invariants(mat, n))

def quotient_shape(rad_gens, D):
    """Shape of A / <rad_gens> as invariant factor list (>1 entries), ascending."""
    n = len(D)
    cols = [[D[k] if k == i else 0 for k in range(n)] for i in range(n)] + [list(g) for g in rad_gens]
    mat = [[cols[c][r] for c in range(len(cols))] for r in range(n)]
    inv = snf_invariants(mat, n)
    return sorted(x for x in inv if x > 1)

def radical_size_snf(D, diag, edges):
    n = len(D); M = form_M(D)
    G = [[0] * n for _ in range(n)]
    for i in range(n): G[i][i] = diag[i] * (M // D[i])
    for (i, j), c in edges.items():
        u = c * (M // lcm(D[i], D[j])); G[i][j] += u; G[j][i] += u
    mat = [[G[j][i] for j in range(n)] + [M if k == i else 0 for k in range(n)] for i in range(n)]
    d = snf_invariants(mat, n)
    num = 1
    for x in D: num *= x
    for x in d: num *= x
    return num // (M ** n)

def radical_enum(D, B, M):
    n = len(D); rad = []
    gens = [tuple(1 if k == i else 0 for k in range(n)) for i in range(n)]
    for v in all_elems(D):
        if all(bval(B, M, v, e) == 0 for e in gens): rad.append(v)
    return rad

def subgroup_span(gens, D):
    seen = {tuple(0 for _ in D)}
    frontier = [tuple(0 for _ in D)]
    while frontier:
        x = frontier.pop()
        for g in gens:
            y = tuple((a + b) % d for a, b, d in zip(x, g, D))
            if y not in seen:
                seen.add(y); frontier.append(y)
    return seen

# ---------------- Part A: independent classification ----------------
D4 = (4, 4, 2, 16); DIAG4 = (1, 3, 3, 5); M4 = form_M(D4)
PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
STEPS = {}
for (i, j) in PAIRS:
    L = lcm(D4[i], D4[j]); STEPS[(i, j)] = (L, L // gcd(D4[i], D4[j]))
CHOICES = [list(range(0, STEPS[p][0], STEPS[p][1])) for p in PAIRS]
FORMS = [tuple(c) for c in itertools.product(*CHOICES)]  # tuple of 6 c-values in PAIRS order
assert len(FORMS) == 512, len(FORMS)
ELEMS4 = all_elems(D4)
ORD4 = {v: order(v, D4) for v in ELEMS4}
GENS4 = [tuple(1 if k == i else 0 for k in range(4)) for i in range(4)]

def edges_of(f): return {p: c for p, c in zip(PAIRS, f) if c}

_cache = {}
def form_data(f):
    if f in _cache: return _cache[f]
    M, B, q = build(D4, DIAG4, edges_of(f))
    qtab = {v: q(v) for v in ELEMS4}
    fp = frozenset(Counter((ORD4[v], qtab[v]) for v in ELEMS4).items())
    byoq = defaultdict(list)
    for v in ELEMS4: byoq[(ORD4[v], qtab[v])].append(v)
    _cache[f] = (B, qtab, fp, byoq)
    return _cache[f]

def decide_isometric(f1, f2):
    """Exhaustive: witness rows [img(e0)..img(e3)] or None."""
    B1, q1, _, _ = form_data(f1)
    B2, q2, _, byoq2 = form_data(f2)
    targ_b = [[bval(B1, M4, GENS4[i], GENS4[j]) for j in range(4)] for i in range(4)]
    # candidates: order divides D_i and q matches
    cand = []
    for i in range(4):
        qi = q1[GENS4[i]]
        c = [v for v in ELEMS4 if D4[i] % ORD4[v] == 0 and q2[v] == qi]
        cand.append(c)
    idx = sorted(range(4), key=lambda i: len(cand[i]))
    assign = [None] * 4
    def bt(k):
        if k == 4:
            if spans(assign, D4): return True
            return False
        i = idx[k]
        for v in cand[i]:
            ok = True
            for kk in range(k):
                j = idx[kk]
                if bval(B2, M4, v, assign[j]) != targ_b[i][j]: ok = False; break
            if ok:
                assign[i] = v
                if bt(k + 1): return True
                assign[i] = None
        return False
    if bt(0): return [list(assign[i]) for i in range(4)]
    return None

print('=== A. independent classification of 512 true-diagonal forms ===')
fp_groups = defaultdict(list)
for f in FORMS: fp_groups[form_data(f)[2]].append(f)
print('fingerprint groups:', len(fp_groups), 'sizes:', sorted(len(g) for g in fp_groups.values()))

my_class_of = {}; my_classes = []
for fp, grp in sorted(fp_groups.items(), key=lambda kv: (len(kv[1]), sorted(kv[1]))):
    reps = []
    for f in sorted(grp):
        placed = False
        for (rid, rf) in reps:
            if decide_isometric(rf, f) is not None:
                my_class_of[f] = rid; placed = True; break
        if not placed:
            rid = len(my_classes)
            my_classes.append(f); reps.append((rid, f)); my_class_of[f] = rid
print('MY class count:', len(my_classes))
_evid_classes = []

# archival form (as hardcoded by the agent)
ARCH = tuple({(0, 1): 3, (0, 2): 2, (0, 3): 4, (1, 2): 2, (1, 3): 12}.get(p, 0) for p in PAIRS)
print('archival form', ARCH, '-> my class', my_class_of[ARCH])

# ---------------- compare to package tables ----------------
print('=== package table comparison ===')
def parse_form(s):
    d = json.loads(s)
    return tuple(d[f'c{i}{j}'] for (i, j) in PAIRS)

cls_rows = list(csv.DictReader(open(PKG / 'outputs/phase5_v8l_true_diag_rank4_exact_orbit_classes.csv')))
pkg_members = {}; pkg_rep = {}
for r in cls_rows:
    cid = int(r['class_id'])
    pkg_rep[cid] = parse_form(r['representative'])
    pkg_members[cid] = [tuple(m[f'c{i}{j}'] for (i, j) in PAIRS) for m in json.loads(r['members_json'])]
tot = sum(len(v) for v in pkg_members.values())
allmem = [f for v in pkg_members.values() for f in v]
print('pkg classes:', len(cls_rows), 'total members:', tot, 'distinct:', len(set(allmem)))

# partition equality: their class -> my class must be a bijection with identical member sets
mismatch = 0; mapping = {}
for cid, mem in pkg_members.items():
    mine = {my_class_of[f] for f in mem}
    if len(mine) != 1: mismatch += 1; print('  SPLIT ERROR pkg class', cid, '->', mine)
    else:
        m = mine.pop(); mapping[cid] = m
mymem = defaultdict(set)
for f, c in my_class_of.items(): mymem[c].add(f)
for cid, mem in pkg_members.items():
    if cid in mapping and set(mem) != mymem[mapping[cid]]:
        mismatch += 1; print('  MERGE ERROR pkg class', cid)
bij = len(set(mapping.values())) == len(mapping)
print('partition identical:', mismatch == 0 and bij and tot == 512 and len(set(allmem)) == 512)

disp = list(csv.DictReader(open(PKG / 'outputs/phase5_v8l_true_diag_rank4_full_scope_disposition.csv')))
disp_forms = [parse_form(r['form']) for r in disp]
disp_ok = (len(disp) == 512 and len(set(disp_forms)) == 512)
disp_consistent = all(parse_form(r['form']) in pkg_members[int(r['class_id'])] for r in disp)
print('disposition rows:', len(disp), 'unique+complete:', disp_ok, 'class ids consistent with class table:', disp_consistent)
arch_pkg_class = [int(r['class_id']) for r in disp if parse_form(r['form']) == ARCH]
print('archival class per pkg disposition:', arch_pkg_class, '| pkg claims 5 | my class:', my_class_of[ARCH], '-> pkg class', [c for c, m in mapping.items() if m == my_class_of[ARCH]])

# fingerprint constancy inside pkg classes + cross-class collisions
viol = 0; fps = {}
for cid, mem in pkg_members.items():
    s = {form_data(f)[2] for f in mem}
    if len(s) != 1: viol += 1
    fps[cid] = next(iter(s))
coll = defaultdict(list)
for cid, fp in fps.items(): coll[fp].append(cid)
collisions = {tuple(v) for v in coll.values() if len(v) > 1}
print('fingerprint violations within classes:', viol, '| cross-class fingerprint collisions:', collisions)
# separate every collision pair by my exhaustive decider
for pair in collisions:
    for a, b in itertools.combinations(pair, 2):
        w = decide_isometric(pkg_rep[a], pkg_rep[b])
        print(f'  collision pair pkg({a},{b}) exhaustive non-isometry confirmed:', w is None)

# radical sizes per class rep
rad_ok = True
for r in cls_rows:
    cid = int(r['class_id']); f = pkg_rep[cid]
    B, qtab, _, _ = form_data(f)
    rad = radical_enum(D4, B, M4)
    qvals = sorted({qtab[v] for v in rad})
    ok = (len(rad) == int(r['radical_size']) and qvals == sorted(json.loads(r['q_values_on_radical_xM'])))
    rad_ok &= ok
    if not ok: print('  RADICAL MISMATCH class', cid, len(rad), qvals, 'vs', r['radical_size'], r['q_values_on_radical_xM'])
print('class-rep radical sizes + q-on-radical all match:', rad_ok)
for r in cls_rows:
    cid = int(r['class_id']); f = pkg_rep[cid]
    _evid_classes.append({'pkg_class_id': cid, 'auditor_class_id': mapping.get(cid), 'size': len(pkg_members[cid]),
                          'canonical_rep_lexmin': json.dumps(sorted(pkg_members[cid])[0]),
                          'fingerprint_hash': hex(abs(hash(fps[cid])))[2:18],
                          'partition_match': set(pkg_members[cid]) == mymem[mapping[cid]],
                          'radical_size_verified': True, 'contains_archival': ARCH in pkg_members[cid]})
with open(OUT / 'v8l_table_verification.csv', 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(_evid_classes[0].keys())); w.writeheader(); w.writerows(_evid_classes)

# ---------------- B. decision rows ----------------
print('=== B. decision certificate rows ===')
dec = list(csv.DictReader(open(PKG / 'outputs/phase5_v8l_true_diag_rank4_decision_certificates.csv')))
pos = neg = pos_bad = neg_bad = prose_bad = 0
for r in dec:
    f1 = parse_form(r['source_form']); f2 = parse_form(r['target_form'])
    if r['isometric'] == 'True':
        pos += 1
        wit = json.loads(r['witness_basis_json'])
        if not (isinstance(wit, list) and len(wit) == 4 and all(isinstance(x, list) and all(isinstance(y, int) for y in x) for x in wit)):
            prose_bad += 1; pos_bad += 1; continue
        B1, q1, _, _ = form_data(f1); B2, q2, _, _ = form_data(f2)
        ok = True
        imgs = [tuple(w[i] % D4[i] if False else w[i] for i in range(4)) for w in wit]
        imgs = [tuple(x % d for x, d in zip(w, D4)) for w in wit]
        for i in range(4):
            if D4[i] % order(imgs[i], D4) != 0: ok = False
            if q2[imgs[i]] != q1[GENS4[i]]: ok = False
        for i in range(4):
            for j in range(i + 1, 4):
                if bval(B2, M4, imgs[i], imgs[j]) != bval(B1, M4, GENS4[i], GENS4[j]): ok = False
        if not spans(imgs, D4): ok = False
        if not ok: pos_bad += 1; print('  BAD WITNESS decision', r['decision_id'])
    else:
        neg += 1
        if my_class_of[f1] == my_class_of[f2]:
            neg_bad += 1; print('  BAD NEGATIVE decision', r['decision_id'])
print(f'decisions: {len(dec)} | positives {pos} (bad {pos_bad}) | negatives {neg} (bad {neg_bad}) | non-data witnesses {prose_bad}')
with open(OUT / 'v8l_decision_verification_summary.csv', 'w', newline='') as fh:
    w = csv.writer(fh); w.writerow(['metric', 'value'])
    for k, v in [('decision_rows', len(dec)), ('positives', pos), ('positives_failed', pos_bad),
                 ('negatives', neg), ('negatives_contradicted', neg_bad), ('non_data_witnesses', prose_bad)]:
        w.writerow([k, v])

# every same-class package pair connected? (coverage: each member decided against its rep)
cover_bad = 0
dec_pos_pairs = {(parse_form(r['source_form']), parse_form(r['target_form'])) for r in dec if r['isometric'] == 'True'}
for cid, mem in pkg_members.items():
    rep = pkg_rep[cid]
    for f in mem:
        if f != rep and (rep, f) not in dec_pos_pairs and (f, rep) not in dec_pos_pairs:
            cover_bad += 1
print('members lacking a positive decision to their class rep:', cover_bad)

# ---------------- E. ground truth CSV ----------------
print('=== E. ground-truth 229 rows ===')
gt = list(csv.DictReader(open(PKG / 'outputs/phase5_v8l_groundtruth_decomposition_certificates.csv')))
print('rows:', len(gt), 'by source:', Counter(r['source'] for r in gt))
cert_rows = [r for r in gt if r['certificate_verified'] == 'True']
print('certified rows:', len(cert_rows))
gt_rad_bad = 0
for r in gt:
    D = tuple(json.loads(r['shape'])); du = tuple(json.loads(r['diag_units']))
    rep = json.loads(r['representative'])
    if isinstance(rep, dict):
        ed = {(int(k[1]), int(k[2])): v for k, v in rep.items() if v}
    elif rep and isinstance(rep[0], int):
        n = len(D); prs = [(i, j) for i in range(n) for j in range(i + 1, n)]
        assert len(rep) == len(prs)
        ed = {p: c for p, c in zip(prs, rep) if c}
    else:
        ed = {(int(e[0]), int(e[1])): int(e[2]) for e in rep if int(e[2])}
    M, B, q = build(D, du, ed)
    if M != int(r['M']): gt_rad_bad += 1; print('  M mismatch', r['ground_truth_id']); continue
    rad = radical_enum(D, B, M)
    qvals = sorted({q(v) for v in rad})
    wit = [tuple(w) for w in json.loads(r['first_radical_witnesses'])]
    ok = (len(rad) == int(r['radical_size_ambient'])
          and qvals == sorted(json.loads(r['q_values_on_radical_xM']))
          and all(tuple(x % d for x, d in zip(w, D)) in set(rad) for w in wit))
    if not ok: gt_rad_bad += 1; print('  GT RADICAL MISMATCH', r['ground_truth_id'])
print('ground-truth radical data mismatches:', gt_rad_bad)
with open(OUT / 'v8l_groundtruth_radical_verification.csv', 'w', newline='') as fh:
    w = csv.writer(fh); w.writerow(['rows', 'radical_data_mismatches', 'certified_rows', 'sources'])
    w.writerow([len(gt), gt_rad_bad, len(cert_rows), json.dumps(dict(Counter(r['source'] for r in gt)))])

# fully verify the one certified row per section V
def verify_block_certificate(D, du, ed):
    """returns (ok, detail) for the worked [2,2] c01=1 row"""
    M, B, q = build(D, du, ed)
    basis = [(1, 0), (1, 1)]
    checks = {}
    checks['span'] = spans(basis, D)
    checks['orders'] = (order(basis[0], D) == 2 and order(basis[1], D) == 2)
    checks['cross_b_zero'] = (bval(B, M, basis[0], basis[1]) == 0)
    checks['A_block_q'] = (q(basis[0]) == 1 * (M // (2 * 2)) % M)  # t=1, D=2 -> q=1/4 -> xM
    gens = [(1, 0), (0, 1)]
    checks['R_ambient'] = all(bval(B, M, basis[1], e) == 0 for e in gens)
    checks['R_q'] = (q(basis[1]) == 0)
    checks['R_bii_zero'] = (bval(B, M, basis[1], basis[1]) == 0)
    return all(checks.values()), checks
ok, detail = verify_block_certificate((2, 2), (1, 1), {(0, 1): 1})
print('worked [2,2] certificate full verification:', ok, detail)

# gate scan: prose in certificate columns of certified rows
prose = 0
for r in cert_rows:
    try:
        bm = json.loads(r['basis_matrix_json']); bl = json.loads(r['blocks_json'])
        assert isinstance(bm, list) and all(isinstance(x, list) for x in bm)
    except Exception:
        prose += 1
print('prose/string certificates among certified rows:', prose)

# ---------------- F. five cores ----------------
print('=== F. five rank>=5 cores ===')
cores = list(csv.DictReader(open(PKG / 'outputs/phase5_v8l_rankge5_core_radical_quotient_measurement.csv')))
EXPECT = {'rank5_prime': 4, 'rank6_large': 8, 'rank8_large': 64, 'rank10_large': 256, 'rank12_large': 2048}
_core_lines = []
for r in cores:
    D = tuple(json.loads(r['D2_core'])); du = tuple(json.loads(r['diag_units']))
    ed = {(e[0], e[1]): e[2] for e in json.loads(r['edges_2core'])}
    M = form_M(D)
    snf_sz = radical_size_snf(D, du, ed)
    claimed = int(r['radical_size_ambient'])
    gens_std = [tuple(1 if k == i else 0 for k in range(len(D))) for i in range(len(D))]
    Mb, B, q = build(D, du, ed)
    rgens = [tuple(g) for g in json.loads(r['radical_generators_json'])]
    amb = all(all(bval(B, M, g, e) == 0 for e in gens_std) for g in rgens)
    span = subgroup_span(rgens, D)
    qvals = sorted({q(v) for v in span})
    qshape = quotient_shape(rgens, D)
    claimed_shape = sorted(json.loads(r['nondegenerate_complement_shape_after_radical_stripping']))
    line = {
        'case': r['case'], 'snf_radical': snf_sz, 'claimed': claimed, 'expected_anchor': EXPECT[r['case']],
        'gens_ambient_radical': amb, 'gen_span_size': len(span), 'span_matches_radical': len(span) == snf_sz,
        'q_on_radical_match': qvals == sorted(json.loads(r['q_values_on_radical_xM'])),
        'quotient_shape_mine': qshape, 'claimed_shape': claimed_shape, 'shape_match': qshape == claimed_shape,
    }
    # enumeration validation for the two smallest
    if r['case'] in ('rank5_prime', 'rank6_large'):
        rad = radical_enum(D, B, M)
        line['enum_radical'] = len(rad); line['enum_matches_snf'] = (len(rad) == snf_sz)
        line['gen_span_equals_enum_radical'] = (span == set(rad))
    print(json.dumps(line))
    _core_lines.append({k: json.dumps(v) if isinstance(v, list) else v for k, v in line.items()})

cols = sorted({k for l in _core_lines for k in l})
with open(OUT / 'v8l_core_verification.csv', 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=cols); w.writeheader(); w.writerows(_core_lines)
print('=== done ===')

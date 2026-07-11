#!/usr/bin/env python3
"""v8m external audit — from-scratch verification. Stdlib only, exact integers.

 1. Rebuild each of the 229 ground-truth forms; re-verify radical size ambient.
 2. Verify every certificate per section V (extended for the package's GRAM
    block type: recorded q/b must match actual values on the basis vectors):
    SNF span; per-vector order = block D; cross-block b = 0; R blocks ambient
    radical + b(v,v)=0 + q in {0,M/2}; GRAM blocks recorded-vs-actual match.
 3. Status coherence:
    - SINGLE_GRAM rows: radical must be trivial (nondegenerate).
    - SPLIT rows: R-block vectors must generate the FULL radical, and the
      GRAM remainder must be nondegenerate (else partial split = overclaim).
    - 26 UNSPLIT rows: PURITY TEST. R pure in A <=> R is a direct summand
      (finite abelian). Non-pure -> emit witness (r, n): r in R∩nA \\ nR ->
      non-summand PROVEN. Pure -> agent split failure is a bug (P6).
 4. F2 stable class keys: recompute lexmin canonical rep + (order,q)-multiset
    fingerprint per verified v8l class; compare to the F2 CSV.
 5. Cross-CSV consistency (failure rows file vs main file).
"""
import csv, json, itertools
from math import gcd
from collections import Counter, defaultdict
from pathlib import Path

PKG = Path('/home/claude/v8m/phase5_v8m_the_229_data_gated_decomposition')
V8L = Path('/home/claude/v8l/phase5_v8l_full_decomposition_under_data_gates')
OUT = Path('/home/claude/audit_v8m/outputs'); OUT.mkdir(parents=True, exist_ok=True)

def lcm(a, b): return a * b // gcd(a, b)

def form_M(D):
    M = 1
    for d in D: M = lcm(M, 2 * d)
    n = len(D)
    for i in range(n):
        for j in range(i + 1, n): M = lcm(M, lcm(D[i], D[j]))
    return M

def build(D, diag, edges):
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

def all_elems(D): return list(itertools.product(*[range(d) for d in D]))

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
    n = len(D)
    cols = [list(v) for v in vectors] + [[D[k] if k == i else 0 for k in range(n)] for i in range(n)]
    mat = [[cols[c][r] for c in range(len(cols))] for r in range(n)]
    return all(x == 1 for x in snf_invariants(mat, n))

def radical_enum(D, B, M):
    n = len(D)
    gens = [tuple(1 if k == i else 0 for k in range(n)) for i in range(n)]
    return [v for v in all_elems(D) if all(bval(B, M, v, e) == 0 for e in gens)]

def subgroup_span(gens, D):
    zero = tuple(0 for _ in D); seen = {zero}; frontier = [zero]
    while frontier:
        x = frontier.pop()
        for g in gens:
            y = tuple((a + b) % d for a, b, d in zip(x, g, D))
            if y not in seen: seen.add(y); frontier.append(y)
    return seen

def parse_edges(rep, D):
    if isinstance(rep, dict):
        return {(int(k[1]), int(k[2])): v for k, v in rep.items() if v}
    if rep and isinstance(rep[0], int):
        n = len(D); prs = [(i, j) for i in range(n) for j in range(i + 1, n)]
        assert len(rep) == len(prs)
        return {p: c for p, c in zip(prs, rep) if c}
    return {(int(e[0]), int(e[1])): int(e[2]) for e in rep if int(e[2])}

def divisors(x):
    return [d for d in range(2, x + 1) if x % d == 0]

def purity_diagnosis(D, radset):
    """Return (is_pure, witness). Non-pure witness: (r, n) with r in R∩nA \\ nR."""
    exp = 1
    for d in D: exp = lcm(exp, d)
    R = set(radset)
    for n in divisors(exp):
        nA = {tuple((n * a) % d for a, d in zip(v, D)) for v in all_elems(D)}
        nR = {tuple((n * a) % d for a, d in zip(v, D)) for v in R}
        bad = (R & nA) - nR
        if bad:
            return False, (sorted(bad)[0], n)
    return True, None

# ---------------- main: 229 rows ----------------
rows = list(csv.DictReader(open(PKG / 'outputs/phase5_v8m_groundtruth_229_decomposition_certificates.csv')))
print('rows:', len(rows), Counter(r['source'] for r in rows))
assert len(rows) == 229

status_ct = Counter(r['decomposition_status'] for r in rows)
print(status_ct)

evid = []
cert_fail = split_fail = purity_bug = nonsummand_proven = rad_mismatch = 0
for r in rows:
    D = tuple(json.loads(r['shape'])); du = tuple(json.loads(r['diag_units']))
    ed = parse_edges(json.loads(r['representative']), D)
    M, B, q = build(D, du, ed)
    ok_M = (M == int(r['M']))
    rad = radical_enum(D, B, M); radset = set(rad)
    ok_rad = (len(rad) == int(r['radical_size_ambient']))
    if not (ok_M and ok_rad): rad_mismatch += 1

    basis = [tuple(x % d for x, d in zip(v, D)) for v in json.loads(r['basis_matrix_json'])]
    blocks = json.loads(r['blocks_json'])
    n = len(D)
    gens_std = [tuple(1 if k == i else 0 for k in range(n)) for i in range(n)]

    c = {}
    c['span'] = spans(basis, D)
    # block membership map
    idx2block = {}
    for bi, blk in enumerate(blocks):
        for pos, i in enumerate(blk['indices']): idx2block[i] = (bi, pos)
    c['indices_cover'] = sorted(idx2block.keys()) == list(range(len(basis)))
    ok_orders = ok_cross = ok_within = True
    for bi, blk in enumerate(blocks):
        Dblk = blk['D']; qrec = blk['q_xM']; brec = blk['b_xM']
        vecs = [basis[i] for i in blk['indices']]
        for pos, v in enumerate(vecs):
            if order(v, D) != Dblk[pos]: ok_orders = False
            if q(v) != qrec[pos] % M: ok_within = False
            for pos2, w in enumerate(vecs):
                if bval(B, M, v, w) != brec[pos][pos2] % M: ok_within = False
        if blk['type'] == 'R':
            for v in vecs:
                if not all(bval(B, M, v, e) == 0 for e in gens_std): ok_within = False
                if bval(B, M, v, v) != 0: ok_within = False
                if q(v) % M not in (0, M // 2): ok_within = False
        if blk['type'] == 'A':
            t = blk.get('t'); Dv = Dblk[0]
            if q(vecs[0]) != (t * (M // (2 * Dv))) % M: ok_within = False
    for i in range(len(basis)):
        for j in range(i + 1, len(basis)):
            if idx2block[i][0] != idx2block[j][0]:
                if bval(B, M, basis[i], basis[j]) != 0: ok_cross = False
    c['orders'] = ok_orders; c['cross_b_zero'] = ok_cross; c['within_block'] = ok_within
    cert_ok = all(c.values())
    if not cert_ok: cert_fail += 1

    st = r['decomposition_status']; extra = {}
    if st == 'NONDEGENERATE_CERTIFIED_AS_SINGLE_GRAM_BLOCK':
        extra['status_coherent'] = (len(rad) == 1 and len(blocks) == 1 and blocks[0]['type'] == 'GRAM')
    elif st == 'RADICAL_DIRECT_SUMMAND_DECOMPOSED_CERTIFIED':
        rvecs = [basis[i] for blk in blocks if blk['type'] == 'R' for i in blk['indices']]
        span = subgroup_span(rvecs, D)
        full_rad = (span == radset)
        gram_blocks = [blk for blk in blocks if blk['type'] == 'GRAM']
        gram_nondeg = True
        for blk in gram_blocks:
            Db = blk['D']; Mb = form_M(tuple(Db))
            # nondegeneracy of recorded block: kernel of recorded b on prod Z/Db
            Bb = [[(blk['b_xM'][i][j] * (Mb // M) if M and Mb % M == 0 else None) for j in range(len(Db))] for i in range(len(Db))]
            # safer: test nondegeneracy in ambient — block vectors' pairwise b as recorded, kernel within the block subgroup:
            bvecs = [basis[i] for i in blk['indices']]
            sub = subgroup_span(bvecs, D)
            deg = [v for v in sub if all(bval(B, M, v, w) == 0 for w in bvecs) and any(v)]
            if deg: gram_nondeg = False
        extra['r_span_equals_full_radical'] = full_rad
        extra['gram_remainder_nondegenerate'] = gram_nondeg
        extra['status_coherent'] = full_rad and gram_nondeg
        if not extra['status_coherent']: split_fail += 1
        # purity must hold here (consistency): radical was split as summand
    elif st == 'CERTIFIED_UNSPLIT_GRAM_BLOCK_RADICAL_SPLIT_BLOCKING_OPEN':
        pure, wit = purity_diagnosis(D, radset)
        fv = tuple(x % d for x, d in zip(json.loads(r['failure_vector']), D))
        extra['failure_vector_is_radical'] = fv in radset
        extra['radical_pure'] = pure
        if pure:
            purity_bug += 1; extra['diagnosis'] = 'RADICAL IS PURE -> SUMMAND EXISTS -> AGENT SPLIT FAILURE IS A BUG (P6)'
        else:
            nonsummand_proven += 1
            extra['diagnosis'] = 'NON_SUMMAND_PROVEN'
            extra['nonsummand_witness_vector'] = list(wit[0]); extra['nonsummand_witness_n'] = wit[1]
        extra['status_coherent'] = extra['failure_vector_is_radical']
    evid.append({'ground_truth_id': r['ground_truth_id'], 'source': r['source'], 'shape': r['shape'],
                 'status': st, 'M_ok': ok_M, 'radical_size_ok': ok_rad,
                 'certificate_verified_by_auditor': cert_ok, **{k: json.dumps(v) if isinstance(v, (list, tuple)) else v for k, v in extra.items()}})

print(f'certificate failures: {cert_fail} | radical data mismatches: {rad_mismatch} | split-claim failures: {split_fail}')
print(f'26-row diagnosis: non-summand proven {nonsummand_proven} | pure (bug) {purity_bug}')

cols = sorted({k for e in evid for k in e})
with open(OUT / 'v8m_229_verification.csv', 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=cols); w.writeheader(); w.writerows(evid)

# purity spot-check on 10 split rows: radical must be pure there
spot = [r for r in rows if r['decomposition_status'] == 'RADICAL_DIRECT_SUMMAND_DECOMPOSED_CERTIFIED'][:10]
sp_ok = True
for r in spot:
    D = tuple(json.loads(r['shape'])); du = tuple(json.loads(r['diag_units']))
    M, B, q = build(D, du, parse_edges(json.loads(r['representative']), D))
    pure, _ = purity_diagnosis(D, set(radical_enum(D, B, M)))
    sp_ok &= pure
print('purity consistency on 10 split rows (must all be pure):', sp_ok)

# ---------------- failure rows CSV cross-check ----------------
frows = list(csv.DictReader(open(PKG / 'outputs/phase5_v8m_radical_split_failure_rows.csv')))
main_fail = {r['ground_truth_id'] for r in rows if r['decomposition_status'] == 'CERTIFIED_UNSPLIT_GRAM_BLOCK_RADICAL_SPLIT_BLOCKING_OPEN'}
print('failure CSV rows:', len(frows), 'ids match main CSV:', {f['ground_truth_id'] for f in frows} == main_fail)

# ---------------- F2 stable class keys ----------------
PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
D4 = (4, 4, 2, 16); DIAG4 = (1, 3, 3, 5); M4 = form_M(D4)
ELEMS4 = all_elems(D4); ORD4 = {v: order(v, D4) for v in ELEMS4}
cls_rows = list(csv.DictReader(open(V8L / 'outputs/phase5_v8l_true_diag_rank4_exact_orbit_classes.csv')))
def parse_form6(d): return tuple(d[f'c{i}{j}'] for (i, j) in PAIRS)
f2 = {int(r['published_class_id']): r for r in csv.DictReader(open(PKG / 'outputs/phase5_v8m_f2_stable_class_keys_true_diag_rank4.csv'))}
print('F2 rows:', len(f2), 'cols:', list(next(iter(f2.values())).keys()))
f2_ok = True
for r in cls_rows:
    cid = int(r['class_id'])
    members = [parse_form6(m) for m in json.loads(r['members_json'])]
    lexmin = sorted(members)[0]
    rep_edges = {p: c for p, c in zip(PAIRS, lexmin) if c}
    M, B, q = build(D4, DIAG4, rep_edges)
    fp = sorted(Counter((ORD4[v], q(v)) for v in ELEMS4).items())
    fp_list = [[o, qq, ct] for (o, qq), ct in fp]
    row = f2[cid]
    their_rep = parse_form6(json.loads(row['canonical_representative']))
    their_fp = json.loads(row['order_q_multiset_fingerprint'])
    ok = (their_rep == lexmin and sorted(map(tuple, their_fp)) == sorted(map(tuple, fp_list)))
    if not ok: f2_ok = False; print('  F2 MISMATCH class', cid, their_rep, lexmin)
print('F2 keys all match auditor recomputation:', f2_ok)
# reconciliation: archival class (verified id 5) canonical rep check
arch_row = f2[5]
print('archival class 5 canonical rep:', arch_row['canonical_representative'])
print('=== done ===')

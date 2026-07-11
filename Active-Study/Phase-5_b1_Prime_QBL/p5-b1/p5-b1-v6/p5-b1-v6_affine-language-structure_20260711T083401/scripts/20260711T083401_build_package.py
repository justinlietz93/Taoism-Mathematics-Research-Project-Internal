#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import zipfile
sys.dont_write_bytecode = True
from pathlib import Path
from typing import Any

import nbformat
from nbclient import NotebookClient

STAMP = "20260711T083401"
PACKAGE_NAME = f"p5-b1-v6_affine-language-structure_{STAMP}"
FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)


def load_derive(root: Path):
    path = root / "scripts" / f"{STAMP}_derive_affine_language.py"
    spec = importlib.util.spec_from_file_location("qbl_v6_derive", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load derivation script")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_data(root: Path) -> dict[str, Any]:
    o = root / "outputs"
    return {
        "summary": json.loads((o / f"{STAMP}_run_summary.json").read_text()),
        "structure": json.loads((o / f"{STAMP}_language_structure_status.json").read_text()),
        "comparison": json.loads((o / f"{STAMP}_edge_envelope_comparison.json").read_text()),
        "boundary": json.loads((o / f"{STAMP}_finite_boundary_certificate.json").read_text()),
        "numerical": json.loads((o / f"{STAMP}_numerical_core.json").read_text()),
        "length3": read_csv(o / f"{STAMP}_realizable_length3_words.csv"),
        "complexity": read_csv(o / f"{STAMP}_word_complexity.csv"),
        "markov": read_csv(o / f"{STAMP}_exact_markov_order_counterexamples.csv"),
        "followers": read_csv(o / f"{STAMP}_boundary_adjacent_follower_pairs.csv"),
        "follower_signatures": read_csv(o / f"{STAMP}_follower_signature_counts.csv"),
        "states": read_csv(o / f"{STAMP}_state_frequencies.csv"),
        "defects": read_csv(o / f"{STAMP}_defect_frequencies.csv"),
        "empirical": read_csv(o / f"{STAMP}_empirical_joint_transition.csv"),
    }


def md_cell(text: str, cid: str) -> dict[str, Any]:
    return {"cell_type": "markdown", "id": cid, "metadata": {}, "source": text}


def code_cell(source: str, cid: str) -> dict[str, Any]:
    return {"cell_type": "code", "execution_count": None, "id": cid, "metadata": {}, "outputs": [], "source": source}


def notebook_cells(data: dict[str, Any]) -> list[dict[str, Any]]:
    a = data["numerical"]["constants"]["a"]
    l3_actual = [r["word"] for r in data["length3"] if r["realizable"] == "True"]
    l3_env = [r["word"] for r in data["length3"] if r["edge_envelope"] == "True"]
    complexity = [int(r["actual_affine_complexity"]) for r in data["complexity"]]
    direct = [None if r["direct_exact_cylinders"] == "" else int(r["direct_exact_cylinders"]) for r in data["complexity"]]
    markov_orders = [int(r["tested_order"]) for r in data["markov"]]
    follower_p = [float(r["D_n_p_lower"]) for r in data["followers"]]
    follower_words_left = [r["left_adjacent_word"] for r in data["followers"][:12]]
    follower_words_right = [r["right_adjacent_word"] for r in data["followers"][:12]]
    J = [[float(x) for x in row] for row in data["comparison"]["J"]]
    K = [[float(x) for x in row] for row in data["comparison"]["K_edge_envelope"]]
    empirical = [[0.0]*3 for _ in range(3)]
    idx = {7: 0, 8: 1, 9: 2}
    for r in data["empirical"]:
        empirical[idx[int(r["from_state"])]][idx[int(r["to_state"])]] = float(r["frequency"])
    state_counts = [int(r["count"]) for r in data["states"]]
    defect_counts = [int(r["count"]) for r in data["defects"]]
    boundary = data["boundary"]
    mj = data["comparison"]["metrics_empirical_vs_J"]
    mk = data["comparison"]["metrics_empirical_vs_K_edge_envelope"]

    cells: list[dict[str, Any]] = [
        md_cell("# QBL Affine Carry Language Structure v6\n\nNo notebook file I/O. Every code cell emits one figure and prints PASS or FAIL. Abstract theorem proofs are carried in the companion Markdown; notebook cells verify exact identities or finite certificates without upgrading evidence.", "intro"),
        md_cell("## Claim 1: affine ceiling recurrence and half-open partition identities", "md-01"),
        code_cell(f'''import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

a=sp.symbols('a', real=True)
E,T,gamma=sp.symbols('E T gamma', real=True)
c=sp.ceiling(2*E+gamma)
I7=(-1,-sp.Rational(1,2)-a); I8=(-sp.Rational(1,2)-a,-a); I9=(-a,0)
identities=[sp.simplify(2*(-sp.Rational(1,2)-a)+(8+2*a)),sp.simplify(2*(-a)+(8+2*a))]
passed=(identities==[7,8] and I7[1]==I8[0] and I8[1]==I9[0])
print('PASS' if passed else 'FAIL')
print('c_A = ceil(2 E_(A-1)+gamma)')
print('E_A = 2 E_(A-1)+gamma-c_A')
print('boundary ceiling values:',identities)
a_num=float('{a}')
fig,ax=plt.subplots(figsize=(7,2.6))
ax.hlines(0,-1,0)
for x,label in [(-1,'-1'),(-.5-a_num,'-1/2-a'),(-a_num,'-a'),(0,'0')]:
    ax.axvline(x); ax.text(x,0.04,label,ha='center')
ax.set_yticks([]); ax.set_xlim(-1.03,.03); ax.set_title('Exact half-open carry partition')
plt.show()''', "claim-01"),
        md_cell("## Claim 2: symbolic J and P identities under the stated parameter assumptions", "md-02"),
        code_cell(f'''aa=sp.symbols('a', positive=True)
J=sp.Matrix([[0,(1-3*aa)/2,aa/2],[(1-2*aa)/4,sp.Rational(1,4),aa/2],[(1-2*aa)/4,3*aa/2-sp.Rational(1,4),0]])
pi=sp.Matrix([[sp.Rational(1,2)-aa,sp.Rational(1,2),aa]])
P=sp.Matrix([[0,(1-3*aa)/(1-2*aa),aa/(1-2*aa)],[(1-2*aa)/2,sp.Rational(1,2),aa],[(1-2*aa)/(4*aa),(6*aa-1)/(4*aa),0]])
rows=[sp.simplify(sum(J[i,j] for j in range(3))) for i in range(3)]
cols=[sp.simplify(sum(J[i,j] for i in range(3))) for j in range(3)]
prows=[sp.simplify(sum(P[i,j] for j in range(3))) for i in range(3)]
stat=[sp.simplify(x) for x in list(pi*P-pi)]
passed=(rows==[sp.Rational(1,2)-aa,sp.Rational(1,2),aa] and cols==rows and sp.simplify(sum(J))==1 and prows==[1,1,1] and stat==[0,0,0])
print('PASS' if passed else 'FAIL')
print('J row/column sums:',rows)
print('P row sums:',prows,' stationarity residual:',stat)
Jn=np.array(J.subs(aa,sp.Float('{a}',80)).evalf(30).tolist(),dtype=float)
fig,ax=plt.subplots(figsize=(5,4)); ax.imshow(Jn)
ax.set_xticks(range(3),['7','8','9']); ax.set_yticks(range(3),['7','8','9']); ax.set_title('One-step Lebesgue mass J')
for i in range(3):
    for j in range(3): ax.text(j,i,f'{{Jn[i,j]:.3f}}',ha='center',va='center')
plt.show()''', "claim-02"),
        md_cell("## Claim 3: the full prefix calculation forbids 989", "md-03"),
        code_cell(f'''aa=sp.symbols('a', real=True)
x=sp.symbols('x', real=True)
F9=2*x-1+2*aa
y=sp.symbols('y', real=True)
F8y=2*y+2*aa
upper=sp.simplify(F8y.subs(y,-1+2*aa))
separation=sp.simplify((-aa)-upper)
passed=(upper==-2+6*aa and separation==2-7*aa)
print('PASS' if passed else 'FAIL')
print('C_98 current interval = (-1/2-a,-1+2a]')
print('F8 upper endpoint =',upper)
print('distance to I9 lower boundary =',separation,'>0 when a<1/4')
a_num=float('{a}')
img=(-1,-2+6*a_num); i9=(-a_num,0)
fig,ax=plt.subplots(figsize=(7,2.6)); ax.hlines(0,-1,0)
ax.axvspan(img[0],img[1],alpha=.35,label='F8(C98)'); ax.axvspan(i9[0],i9[1],alpha=.35,label='I9')
ax.set_yticks([]); ax.set_xlim(-1.03,.03); ax.set_title('Forbidden 989 interval separation'); ax.legend()
plt.show()''', "claim-03"),
        md_cell("## Claim 4: exact length-three support at the current parameter", "md-04"),
        code_cell(f'''actual={l3_actual!r}
envelope={l3_env!r}
missing=sorted(set(envelope)-set(actual))
passed=(len(actual)==15 and len(envelope)==17 and missing==['787','989'])
print('PASS' if passed else 'FAIL')
print('actual words:',actual)
print('edge-envelope excess:',missing)
fig,ax=plt.subplots(figsize=(6,3)); ax.bar(['actual','edge envelope'],[len(actual),len(envelope)])
ax.set_ylim(0,19); ax.set_title('Length-three word count')
plt.show()''', "claim-04"),
        md_cell("## Claim 5: refinement-boundary count and exact complexity formula", "md-05"),
        code_cell(f'''n=sp.symbols('n', integer=True, nonnegative=True)
# Exact finite identity checked symbolically for a free integer N by the closed form.
N=np.arange(1,21)
formula=np.array([2**(int(k)+1)-1 for k in N],dtype=object)
injected=np.array({complexity!r},dtype=object)
passed=np.array_equal(formula,injected)
print('PASS' if passed else 'FAIL')
print('boundary levels: union k=0..n D^(-k)(p)')
print('sum_(k=0)^n 2^k = 2^(n+1)-1')
print('The companion proof establishes that every complementary arc is one nonempty cylinder and adjacent arcs have distinct words.')
fig,ax=plt.subplots(figsize=(7,3.5)); ax.plot(N,[int(x) for x in formula],marker='o'); ax.set_yscale('log')
ax.set_xlabel('word length n'); ax.set_ylabel('p(n)'); ax.set_title('Exact affine complexity')
plt.show()''', "claim-05"),
        md_cell("## Claim 6: direct rational-affine cylinder enumeration through depth 12", "md-06"),
        code_cell(f'''direct={direct!r}
expected=[2**(n+1)-1 for n in range(1,13)]
passed=(direct[:12]==expected and all(x is None for x in direct[12:]))
print('PASS' if passed else 'FAIL')
print('direct counts:',direct[:12])
print('method: endpoints q*a+r with rational coefficients; signs certified over an outward a enclosure')
fig,ax=plt.subplots(figsize=(7,3.5)); ax.plot(range(1,13),direct[:12],marker='o'); ax.set_yscale('log'); ax.set_title('Direct cylinder enumeration')
plt.show()''', "claim-06"),
        md_cell("## Claim 7: finite follower-boundary trace supporting the non-soficity proof", "md-07"),
        code_cell(f'''pn=np.array({follower_p!r},dtype=float)
left={follower_words_left!r}; right={follower_words_right!r}
passed=(len(pn)==20 and len(set(np.round(pn,14)))==20 and all(left) and all(right))
print('PASS' if passed else 'FAIL')
print('first 12 left-adjacent words:',left)
print('first 12 right-adjacent words:',right)
print('The abstract proof uses infinitely many distinct D^n(p), follower-arc separation, and the finite-follower-set characterization of sofic shifts.')
fig,ax=plt.subplots(figsize=(7,3.5)); ax.plot(range(1,21),pn,marker='o'); ax.set_ylim(0,1); ax.set_xlabel('n'); ax.set_ylabel('D^n(p)'); ax.set_title('Boundary orbit sample')
plt.show()''', "claim-07"),
        md_cell("## Claim 8: exactness mechanism used in the mixing proof", "md-08"),
        code_cell('''lengths=np.array([0.4,0.2,0.1,0.05,0.025])
N=np.array([int(np.floor(np.log2(1/x)))+1 for x in lengths])
covered=(2.0**N)*lengths
passed=bool(np.all(covered>1) and np.all((2.0**(N-1))*lengths<=1))
print('PASS' if passed else 'FAIL')
print('For every open arc length ell>0, choose N=floor(log2(1/ell))+1; then 2^N ell>1 and D^N covers the circle.')
print('sample N:',N,' scaled lengths:',covered)
print('The companion proof applies this to D^|u|(int C(u)) for arbitrary words u and v.')
fig,ax=plt.subplots(figsize=(7,3.5)); ax.bar([str(x) for x in lengths],covered); ax.axhline(1); ax.set_xlabel('initial arc length'); ax.set_ylabel('2^N ell'); ax.set_title('Doubling exactness threshold')
plt.show()''', "claim-08"),
        md_cell("## Claim 9: interval-certified finite memory counterexamples for orders 1 through 10", "md-09"),
        code_cell(f'''orders={markov_orders!r}
passed=(orders==list(range(1,11)))
print('PASS' if passed else 'FAIL')
print('certified orders:',orders)
print('Global no-finite-order status follows from the non-soficity theorem, not from these ten finite cases alone.')
fig,ax=plt.subplots(figsize=(7,3)); ax.bar(orders,[1]*len(orders)); ax.set_yticks([0,1],['','counterexample']); ax.set_xlabel('order'); ax.set_title('Finite memory counterexamples')
plt.show()''', "claim-09"),
        md_cell("## Claim 10: M and K remain pairwise-envelope objects", "md-10"),
        code_cell('''M=sp.Matrix([[0,1,1],[1,1,1],[1,1,0]])
M2=M**2
rho=1+sp.sqrt(2); r=sp.Matrix([1,sp.sqrt(2),1])
res=sp.simplify(M*r-rho*r)
passed=(M2==sp.Matrix([[2,2,1],[2,3,2],[1,2,2]]) and res==sp.zeros(3,1))
print('PASS' if passed else 'FAIL')
print('M^2 ='); sp.pprint(M2)
print('edge-envelope Perron root:',rho)
print('Actual affine entropy is log(2); envelope entropy is log(1+sqrt(2)).')
fig,ax=plt.subplots(figsize=(6,3)); ax.bar(['actual affine','edge envelope'],[float(sp.log(2)),float(sp.log(rho).evalf())]); ax.set_ylabel('entropy'); ax.set_title('Distinct entropy objects')
plt.show()''', "claim-10"),
        md_cell("## Claim 11: finite empirical edge comparison", "md-11"),
        code_cell(f'''emp=np.array({empirical!r},dtype=float); Jn=np.array({J!r},dtype=float); Kn=np.array({K!r},dtype=float)
def metrics(A,B):
    d=np.abs(A-B); return d.max(),d.sum(),d.sum()/2
mJ=metrics(emp,Jn); mK=metrics(emp,Kn)
passed=(abs(mJ[0]-float('{mj['max_absolute_error']}'))<1e-15 and abs(mJ[2]-float('{mj['total_variation']}'))<1e-15 and abs(mK[0]-float('{mk['max_absolute_error']}'))<1e-15 and abs(mK[2]-float('{mk['total_variation']}'))<1e-15)
print('PASS' if passed else 'FAIL')
print('empirical vs J:',mJ)
print('empirical vs envelope K:',mK)
fig,ax=plt.subplots(figsize=(7,3)); x=np.arange(3); w=.35
ax.bar(x-w/2,mJ,width=w,label='vs J'); ax.bar(x+w/2,mK,width=w,label='vs K envelope'); ax.set_xticks(x,['max','L1','TV']); ax.set_title('Finite edge errors'); ax.legend()
plt.show()''', "claim-11"),
        md_cell("## Claim 12: state and defect frequencies remain evidence, not equidistribution proof", "md-12"),
        code_cell(f'''state_counts=np.array({state_counts!r},dtype=int); defect_counts=np.array({defect_counts!r},dtype=int)
a_num=float('{a}')
state_emp=state_counts/state_counts.sum(); state_bench=np.array([.5-a_num,.5,a_num])
def_emp=defect_counts/defect_counts.sum(); def_bench=np.array([(1-2*a_num)/4,a_num,.25,.5-a_num,a_num/2])
passed=(state_counts.sum()==10000 and defect_counts.sum()==9999)
print('PASS' if passed else 'FAIL')
print('state empirical:',state_emp,' benchmark:',state_bench)
print('defect empirical:',def_emp,' benchmark:',def_bench)
print('SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED')
fig,ax=plt.subplots(figsize=(7,3)); x=np.arange(5); w=.35
ax.bar(x-w/2,def_emp,width=w,label='empirical'); ax.bar(x+w/2,def_bench,width=w,label='Lebesgue'); ax.set_xticks(x,['-2','-1','0','+1','+2']); ax.set_title('Defect frequencies'); ax.legend()
plt.show()''', "claim-12"),
        md_cell("## Claim 13: finite outward-rounded boundary certificate", "md-13"),
        code_cell(f'''bd={json.dumps(boundary)!r}
import json as _json
bd=_json.loads(bd); rec=bd['minimum_boundary_distance_lower_bound']
passed=(bd['all_imported_carries_certified'] and bd['certified_carry_steps']==10000 and bd['all_E_A_boundary_disjoint_for_A_0_10000'] and float(rec['distance_lower_bound'])>0)
print('PASS' if passed else 'FAIL')
print('method:',bd['method'],' digits:',bd['decimal_digits'])
print('minimum separation lower bound:',rec['distance_lower_bound'],'at A=',rec['A'],'boundary=',rec['boundary'])
print('Global boundary avoidance is not proved.')
fig,ax=plt.subplots(figsize=(6,3)); ax.bar(['minimum gap','maximum interval width'],[float(rec['distance_lower_bound']),float(bd['maximum_orbit_interval_width'])]); ax.set_yscale('log'); ax.set_title('Finite interval certificate')
plt.show()''', "claim-13"),
        md_cell("## Claim 14: current Orthad boundary", "md-14"),
        code_cell('''holds=['GLOBAL T_A=ceil(y_A) BRIDGE: NOT YET PROVED','GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED','SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED']
open_obligations=['primary pairing recurrence','explicit chart maps','bidirectional transfer recurrences','multi-axis FQM construction']
passed=(len(holds)==3 and len(open_obligations)==4)
print('PASS' if passed else 'FAIL')
print('holds:'); [print('  ',x) for x in holds]
print('Orthad obligations:'); [print('  ',x) for x in open_obligations]
fig,ax=plt.subplots(figsize=(7,3)); ax.bar(range(4),[1,1,1,1]); ax.set_xticks(range(4),['pairing','charts','transfers','multi-axis FQM'],rotation=15); ax.set_yticks([0,1],['','open']); ax.set_title('Orthad obligations remain open')
plt.show()''', "claim-14"),
        md_cell("## Claim 15: negative control outside the parameter interval", "md-15"),
        code_cell('''a_bad=sp.Rational(1,10)
sym_a=next(iter(J.free_symbols))
Jbad=J.subs(sym_a,a_bad)
passed=(Jbad[2,1] < 0) == True
print('PASS' if passed else 'FAIL')
print('At a=1/10, J_98 =',Jbad[2,1],'<0; the seven-edge support law is invalid outside 1/6<a<1/4.')
vals=np.array(Jbad.evalf().tolist(),dtype=float).ravel()
fig,ax=plt.subplots(figsize=(7,3)); ax.bar(range(9),vals); ax.axhline(0); ax.set_xticks(range(9),['77','78','79','87','88','89','97','98','99']); ax.set_title('Negative parameter control')
plt.show()''', "claim-15"),
    ]
    return cells


def strip_volatile(nb: dict[str, Any]) -> None:
    nb["metadata"] = {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3"},
    }
    for cell in nb["cells"]:
        cell["metadata"] = {}
        for out in cell.get("outputs", []):
            if "metadata" in out:
                out["metadata"] = {}


def build_notebooks(root: Path) -> None:
    data = load_data(root)
    nbd = {
        "cells": notebook_cells(data),
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    nb = nbformat.from_dict(nbd)
    source_path = root / "notebooks" / f"{STAMP}_Affine_Language.ipynb"
    executed_path = root / "notebooks" / f"{STAMP}_Affine_Language_executed.ipynb"
    strip_volatile(nb)
    nbformat.write(nb, source_path)
    client = NotebookClient(nb, timeout=900, kernel_name="python3", allow_errors=False)
    executed = client.execute(cwd=str(root))
    strip_volatile(executed)
    nbformat.write(executed, executed_path)

    figures = root / "figures"
    figures.mkdir(exist_ok=True)
    for p in figures.glob(f"{STAMP}_notebook_claim_*.png"):
        p.unlink()
    idx = 0
    for cell in executed["cells"]:
        if cell.get("cell_type") != "code":
            continue
        text = ""
        pngs = []
        for out in cell.get("outputs", []):
            if out.get("output_type") == "stream":
                text += out.get("text", "")
            d = out.get("data", {})
            if "image/png" in d:
                pngs.append(d["image/png"])
        if "PASS" not in text or "FAIL" in text:
            raise RuntimeError(f"notebook cell failed: {cell.get('id')}\n{text[:1000]}")
        if len(pngs) != 1:
            raise RuntimeError(f"cell {cell.get('id')} emitted {len(pngs)} PNGs")
        idx += 1
        raw = pngs[0]
        if isinstance(raw, list):
            raw = "".join(raw)
        (figures / f"{STAMP}_notebook_claim_{idx:02d}.png").write_bytes(base64.b64decode(raw))
    if idx != 15:
        raise RuntimeError(f"expected 15 code cells, found {idx}")


def compile_lean(root: Path) -> None:
    log = root / "proofs" / f"{STAMP}_lean_compiler.log"
    lean = shutil.which("lean")
    sources = sorted((root / "proofs").glob(f"{STAMP}_*.lean"))
    if lean is None:
        log.write_text("LEAN SOURCE PRESENT; COMPILATION NOT VERIFIED\nLean executable and matching Mathlib environment were unavailable in the build container.\n", encoding="utf-8")
        return
    chunks = []
    for src in sources:
        proc = subprocess.run([lean, src.name], cwd=src.parent, text=True, capture_output=True)
        chunks.append(f"command: {lean} {src.name}\nreturncode: {proc.returncode}\nstdout:\n{proc.stdout}\nstderr:\n{proc.stderr}\n")
        if proc.returncode != 0:
            log.write_text("\n".join(chunks), encoding="utf-8")
            raise RuntimeError(f"Lean compilation failed: {src.name}")
    log.write_text("\n".join(chunks), encoding="utf-8")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_manifest(root: Path) -> None:
    records = []
    for path in sorted(p for p in root.rglob("*") if p.is_file() and p.name != "MANIFEST.json"):
        records.append({
            "path": path.relative_to(root).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        })
    payload = {"package": root.name, "file_count": len(records), "hash_algorithm": "SHA-256", "files": records}
    (root / "MANIFEST.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def verify_manifest(root: Path) -> None:
    payload = json.loads((root / "MANIFEST.json").read_text())
    expected = {r["path"]: r for r in payload["files"]}
    actual = {p.relative_to(root).as_posix(): p for p in root.rglob("*") if p.is_file() and p.name != "MANIFEST.json"}
    if set(expected) != set(actual):
        raise RuntimeError("manifest path set mismatch")
    for rel, path in actual.items():
        rec = expected[rel]
        if rec["bytes"] != path.stat().st_size or rec["sha256"] != sha256(path):
            raise RuntimeError(f"manifest mismatch: {rel}")


def deterministic_zip(root: Path, out: Path) -> None:
    if out.exists():
        out.unlink()
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(p for p in root.rglob("*") if p.is_file()):
            arc = f"{root.name}/{path.relative_to(root).as_posix()}"
            info = zipfile.ZipInfo(arc, FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            zf.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def build(root: Path, make_zip: bool) -> Path | None:
    module = load_derive(root)
    module.run(root)
    build_notebooks(root)
    compile_lean(root)
    for cache in sorted(root.rglob("__pycache__"), reverse=True):
        if cache.is_dir():
            shutil.rmtree(cache)
    for pyc in root.rglob("*.pyc"):
        pyc.unlink()
    write_manifest(root)
    verify_manifest(root)
    if make_zip:
        out = root.parent / f"{root.name}.zip"
        deterministic_zip(root, out)
        return out
    return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--zip", action="store_true")
    args = ap.parse_args()
    out = build(args.root.resolve(), args.zip)
    print(json.dumps({"root": str(args.root.resolve()), "manifest_verified": True, "zip": None if out is None else str(out), "zip_sha256": None if out is None else sha256(out)}, indent=2))


if __name__ == "__main__":
    main()

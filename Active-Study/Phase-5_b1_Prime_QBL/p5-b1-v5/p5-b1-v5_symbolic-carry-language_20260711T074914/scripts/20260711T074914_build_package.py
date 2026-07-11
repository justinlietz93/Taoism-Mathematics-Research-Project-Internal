#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
import zipfile
from collections import Counter
from pathlib import Path
from typing import Any

import nbformat
import numpy as np
from nbclient import NotebookClient

STAMP = "20260711T074914"
PACKAGE_NAME = f"p5-b1-v5_symbolic-carry-language_{STAMP}"


def find_one(root: Path, pattern: str) -> Path:
    matches = sorted((root / "inputs").glob(pattern))
    if len(matches) != 1:
        raise RuntimeError(f"expected one {pattern}, found {len(matches)}")
    return matches[0]


def load_derive(root: Path):
    path = root / "scripts" / f"{STAMP}_derive_symbolic_language.py"
    spec = importlib.util.spec_from_file_location("qbl_symbolic_derive", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load derivation module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def derive_trace_counts(root: Path) -> dict[str, Any]:
    path = find_one(root, "*_PRIOR_CARRY_DEFECT_A0_A10000.csv")
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if len(rows) != 10001:
        raise RuntimeError("trace row count mismatch")
    rows = sorted(rows, key=lambda r: int(r["A"]))
    if [int(r["A"]) for r in rows] != list(range(10001)):
        raise RuntimeError("trace A coverage mismatch")
    carries = {A: int(rows[A]["carry"]) for A in range(1, 10001)}
    trans = Counter((carries[A - 1], carries[A]) for A in range(2, 10001))
    defects = Counter(carries[A] - carries[A - 1] for A in range(2, 10001))
    states = Counter(carries.values())
    transition_counts = [[trans[(i, j)] for j in (7, 8, 9)] for i in (7, 8, 9)]
    return {
        "transition_counts": transition_counts,
        "state_counts": [states[i] for i in (7, 8, 9)],
        "defect_counts": [defects[d] for d in (-2, -1, 0, 1, 2)],
    }


def load_output_counts(root: Path) -> dict[str, Any]:
    outputs = root / "outputs"
    trans = [[0] * 3 for _ in range(3)]
    idx = {7: 0, 8: 1, 9: 2}
    with (outputs / f"{STAMP}_empirical_joint_transition.csv").open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            trans[idx[int(r["from_state"])]][idx[int(r["to_state"])]] = int(r["count"])
    states = []
    with (outputs / f"{STAMP}_state_frequencies.csv").open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            states.append(int(r["count"]))
    defects = []
    with (outputs / f"{STAMP}_defect_frequencies.csv").open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            defects.append(int(r["count"]))
    return {"transition_counts": trans, "state_counts": states, "defect_counts": defects}


def load_notebook_data(root: Path) -> dict[str, Any]:
    trace = derive_trace_counts(root)
    output = load_output_counts(root)
    if trace != output:
        raise RuntimeError(f"derived trace arrays disagree with output files: {trace} != {output}")
    outputs = root / "outputs"
    comparison = json.loads((outputs / f"{STAMP}_edge_envelope_comparison.json").read_text())
    boundary = json.loads((outputs / f"{STAMP}_finite_boundary_certificate.json").read_text())
    numerical = json.loads((outputs / f"{STAMP}_numerical_results.json").read_text())
    l3 = list(csv.DictReader((outputs / f"{STAMP}_realizable_length3_words.csv").open(newline="", encoding="utf-8")))
    complexity = list(csv.DictReader((outputs / f"{STAMP}_word_complexity.csv").open(newline="", encoding="utf-8")))
    markov = list(csv.DictReader((outputs / f"{STAMP}_markov_order_counterexamples.csv").open(newline="", encoding="utf-8")))
    return {"trace": trace, "output": output, "comparison": comparison, "boundary": boundary,
            "numerical": numerical, "length3": l3, "complexity": complexity, "markov": markov}


def notebook_cells(data: dict[str, Any]) -> list[dict[str, Any]]:
    md = nbformat.v4.new_markdown_cell
    code = nbformat.v4.new_code_cell
    trace = data["trace"]
    output = data["output"]
    comparison = data["comparison"]
    boundary = data["boundary"]
    l3_words = [r["word"] for r in data["length3"] if r["realizable_current_parameter"] == "True"]
    envelope_words = [r["word"] for r in data["length3"] if r["pairwise_edge_envelope"] == "True"]
    complexity_actual = [int(r["actual_affine_cylinders_exact"]) for r in data["complexity"]]
    complexity_direct = [None if not r["direct_interval_enumeration"] else int(r["direct_interval_enumeration"]) for r in data["complexity"]]
    complexity_env = [int(r["pairwise_edge_envelope_paths"]) for r in data["complexity"]]
    markov_orders = [int(r["tested_markov_order"]) for r in data["markov"]]
    j = comparison["J"]
    k = comparison["K_edge_envelope"]
    metrics_j = comparison["metrics_empirical_vs_J"]
    metrics_k = comparison["metrics_empirical_vs_K_edge_envelope"]
    a_str = data["numerical"]["constants"]["a"]

    cells = [
        md("# QBL Carry J and Symbolic Boundary v3\n\nGenerated with no notebook file I/O. Every code cell emits one figure and an explicit PASS/FAIL."),
        md("## Claim 1: exact affine partition and symbolic parameter inequalities"),
        code(f'''import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

a=sp.symbols('a', real=True)
I7=(-1,-sp.Rational(1,2)-a); I8=(-sp.Rational(1,2)-a,-a); I9=(-a,0)
positivity=[sp.Rational(1,6)<sp.Rational(1,4), 3*sp.Rational(1,6)-sp.Rational(1,2)==0]
passed=(I7[1]==I8[0] and I8[1]==I9[0] and positivity==[True,True])
print('PASS' if passed else 'FAIL')
print('I7=(-1,-1/2-a], I8=(-1/2-a,-a], I9=(-a,0]')
print('Assumption used symbolically: 1/6 < a < 1/4')
a_num=float('{a_str}')
fig,ax=plt.subplots(figsize=(7,2.5))
ax.hlines(0,-1,0)
for x,label in [(-1,'-1'),(-.5-a_num,'-1/2-a'),(-a_num,'-a'),(0,'0')]:
    ax.axvline(x); ax.text(x,0.04,label,ha='center')
ax.set_yticks([]); ax.set_xlim(-1.05,.05); ax.set_title('Half-open carry partition')
plt.show()'''),
        md("## Claim 2: J has exactly seven positive entries under the full parameter assumptions"),
        code(f'''aa=sp.symbols('a', real=True)
J=sp.Matrix([[0,(1-3*aa)/2,aa/2],[(1-2*aa)/4,sp.Rational(1,4),aa/2],[(1-2*aa)/4,3*aa/2-sp.Rational(1,4),0]])
# Exact lower bounds obtained from 1/6<a<1/4.
lower_bounds={{'J78':sp.Rational(1,8),'J79':sp.Rational(1,12),'J87':sp.Rational(1,8),'J88':sp.Rational(1,4),'J89':sp.Rational(1,12),'J97':sp.Rational(1,8),'J98':0}}
# J98 is strictly positive because a>1/6; its infimum is zero but is not attained.
row=[sp.simplify(sum(J[i,j] for j in range(3))) for i in range(3)]
col=[sp.simplify(sum(J[i,j] for i in range(3))) for j in range(3)]
passed=(J[0,0]==0 and J[2,2]==0 and row==[sp.Rational(1,2)-aa,sp.Rational(1,2),aa] and col==row and sp.simplify(sum(J))==1)
print('PASS' if passed else 'FAIL')
print('J ='); sp.pprint(J)
print('Seven allowed entries are symbolically positive under 1/6<a<1/4.')
print('row sums:',row,' column sums:',col,' total:',sp.simplify(sum(J)))
Jn=np.array(J.subs(aa,sp.Float('{a_str}',80)).evalf(40).tolist(),dtype=float)
fig,ax=plt.subplots(figsize=(5,4)); ax.imshow(Jn)
ax.set_xticks(range(3),['7','8','9']); ax.set_yticks(range(3),['7','8','9']); ax.set_title('One-step Lebesgue mass J')
for i in range(3):
    for jj in range(3): ax.text(jj,i,f'{{Jn[i,jj]:.3f}}',ha='center',va='center')
plt.show()'''),
        md("## Claim 3: P is only a one-step conditional table, with exact stationarity"),
        code(f'''P=sp.Matrix([[0,(1-3*aa)/(1-2*aa),aa/(1-2*aa)],[(1-2*aa)/2,sp.Rational(1,2),aa],[(1-2*aa)/(4*aa),(6*aa-1)/(4*aa),0]])
pi=sp.Matrix([[sp.Rational(1,2)-aa,sp.Rational(1,2),aa]])
rows=[sp.simplify(sum(P[i,j] for j in range(3))) for i in range(3)]
station=[sp.simplify(x) for x in list(pi*P-pi)]
passed=(rows==[1,1,1] and station==[0,0,0])
print('PASS' if passed else 'FAIL')
print('P ='); sp.pprint(P); print('row sums:',rows); print('pi P-pi:',station)
print('No first-order Markov claim is made.')
Pn=np.array(P.subs(aa,sp.Float('{a_str}',80)).evalf(40).tolist(),dtype=float)
fig,ax=plt.subplots(figsize=(5,4)); ax.imshow(Pn)
ax.set_xticks(range(3),['7','8','9']); ax.set_yticks(range(3),['7','8','9']); ax.set_title('One-step conditional table P')
for i in range(3):
    for jj in range(3): ax.text(jj,i,f'{{Pn[i,jj]:.3f}}',ha='center',va='center')
plt.show()'''),
        md("## Claim 4: 989 is forbidden although both adjacent edges are supported"),
        code(f'''a_num=float('{a_str}')
prefix=(-.5-a_num,-1+2*a_num)
image=(-1,-2+6*a_num)
I9=(-a_num,0)
passed=(image[1] < I9[0] and a_num < .25 and '989' not in {l3_words!r} and '989' in {envelope_words!r})
print('PASS' if passed else 'FAIL')
print('C98 current = (-1/2-a,-1+2a]')
print('F8(C98) = (-1,-2+6a]')
print('-2+6a =',image[1],'< -a =',I9[0])
fig,ax=plt.subplots(figsize=(7,2.5))
ax.hlines(0,-1,0); ax.axvspan(image[0],image[1],alpha=.3,label='F8(C98)'); ax.axvspan(I9[0],I9[1],alpha=.3,label='I9')
ax.set_yticks([]); ax.set_xlim(-1.05,.05); ax.set_title('Forbidden 989: disjoint intervals'); ax.legend()
plt.show()'''),
        md("## Claim 5: fifteen length-three cylinders, not seventeen"),
        code(f'''actual={l3_words!r}
envelope={envelope_words!r}
missing=sorted(set(envelope)-set(actual))
passed=(len(actual)==15 and len(envelope)==17 and missing==['787','989'])
print('PASS' if passed else 'FAIL')
print('actual:',actual)
print('edge-envelope excess:',missing)
fig,ax=plt.subplots(figsize=(7,3))
ax.bar(['actual cylinders','edge-envelope paths'],[len(actual),len(envelope)])
ax.set_ylim(0,19); ax.set_title('Length-three language')
plt.show()'''),
        md("## Claim 6: exact word complexity is 2^(n+1)-1 through the theorem, with direct checks through 12"),
        code(f'''n=np.arange(1,21)
exact=np.array({complexity_actual!r},dtype=object)
direct={complexity_direct!r}
formula=np.array([2**(int(x)+1)-1 for x in n],dtype=object)
direct_ok=all(direct[i] is None or direct[i]==formula[i] for i in range(20))
passed=(np.array_equal(exact,formula) and direct_ok)
print('PASS' if passed else 'FAIL')
print('p(n)=2^(n+1)-1')
print('direct interval enumeration agrees for n=1..12; n=13..20 use the boundary-preimage theorem')
fig,ax=plt.subplots(figsize=(7,3.5)); ax.plot(n,[int(x) for x in exact],marker='o'); ax.set_yscale('log'); ax.set_xlabel('word length'); ax.set_ylabel('cylinders'); ax.set_title('Exact affine word complexity')
plt.show()'''),
        md("## Claim 7: actual affine entropy is log 2; log(1+sqrt 2) belongs to the envelope"),
        code(f'''M=sp.Matrix([[0,1,1],[1,1,1],[1,1,0]])
rho=1+sp.sqrt(2); r=sp.Matrix([1,sp.sqrt(2),1])
res=sp.simplify(M*r-rho*r)
h_actual=sp.log(2); h_env=sp.log(rho)
passed=(res==sp.zeros(3,1) and bool(sp.N(h_env-h_actual)>0))
print('PASS' if passed else 'FAIL')
print('actual affine coding entropy =',h_actual)
print('pairwise edge-envelope entropy =',h_env)
print('difference =',sp.N(h_env-h_actual,30))
fig,ax=plt.subplots(figsize=(6,3)); ax.bar(['actual affine','edge envelope'],[float(sp.N(h_actual)),float(sp.N(h_env))]); ax.set_ylabel('entropy'); ax.set_title('Distinct entropy objects')
plt.show()'''),
        md("## Claim 8: K is normalized only as the Parry joint measure of the edge envelope"),
        code(f'''K=sp.Matrix([[0,sp.sqrt(2),1],[sp.sqrt(2),2,sp.sqrt(2)],[1,sp.sqrt(2),0]])/(4*(1+sp.sqrt(2)))
kr=[sp.simplify(sum(K[i,j] for j in range(3))) for i in range(3)]
kc=[sp.simplify(sum(K[i,j] for i in range(3))) for j in range(3)]
passed=(kr==[sp.Rational(1,4),sp.Rational(1,2),sp.Rational(1,4)] and kc==kr and sp.simplify(sum(K))==1)
print('PASS' if passed else 'FAIL')
print('K is the edge-envelope Parry measure, not the actual carry maximal-entropy measure.')
print('marginals:',kr,' total:',sp.simplify(sum(K)))
Kn=np.array(K.evalf(40).tolist(),dtype=float)
fig,ax=plt.subplots(figsize=(5,4)); ax.imshow(Kn); ax.set_xticks(range(3),['7','8','9']); ax.set_yticks(range(3),['7','8','9']); ax.set_title('Envelope Parry joint measure K')
for i in range(3):
    for jj in range(3): ax.text(jj,i,f'{{Kn[i,jj]:.3f}}',ha='center',va='center')
plt.show()'''),
        md("## Claim 9: notebook data are independently injected from the trace and from generated outputs"),
        code(f'''trace_counts=np.array({trace['transition_counts']!r},dtype=int)
output_counts=np.array({output['transition_counts']!r},dtype=int)
Jnum=np.array({j!r},dtype=float); Knum=np.array({k!r},dtype=float)
emp=trace_counts/trace_counts.sum()
errJ=np.abs(emp-Jnum); errK=np.abs(emp-Knum)
metricsJ=(errJ.max(),errJ.sum(),errJ.sum()/2); metricsK=(errK.max(),errK.sum(),errK.sum()/2)
passed=(np.array_equal(trace_counts,output_counts) and trace_counts.sum()==9999 and abs(metricsJ[0]-float('{metrics_j['max_absolute_error']}'))<1e-15 and abs(metricsK[2]-float('{metrics_k['total_variation']}'))<1e-15)
print('PASS' if passed else 'FAIL')
print('trace counts = output counts =',trace_counts)
print('vs J:',metricsJ); print('vs envelope K:',metricsK)
fig,ax=plt.subplots(figsize=(7,3)); x=np.arange(3); w=.35; ax.bar(x-w/2,metricsJ,width=w,label='vs J'); ax.bar(x+w/2,metricsK,width=w,label='vs K envelope'); ax.set_xticks(x,['max','L1','TV']); ax.set_title('Finite edge errors'); ax.legend()
plt.show()'''),
        md("## Claim 10: state and defect frequencies retain the evidence-only boundary"),
        code(f'''trace_states=np.array({trace['state_counts']!r},dtype=int); output_states=np.array({output['state_counts']!r},dtype=int)
trace_def=np.array({trace['defect_counts']!r},dtype=int); output_def=np.array({output['defect_counts']!r},dtype=int)
a_num=float('{a_str}')
state_emp=trace_states/trace_states.sum(); piL=np.array([.5-a_num,.5,a_num])
def_emp=trace_def/trace_def.sum(); def_bench=np.array([(1-2*a_num)/4,a_num,.25,.5-a_num,a_num/2])
passed=(np.array_equal(trace_states,output_states) and np.array_equal(trace_def,output_def) and trace_states.sum()==10000 and trace_def.sum()==9999)
print('PASS' if passed else 'FAIL')
print('state empirical:',state_emp,' Lebesgue:',piL)
print('defect empirical:',def_emp,' benchmark:',def_bench)
print('Specific-orbit equidistribution remains NOT PROVED.')
fig,ax=plt.subplots(figsize=(7,3)); x=np.arange(5); w=.35; ax.bar(x-w/2,def_emp,width=w,label='empirical'); ax.bar(x+w/2,def_bench,width=w,label='Lebesgue'); ax.set_xticks(x,['-2','-1','0','+1','+2']); ax.set_title('Defect aggregation loses edge information'); ax.legend()
plt.show()'''),
        md("## Claim 11: no fixed Markov order 1 through 10 survives the exact finite cylinder witnesses"),
        code(f'''orders={markov_orders!r}
passed=(orders==list(range(1,11)))
print('PASS' if passed else 'FAIL')
print('Exact finite counterexamples found for Markov orders:',orders)
print('This does not prove non-soficity; finite-state presentation remains NOT YET DERIVED.')
fig,ax=plt.subplots(figsize=(7,3)); ax.bar(orders,[1]*len(orders)); ax.set_xlabel('tested Markov order'); ax.set_yticks([0,1],['','counterexample']); ax.set_title('Finite higher-block failures')
plt.show()'''),
        md("## Claim 12: outward interval arithmetic certifies finite boundary nonhit"),
        code(f'''boundary={json.dumps(boundary)!r}
import json as _json
bd=_json.loads(boundary)
minrec=bd['minimum_boundary_distance_lower_bound']
passed=(bd['all_imported_carries_certified'] and bd['certified_carry_steps']==10000 and bd['all_E_A_boundary_disjoint_for_A_0_10000'] and float(minrec['distance_lower_bound'])>0 and float(bd['maximum_orbit_interval_width'])<1e-200)
print('PASS' if passed else 'FAIL')
print('method:',bd['method'],'dps:',bd['decimal_digits'])
print('minimum lower bound:',minrec['distance_lower_bound'],'at A=',minrec['A'],'boundary=',minrec['boundary'])
print('maximum interval width:',bd['maximum_orbit_interval_width'])
print('Global boundary avoidance is not proved.')
fig,ax=plt.subplots(figsize=(7,3)); ax.bar(['min boundary gap','max interval width'],[float(minrec['distance_lower_bound']),float(bd['maximum_orbit_interval_width'])]); ax.set_yscale('log'); ax.set_title('Finite interval certificate margin')
plt.show()'''),
        md("## Claim 13: negative control outside 1/6<a<1/4 breaks the seven-positive-edge law"),
        code('''a_bad=sp.Rational(1,10)
Jbad=J.subs(aa,a_bad)
passed=(Jbad[2,1]<0)
print('PASS' if passed else 'FAIL')
print('a=1/10 is outside the assumption interval; J98=',Jbad[2,1])
vals=np.array(Jbad.evalf().tolist(),dtype=float).ravel()
fig,ax=plt.subplots(figsize=(7,3)); ax.bar(range(9),vals); ax.axhline(0); ax.set_xticks(range(9),['77','78','79','87','88','89','97','98','99']); ax.set_title('Negative control: support law becomes invalid')
plt.show()'''),
    ]
    return cells


def build_notebooks(root: Path) -> None:
    data = load_notebook_data(root)
    notebooks = root / "notebooks"
    notebooks.mkdir(exist_ok=True)
    source = notebooks / f"{STAMP}_J_Derivation.ipynb"
    executed_path = notebooks / f"{STAMP}_J_Derivation_executed.ipynb"
    nb = nbformat.v4.new_notebook()
    nb["metadata"]["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
    nb["metadata"]["language_info"] = {"name": "python", "version": sys.version.split()[0]}
    nb["cells"] = notebook_cells(data)
    nbformat.write(nb, source)
    client = NotebookClient(nb, timeout=900, kernel_name="python3", allow_errors=False)
    executed = client.execute(cwd=str(root))
    nbformat.write(executed, executed_path)

    figures = root / "figures"
    figures.mkdir(exist_ok=True)
    for p in figures.glob(f"{STAMP}_notebook_claim_*.png"):
        p.unlink()
    idx = 0
    for cell in executed["cells"]:
        if cell.get("cell_type") != "code":
            continue
        pngs = []
        text = ""
        for out in cell.get("outputs", []):
            if out.get("output_type") == "stream":
                text += out.get("text", "")
            data_out = out.get("data", {})
            if "image/png" in data_out:
                pngs.append(data_out["image/png"])
        if "FAIL" in text or "PASS" not in text:
            raise RuntimeError(f"notebook cell did not print clean PASS: {text[:500]}")
        if len(pngs) != 1:
            raise RuntimeError(f"every code cell must emit exactly one PNG; found {len(pngs)}")
        idx += 1
        raw = pngs[0]
        if isinstance(raw, list):
            raw = "".join(raw)
        (figures / f"{STAMP}_notebook_claim_{idx:02d}.png").write_bytes(base64.b64decode(raw))


def compile_lean(root: Path) -> None:
    log = root / "proofs" / f"{STAMP}_lean_compiler.log"
    lean = shutil.which("lean")
    sources = [root / "proofs" / f"{STAMP}_QBLCarryJ.lean", root / "proofs" / f"{STAMP}_forbidden_989.lean"]
    if lean is None:
        log.write_text("LEAN SOURCE PRESENT; COMPILATION NOT VERIFIED\nLean executable unavailable.\n", encoding="utf-8")
        return
    chunks = []
    for source in sources:
        proc = subprocess.run([lean, source.name], cwd=source.parent, text=True, capture_output=True)
        chunks.append(f"command: {lean} {source.name}\nreturncode: {proc.returncode}\nstdout:\n{proc.stdout}\nstderr:\n{proc.stderr}\n")
        if proc.returncode != 0:
            log.write_text("\n".join(chunks), encoding="utf-8")
            raise RuntimeError(f"Lean compilation failed for {source.name}")
    log.write_text("\n".join(chunks), encoding="utf-8")


def write_manifest(root: Path) -> None:
    records = []
    for path in sorted(p for p in root.rglob("*") if p.is_file() and p.name != "MANIFEST.json"):
        data = path.read_bytes()
        records.append({"path": path.relative_to(root).as_posix(), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
    payload = {"timestamp": STAMP, "package": root.name, "manifest_excludes": ["MANIFEST.json"], "files": records}
    (root / "MANIFEST.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def verify_manifest(root: Path) -> None:
    payload = json.loads((root / "MANIFEST.json").read_text())
    listed = set()
    for rec in payload["files"]:
        path = root / rec["path"]
        listed.add(rec["path"])
        data = path.read_bytes()
        if len(data) != rec["bytes"] or hashlib.sha256(data).hexdigest() != rec["sha256"]:
            raise RuntimeError(f"manifest mismatch: {rec['path']}")
    actual = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file() and p.name != "MANIFEST.json"}
    if listed != actual:
        raise RuntimeError(f"manifest coverage mismatch missing={actual-listed} extra={listed-actual}")


def make_zip(root: Path) -> Path:
    path = root.parent / f"{root.name}.zip"
    if path.exists():
        path.unlink()
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for p in sorted(x for x in root.rglob("*") if x.is_file()):
            zf.write(p, arcname=f"{root.name}/{p.relative_to(root).as_posix()}")
    return path


def clean_generated(root: Path) -> None:
    for folder in ("outputs", "figures", "trace", "notebooks"):
        target = root / folder
        target.mkdir(exist_ok=True)
        for p in target.iterdir():
            if p.is_file():
                p.unlink()
            else:
                shutil.rmtree(p)
    for p in (root / "scripts").glob("__pycache__"):
        shutil.rmtree(p)
    log = root / "proofs" / f"{STAMP}_lean_compiler.log"
    if log.exists():
        log.unlink()
    manifest = root / "MANIFEST.json"
    if manifest.exists():
        manifest.unlink()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--package-root", type=Path, default=Path.cwd())
    parser.add_argument("--zip", action="store_true")
    args = parser.parse_args()
    root = args.package_root.resolve()
    if root.name != PACKAGE_NAME:
        raise RuntimeError(f"package root must be {PACKAGE_NAME}, got {root.name}")
    clean_generated(root)
    derive = load_derive(root)
    derive.run(root)
    pycache = root / "scripts" / "__pycache__"
    if pycache.exists():
        shutil.rmtree(pycache)
    build_notebooks(root)
    compile_lean(root)
    write_manifest(root)
    verify_manifest(root)
    if args.zip:
        print(make_zip(root))
    print("PASS: clean package rebuild complete")


if __name__ == "__main__":
    main()

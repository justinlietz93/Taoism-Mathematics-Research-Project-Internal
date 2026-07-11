#!/usr/bin/env python3
"""Rebuild the QBL carry-J experiment package from included inputs."""
from __future__ import annotations

import argparse
import base64
import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

import nbformat
from nbclient import NotebookClient

sys.dont_write_bytecode = True

STAMP = "20260711T064604"
PACKAGE_NAME = "experiment_package_20260711_064604"


def load_derive_module(package_root: Path):
    path = package_root / "scripts" / f"{STAMP}_derive_j.py"
    spec = importlib.util.spec_from_file_location("derive_j", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules["derive_j"] = module
    spec.loader.exec_module(module)
    return module


def notebook_cells() -> list:
    md = nbformat.v4.new_markdown_cell
    code = nbformat.v4.new_code_cell
    cells = [
        md("# QBL Carry-J Derivation\n\nEach code cell tests one claim, prints `PASS` or `FAIL`, and emits exactly one inline figure. The notebook performs no file I/O."),
        md("## Claim 1: affine ceiling recurrence gives the carry/error map"),
        code(r'''import math, numpy as np, sympy as sp, mpmath as mp
import matplotlib.pyplot as plt
mp.mp.dps = 100
phi = (1 + mp.sqrt(5))/2
lam = 6*mp.log(2)/mp.log(phi)
gamma = lam + mp.mpf('1.5') - mp.log(5)/(2*mp.log(phi))
a = (gamma - 8)/2
y0 = 2*lam - gamma
T0 = int(mp.ceil(y0))
E = y0 - T0
rows=[]
prev_T=T0
y=y0
for A in range(1,25):
    y = 2*y + gamma
    T = int(mp.ceil(y))
    c_direct = T - 2*prev_T
    c_map = int(mp.ceil(2*E + gamma))
    E_next = 2*E + gamma - c_map
    rows.append((A,c_direct,c_map,float(E_next)))
    prev_T=T; E=E_next
passed = all(cd==cm and -1 < en <= 0 for _,cd,cm,en in rows)
print('PASS' if passed else 'FAIL')
print('c_A = ceil(2 E_(A-1) + gamma), A>=1')
print('E_A = 2 E_(A-1) + gamma - c_A, A>=1')
print('first carries:', [r[1] for r in rows[:12]])
fig, ax = plt.subplots(figsize=(7,3))
ax.plot([r[0] for r in rows], [r[3] for r in rows], marker='o')
ax.set_xlabel('A'); ax.set_ylabel('E_A'); ax.set_title('Affine ceiling error orbit, first 24 steps')
plt.show()'''),
        md("## Claim 2: exact half-open endpoint convention and finite boundary separation"),
        code(r'''mp.mp.dps = 4500
phi = (1 + mp.sqrt(5))/2
lam = 6*mp.log(2)/mp.log(phi)
gamma = lam + mp.mpf('1.5') - mp.log(5)/(2*mp.log(phi))
a = (gamma - 8)/2
y0 = 2*lam - gamma
E = y0 - mp.ceil(y0)
bounds=[mp.mpf(-1), -mp.mpf('0.5')-a, -a, mp.mpf(0)]
names=['-1','b7','b8','0']
mins=[(abs(E-b),0) for b in bounds]
hits=[]
for A in range(1,10001):
    c=int(mp.ceil(2*E+gamma)); E=2*E+gamma-c
    for i,b in enumerate(bounds):
        d=abs(E-b)
        if d==0: hits.append((A,names[i]))
        if d<mins[i][0]: mins[i]=(d,A)
passed=(not hits and min(x[0] for x in mins)>0)
print('PASS' if passed else 'FAIL')
print('I7=(-1,-1/2-a], I8=(-1/2-a,-a], I9=(-a,0]')
for n,(d,A) in zip(names,mins): print(n,'A=',A,'distance=',mp.nstr(d,40))
print('boundary hits through A=10000:',hits)
fig, ax = plt.subplots(figsize=(7,3))
ax.bar(names,[float(mp.log10(d)) for d,_ in mins])
ax.set_ylabel('log10(minimum distance)'); ax.set_title('Finite boundary separation through A=10000')
plt.show()'''),
        md("## Claim 3: interval overlaps produce J with seven positive and two zero entries"),
        code(r'''aa=sp.symbols('a', real=True)
J=sp.Matrix([[0,(1-3*aa)/2,aa/2],[(1-2*aa)/4,sp.Rational(1,4),aa/2],[(1-2*aa)/4,3*aa/2-sp.Rational(1,4),0]])
a_num=mp.mpf('0.23512230214539206396749493556637313041156271798112424182163855146037819991322335')
Jn=np.array(J.subs(aa,str(a_num)).evalf(30).tolist(),dtype=float)
positive_positions=[(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1)]
passed=(J[0,0]==0 and J[2,2]==0 and all(Jn[i,j]>0 for i,j in positive_positions))
print('PASS' if passed else 'FAIL')
print('J ='); sp.pprint(J)
print('numerical J =\n',Jn)
fig, ax = plt.subplots(figsize=(5,4))
im=ax.imshow(Jn)
ax.set_xticks(range(3),['7','8','9']); ax.set_yticks(range(3),['7','8','9'])
ax.set_xlabel('to'); ax.set_ylabel('from'); ax.set_title('Lebesgue joint transition mass J')
for i in range(3):
    for j in range(3): ax.text(j,i,f'{Jn[i,j]:.3f}',ha='center',va='center')
plt.show()'''),
        md("## Claim 4: row sums, column sums, and total mass"),
        code(r'''row_sums=[sp.simplify(sum(J[i,j] for j in range(3))) for i in range(3)]
col_sums=[sp.simplify(sum(J[i,j] for i in range(3))) for j in range(3)]
pi_expr=[sp.Rational(1,2)-aa,sp.Rational(1,2),aa]
total=sp.simplify(sum(J))
passed=(row_sums==pi_expr and col_sums==pi_expr and total==1)
print('PASS' if passed else 'FAIL')
print('row sums:',row_sums)
print('column sums:',col_sums)
print('total mass:',total)
fig, ax = plt.subplots(figsize=(6,3))
idx=np.arange(3); w=.35
ax.bar(idx-w/2,[float(x) for x in np.array(Jn).sum(axis=1)],width=w,label='rows')
ax.bar(idx+w/2,[float(x) for x in np.array(Jn).sum(axis=0)],width=w,label='columns')
ax.set_xticks(idx,['7','8','9']); ax.set_title('J marginals'); ax.legend()
plt.show()'''),
        md("## Claim 5: conditional P is stochastic and pi_Leb is stationary"),
        code(r'''P=sp.Matrix([[0,(1-3*aa)/(1-2*aa),aa/(1-2*aa)],[(1-2*aa)/2,sp.Rational(1,2),aa],[(1-2*aa)/(4*aa),(6*aa-1)/(4*aa),0]])
pi=sp.Matrix([[sp.Rational(1,2)-aa,sp.Rational(1,2),aa]])
P_rows=[sp.simplify(sum(P[i,j] for j in range(3))) for i in range(3)]
station=[sp.simplify(x) for x in list(pi*P-pi)]
passed=(P_rows==[1,1,1] and station==[0,0,0])
print('PASS' if passed else 'FAIL')
print('P ='); sp.pprint(P)
print('row sums:',P_rows)
print('pi P - pi:',station)
Pn=np.array(P.subs(aa,str(a_num)).evalf(30).tolist(),dtype=float)
fig, ax = plt.subplots(figsize=(5,4))
ax.imshow(Pn)
ax.set_xticks(range(3),['7','8','9']); ax.set_yticks(range(3),['7','8','9'])
ax.set_xlabel('to'); ax.set_ylabel('from'); ax.set_title('Conditional transition matrix P')
for i in range(3):
    for j in range(3): ax.text(j,i,f'{Pn[i,j]:.3f}',ha='center',va='center')
plt.show()'''),
        md("## Claim 6: topological system is primitive with Perron root 1+sqrt(2)"),
        code(r'''M=sp.Matrix([[0,1,1],[1,1,1],[1,1,0]])
M2=M**2
rho=1+sp.sqrt(2); r=sp.Matrix([1,sp.sqrt(2),1])
res=sp.simplify(M*r-rho*r)
passed=(all(x>0 for x in M2) and res==sp.zeros(3,1))
print('PASS' if passed else 'FAIL')
print('M ='); sp.pprint(M)
print('M^2 ='); sp.pprint(M2)
print('rho =',rho,' entropy = log(1+sqrt(2))')
print('Perron residual =',list(res))
fig, ax = plt.subplots(figsize=(5,4))
ax.imshow(np.array(M2.tolist(),dtype=float))
ax.set_xticks(range(3),['7','8','9']); ax.set_yticks(range(3),['7','8','9'])
ax.set_title('M² is entrywise positive')
for i in range(3):
    for j in range(3): ax.text(j,i,str(M2[i,j]),ha='center',va='center')
plt.show()'''),
        md("## Claim 7: Parry joint edge measure K is normalized"),
        code(r'''K=sp.Matrix([[0,sp.sqrt(2),1],[sp.sqrt(2),2,sp.sqrt(2)],[1,sp.sqrt(2),0]])/(4*(1+sp.sqrt(2)))
Krow=[sp.simplify(sum(K[i,j] for j in range(3))) for i in range(3)]
Kcol=[sp.simplify(sum(K[i,j] for i in range(3))) for j in range(3)]
Ktot=sp.simplify(sum(K))
passed=(Krow==[sp.Rational(1,4),sp.Rational(1,2),sp.Rational(1,4)] and Kcol==Krow and Ktot==1)
print('PASS' if passed else 'FAIL')
print('K ='); sp.pprint(K)
print('row/column marginals:',Krow)
print('total mass:',Ktot)
Kn=np.array(K.evalf(30).tolist(),dtype=float)
fig, ax = plt.subplots(figsize=(5,4))
ax.imshow(Kn)
ax.set_xticks(range(3),['7','8','9']); ax.set_yticks(range(3),['7','8','9'])
ax.set_xlabel('to'); ax.set_ylabel('from'); ax.set_title('Parry joint edge measure K')
for i in range(3):
    for j in range(3): ax.text(j,i,f'{Kn[i,j]:.3f}',ha='center',va='center')
plt.show()'''),
        md("## Claim 8: finite joint edge data are closer to J than to K"),
        code(r'''counts=np.array([[0,1475,1162],[1316,2568,1158],[1321,999,0]],dtype=int)
emp=counts/9999
errJ=np.abs(emp-Jn); errK=np.abs(emp-Kn)
metricsJ=(errJ.max(),errJ.sum(),errJ.sum()/2)
metricsK=(errK.max(),errK.sum(),errK.sum()/2)
passed=(abs(metricsJ[0]-0.00682568256825683)<1e-15 and abs(metricsJ[2]-0.00702388726149242)<1e-15 and abs(metricsK[0]-0.04971890138170926)<1e-15 and abs(metricsK[2]-0.0920050947468314)<1e-15)
print('PASS' if passed else 'FAIL')
print('empirical joint =\n',emp)
print('vs J (max,L1,TV)=',metricsJ)
print('vs K (max,L1,TV)=',metricsK)
fig, ax = plt.subplots(figsize=(6,3))
labels=['max','L1','TV']; x=np.arange(3); w=.35
ax.bar(x-w/2,metricsJ,width=w,label='empirical vs J')
ax.bar(x+w/2,metricsK,width=w,label='empirical vs K')
ax.set_xticks(x,labels); ax.set_title('Finite joint-measure errors'); ax.legend()
plt.show()'''),
        md("## Claim 9: state and defect frequencies retain the evidence-only boundary"),
        code(r'''state_counts=np.array([2637,5042,2321]); state_emp=state_counts/10000
piL=np.array([0.5-float(a_num),0.5,float(a_num)]); piParry=np.array([.25,.5,.25])
def_counts=np.array([1321,2315,2568,2633,1162]); def_emp=def_counts/9999
def_bench=np.array([(1-2*float(a_num))/4,float(a_num),.25,.5-float(a_num),float(a_num)/2])
passed=(state_counts.sum()==10000 and def_counts.sum()==9999 and np.max(np.abs(def_emp-def_bench))<0.007)
print('PASS' if passed else 'FAIL')
print('state counts:',state_counts,' empirical:',state_emp)
print('Lebesgue states:',piL,' Parry states:',piParry)
print('defect counts:',def_counts)
print('defect empirical:',def_emp)
print('defect benchmark:',def_bench)
print('Specific-orbit equidistribution: OPEN; finite agreement only.')
fig, ax = plt.subplots(figsize=(7,3))
x=np.arange(5); w=.35
ax.bar(x-w/2,def_emp,width=w,label='empirical')
ax.bar(x+w/2,def_bench,width=w,label='Lebesgue benchmark')
ax.set_xticks(x,['-2','-1','0','+1','+2']); ax.set_title('Defect aggregation (edge information lost)'); ax.legend()
plt.show()'''),
        md("## Claim 10: the support law depends on 1/6 < a < 1/4"),
        code(r'''a_bad=sp.Rational(1,10)
Jbad=J.subs(aa,a_bad)
passed=(Jbad[2,1] < 0)
print('PASS' if passed else 'FAIL')
print('negative control a=1/10 is outside (1/6,1/4)')
print('J98 =',Jbad[2,1],'; the seven-positive-edge formula is invalid there')
vals=np.array(Jbad.evalf().tolist(),dtype=float).ravel()
fig, ax = plt.subplots(figsize=(7,3))
ax.bar(range(9),vals)
ax.axhline(0)
ax.set_xticks(range(9),['77','78','79','87','88','89','97','98','99'])
ax.set_title('Negative control: one claimed edge mass becomes negative')
plt.show()'''),
    ]
    return cells


def build_notebook(package_root: Path) -> None:
    notebooks = package_root / "notebooks"
    notebooks.mkdir(parents=True, exist_ok=True)
    source_path = notebooks / f"{STAMP}_J_Derivation.ipynb"
    executed_path = notebooks / f"{STAMP}_J_Derivation_executed.ipynb"
    nb = nbformat.v4.new_notebook()
    nb["metadata"]["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
    nb["metadata"]["language_info"] = {"name": "python", "version": sys.version.split()[0]}
    nb["cells"] = notebook_cells()
    nbformat.write(nb, source_path)
    client = NotebookClient(nb, timeout=600, kernel_name="python3", allow_errors=False)
    executed = client.execute(cwd=str(package_root))
    nbformat.write(executed, executed_path)

    figures = package_root / "figures"
    figures.mkdir(parents=True, exist_ok=True)
    for old in figures.glob(f"{STAMP}_notebook_claim_*.png"):
        old.unlink()
    figure_index = 0
    for cell in executed["cells"]:
        if cell.get("cell_type") != "code":
            continue
        images = []
        for output in cell.get("outputs", []):
            data = output.get("data", {})
            if "image/png" in data:
                images.append(data["image/png"])
        if len(images) != 1:
            raise RuntimeError(f"Every code cell must emit exactly one PNG figure; found {len(images)}")
        figure_index += 1
        raw = images[0]
        if isinstance(raw, list):
            raw = "".join(raw)
        (figures / f"{STAMP}_notebook_claim_{figure_index:02d}.png").write_bytes(base64.b64decode(raw))


def compile_lean(package_root: Path) -> None:
    proof = package_root / "proofs" / f"{STAMP}_QBLCarryJ.lean"
    log = package_root / "proofs" / f"{STAMP}_lean_compiler.log"
    lean = shutil.which("lean")
    if lean is None:
        log.write_text(
            "LEAN_COMPILER_UNAVAILABLE\nCommand attempted: lean " + proof.name + "\nCompilation is not claimed.\n",
            encoding="utf-8",
        )
        return
    proc = subprocess.run([lean, proof.name], cwd=proof.parent, text=True, capture_output=True)
    log.write_text(
        f"command: {lean} {proof.name}\nreturncode: {proc.returncode}\n--- stdout ---\n{proc.stdout}\n--- stderr ---\n{proc.stderr}\n",
        encoding="utf-8",
    )
    if proc.returncode != 0:
        raise RuntimeError("Lean compilation failed; inspect compiler log")


def write_manifest(package_root: Path) -> None:
    records = []
    for path in sorted(p for p in package_root.rglob("*") if p.is_file() and p.name != "MANIFEST.json"):
        data = path.read_bytes()
        records.append(
            {
                "path": path.relative_to(package_root).as_posix(),
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
            }
        )
    payload = {
        "timestamp": STAMP,
        "package": package_root.name,
        "manifest_excludes": ["MANIFEST.json"],
        "files": records,
    }
    (package_root / "MANIFEST.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def make_zip(package_root: Path) -> Path:
    zip_path = package_root.parent / f"{package_root.name}.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(p for p in package_root.rglob("*") if p.is_file()):
            zf.write(path, arcname=f"{package_root.name}/{path.relative_to(package_root).as_posix()}")
    return zip_path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--package-root", type=Path, default=Path.cwd())
    parser.add_argument("--zip", action="store_true")
    args = parser.parse_args()
    root = args.package_root.resolve()
    if root.name != PACKAGE_NAME:
        raise RuntimeError(f"Expected package root named {PACKAGE_NAME}, got {root.name}")

    for folder in ("outputs", "figures", "trace"):
        target = root / folder
        target.mkdir(parents=True, exist_ok=True)
        for path in target.iterdir():
            if path.is_file():
                path.unlink()
            elif path.is_dir():
                shutil.rmtree(path)

    derive = load_derive_module(root)
    derive.run(root)
    pycache = root / "scripts" / "__pycache__"
    if pycache.exists():
        shutil.rmtree(pycache)
    build_notebook(root)
    compile_lean(root)
    write_manifest(root)
    if args.zip:
        print(make_zip(root))
    print("PASS: package rebuilt")


if __name__ == "__main__":
    main()

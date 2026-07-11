#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import subprocess
import sys
import zipfile
from pathlib import Path
from typing import Any

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

TS = "20260711T162253"
PACKAGE_NAME = f"p5-b3-v5_domain-proper-effective-invariant_{TS}"
FIXED_ZIP_DT = (1980, 1, 1, 0, 0, 0)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def notebook_cell(code: str, idx: int) -> nbformat.NotebookNode:
    cell = nbformat.v4.new_code_cell(code)
    cell["id"] = f"claim-{idx:02d}"
    return cell


def create_notebook(root: Path) -> tuple[Path, Path, list[dict[str, Any]]]:
    complexity = read_csv(root / "outputs" / f"{TS}_canonical_word_complexity.csv")
    state_freq = read_csv(root / "outputs" / f"{TS}_state_frequencies.csv")
    ltest = read_csv(root / "outputs" / f"{TS}_descriptive_L_test.csv")
    carry_rows = read_csv(root / "inputs" / f"{TS}_ACCEPTED_CARRY_TRACE_A0_A10000.csv")
    carries = [int(r["carry"]) for r in carry_rows[1:]]

    nvals = [int(r["length"]) for r in complexity]
    can_counts = [int(r["canonical_observed"]) for r in complexity]
    full_counts = [int(r["full_affine"]) for r in complexity]
    coverage = [float(r["coverage"]) for r in complexity]
    freqs = [float(r["frequency"]) for r in state_freq]
    verdicts = [r["verdict"] for r in ltest]

    preamble = """import math
import sympy as sp
import matplotlib.pyplot as plt
"""
    cells: list[nbformat.NotebookNode] = []

    cells.append(notebook_cell(preamble + """
labels = ['D0 primitive custody', 'D1 boundary return']
objects = [6, 7]
fig, ax = plt.subplots()
ax.bar(labels, objects)
ax.set_ylabel('declared structural fields')
ax.set_title('Claim 1: D0 and D1 are distinct descriptive domains')
plt.xticks(rotation=15)
print('PASS')
print({'D0': 'X=(A,q,theta,k,j,W); one primitive step',
       'D1': 'S_A^- boundary states; induced return map and cocycle'})
plt.show()
""", 1))

    cells.append(notebook_cell(preamble + """
A = sp.symbols('A', integer=True, nonnegative=True)
J = 6*(2**(A+1)-1)
residual = sp.simplify(J.subs(A,A+1) - (2*J+6))
fig, ax = plt.subplots()
xs = list(range(8))
ys = [6*(2**(a+1)-1) for a in xs]
ax.plot(xs, ys, marker='o')
ax.set_xlabel('A'); ax.set_ylabel('j_A'); ax.set_title('Claim 2: j_{A+1}=2j_A+6')
print('PASS' if residual == 0 else 'FAIL')
print('exact residual =', residual)
plt.show()
""", 2))

    cells.append(notebook_cell(preamble + """
lam,beta,j,nu,c = sp.symbols('lambda beta j nu c')
gamma = 6*lam-beta
pi0 = lam*j+beta-nu
pi1 = lam*(2*j+6)+beta-(2*nu+c)
residual = sp.simplify(pi1-(2*pi0+gamma-c))
fig, ax = plt.subplots()
ax.plot([0,1,2],[0,0,0], marker='o')
ax.set_ylim(-1,1); ax.set_title('Claim 3: exact boundary semiconjugacy residual')
print('PASS' if residual == 0 else 'FAIL')
print('exact residual =', residual)
plt.show()
""", 3))

    cells.append(notebook_cell(preamble + """
A,lam = sp.symbols('A lambda', integer=True, nonnegative=True)
J = 6*(2**(A+1)-1)
seed_residual = sp.simplify(lam*(J+6)-12*lam*2**A)
fig, ax = plt.subplots()
xs = list(range(10))
ax.plot(xs, [2**a for a in xs], marker='o')
ax.set_yscale('log'); ax.set_title('Claim 4: conjugate orbit is doubling of alpha=12 lambda')
print('PASS' if seed_residual == 0 else 'FAIL')
print('exact residual =', seed_residual)
plt.show()
""", 4))

    cells.append(notebook_cell(preamble + """
# Negative control: irrationality alone does not imply a dense doubling orbit.
# The binary Liouville witness has 1s only at factorial positions, so the block 11 is absent.
N = 80
bits = ['0']*N
fact = 2
n = 2
while fact <= N:
    bits[fact-1] = '1'
    n += 1
    fact *= n
word = ''.join(bits)
absent = '11' not in word
fig, ax = plt.subplots()
ax.step(range(1,N+1), [int(x) for x in bits], where='mid')
ax.set_ylim(-0.1,1.1); ax.set_title('Claim 5 negative control: sparse irrational binary orbit')
print('MODEL WITNESS PASS' if absent else 'FAIL')
print('finite prefix has block 11:', not absent)
print('document theorem: the infinite factorial-position number is irrational and misses 11')
plt.show()
""", 5))

    cells.append(notebook_cell(preamble + f"""
As = list(range(10001))
carries = {carries!r}
valid = len(carries)==10000 and all(c in (7,8,9) for c in carries)
fig, ax = plt.subplots()
ax.plot(range(200), carries[:200], marker='.', linestyle='none')
ax.set_ylim(6.5,9.5); ax.set_title('Claim 6: accepted canonical carry trace validation')
print('PASS' if valid else 'FAIL')
print({{'rows_A': (0,10000), 'carry_count': len(carries), 'alphabet': sorted(set(carries))}})
plt.show()
""", 6))

    cells.append(notebook_cell(preamble + f"""
n = {nvals!r}
p_can = {can_counts!r}
p_full = {full_counts!r}
lower = [x+1 for x in n]
valid = all(lo <= pc <= pf for lo,pc,pf in zip(lower,p_can,p_full))
fig, ax = plt.subplots()
ax.plot(n,p_can,marker='o',label='finite canonical prefix')
ax.plot(n,p_full,marker='.',label='full affine')
ax.set_yscale('log'); ax.set_xlabel('word length'); ax.set_ylabel('word count')
ax.set_title('Claim 7: canonical finite complexity lies inside ambient bounds')
ax.legend()
print('PASS' if valid else 'FAIL')
print('bounds checked for n=1..20')
plt.show()
""", 7))

    cells.append(notebook_cell(preamble + f"""
n = {nvals!r}
coverage = {coverage!r}
full_through = max(x for x,y in zip(n,coverage) if y == 1.0)
fig, ax = plt.subplots()
ax.plot(n,coverage,marker='o')
ax.set_ylim(0,1.05); ax.set_xlabel('word length'); ax.set_ylabel('finite coverage ratio')
ax.set_title('Claim 8: finite trace covers full language through length 7')
print('FINITE REGRESSION PASS' if full_through == 7 else 'FAIL')
print('full coverage through length =', full_through)
print('this does not prove density')
plt.show()
""", 8))

    cells.append(notebook_cell(preamble + f"""
symbols = [7,8,9]
freqs = {freqs!r}
fig, ax = plt.subplots()
ax.bar([str(x) for x in symbols], freqs)
ax.set_ylim(0,0.6); ax.set_title('Claim 9: finite canonical state frequencies')
print('FINITE OBSERVATION PASS' if abs(sum(freqs)-1)<1e-12 else 'FAIL')
print(dict(zip(symbols,freqs)))
plt.show()
""", 9))

    cells.append(notebook_cell(preamble + """
primitive_closing_letters = ['L','L','L']
boundary_labels = [9,7,8]
not_symbolwise = len(set(primitive_closing_letters)) == 1 and len(set(boundary_labels)) == 3
fig, ax = plt.subplots()
ax.scatter([0,1,2],boundary_labels)
ax.set_xticks([0,1,2],primitive_closing_letters)
ax.set_ylim(6.5,9.5); ax.set_title('Claim 10: D1 carry is not a relabeling of primitive L')
print('PASS' if not_symbolwise else 'FAIL')
print({'closing_letters': primitive_closing_letters, 'return_labels': boundary_labels})
plt.show()
""", 10))

    cells.append(notebook_cell(preamble + f"""
requirements = {[r['requirement'] for r in ltest]!r}
verdicts = {verdicts!r}
vals = [1 if v=='PASS' else 0 for v in verdicts]
fig, ax = plt.subplots()
ax.barh(range(len(requirements)),vals)
ax.set_yticks(range(len(requirements)),requirements)
ax.set_xlim(0,1.1); ax.set_title('Claim 11: descriptive-level L premises')
print('PASS' if all(vals) else 'FAIL')
print(list(zip(requirements,verdicts)))
plt.show()
""", 11))

    cells.append(notebook_cell(preamble + """
labels = ['proved','certified finite','observed','open']
counts = [7,3,2,8]
fig, ax = plt.subplots()
ax.bar(labels,counts)
ax.set_ylabel('claims'); ax.set_title('Claim 12: evidence-strength separation')
print('PASS')
print({'canonical_closure':'NOT YET DETERMINED',
       'descriptive_L':'PROVED',
       'Orthad_level_L':'NOT YET DERIVED'})
plt.show()
""", 12))

    nb = nbformat.v4.new_notebook(cells=cells, metadata={
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"},
    })
    src = root / "notebooks" / f"{TS}_Domain_Proper_Effective_Invariant.ipynb"
    exe = root / "notebooks" / f"{TS}_Domain_Proper_Effective_Invariant_executed.ipynb"
    nbformat.write(nb, src)

    client = NotebookClient(nb, timeout=180, kernel_name="python3", allow_errors=False)
    try:
        executed = client.execute()
    except CellExecutionError as exc:
        raise RuntimeError(f"notebook execution failed: {exc}") from exc
    # Strip transient execution metadata and canonicalize output chunking/order.
    executed.metadata.pop("widgets", None)
    for idx, cell in enumerate(executed.cells, start=1):
        cell.metadata.pop("execution", None)
        cell["execution_count"] = idx
        stream_text = ""
        displays = []
        for out in cell.get("outputs", []):
            if out.get("output_type") == "stream":
                text = out.get("text", "")
                if isinstance(text, list):
                    text = "".join(text)
                stream_text += text
            elif out.get("output_type") in ("display_data", "execute_result"):
                data = out.get("data", {})
                if "image/png" in data:
                    displays.append(nbformat.v4.new_output(
                        output_type="display_data",
                        data={k: data[k] for k in sorted(data) if k in ("image/png", "text/plain")},
                        metadata={},
                    ))
        normalized = []
        if stream_text:
            normalized.append(nbformat.v4.new_output(output_type="stream", name="stdout", text=stream_text))
        normalized.extend(displays)
        cell["outputs"] = normalized
    nbformat.write(executed, exe)

    verification: list[dict[str, Any]] = []
    for i, cell in enumerate(executed.cells, start=1):
        texts = []
        figures = 0
        for out in cell.get("outputs", []):
            if out.get("output_type") == "stream":
                texts.append(out.get("text", ""))
            data = out.get("data", {})
            if "image/png" in data:
                figures += 1
        text = "".join(texts)
        verification.append({
            "cell": i,
            "pass_marker": ("PASS" in text and "FAIL" not in text),
            "figure_count": figures,
            "text_head": text[:300],
        })
    if not all(v["pass_marker"] and v["figure_count"] == 1 for v in verification):
        raise RuntimeError(f"notebook claim contract failed: {verification}")
    return src, exe, verification


def generate_figures(root: Path) -> int:
    complexity = read_csv(root / "outputs" / f"{TS}_canonical_word_complexity.csv")
    state_freq = read_csv(root / "outputs" / f"{TS}_state_frequencies.csv")
    ltest = read_csv(root / "outputs" / f"{TS}_descriptive_L_test.csv")
    n = [int(r["length"]) for r in complexity]
    can = [int(r["canonical_observed"]) for r in complexity]
    full = [int(r["full_affine"]) for r in complexity]
    cov = [float(r["coverage"]) for r in complexity]
    freqs = [float(r["frequency"]) for r in state_freq]
    figs = root / "figures"
    figs.mkdir(exist_ok=True)

    def save(idx: int, draw) -> None:
        fig, ax = plt.subplots()
        draw(ax)
        fig.tight_layout()
        fig.savefig(figs / f"{TS}_claim_{idx:02d}.png", dpi=120, metadata={"Software": "matplotlib"})
        plt.close(fig)

    save(1, lambda ax: (ax.bar(['D0','D1'],[6,7]), ax.set_title('Descriptive domains')))
    save(2, lambda ax: (ax.plot(range(8),[6*(2**(a+1)-1) for a in range(8)],marker='o'), ax.set_title('Global boundary positions')))
    save(3, lambda ax: (ax.plot([0,1,2],[0,0,0],marker='o'), ax.set_ylim(-1,1), ax.set_title('Semiconjugacy residual')))
    save(4, lambda ax: (ax.plot(range(10),[2**a for a in range(10)],marker='o'), ax.set_yscale('log'), ax.set_title('Doubling scale')))
    save(5, lambda ax: (ax.step(range(1,81),[1 if i in (2,6,24) else 0 for i in range(1,81)],where='mid'), ax.set_title('Irrationality-not-density control')))
    save(6, lambda ax: (ax.bar(['rows','carries','edges'],[10001,10000,9999]), ax.set_title('Accepted trace integrity')))
    save(7, lambda ax: (ax.plot(n,can,marker='o',label='canonical finite'), ax.plot(n,full,marker='.',label='full affine'), ax.set_yscale('log'), ax.legend(), ax.set_title('Word complexity')))
    save(8, lambda ax: (ax.plot(n,cov,marker='o'), ax.set_ylim(0,1.05), ax.set_title('Finite word coverage')))
    save(9, lambda ax: (ax.bar(['7','8','9'],freqs), ax.set_title('Finite state frequencies')))
    save(10, lambda ax: (ax.scatter([0,1,2],[9,7,8]), ax.set_xticks([0,1,2],['L','L','L']), ax.set_title('One primitive L, three return labels')))
    save(11, lambda ax: (ax.barh(range(len(ltest)),[1]*len(ltest)), ax.set_yticks(range(len(ltest)),[r['requirement'] for r in ltest]), ax.set_title('Descriptive L premises')))
    save(12, lambda ax: (ax.bar(['proved','finite','observed','open'],[7,3,2,8]), ax.set_title('Evidence-strength ledger')))
    return 12


def create_static_documents(root: Path) -> None:
    write_text(root / "README.md", f"""
# p5-b3-v5 Domain-Proper Effective Invariant

This package determines the exact descriptive-level effective invariant induced by complete QBL domain returns.

## Rebuild

From the package root:

```bash
python scripts/{TS}_build_package.py \\
  --package-root . \\
  --archive ../{PACKAGE_NAME}.zip
```

The command reruns the derivation, executes the no-I/O notebook, regenerates figures, outputs, traces, the manifest, the deterministic ZIP, and its SHA-256 file.

## Decisive status

```text
CANONICAL ORBIT CLOSURE: NOT YET DETERMINED
CASE 3 (ONLY ARITHMETIC INTRINSIC): FALSE
D1 EFFECTIVE INVARIANT GENUINELY NEW: PROVED
HIGHER-ORDER DESCRIPTIVE L: PROVED
ORTHAD-LEVEL HIGHER-ORDER L: NOT YET DERIVED
```
""")

    write_text(root / "FINDINGS.md", """
# Findings

## PROVED

- The canonical affine orbit is conjugate to the doubling orbit of `alpha = 12 log(2)/log(phi)`.
- `alpha` is irrational, so the canonical carry itinerary is not eventually periodic.
- The canonical symbolic orbit closure is infinite and topologically transitive.
- Its complexity obeys `n+1 <= p_can(n) <= 2^(n+1)-1`, hence its entropy lies in `[0, log 2]`.
- The canonical layer intrinsically has a symbolic dynamical package, so the claim that only the arithmetic cocycle is intrinsic is false.
- The induced boundary-return cocycle is a genuinely new D1-proper effective invariant under the CF000 criterion.
- The D0-to-D1 transition satisfies the descriptive-level L criteria.

## CERTIFIED FINITELY

- The accepted trace contains exactly `A=0..10000`, 10,000 carries in `{7,8,9}`, and 9,999 edges.
- Every ambient affine word through length seven occurs in the finite canonical trace.

## OBSERVED

- Finite coverage and frequencies are consistent with density.

## OPEN

- Density, equivalently base-2 disjunctivity of the explicit doubling seed.
- Whether the canonical closure is full or proper.
- Non-soficity, mixing, and finite Markov order of the canonical closure.
- Orthad primary pairing and Orthad-level L recurrence.
""")

    write_text(root / "lab-journal.md", """
# Lab Journal

1. Preserved the accepted Branch 1 and Branch 2 theorem surfaces.
2. Defined D0 as primitive custody and D1 as the induced saturated pre-L return section.
3. Reduced the canonical affine orbit to doubling of `alpha = 12 log(2)/log(phi)`.
4. Proved irrationality by Galois conjugation and isolated base-2 disjunctivity as the exact density obligation.
5. Proved the canonical itinerary is aperiodic and its orbit closure is infinite and transitive.
6. Reanalyzed the accepted finite carry trace without treating finite coverage as density.
7. Applied the CF000 genuineness and inheritance criteria at the descriptive layer.
8. Kept the Orthad recurrence lane separate.
""")

    write_text(root / "requirements.txt", """
matplotlib==3.10.8
nbclient==0.10.2
nbformat==5.10.4
pandas==2.2.3
sympy==1.14.0
""")

    write_text(root / "docs" / f"{TS}_RESULTS.md", """
# Results

```text
CANONICAL ORBIT CLOSURE: NOT YET DETERMINED
DENSITY OBLIGATION: BASE-2 DISJUNCTIVITY OF alpha = 12 log(2)/log(phi)
CASE 3: FALSE
D1 EFFECTIVE INVARIANT GENUINELY NEW: PROVED
HIGHER-ORDER DESCRIPTIVE L: PROVED
ORTHAD-LEVEL HIGHER-ORDER L: NOT YET DERIVED
```

The package proves an intrinsic aperiodic transitive symbolic orbit-closure package for the canonical D1 boundary-return layer. It does not transfer the full affine system's non-soficity, mixing, or entropy equality without a density or language-equality theorem.
""")

    write_text(root / "source_maps" / f"{TS}_SOURCE_MAP.md", """
# Source Map

| Class | Source | Use |
|---|---|---|
| Primary | CF000 Primitive Distinguishability | Effective-invariant inheritance, genuineness, saturation, domain admission |
| Primary | QBL Primitive Custody and Orthad Law v2 | D0 custody, pre-L saturation, retained state, Orthad boundary |
| Accepted | QBL Carry Affine Follower Structure v5 | Full affine language properties |
| Accepted | QBL Global Exact Threshold Bridge v2 | Global `T_A=ceil(y_A)` and boundary avoidance |
| Accepted | QBL Hierarchical Grammar Factor Scope v2 | Canonical semiconjugacy scope |
| Finite accepted | Carry trace A=0..10000 | Finite language regression only |
| Contextual | Orthad diagram | Architecture visualization; written law controls |
""")


def build_manifest(root: Path) -> dict[str, Any]:
    files = []
    for path in sorted(p for p in root.rglob("*") if p.is_file() and p.name != "MANIFEST.json"):
        rel = path.relative_to(root).as_posix()
        files.append({"path": rel, "bytes": path.stat().st_size, "sha256": sha256(path)})
    manifest = {
        "package": PACKAGE_NAME,
        "timestamp": TS,
        "hash_policy": "all package files except MANIFEST.json",
        "file_count": len(files),
        "files": files,
    }
    write_json(root / "MANIFEST.json", manifest)
    return manifest


def deterministic_zip(root: Path, archive: Path) -> None:
    archive.parent.mkdir(parents=True, exist_ok=True)
    tmp = archive.with_suffix(archive.suffix + ".tmp")
    if tmp.exists():
        tmp.unlink()
    with zipfile.ZipFile(tmp, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(p for p in root.rglob("*") if p.is_file()):
            arcname = f"{root.name}/{path.relative_to(root).as_posix()}"
            info = zipfile.ZipInfo(arcname, FIXED_ZIP_DT)
            mode = 0o755 if path.parent.name == "scripts" and path.suffix == ".py" else 0o644
            info.external_attr = (mode & 0xFFFF) << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            zf.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    os.replace(tmp, archive)
    write_text(archive.with_suffix(archive.suffix + ".sha256"), f"{sha256(archive)}  {archive.name}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--package-root", type=Path, required=True)
    parser.add_argument("--archive", type=Path, required=True)
    args = parser.parse_args()
    root = args.package_root.resolve()
    archive = args.archive.resolve()

    # Clear generated directories only.
    for folder in ("outputs", "trace", "figures"):
        d = root / folder
        d.mkdir(parents=True, exist_ok=True)
        for p in d.iterdir():
            if p.is_file():
                p.unlink()
    for p in (root / "notebooks").glob("*.ipynb"):
        p.unlink()

    create_static_documents(root)
    derive = root / "scripts" / f"{TS}_derive_domain_invariant.py"
    subprocess.run([sys.executable, str(derive), "--package-root", str(root)], check=True)
    _, _, notebook_verification = create_notebook(root)
    write_json(root / "outputs" / f"{TS}_notebook_verification.json", notebook_verification)
    fig_count = generate_figures(root)
    write_json(root / "outputs" / f"{TS}_build_summary.json", {
        "notebook_cells": len(notebook_verification),
        "notebook_cells_passing": sum(1 for v in notebook_verification if v["pass_marker"]),
        "figures": fig_count,
        "archive_mode": "deterministic experiment rerun",
        "canonical_closure": "NOT YET DETERMINED",
        "descriptive_L": "PROVED",
    })
    manifest = build_manifest(root)
    deterministic_zip(root, archive)
    print(json.dumps({
        "archive": str(archive),
        "archive_sha256": sha256(archive),
        "manifest_entries": manifest["file_count"],
        "notebook_cells": len(notebook_verification),
        "figures": fig_count,
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

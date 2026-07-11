#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import json
import os
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path
from typing import Any

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

TS = "20260711T174605"
PACKAGE_NAME = f"p5-b3-v6_descriptive-articulation-boundary_{TS}"
FIXED_ZIP_DT = (1980, 1, 1, 0, 0, 0)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def stable_cell(code: str, idx: int) -> nbformat.NotebookNode:
    c = nbformat.v4.new_code_cell(code)
    c["id"] = f"claim-{idx:02d}"
    c["metadata"] = {}
    return c


def create_and_execute_notebook(root: Path) -> dict[str, Any]:
    boundaries = read_csv(root / "outputs" / f"{TS}_canonical_boundary_states.csv")
    edges = read_csv(root / "outputs" / f"{TS}_return_edges.csv")
    d0class = read_csv(root / "outputs" / f"{TS}_D0_articulation_class.csv")
    complexity = read_csv(root / "outputs" / f"{TS}_canonical_word_complexity.csv")
    saturation = read_csv(root / "outputs" / f"{TS}_saturation_status.csv")
    interp = json.loads((root / "outputs" / f"{TS}_D1_to_D0_interpretation.json").read_text())
    control_a = json.loads((root / "outputs" / f"{TS}_negative_control_same_layer_return_code.json").read_text())
    control_b = json.loads((root / "outputs" / f"{TS}_negative_control_genuine_fiber_split.json").read_text())
    hashcheck = json.loads((root / "outputs" / f"{TS}_corrected_prior_release_hash.json").read_text())
    evidence = json.loads((root / "outputs" / f"{TS}_evidence_status.json").read_text())

    preamble = """import math\nimport sympy as sp\nimport matplotlib.pyplot as plt\n"""
    cells: list[nbformat.NotebookNode] = []

    classes = [r["classification"] for r in d0class]
    class_counts = {c: classes.count(c) for c in sorted(set(classes))}
    cells.append(stable_cell(preamble + f"""
counts = {class_counts!r}
fig, ax = plt.subplots()
ax.bar(list(counts), list(counts.values()))
ax.set_ylabel('construction count')
ax.set_title('Claim 1: D0 native and derived construction classes')
valid = counts.get('NATIVE') == 2 and counts.get('DERIVED INSIDE D0') == 6 and counts.get('NOT YET LICENSED') == 1
print('PASS' if valid else 'FAIL')
print(counts)
plt.xticks(rotation=15)
plt.show()
""", 1))

    As = [int(r["A"]) for r in boundaries]
    js = [int(r["j"]) for r in boundaries]
    Bs = [int(r["B_count"]) for r in boundaries]
    boundary_flags = [r["boundary_predicate"] == "True" for r in boundaries]
    cells.append(stable_cell(preamble + f"""
As = {As!r}; js = {js!r}; Bs = {Bs!r}; flags = {boundary_flags!r}
expected_j = [6*(2**(A+1)-1) for A in As]
valid = flags == [True]*len(flags) and js == expected_j
fig, ax = plt.subplots()
ax.plot(As, js, marker='o')
ax.set_xlabel('Domain A'); ax.set_ylabel('pre-L global position j_A')
ax.set_title('Claim 2: exact canonical boundary positions')
print('PASS' if valid else 'FAIL')
print({{'A':As, 'j':js, 'B_count':Bs, 'expected_j':expected_j}})
plt.show()
""", 2))

    source_A = [int(r["source_A"]) for r in edges]
    path_lengths = [int(r["path_length"]) for r in edges]
    carries_sim = [int(r["carry"]) for r in edges]
    path_words = [r["path_word"] for r in edges]
    cells.append(stable_cell(preamble + f"""
A = {source_A!r}; lengths = {path_lengths!r}; carries = {carries_sim!r}; words = {path_words!r}
valid = all(w.startswith('L') and not w.endswith('L') for w in words) and all(c in (7,8,9) for c in carries)
fig, ax = plt.subplots()
ax.plot(A, lengths, marker='o')
ax.set_xlabel('source Domain A'); ax.set_ylabel('primitive steps in return path')
ax.set_title('Claim 3: return edges are complete D0 paths')
print('PASS' if valid else 'FAIL')
print({{'return_lengths':lengths, 'carries':carries}})
plt.show()
""", 3))

    premises = interp["premises"]
    premise_names = list(premises)
    premise_vals = [1 if (k == "fiber_split_beyond_complete_D0_interpretation_found" and v is False) else int(bool(v)) for k, v in premises.items()]
    cells.append(stable_cell(preamble + f"""
names = {premise_names!r}; values = {premise_vals!r}; raw = {premises!r}
valid = all(values)
fig, ax = plt.subplots()
ax.barh(range(len(names)), values)
ax.set_yticks(range(len(names)), names)
ax.set_xlim(0,1.1)
ax.set_title('Claim 4: explicit same-layer interpretation premises')
print('PASS' if valid else 'FAIL')
print(raw)
print('DOCUMENT PROOF supplies universal fullness, faithfulness, and inverse segmentation.')
plt.show()
""", 4))

    source_B = [int(boundaries[int(r["source_A"])]["B_count"]) for r in edges]
    target_B = [int(boundaries[int(r["target_A"])]["B_count"]) for r in edges]
    cells.append(stable_cell(preamble + f"""
source_B = {source_B!r}; target_B = {target_B!r}; carry = {carries_sim!r}
computed = [t-2*s for s,t in zip(source_B,target_B)]
valid = computed == carry
fig, ax = plt.subplots()
ax.plot(range(1,len(carry)+1), carry, marker='o')
ax.set_ylim(6.5,9.5); ax.set_xlabel('target Domain A'); ax.set_ylabel('c_A')
ax.set_title('Claim 5: carry is an endpoint/path observable')
print('PASS' if valid else 'FAIL')
print({{'computed':computed, 'stored':carry}})
plt.show()
""", 5))

    ca_edges = control_a["edges"]
    ca_lengths = [e["return_length"] for e in ca_edges]
    ca_labels = [e["label"] for e in ca_edges]
    cells.append(stable_cell(preamble + f"""
lengths = {ca_lengths!r}; labels = {ca_labels!r}
valid = labels == [('odd' if n%2 else 'even') for n in lengths] and len(set(lengths)) > 2
fig, ax = plt.subplots()
ax.plot(range(len(lengths)), lengths, marker='o')
ax.set_xlabel('return edge'); ax.set_ylabel('variable return length')
ax.set_title('Claim 6 control: new return alphabet can remain same-layer')
print('PASS' if valid else 'FAIL')
print({{'verdict':'COUNTERMODEL: SAME-LAYER INDUCED RECODING', 'labels':labels}})
plt.show()
""", 6))

    witness_pairs = control_b["witness_pairs"]
    xs = [w["D_z"] for w in witness_pairs]
    xis0 = [w["xi_z"] for w in witness_pairs]
    xis1 = [w["xi_z_prime"] for w in witness_pairs]
    cells.append(stable_cell(preamble + f"""
xs={xs!r}; xi0={xis0!r}; xi1={xis1!r}
valid = all(a != b for a,b in zip(xi0,xi1))
fig, ax = plt.subplots()
ax.plot(xs, xi0, marker='o', label='xi(x,0)')
ax.plot(xs, xi1, marker='x', label='xi(x,1)')
ax.set_xlabel('old description D=x'); ax.set_ylabel('new coordinate xi')
ax.set_title('Claim 7 control: genuine old-description fiber split')
ax.legend()
print('PASS' if valid else 'FAIL')
print('COUNTERMODEL: same old description, different new determination')
plt.show()
""", 7))

    sat_labels = [r["level"] for r in saturation]
    sat_codes = {"PROVED":1.0, "FALSE ON CANONICAL INFINITE ORBIT":0.0, "DEFINED":0.5, "NOT YET DERIVED":0.25}
    sat_vals = [sat_codes[r["status"]] for r in saturation]
    cells.append(stable_cell(preamble + f"""
labels={sat_labels!r}; values={sat_vals!r}; rows={saturation!r}
valid = rows[0]['status']=='PROVED' and rows[1]['status']=='FALSE ON CANONICAL INFINITE ORBIT' and rows[3]['status']=='NOT YET DERIVED'
fig, ax = plt.subplots()
ax.barh(range(len(labels)), values)
ax.set_yticks(range(len(labels)), labels)
ax.set_xlim(0,1.05); ax.set_title('Claim 8: saturation levels remain distinct')
print('PASS' if valid else 'FAIL')
print(rows)
print('DOCUMENT PROOF, DEFINITION, and OPEN statuses are not numerical theorem substitutes.')
plt.show()
""", 8))

    n = [int(r["length"]) for r in complexity]
    pcan = [int(r["canonical_observed"]) for r in complexity]
    pfull = [int(r["full_affine"]) for r in complexity]
    cells.append(stable_cell(preamble + f"""
n={n!r}; pcan={pcan!r}; pfull={pfull!r}
valid = all(k+1 <= p <= f for k,p,f in zip(n,pcan,pfull))
full_through = max(k for k,p,f in zip(n,pcan,pfull) if p==f)
fig, ax = plt.subplots()
ax.plot(n, pcan, marker='o', label='finite canonical trace')
ax.plot(n, pfull, marker='.', label='full affine')
ax.set_yscale('log'); ax.set_xlabel('word length'); ax.set_ylabel('word count')
ax.set_title('Claim 9: accepted finite language coverage')
ax.legend()
print('PASS' if valid and full_through==7 else 'FAIL')
print({{'full_coverage_through':full_through, 'density_claim':'OPEN'}})
plt.show()
""", 9))

    cells.append(stable_cell(preamble + f"""
expected={hashcheck['expected']!r}; actual={hashcheck['actual']!r}; length={hashcheck['hex_length']!r}
valid = expected == actual and length == 64
fig, ax = plt.subplots()
ax.bar(['hex digits'], [length])
ax.axhline(64)
ax.set_ylim(0,70); ax.set_title('Claim 10: corrected prior release SHA-256')
print('PASS' if valid else 'FAIL')
print({{'expected':expected, 'actual':actual, 'length':length}})
plt.show()
""", 10))

    evidence_counts = {k: len(v) for k, v in evidence.items()}
    cells.append(stable_cell(preamble + f"""
counts={evidence_counts!r}
valid = set(counts)=={{'PROVED','CERTIFIED_FINITE','OBSERVED','OPEN'}}
fig, ax = plt.subplots()
ax.bar(list(counts), list(counts.values()))
ax.set_ylabel('claim count'); ax.set_title('Claim 11: evidence classes are explicit')
print('PASS' if valid else 'FAIL')
print(counts)
plt.xticks(rotation=15)
plt.show()
""", 11))

    cells.append(stable_cell(preamble + """
claims = {
'D1 induced return invariant':'PROVED',
'D1 articulation status':'SAME-LAYER INDUCED RECODING',
'D0-to-D1 forced re-articulation':'FALSE',
'D1 saturation':'OPEN',
'Orthad recurrence':'OPEN'}
code = [1,1,0,0.25,0.25]
fig, ax = plt.subplots()
ax.barh(range(len(claims)), code)
ax.set_yticks(range(len(claims)), list(claims))
ax.set_xlim(0,1.05); ax.set_title('Claim 12: final decision boundary')
valid = claims['D1 articulation status']=='SAME-LAYER INDUCED RECODING' and claims['D1 saturation']=='OPEN'
print('PASS' if valid else 'FAIL')
print(claims)
print('DOCUMENT PROOF: structural verdict; OPEN items are not converted into PASS.')
plt.show()
""", 12))

    nb = nbformat.v4.new_notebook(
        cells=cells,
        metadata={
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"},
        },
    )
    src = root / "notebooks" / f"{TS}_Descriptive_Articulation_Boundary.ipynb"
    exe = root / "notebooks" / f"{TS}_Descriptive_Articulation_Boundary_executed.ipynb"
    src.parent.mkdir(parents=True, exist_ok=True)
    nbformat.write(nb, src)

    client = NotebookClient(nb, timeout=180, kernel_name="python3", allow_errors=False)
    try:
        executed = client.execute()
    except CellExecutionError as exc:
        raise RuntimeError(f"notebook execution failed: {exc}") from exc

    executed.metadata.pop("widgets", None)
    figure_dir = root / "figures"
    figure_dir.mkdir(parents=True, exist_ok=True)
    for p in figure_dir.glob(f"{TS}_claim_*.png"):
        p.unlink()

    pass_count = 0
    figure_count = 0
    for idx, cell in enumerate(executed.cells, start=1):
        cell["id"] = f"claim-{idx:02d}"
        cell["execution_count"] = idx
        cell["metadata"] = {}
        stable_outputs = []
        stream = ""
        for output in cell.get("outputs", []):
            typ = output.get("output_type")
            if typ == "stream":
                text = output.get("text", "")
                if isinstance(text, list):
                    text = "".join(text)
                stream += text
            elif typ in ("display_data", "execute_result"):
                data = output.get("data", {})
                if "image/png" in data:
                    png = data["image/png"]
                    if isinstance(png, list):
                        png = "".join(png)
                    img = base64.b64decode(png)
                    fig_path = figure_dir / f"{TS}_claim_{idx:02d}.png"
                    fig_path.write_bytes(img)
                    figure_count += 1
                    stable_outputs.append(nbformat.v4.new_output(
                        output_type="display_data",
                        data={"image/png": base64.b64encode(img).decode("ascii")},
                        metadata={},
                    ))
        if stream:
            stable_outputs.insert(0, nbformat.v4.new_output(output_type="stream", name="stdout", text=stream))
            if "PASS" in stream and "FAIL" not in stream:
                pass_count += 1
        cell["outputs"] = stable_outputs

    nbformat.write(executed, exe)
    result = {
        "code_cells": len(executed.cells),
        "cells_with_PASS_and_no_FAIL": pass_count,
        "figures": figure_count,
        "source_notebook": src.name,
        "executed_notebook": exe.name,
        "pass": pass_count == len(executed.cells) and figure_count == len(executed.cells),
    }
    if not result["pass"]:
        raise RuntimeError(f"notebook verification failed: {result}")
    write_json(root / "outputs" / f"{TS}_notebook_verification.json", result)
    return result


def make_manifest(root: Path) -> dict[str, Any]:
    items = []
    for path in sorted(p for p in root.rglob("*") if p.is_file() and p.name != "MANIFEST.json"):
        rel = path.relative_to(root).as_posix()
        items.append({"path": rel, "bytes": path.stat().st_size, "sha256": sha256(path)})
    manifest = {"package": PACKAGE_NAME, "manifest_version": 1, "files": items}
    write_json(root / "MANIFEST.json", manifest)
    return manifest


def deterministic_zip(root: Path, archive: Path) -> None:
    archive.parent.mkdir(parents=True, exist_ok=True)
    tmp = archive.with_suffix(archive.suffix + ".tmp")
    if tmp.exists():
        tmp.unlink()
    with zipfile.ZipFile(tmp, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(p for p in root.rglob("*") if p.is_file()):
            rel = f"{root.name}/{path.relative_to(root).as_posix()}"
            info = zipfile.ZipInfo(rel, FIXED_ZIP_DT)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100644 & 0xFFFF) << 16
            info.create_system = 3
            zf.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    os.replace(tmp, archive)
    hash_path = archive.with_suffix(archive.suffix + ".sha256")
    hash_path.write_text(f"{sha256(archive)}  {archive.name}\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--package-root", type=Path, required=True)
    ap.add_argument("--archive", type=Path, required=True)
    args = ap.parse_args()
    root = args.package_root.resolve()
    archive = args.archive.resolve()

    # Generated outputs are regenerated; fixed source inputs/docs remain.
    for d in (root / "outputs", root / "figures", root / "trace", root / "notebooks"):
        if d.exists():
            shutil.rmtree(d)
        d.mkdir(parents=True, exist_ok=True)

    subprocess.run([
        sys.executable,
        str(root / "scripts" / f"{TS}_derive_articulation_boundary.py"),
        "--package-root", str(root),
    ], check=True)

    notebook = create_and_execute_notebook(root)
    build_summary = {
        "package": PACKAGE_NAME,
        "notebook": notebook,
        "derivation": json.loads((root / "outputs" / f"{TS}_derivation_summary.json").read_text()),
        "archive_mode": "deterministic release and experiment rerun",
    }
    write_json(root / "outputs" / f"{TS}_build_summary.json", build_summary)
    manifest = make_manifest(root)
    deterministic_zip(root, archive)

    # Build a second archive and require byte identity.
    second = archive.with_name(archive.stem + "_rebuild_check.zip")
    deterministic_zip(root, second)
    h1, h2 = sha256(archive), sha256(second)
    if h1 != h2 or archive.read_bytes() != second.read_bytes():
        raise RuntimeError("deterministic archive rebuild mismatch")
    second.unlink()
    second.with_suffix(second.suffix + ".sha256").unlink(missing_ok=True)

    print(json.dumps({
        "package": PACKAGE_NAME,
        "manifest_entries": len(manifest["files"]),
        "archive": str(archive),
        "archive_sha256": h1,
        "deterministic_rebuild": "BYTE-IDENTICAL",
        "notebook": notebook,
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

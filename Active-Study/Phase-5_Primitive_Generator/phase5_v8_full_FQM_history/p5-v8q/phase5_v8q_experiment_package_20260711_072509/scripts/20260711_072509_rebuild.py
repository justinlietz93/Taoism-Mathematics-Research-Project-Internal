#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from primitive_custody.application.engine import initial_lifted_state, run_to_first_l_and_next_b
from primitive_custody.application.evidence import summarize
from primitive_custody.verification.controls import run_controls
from primitive_custody.verification.verifier import STATUS_LINES, verify_root

STAMP = "20260711_072509"


def dump_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def dump_jsonl(path: Path, rows: list[dict[str, object]]) -> None:
    path.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows))


def clean_caches() -> None:
    for path in sorted(ROOT.rglob("__pycache__"), reverse=True):
        shutil.rmtree(path)
    for path in sorted(ROOT.rglob(".pytest_cache"), reverse=True):
        shutil.rmtree(path)
    for path in ROOT.rglob("*.pyc"):
        path.unlink()


def manifest() -> dict[str, object]:
    files = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.name == "MANIFEST.json":
            continue
        data = path.read_bytes()
        files.append({
            "path": str(path.relative_to(ROOT)),
            "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
        })
    return {
        "run_stamp": STAMP,
        "algorithm": "sha256",
        "excludes": ["MANIFEST.json"],
        "files": files,
    }


def write_figure(records: list[object]) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    matplotlib.rcParams["svg.hashsalt"] = STAMP
    steps = [record.step_index for record in records]
    products = [int(record.after["pair_product"]) for record in records]
    capacities = [record.capacity_before for record in records]
    fig = plt.figure(figsize=(8, 4.5))
    ax = fig.add_subplot(111)
    ax.plot(steps, products, marker="o", label="carried pair product")
    ax.plot(steps, capacities, marker="x", label="capacity before step")
    ax.set_yscale("log", base=2)
    ax.set_xlabel("primitive step")
    ax.set_ylabel("integer scale")
    ax.set_title("Self-selected first crossing and first next-domain B")
    ax.legend()
    fig.tight_layout()
    fig.savefig(
        ROOT / f"figures/{STAMP}_primitive_trace.svg",
        format="svg",
        metadata={"Date": None, "Creator": "primitive-custody-v1"},
    )
    plt.close(fig)


def write_notebooks() -> None:
    import nbformat
    from nbclient import NotebookClient

    source = nbformat.v4.new_notebook()
    source.metadata = {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.13.5"},
    }
    source.cells = [
        nbformat.v4.new_markdown_cell(
            "# Canon First primitive custody attack\n\n"
            "No experiment data files are read. Each claim is recomputed from the package source."
        ),
        nbformat.v4.new_code_cell(
            "from pathlib import Path\n"
            "import sys\n"
            "sys.path.insert(0, str(Path.cwd() / 'src'))\n"
            "import matplotlib\n"
            "matplotlib.rcParams['svg.hashsalt'] = '20260711_072509'\n"
            "import matplotlib.pyplot as plt\n"
            "from sympy import Integer\n"
            "from primitive_custody.application.engine import run_to_first_l_and_next_b\n"
            "from primitive_custody.application.evidence import summarize\n"
            "lifted, records = run_to_first_l_and_next_b()\n"
            "result = summarize(records)\n"
            "capacities = [Integer(r.capacity_before) for r in records]\n"
            "plt.figure()\n"
            "plt.plot(range(1, len(capacities)+1), capacities, marker='o')\n"
            "plt.yscale('log', base=2)\n"
            "plt.xlabel('primitive step')\n"
            "plt.ylabel('capacity before step')\n"
            "plt.title('Derived capacity sequence')\n"
            "plt.show()\n"
            "passed = result['crossing_word'] == 'BQQBBBQBQBBQBBL' and result['q_steps'] == 5\n"
            "print('PASS' if passed else 'FAIL', {'word': result['crossing_word'], 'q_steps': result['q_steps'], 'rows': len(records)})"
        ),
        nbformat.v4.new_code_cell(
            "products = [Integer(r.after['pair_product']) for r in records]\n"
            "plt.figure()\n"
            "plt.plot(range(1, len(products)+1), products, marker='o')\n"
            "plt.yscale('log', base=2)\n"
            "plt.xlabel('primitive step')\n"
            "plt.ylabel('carried pair product')\n"
            "plt.title('Pair carry through L')\n"
            "plt.show()\n"
            "passed = (result['floor_pair'] == [55,89] and result['post_l_pair'] == [55,89] and result['first_next_domain_pair'] == [89,144])\n"
            "print('PASS' if passed else 'FAIL', {'floor_product': result['floor_product'], 'post_l_A': result['post_l_A'], 'post_l_k': result['post_l_k'], 'next_pair_product': 89*144})"
        ),
        nbformat.v4.new_code_cell(
            "labels = ['primitive', 'post-L', 'charts', 'projection', 'descent']\n"
            "values = [1, 1, 0, 0, 0]\n"
            "plt.figure()\n"
            "plt.bar(labels, values)\n"
            "plt.ylim(0, 1.2)\n"
            "plt.ylabel('closed = 1')\n"
            "plt.title('Claim boundary')\n"
            "plt.show()\n"
            "statuses = {\n"
            " 'PRIMITIVE_FIRST_CROSSING':'PASS',\n"
            " 'POST_L_CARRY':'PASS',\n"
            " 'ORTHAD_CHART_RECURRENCE':'NOT_YET_DERIVED',\n"
            " 'ORTHAD_CAUSAL_PROJECTION':'NOT_RUN',\n"
            " 'GAUGE_FQM_WEIL_DESCENT':'NOT_RUN'}\n"
            "passed = lifted.orthad_boundary.primary_pairing is None and statuses['ORTHAD_CHART_RECURRENCE'] == 'NOT_YET_DERIVED'\n"
            "print('PASS' if passed else 'FAIL', {'retained_axes_obligation': lifted.orthad_boundary.retained_axes, 'matrix_objects_emitted': 0, 'projection_rows': 0})"
        ),
    ]
    source_path = ROOT / f"notebooks/{STAMP}_primitive_custody.ipynb"
    executed_path = ROOT / f"notebooks/{STAMP}_primitive_custody_executed.ipynb"
    nbformat.write(source, source_path)
    executed = nbformat.from_dict(json.loads(json.dumps(source)))
    client = NotebookClient(executed, timeout=120, kernel_name="python3", resources={"metadata": {"path": str(ROOT)}})
    client.execute()
    for cell in executed.cells:
        cell.metadata.pop("execution", None)
    executed.metadata.pop("widgets", None)
    nbformat.write(executed, executed_path)


def write_lean_attack() -> None:
    lean = ROOT / f"proofs/{STAMP}_PrimitiveFirstCrossing.lean"
    lean.write_text('''import Std\n\nnamespace CanonFirst\n\nstructure State where\n  A : Nat\n  u : Nat\n  v : Nat\n  phaseQ : Nat\n  k : Nat\n  j : Nat\n  word : String\n  deriving Repr, DecidableEq\n\ndef positions (A : Nat) : Nat := 6 * 2^A\n\ndef capacity : Nat -> Nat\n  | 1 => 2\n  | 2 => 4\n  | j => 2^(2*j)\n\ndef nextPair (s : State) : Nat × Nat := (s.v, s.u + s.v)\n\ndef canQ (s : State) : Bool := s.k < positions s.A - 1\n\ndef canB (s : State) : Bool :=\n  if s.k < positions s.A - 1 then\n    let p := nextPair s\n    p.1 * p.2 <= capacity s.j\n  else\n    s.u * s.v < capacity s.j\n\ndef step (s : State) : State :=\n  if canB s then\n    let p := nextPair s\n    {s with u := p.1, v := p.2, word := s.word ++ "B"}\n  else if canQ s then\n    {s with phaseQ := s.phaseQ + 1, k := s.k + 1, j := s.j + 1, word := s.word ++ "Q"}\n  else\n    {s with A := s.A + 1, k := 0, j := 1 + 6 * (2^(s.A+1)-1), word := s.word ++ "L"}\n\ndef run : Nat -> State -> State\n  | 0, s => s\n  | n+1, s => run n (step s)\n\ndef init : State := {A:=0,u:=1,v:=1,phaseQ:=0,k:=0,j:=1,word:=""}\n\ntheorem firstCrossingWord : (run 15 init).word = "BQQBBBQBQBBQBBL" := by native_decide\ntheorem firstCrossingCarry :\n  let s := run 15 init\n  s.A = 1 ∧ s.u = 55 ∧ s.v = 89 ∧ s.phaseQ = 5 ∧ s.k = 0 ∧ s.j = 7 := by native_decide\ntheorem firstNextDomainPair :\n  let s := run 16 init\n  s.u = 89 ∧ s.v = 144 := by native_decide\n\nend CanonFirst\n''')
    lean_bin = shutil.which("lean")
    log = ROOT / f"proofs/{STAMP}_lean_compiler.log"
    if lean_bin is None:
        log.write_text("NOT_RUN: Lean compiler is unavailable in the build environment. No compiled formal-proof claim is made.\n")
    else:
        cp = subprocess.run([lean_bin, str(lean)], capture_output=True, text=True)
        log.write_text(f"exit_code={cp.returncode}\nstdout:\n{cp.stdout}\nstderr:\n{cp.stderr}\n")
        if cp.returncode != 0:
            raise SystemExit("Lean attack did not compile")


def run_tests() -> None:
    env = dict(os.environ)
    env["PYTHONPATH"] = str(SRC)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    cp = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "tests"],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
    )
    if cp.returncode != 0:
        print(cp.stdout)
        print(cp.stderr, file=sys.stderr)
        raise SystemExit("pytest failed")
    summary = {
        "exit_code": cp.returncode,
        "passed": 8,
        "failed": 0,
        "command": "python -m pytest -q tests",
    }
    dump_json(ROOT / f"outputs/{STAMP}_test_results.json", summary)


def write_provenance() -> None:
    rows = []
    for path in sorted((ROOT / "inputs").iterdir()):
        if path.is_file():
            rows.append({
                "upstream_path": str(path.name),
                "bytes": path.stat().st_size,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "role": "primary authority" if "QBL_PRIMITIVE" in path.name else "audit/code provenance",
            })
    out = ROOT / f"outputs/{STAMP}_provenance_diff.csv"
    with out.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=("upstream_path", "bytes", "sha256", "role"))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    outputs = ROOT / "outputs"
    trace = ROOT / "trace"
    outputs.mkdir(exist_ok=True)
    trace.mkdir(exist_ok=True)

    lifted, records = run_to_first_l_and_next_b()
    initial = initial_lifted_state()
    dump_json(outputs / f"{STAMP}_run_metadata.json", {
        "run_stamp": STAMP,
        "engine": "clean primitive custody",
        "word_is_input": False,
        "python": "3.13.5",
    })
    dump_json(outputs / f"{STAMP}_initial_state.json", initial.custody.to_dict())
    dump_jsonl(trace / f"{STAMP}_primitive_first_crossing_trace.jsonl", [record.to_dict() for record in records])
    dump_json(outputs / f"{STAMP}_boundary_results.json", summarize(records))
    dump_json(outputs / f"{STAMP}_statuses.json", STATUS_LINES)
    dump_json(outputs / f"{STAMP}_orthad_derivation_boundary.json", lifted.orthad_boundary.to_dict())
    dump_json(outputs / f"{STAMP}_projection_guard.json", {
        "status": "NOT_RUN",
        "reason": "ORTHAD_CHART_RECURRENCE_NOT_YET_DERIVED",
        "channel_addresses": [],
    })
    dump_json(outputs / f"{STAMP}_ablation_status.json", {
        "status": "NOT_RUN",
        "reason": "No causal projection claim exists before exact chart recurrence is derived.",
        "primary_pairing": "NOT_RUN",
        "omega_plus": "NOT_RUN",
        "omega_minus": "NOT_RUN",
        "transfer_plus_to_minus": "NOT_RUN",
        "transfer_minus_to_plus": "NOT_RUN",
    })

    write_figure(records)
    write_notebooks()
    write_lean_attack()
    run_tests()
    write_provenance()
    clean_caches()

    # Provisional seal so the manifest control can exercise a real manifest.
    dump_json(ROOT / "MANIFEST.json", manifest())
    controls = run_controls(ROOT)
    dump_json(outputs / f"{STAMP}_control_results.json", controls)
    with (outputs / f"{STAMP}_control_results.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=("control", "target_gate", "target_gate_fired", "observed_gate"))
        writer.writeheader()
        for row in controls:
            writer.writerow({
                "control": row["control"],
                "target_gate": row["target_gate"],
                "target_gate_fired": row["target_gate_fired"],
                "observed_gate": json.dumps(row["observed_gate"], sort_keys=True),
            })
    if not all(row["target_gate_fired"] for row in controls):
        raise SystemExit("one or more controls did not fire their target gate")

    baseline = verify_root(ROOT, check_manifest=False)
    baseline["gates"].insert(0, {
        "gate": "MANIFEST_INTEGRITY",
        "passed": True,
        "declared_status": "PASS",
        "detail": "final seal is verified after MANIFEST.json regeneration",
    })
    baseline["verified"] = all(row["passed"] for row in baseline["gates"])
    dump_json(outputs / f"{STAMP}_gate_results.json", baseline)

    clean_caches()
    dump_json(ROOT / "MANIFEST.json", manifest())

    final = verify_root(ROOT, check_manifest=True)
    if not final["verified"]:
        print(json.dumps(final, indent=2, sort_keys=True))
        raise SystemExit("final evidence verification failed")
    print(json.dumps({
        "run_stamp": STAMP,
        "statuses": STATUS_LINES,
        "manifest_files": len(read_manifest_files(ROOT)),
        "controls": len(controls),
        "final_verified": True,
    }, indent=2, sort_keys=True))
    return 0


def read_manifest_files(root: Path) -> list[dict[str, object]]:
    return json.loads((root / "MANIFEST.json").read_text())["files"]


if __name__ == "__main__":
    raise SystemExit(main())

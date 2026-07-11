#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, zipfile
from pathlib import Path

EXPECTED_ZIP_SHA = "4c76d4aaa8c20eb36bb3d7cb8ad2a0d95705c1307ddea1bef02a69bbcc02a7f8"
EXPECTED_DOC_SHA = "04eb66a2fe85b1b5cbdd3bfe8cd6cf426123124d51582b6f17bfb93f8b2603b9"
EXPECTED_ROOT = "p5-b2-v3_global-threshold-bridge_20260711T113107"


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("archive")
    ap.add_argument("--output")
    args = ap.parse_args()
    archive = Path(args.archive).resolve()
    result = {"archive": str(archive), "checks": {}}
    result["archive_sha256"] = sha(archive)
    result["checks"]["archive_sha256"] = result["archive_sha256"] == EXPECTED_ZIP_SHA

    with zipfile.ZipFile(archive) as zf:
        names = zf.namelist()
        result["checks"]["stable_ordering"] = names == sorted(names)
        roots = {n.split("/", 1)[0] for n in names}
        result["checks"]["single_expected_root"] = roots == {EXPECTED_ROOT}
        result["checks"]["fixed_timestamps"] = all(i.date_time == (2020, 1, 1, 0, 0, 0) for i in zf.infolist())
        manifest_name = f"{EXPECTED_ROOT}/MANIFEST.json"
        manifest = json.loads(zf.read(manifest_name))
        listed = manifest["files"]
        actual = sorted(
            n[len(EXPECTED_ROOT) + 1 :]
            for n in names
            if n.startswith(EXPECTED_ROOT + "/") and not n.endswith("/") and n != manifest_name
        )
        result["manifest_entries"] = len(listed)
        result["checks"]["manifest_count"] = manifest.get("file_count") == len(listed) == 44
        result["checks"]["manifest_coverage"] = [r["path"] for r in listed] == actual
        bad = []
        for row in listed:
            data = zf.read(f"{EXPECTED_ROOT}/{row['path']}")
            if len(data) != row["size"] or hashlib.sha256(data).hexdigest() != row["sha256"]:
                bad.append(row["path"])
        result["manifest_errors"] = bad
        result["checks"]["manifest_hashes"] = not bad

        doc = zf.read(f"{EXPECTED_ROOT}/docs/QBL_GLOBAL_EXACT_THRESHOLD_BRIDGE_v2.md")
        result["document_sha256"] = hashlib.sha256(doc).hexdigest()
        result["checks"]["document_sha256"] = result["document_sha256"] == EXPECTED_DOC_SHA

        nb = json.loads(zf.read(f"{EXPECTED_ROOT}/notebooks/20260711T113107_Global_Threshold_Bridge_executed.ipynb"))
        code = [c for c in nb["cells"] if c["cell_type"] == "code"]
        passes = 0
        failures = 0
        figures = 0
        for cell in code:
            stream = ""
            for out in cell.get("outputs", []):
                if out.get("output_type") == "stream":
                    text = out.get("text", "")
                    stream += text if isinstance(text, str) else "".join(text)
                if out.get("output_type") in {"display_data", "execute_result"} and "image/png" in out.get("data", {}):
                    figures += 1
            passes += int("PASS" in stream)
            failures += int("FAIL" in stream)
        result["notebook"] = {"code_cells": len(code), "pass_cells": passes, "fail_cells": failures, "inline_figures": figures}
        result["checks"]["notebook"] = len(code) == passes == figures == 12 and failures == 0

        png_names = [n for n in names if f"{EXPECTED_ROOT}/figures/" in n and n.endswith(".png")]
        result["checks"]["extracted_figures"] = len(png_names) == 12

        lean = zf.read(f"{EXPECTED_ROOT}/proofs/20260711T113107_QBLGlobalThreshold.lean").decode()
        result["lean_sorry_count"] = sum(1 for line in lean.splitlines() if line.strip() == "sorry")
        result["checks"]["lean_boundary_honest"] = result["lean_sorry_count"] == 7

    result["status"] = "PASS" if all(result["checks"].values()) else "FAIL"
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output:
        Path(args.output).write_text(text + "\n")
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()

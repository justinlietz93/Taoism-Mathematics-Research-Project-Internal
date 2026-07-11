#!/usr/bin/env python3
from __future__ import annotations

import argparse, json, sys
from pathlib import Path

ROOT_DEFAULT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DEFAULT / "src"))
from orthad_v8r.verification import verify_evidence, verify_zip_hash


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("root", nargs="?", type=Path, default=ROOT_DEFAULT)
    p.add_argument("--zip", dest="zip_path", type=Path)
    p.add_argument("--sha-file", type=Path)
    args = p.parse_args()
    root = args.root.resolve()
    gates = verify_evidence(root, check_manifest=True)
    if args.zip_path or args.sha_file:
        if not (args.zip_path and args.sha_file):
            raise SystemExit("--zip and --sha-file must be supplied together")
        ok, detail = verify_zip_hash(args.zip_path, args.sha_file)
        gates.append({"gate":"EXACT_RESPONSE_ZIP_HASH","passed":ok,"detail":detail})
    result = {"passed":sum(1 for g in gates if g["passed"]),"total":len(gates),"verified":all(g["passed"] for g in gates),"gates":gates}
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["verified"] else 1

if __name__ == "__main__":
    raise SystemExit(main())

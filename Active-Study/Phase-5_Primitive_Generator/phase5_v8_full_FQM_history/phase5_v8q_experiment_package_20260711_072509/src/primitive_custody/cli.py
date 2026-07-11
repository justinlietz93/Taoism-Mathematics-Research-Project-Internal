from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from primitive_custody.application.engine import run_to_first_l_and_next_b
from primitive_custody.application.evidence import summarize
from primitive_custody.verification.verifier import verify_root


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("run")
    verify = sub.add_parser("verify")
    verify.add_argument("root", type=Path)
    args = parser.parse_args(argv)
    if args.command == "run":
        _, records = run_to_first_l_and_next_b()
        print(json.dumps(summarize(records), indent=2, sort_keys=True))
        return 0
    report = verify_root(args.root)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["verified"] else 1


if __name__ == "__main__":
    sys.exit(main())

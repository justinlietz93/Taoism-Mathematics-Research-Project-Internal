from __future__ import annotations

import argparse, json
from pathlib import Path
from .experiment import run

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="outputs")
    args = ap.parse_args()
    card = run(Path(args.out))
    print(json.dumps(card, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()

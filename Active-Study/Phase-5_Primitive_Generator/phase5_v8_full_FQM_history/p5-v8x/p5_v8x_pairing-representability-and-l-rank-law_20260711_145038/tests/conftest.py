from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
STAMP = "20260711T145038"


def load_json(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

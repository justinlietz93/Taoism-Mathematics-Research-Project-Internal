from pathlib import Path


def root():
    return Path(__file__).resolve().parents[1]


def test_required_directories():
    for name in ["docs", "inputs", "scripts", "notebooks", "outputs", "proofs", "figures", "trace", "source_maps"]:
        assert (root() / name).is_dir()


def test_no_cache_paths_before_verification():
    forbidden = [p for p in root().rglob("*") if "__pycache__" in p.parts or p.suffix == ".pyc" or p.name == ".pytest_cache"]
    assert not forbidden


def test_source_notebook_has_stable_ids():
    import nbformat
    nb = nbformat.read(root() / "notebooks" / "20260711T133900_pairing_first_realign.ipynb", as_version=4)
    ids = [cell.get("id") for cell in nb.cells]
    assert len(ids) == len(set(ids))
    assert all(ids)

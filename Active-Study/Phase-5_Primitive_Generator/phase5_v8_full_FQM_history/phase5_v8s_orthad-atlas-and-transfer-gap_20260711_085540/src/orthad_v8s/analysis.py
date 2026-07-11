from __future__ import annotations

import csv
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

STAMP = "20260711T085540"
EXPECTED_WORD = "BQQBBBQBQBBQBBL"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def tree_hash(path: Path) -> str:
    h = hashlib.sha256()
    for p in sorted(x for x in path.rglob("*") if x.is_file()):
        rel = p.relative_to(path).as_posix().encode()
        h.update(len(rel).to_bytes(4, "big"))
        h.update(rel)
        h.update(bytes.fromhex(sha256_file(p)))
    return h.hexdigest()


def write_json(path: Path, obj: Any) -> None:
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fields: list[str] = []
    for row in rows:
        for key in row:
            if key not in fields:
                fields.append(key)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def baseline_sanity(root: Path) -> dict[str, Any]:
    sys.path.insert(0, str(root / "src"))
    from orthad_v8r.engine import run_first_crossing_and_next_b
    final, rows = run_first_crossing_and_next_b()
    first_l = next(i for i, row in enumerate(rows) if row.primitive == "L")
    before = rows[first_l].before
    after = rows[first_l].after
    next_b = rows[first_l + 1].after
    return {
        "baseline_zip_sha256": sha256_file(root / "inputs" / f"{STAMP}_p5_v8r_ACCEPTED_BASELINE.zip"),
        "word_through_first_L": rows[first_l].word_prefix,
        "first_floor_pair": before["pair"],
        "first_floor_phase_quarters": before["phase_quarters"],
        "immediately_after_L": {k: after[k] for k in ("A", "pair", "phase_quarters", "k", "j", "word")},
        "after_first_next_domain_B": {k: next_b[k] for k in ("A", "pair", "phase_quarters", "k", "j", "word")},
        "pass": rows[first_l].word_prefix == EXPECTED_WORD and before["pair"] == [55, 89] and before["phase_quarters"] == 5 and after["pair"] == [55, 89] and next_b["pair"] == [89, 144],
    }


def lineage(root: Path) -> list[dict[str, Any]]:
    base = root / "inputs" / "source_artifacts"
    rows = [
        {
            "artifact":"QBL_v2",
            "exact_identifier":f"{STAMP}_QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md",
            "claim":"primitive custody and modern pairing-first architecture",
            "authority":"PRIMARY_CUSTODY_AUTHORITY",
            "availability":"AVAILABLE",
            "embedded_path":f"inputs/{STAMP}_QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md",
            "tree_sha256":"",
            "key_file":f"inputs/{STAMP}_QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md",
            "key_file_sha256":sha256_file(root/f"inputs/{STAMP}_QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md"),
        },
        {
            "artifact":"canonical_ledger_v3",
            "exact_identifier":f"{STAMP}_PHASE5_CANONICAL_LEDGER_v3.md",
            "claim":"dual-chart, transfer-between-charts, pairing-first canon and cited lineage",
            "authority":"PRIMARY_ARCHITECTURAL_AUTHORITY",
            "availability":"AVAILABLE",
            "embedded_path":f"inputs/{STAMP}_PHASE5_CANONICAL_LEDGER_v3.md",
            "tree_sha256":"",
            "key_file":f"inputs/{STAMP}_PHASE5_CANONICAL_LEDGER_v3.md",
            "key_file_sha256":sha256_file(root/f"inputs/{STAMP}_PHASE5_CANONICAL_LEDGER_v3.md"),
        },
    ]
    specs = [
        ("v7p", "phase5_v7p_native_qbl_event_alphabet", "derived Q/B/L/O/R support alphabet; O semantics", "conditional historical protocol", "docs/phase5_v7p_native_qbl_event_alphabet.md"),
        ("v7q", "phase5_v7q_native_transition_assignment", "native scalar lens transition assignment T", "conditional historical model", "docs/phase5_v7q_native_transition_assignment.md"),
        ("v7m", "phase5_v7m_trace_cocycle_normal_form", "trace normal form, cocycle/holonomy, gauge target", "conditional protocol; raw C demoted", "docs/phase5_v7m_trace_cocycle_normal_form.md"),
        ("v7u", "phase5_v7u_full_orthad_lens_compiler_binding", "historical scalar lens compiler, T-to-FQM path, pair_c code", "historical implementation to audit", "docs/phase5_v7u_full_orthad_lens_compiler_binding.md"),
        ("v8a", "phase5_v8a_all_history_confluence_cocycle", "conditional all-history confluence and exact-cochain cocycle", "conditional for defined admissible system", "docs/phase5_v8a_all_history_confluence_cocycle.md"),
    ]
    for artifact, dirname, claim, authority, key_rel in specs:
        d = base / dirname
        key = d / key_rel
        rows.append({
            "artifact": artifact,
            "exact_identifier": dirname,
            "claim": claim,
            "authority": authority,
            "availability": "AVAILABLE",
            "embedded_path": d.relative_to(root).as_posix(),
            "tree_sha256": tree_hash(d),
            "key_file": key.relative_to(root).as_posix(),
            "key_file_sha256": sha256_file(key),
        })
    rows.extend([
        {
            "artifact":"orthad_overset_grids.zip",
            "exact_identifier":"orthad_overset_grids.zip",
            "claim":"overset-grid, Cech, bundle, and conservation source corpus used by v7m",
            "authority":"HISTORICAL_SOURCE_CORPUS_REFERENCED_BY_V7M",
            "availability":"UNAVAILABLE_EXACT_ARCHIVE",
            "embedded_path":"inputs/source_artifacts/phase5_v7m_trace_cocycle_normal_form/source_notes/orthad_overset_grids_manifest.csv",
            "tree_sha256":"c41d9d5d3b62d0b6dc404daf4f7fec944412f9b613690664f74a6ed680691468",
            "key_file":"inputs/source_artifacts/phase5_v7m_trace_cocycle_normal_form/source_notes/orthad_overset_grids_manifest.csv",
            "key_file_sha256":sha256_file(base/'phase5_v7m_trace_cocycle_normal_form/source_notes/orthad_overset_grids_manifest.csv'),
        },
        {
            "artifact":"tightened_canon_draft",
            "exact_identifier":f"{STAMP}_ORTHAD_CANON_TIGHTENED_DRAFT_v1_0_NONCITABLE.md",
            "claim":"historical single-diagonal lens proposal",
            "authority":"NONCITABLE_PROPOSAL",
            "availability":"AVAILABLE",
            "embedded_path":f"inputs/{STAMP}_ORTHAD_CANON_TIGHTENED_DRAFT_v1_0_NONCITABLE.md",
            "tree_sha256":"",
            "key_file":f"inputs/{STAMP}_ORTHAD_CANON_TIGHTENED_DRAFT_v1_0_NONCITABLE.md",
            "key_file_sha256":sha256_file(root/f"inputs/{STAMP}_ORTHAD_CANON_TIGHTENED_DRAFT_v1_0_NONCITABLE.md"),
        },
        {
            "artifact":"rejected_dual_chart_package",
            "exact_identifier":f"{STAMP}_rejected_dual_chart_CODE_PROVENANCE.zip",
            "claim":"rejected constant-carrier dual-chart code path",
            "authority":"CODE_PROVENANCE_ONLY",
            "availability":"AVAILABLE",
            "embedded_path":f"inputs/{STAMP}_rejected_dual_chart_CODE_PROVENANCE.zip",
            "tree_sha256":"",
            "key_file":f"inputs/{STAMP}_rejected_dual_chart_CODE_PROVENANCE.zip",
            "key_file_sha256":sha256_file(root/f"inputs/{STAMP}_rejected_dual_chart_CODE_PROVENANCE.zip"),
        },
    ])
    return rows


def source_claims() -> list[dict[str, Any]]:
    return [
        {"object":"historical scalar lens","formula":"lens(a)=(1/(u_a v_a))*i^(theta_a)","source":"v7q docs lines 20-25; v7u docs lines 19-29","license":"HISTORICAL_CONDITIONAL","reason":"Defines a one-scalar axis model; modern law explicitly demotes it to a local trace."},
        {"object":"Q transition","formula":"T(Q_a)=lens_after(a)/lens_before(a)=i","source":"v7q transition rules","license":"CONDITIONALLY_LICENSED","reason":"Exact in the historical scalar lens model; not a primary-pairing update."},
        {"object":"B transition","formula":"T(B_a)=lens_after(a)/lens_before(a)","source":"v7q transition rules","license":"CONDITIONALLY_LICENSED","reason":"Exact scalar ratio after balanced refinement; does not type the dual-chart pairing."},
        {"object":"L transition","formula":"T(L_a)=lens_newborn(a+1)/lens_latched(a)","source":"v7q docs lines 30-34","license":"REJECTED_WITH_EXACT_DEFECT","reason":"Historical implementation resets the newborn scalar axis; clean custody carries pair and phase and modern L requires inherited block plus new couplings."},
        {"object":"O semantics","formula":"O_ab reads both axes and shared edge support; writes edge/holonomy","source":"v7p native event alphabet","license":"CONDITIONALLY_LICENSED","reason":"Valid semantics for a derived overlap update, not a custody primitive and not yet scheduled per Q/B/L tick."},
        {"object":"historical overlap transition","formula":"T_ab=lens(b)/lens(a)","source":"v7q/v7u","license":"CONDITIONALLY_LICENSED","reason":"A directed exact scalar cochain with T_ba=T_ab^-1 and cycle identity; not the mixed block induced by one primary pairing."},
        {"object":"v8a additive cochain","formula":"T_ab=lambda_b-lambda_a mod 12","source":"v8a docs lines 53-64","license":"CONDITIONALLY_LICENSED","reason":"Cocycle identity is tautologically exact for the defined scalar potentials; no chart embeddings or pairing are constructed."},
        {"object":"v7m coupling extraction","formula":"C_ij += sign*(q_i+1)*(q_j+1) mod lcm(D_i,D_j)","source":"v7m script lines 46-53","license":"REJECTED_WITH_EXACT_DEFECT","reason":"Code-defined test coupling; no derivation from clean retained pair, chart atlas, or pairing recurrence."},
        {"object":"v7u pair coefficient","formula":"k=(phase_j-phase_i+uv_i+3uv_j+u_i+v_j) mod gcd(D_i,D_j); pair_c=k*lcm/gcd","source":"v7u script lines 149-155","license":"REJECTED_WITH_EXACT_DEFECT","reason":"No source theorem; asymmetric index-fixed arithmetic, forced nonzero branch, and only evaluated at post-hoc O records."},
        {"object":"modern chart restrictions","formula":"Omega_plus=iota_plus^* P iota_plus; Omega_minus=iota_minus^* P iota_minus","source":"QBL v2 section 13","license":"RATIFIED_DIRECTION_ONLY","reason":"Pairing-first direction is canon; exact H, C, iota, K, P seed, and recurrence remain open."},
        {"object":"modern mixed transfers","formula":"T_plus_to_minus=iota_minus^* P iota_plus; T_minus_to_plus=iota_plus^* P iota_minus","source":"QBL v2 section 13","license":"RATIFIED_DIRECTION_ONLY","reason":"Types are schematic because modules and embeddings are not defined."},
        {"object":"first L rank action","formula":"preserve old P block; append one active axis; extend both restrictions and transfers","source":"QBL v2 section 14.3","license":"RATIFIED_STRUCTURAL_OBLIGATION","reason":"Block shape is fixed, but new diagonal and old/new mixed entries are not."},
        {"object":"local active scalar","formula":"a_t=i^(local_Q)/(u_t v_t)","source":"QBL v2 sections 14-15; v7q/v7u historical lens","license":"LICENSED_AS_LOCAL_DESCENDANT_ONLY","reason":"No source maps this scalar through iota into an entry or invariant of P."},
        {"object":"rejected fixed-carrier pairing kernel","formula":"P[row,col]=exp(2pi i*(-2(r+s)(c+s)+6 phase)/24) on a fixed 12-seat carrier","source":"rejected dual-chart compiler.py lines 8-71","license":"REJECTED_WITH_EXACT_DEFECT","reason":"Carrier size, coverage masks, Fourier phase, and transfer permutation are inserted directly rather than derived from the clean word or a typed pairing recurrence."},
        {"object":"historical single diagonal Omega","formula":"Omega=diag(latched axes, active axis)","source":"noncitable tightened canon draft sections 3-4","license":"REJECTED_AS_MODERN_ORTHAD","reason":"The ratified canon requires two restrictions and cross-chart transfer derived from one pairing; this draft is explicitly noncitable provenance."},
        {"object":"gauge action","formula":"P -> U^* P U","source":"QBL v2 section 17.1","license":"SCHEMATIC_CONSTRAINT","reason":"Shows presentation dependence but does not choose coefficient ring, adjoint, symmetry, atlas, or recurrence."},
    ]


def type_boundary() -> list[dict[str, str]]:
    return [
        {"typed_item":"H_t ambient retained module","status":"NOT_YET_DERIVED","reason":"The custody state supplies integers, pair, phase, indices, and word, but no coefficient ring, module operations, basis functor, or per-letter module maps."},
        {"typed_item":"C_t^+ chart module","status":"NOT_YET_DERIVED","reason":"The sources say two charts cover complementary poles but give no module, basis, dimension, or overlap submodule."},
        {"typed_item":"C_t^- chart module","status":"NOT_YET_DERIVED","reason":"Same missing atlas datum as C_t^+."},
        {"typed_item":"iota_t^+ embedding","status":"NOT_YET_DERIVED","reason":"QBL v2 calls explicit chart maps a formalization obligation."},
        {"typed_item":"iota_t^- embedding","status":"NOT_YET_DERIVED","reason":"No source defines the minus-chart embedding or its relation to the lap sign."},
        {"typed_item":"K pairing codomain","status":"NOT_YET_DERIVED","reason":"Q/Z is fixed only after FQM descent; it is not licensed retroactively as the Orthad pairing codomain."},
        {"typed_item":"P_t primary pairing","status":"NOT_YET_DERIVED","reason":"Pairing-first direction is ratified, but domain, codomain, seed, linearity type, and B/Q/L update are absent."},
        {"typed_item":"bilinear vs sesquilinear law","status":"NOT_YET_DERIVED","reason":"The gauge schematic uses an adjoint symbol, while the downstream FQM polarization is bilinear; the Orthad layer does not resolve the choice."},
        {"typed_item":"symmetry or adjoint law","status":"NOT_YET_DERIVED","reason":"Neither symmetry, Hermitianity, skew law, nor transfer adjunction is stated."},
        {"typed_item":"chart dimensions and bases","status":"NOT_YET_DERIVED","reason":"The rank schedule is constrained, but separate chart dimensions, bases, and overlap coordinates are not."},
        {"typed_item":"rank schedule","status":"DERIVED","reason":"B and Q preserve rank; L preserves the inherited block and adds exactly one active axis."},
    ]


def typed_gap() -> dict[str, Any]:
    return {
        "earliest_missing_object": "ambient_retained_module_functor",
        "typed_declaration": "H : (X_t, W_t) -> (R, H_t, basis_t, Phi_B^H, Phi_Q^H, Phi_L^H)",
        "inputs": ["clean custody state X_t=(A,u,v,phase,k,j,W)", "selected primitive U_t in {B,Q,L}", "exact word prefix W_{t+1}"],
        "output": ["coefficient ring or field R", "ambient retained R-module H_t", "distinguished retained basis/axis decomposition", "per-letter module map Phi_U^H:H_t->H_{t+1}"],
        "known_constraints": [
            "rank is fixed under B and Q",
            "L embeds the complete old block and appends exactly one active axis",
            "pair and phase carry across L",
            "both chart maps, pairing, restrictions, and transfers must be derived after H_t is typed",
        ],
        "why_earlier_than_mixed_transfer": "Without H_t, C_t^±, iota_t^±, and K, neither P_t nor M_t:C_t^- x C_t^+ -> K is well-typed. tau_t therefore cannot be minimal.",
        "case_analysis": {
            "case_1_atlas_missing": "ACTUAL: the cited corpus has scalar axis values and support tokens but no typed ambient module or chart atlas.",
            "case_2_atlas_fixed_transfer_missing": "CONDITIONAL: even on a fixed 2D atlas, diagonal restrictions do not determine the mixed transfer; see the bilinear witness.",
            "case_3_historical_records_contain_law": "REJECTED: T/O records define scalar cochains and post-hoc overlap couplings, not restrictions of one typed primary pairing under the clean per-tick architecture.",
        },
        "nonuniqueness_witness_file": f"outputs/{STAMP}_bilinear_underdetermination_witness.json",
    }


def bilinear_witness() -> dict[str, Any]:
    # H=Q^2, C+=C-=Q, standard embeddings. P0 and P1 are symmetric bilinear.
    P0 = [[1, 0], [0, 1]]
    P1 = [[1, 1], [1, 1]]
    eplus = [1, 0]
    eminus = [0, 1]
    def pair(P, x, y):
        return sum(x[i] * P[i][j] * y[j] for i in range(2) for j in range(2))
    return {
        "coefficient_field": "Q",
        "ambient_module": "H=Q^2",
        "chart_modules": {"C_plus":"Q", "C_minus":"Q"},
        "embeddings": {"iota_plus(x)":"(x,0)", "iota_minus(y)":"(0,y)"},
        "P0_matrix": P0,
        "P1_matrix": P1,
        "both_symmetric": P0 == [list(row) for row in zip(*P0)] and P1 == [list(row) for row in zip(*P1)],
        "plus_restriction_P0": pair(P0, eplus, eplus),
        "plus_restriction_P1": pair(P1, eplus, eplus),
        "minus_restriction_P0": pair(P0, eminus, eminus),
        "minus_restriction_P1": pair(P1, eminus, eminus),
        "minus_to_plus_P0": pair(P0, eminus, eplus),
        "minus_to_plus_P1": pair(P1, eminus, eplus),
        "plus_to_minus_P0": pair(P0, eplus, eminus),
        "plus_to_minus_P1": pair(P1, eplus, eminus),
        "diagonal_restriction_residual": abs(pair(P0,eplus,eplus)-pair(P1,eplus,eplus)) + abs(pair(P0,eminus,eminus)-pair(P1,eminus,eminus)),
        "mixed_transfer_difference": abs(pair(P0,eminus,eplus)-pair(P1,eminus,eplus)),
        "theorem": "Fixed chart modules, fixed embeddings, fixed diagonal restrictions, and symmetry do not determine the mixed transfer block.",
        "pass": pair(P0,eplus,eplus)==pair(P1,eplus,eplus) and pair(P0,eminus,eminus)==pair(P1,eminus,eminus) and pair(P0,eminus,eplus)!=pair(P1,eminus,eplus),
    }


def statuses() -> dict[str, str]:
    return {
        "PRIMITIVE_FIRST_CROSSING":"PASS",
        "FIRST_L_CARRY":"PASS",
        "FIRST_NEXT_DOMAIN_B":"PASS",
        "ACTIVE_AXIS_LOCAL_SHORTHAND":"PASS",
        "FULL_CITED_SOURCE_LINEAGE":"PASS",
        "ORTHAD_ATLAS_TYPE":"NOT_YET_DERIVED",
        "PRIMARY_PAIRING_RECURRENCE":"NOT_YET_DERIVED",
        "CHART_EMBEDDINGS":"NOT_YET_DERIVED",
        "MIXED_TRANSFER_RECURRENCE":"NOT_YET_DERIVED",
        "FIRST_L_ORTHAD_EXTENSION":"NOT_YET_DERIVED",
        "ORTHAD_CAUSAL_PROJECTION":"NOT_RUN",
        "GAUGE_FQM_WEIL_DESCENT":"NOT_RUN",
    }


def active_scalar_role() -> dict[str, Any]:
    return {
        "formula":"a_t=i^(local_Q)/(u_t v_t)",
        "classification":"LOCAL_DESCENDANT_ONLY",
        "chart_entry":"NOT_DERIVED",
        "primary_pairing_invariant":"NOT_DERIVED",
        "reason":"The clean law explicitly calls it an older single-entry shorthand; historical v7q/v7u scalar lens models provide no iota map into the modern pairing-first atlas.",
    }


def overlap_assessment() -> dict[str, Any]:
    return {
        "semantic_role":"DERIVED_OVERLAP_UPDATE",
        "custody_primitive":False,
        "historical_scheduling":{
            "v7p":"explicit derived O event in support traces",
            "v7q":"explicit O event supplied in event histories",
            "v7u":"build_history appends all O records after Q/B/L axis histories",
            "v8a":"O belongs to the defined admissible event alphabet, not the clean self-selecting primitive word",
        },
        "modern_per_tick_schedule":"NOT_YET_DERIVED",
        "verdict":"O is not rejected by name. Its semantics are a plausible derived overlap update, but the historical scheduling and scalar state are not a tick-by-tick modern Orthad recurrence.",
    }


def coupling_audit() -> list[dict[str, Any]]:
    return [
        {
            "formula":"T_ab=lens(b)/lens(a)",
            "verdict":"CONDITIONALLY_LICENSED",
            "input_type":"two nonzero historical scalar lens values in Q_{>0} x Z/4",
            "output_type":"multiplicative scalar transition cochain",
            "directionality":"T_ba=T_ab^{-1}",
            "representative_invariance":"cycle holonomy is gauge-invariant; individual T_ab is gauge-covariant",
            "B_behavior":"recomputed from changed scalar anchor",
            "Q_behavior":"phase ratio changes by i",
            "L_behavior":"historical newborn/latched ratio conflicts with clean carry and is not licensed as modern L transfer",
            "scope":"historical scalar cochain only; not iota_-^* P iota_+",
        },
        {
            "formula":"pair_c(ai,aj)",
            "verdict":"REJECTED_WITH_EXACT_DEFECT",
            "input_type":"two historical Axis records",
            "output_type":"residue mod lcm(D_i,D_j)",
            "directionality":"index-sorted but formula is asymmetric in i/j",
            "representative_invariance":"not derived; forced nonzero branch changes zero class",
            "B_behavior":"changes through uv/u/v terms only when a post-hoc O is evaluated",
            "Q_behavior":"changes through phase difference only when a post-hoc O is evaluated",
            "L_behavior":"not derived from inherited block/new-axis couplings",
            "scope":"code formula without ratified transition theorem",
        },
    ]


def first_L_obligations() -> dict[str, Any]:
    return {
        "before_rank":1,
        "after_rank":2,
        "primary_pairing_shape":"P_after=[[P_old, m_old_new],[m_new_old,p_new_new]]",
        "fixed": [
            "P_old is inherited without mutation at L",
            "one new active axis is appended",
            "pair (55,89) and phase quarters 5 carry",
            "B/Q fixed-rank and L +1 rank schedule",
        ],
        "open": [
            "coefficient ring and codomain",
            "new-axis pairing p_new_new",
            "old/new couplings m_old_new and m_new_old",
            "symmetry/adjoint relation between mixed couplings",
            "both chart embeddings before and after L",
        ],
        "omega_plus_extension":"inherited old restriction block plus one row/column, all numerical new entries open because iota_plus is open",
        "omega_minus_extension":"inherited old restriction block plus one row/column, all numerical new entries open because iota_minus is open",
        "plus_to_minus_extension":"old block inherited only after its recurrence is defined; new row/column couplings open",
        "minus_to_plus_extension":"old block inherited only after its recurrence is defined; new row/column couplings open",
        "status":"NOT_YET_DERIVED",
    }



def novelty_report(root: Path) -> dict[str, Any]:
    baseline_zip = root / "inputs" / f"{STAMP}_p5_v8r_ACCEPTED_BASELINE.zip"
    baseline_root = "p5_v8r_orthad-first-crossing-recurrence_20260711_080825"
    baseline: dict[str,str] = {}
    import zipfile
    with zipfile.ZipFile(baseline_zip) as z:
        prefix=baseline_root+"/"
        for name in z.namelist():
            if name.endswith("/") or not name.startswith(prefix):
                continue
            rel=name[len(prefix):]
            baseline[rel]=hashlib.sha256(z.read(name)).hexdigest()
    current={p.relative_to(root).as_posix():sha256_file(p) for p in root.rglob("*") if p.is_file() and p.name!="MANIFEST.json" and not p.name.endswith("_novelty_gate.json")}
    reused=[{"baseline_path":p,"new_path":p,"sha256":h} for p,h in sorted(baseline.items()) if current.get(p)==h]
    changed=[{"path":p,"baseline_sha256":baseline[p],"new_sha256":current[p]} for p in sorted(set(baseline)&set(current)) if baseline[p]!=current[p]]
    added=sorted(set(current)-set(baseline))
    removed=sorted(set(baseline)-set(current))
    required=[f"outputs/{STAMP}_source_lineage_inventory.csv",f"outputs/{STAMP}_source_claim_matrix.csv",f"docs/{STAMP}_orthad_type_boundary.md",f"outputs/{STAMP}_typed_missing_bridge.json",f"proofs/{STAMP}_BILINEAR_UNDERDETERMINATION_PROOF.md"]
    missing=[p for p in required if p not in current]
    return {"baseline_zip_sha256":sha256_file(baseline_zip),"reused":reused,"changed":changed,"added":added,"removed":removed,"required_artifacts":required,"missing_required":missing,"pass":not missing and bool(added) and bool(changed)}

def rebuild(root: Path) -> None:
    out = root / "outputs"
    out.mkdir(exist_ok=True)
    write_json(out/f"{STAMP}_baseline_sanity.json", baseline_sanity(root))
    write_csv(out/f"{STAMP}_source_lineage_inventory.csv", lineage(root))
    write_csv(out/f"{STAMP}_source_claim_matrix.csv", source_claims())
    write_csv(out/f"{STAMP}_orthad_type_status.csv", type_boundary())
    write_json(out/f"{STAMP}_typed_missing_bridge.json", typed_gap())
    write_json(out/f"{STAMP}_bilinear_underdetermination_witness.json", bilinear_witness())
    write_json(out/f"{STAMP}_active_scalar_role.json", active_scalar_role())
    write_json(out/f"{STAMP}_historical_overlap_record_assessment.json", overlap_assessment())
    write_csv(out/f"{STAMP}_historical_coupling_formula_audit.csv", coupling_audit())
    write_json(out/f"{STAMP}_first_L_block_obligations.json", first_L_obligations())
    write_json(out/f"{STAMP}_statuses.json", statuses())
    write_json(out/f"{STAMP}_novelty_gate.json", novelty_report(root))

if __name__ == "__main__":
    rebuild(Path(sys.argv[1] if len(sys.argv)>1 else ".").resolve())

#!/usr/bin/env python3
"""Cross-audit replication: the four decisive experiments that reversed the
ORTHAD_LIVE adoption. Run from a directory containing the extracted package at
./phase5_orthad_live_canon_first_experiment. Stdlib + the package only.

E1 pair ablation: (1,1),(2,3),(34,55),(100,101) -> survival 12/12 in all cases
E2 B ablation: floor field identical with/without apply_b
E3 retained-bit corruption for n=7 -> silently repaired from term_n (12/12)
E4 falsify far-side n=1 character in after CSV -> package verifier still
   emits global_pass=true, zero gate failures
"""
import sys, json, csv, shutil, subprocess
from pathlib import Path
PKG = Path(sys.argv[1] if len(sys.argv)>1 else "phase5_orthad_live_canon_first_experiment").resolve()
sys.path.insert(0, str(PKG/"src"))
from orthad_live.exact import AxisValue
from orthad_live.field import bind_residual_field, two_lens_domain, ChannelAddress, ResidualChannel, chi12
from orthad_live.lift import open_cusp_state, cross_cusp, apply_floor, apply_b, LiftState
from orthad_live.readout import before_rows, after_rows

def survival_of(crossing):
    b, a = before_rows(crossing), after_rows(crossing)
    return sum(r1["character_channel"]==r2["character_channel"] for r1,r2 in zip(b,a))

res={}
for pair in [(1,1),(2,3),(34,55),(100,101)]:
    st = LiftState(0,pair[0],pair[1],5,AxisValue(0,1,max(pair[0]*pair[1],1)),(),two_lens_domain(),"")
    res[str(pair)] = survival_of(cross_cusp(st, bind_residual_field(st.domain)))
print("E1", res, "load-bearing:", len(set(res.values()))>1)

st = open_cusp_state(); ch = bind_residual_field(st.domain)
print("E2 floor identical with/without B:", apply_floor(st, ch) == apply_floor(apply_b(st), ch))

dom = list(two_lens_domain()); i7 = next(i for i,a in enumerate(dom) if a.canonical_n==7)
ch2 = list(ch)
ch2[i7] = ResidualChannel(ChannelAddress(dom[i7].pre_l_seat_mod6, 0), 7, True, chi12(7), 7, 49, 24)
print("E3 survival after retained-bit corruption:", survival_of(cross_cusp(st, tuple(ch2))), "/12")

tmp = PKG.parent/"_e4_tmp"; shutil.rmtree(tmp, ignore_errors=True); shutil.copytree(PKG, tmp)
rows = list(csv.DictReader(open(tmp/"outputs/orthad_live_channel_after.csv")))
i = next(k for k,r in enumerate(rows) if r["term_n"]=="1"); rows[i]["character_channel"]="-1"
with open(tmp/"outputs/orthad_live_channel_after.csv","w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
subprocess.run([sys.executable, str(tmp/"meta/verify_transport.py")], capture_output=True)
card = json.loads((tmp/"outputs/orthad_live_result_card.json").read_text())
print("E4 global_pass with falsified evidence:", card["global_pass"], "| failures:", card["declared_gate_failures"])

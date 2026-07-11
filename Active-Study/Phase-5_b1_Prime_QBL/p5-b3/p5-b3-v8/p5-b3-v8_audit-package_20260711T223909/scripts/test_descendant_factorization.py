#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

# The equation D = R(P) is satisfiable for any independently chosen D
# when R may be chosen after D as a constant function.
primary = {'history':'BQQ', 'rank':1}
independent_targets = {
    '++': {'value': 17},
    '--': {'value': -4},
    '+-': {'value': 'left-to-right'},
    '-+': {'value': 'right-to-left'},
}

def constant_map(target):
    return lambda _p: target

checks={k: constant_map(v)(primary)==v for k,v in independent_targets.items()}
result={
    'equation_D_equals_R_of_P_passes': all(checks.values()),
    'descendants_were_chosen_independently': True,
    'certificate': 'Arbitrary target descendants satisfy D=R(P) through state-dependent constant maps.',
    'required_guard': 'R must factor through fixed placement data and a realization-fixed restriction constructor; identical P and structural data must force identical D.',
    'placement_checks': checks,
}
print(json.dumps(result, indent=2, sort_keys=True))
(Path(__file__).resolve().parents[1] / 'outputs' / 'descendant-factorization-vacuity.json').write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')

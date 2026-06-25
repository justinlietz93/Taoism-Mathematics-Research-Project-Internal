# Code Review Queue

Created: 2026-06-23T20:58:34Z

## Locked reminder from user

Before the close-read is considered wrapped, review the code the user found and packaged. Do not let the paper reading finish without a code-side pass.

## Rule

The code review is not a quick script verdict. It is a source-reading pass parallel to the paper close-read.

For each code target, record:

- path
- purpose / README claim
- core structures implemented
- Q-like mechanics
- B-like mechanics
- L-like mechanics
- projection / witness-loss mechanics
- shadow / q-series / modular mechanics if present
- exact constants: 4, 6, 8, 9, 12, 24, 55, 89, 4895
- whether the implementation is a demonstration, verifier, formal attack, or production-style engine
- citations to adjacent paper/package README when available

## External / Taoism-math code targets

| Priority | Path | Why it matters | Status |
|---:|---|---|---|
| 1 | `source/code/yinyang_transform.py` | Likely direct transformation/geometry code; check for Yin-Yang phase geometry, rotation, center/radius, modular/coordinate transformation. | queued |
| 2 | `source/code/MFE_pub-main/` | External numerical code package; check whether MFE/Four-Element/field code has center/axis, grid, boundary, iteration, RHS, interpolation, field mechanics. | queued |
| 3 | `source/code/iching-wilhelm-dataset-master/` | I Ching hexagram data/wheel; check binary encoding, ordering, line transformations, wheel/circular arrangement. | queued |
| 4 | `source/code/pencil-code-master.zip` | External simulation code; check only if paper linkage indicates relevance. | queued |

## Internal Phase Calculus code targets

| Priority | Path | Why it matters | Status |
|---:|---|---|---|
| 1 | `source/Phase-Calculus-Research-Pkgs/CF19_The_Full_Lifted_Object/code/farey_balanced/` | Direct B/Farey depth anchor implementation; check `(55,89)`, `4895`, depth 9, assembly kernel. | queued |
| 2 | `source/Phase-Calculus-Research-Pkgs/CF19_The_Full_Lifted_Object/code/xi_full_engine/` | Xi engine source; check retained-state/operator mechanics. | queued |
| 3 | `source/Phase-Calculus-Research-Pkgs/CF19_The_Full_Lifted_Object/code/python/overflow_to_55_89_code.py` | Direct depth/floor-anchor witness. | queued |
| 4 | `source/Phase-Calculus-Research-Pkgs/CF19_The_Full_Lifted_Object/code/python/ramanujan_residual_balanced_windows_code.py` | Shadow/residual bridge; check q-series and window logic. | queued |
| 5 | `source/Phase-Calculus-Research-Pkgs/*/lean*`, `formal/`, `sympy/`, `scripts/` | Formal/code verification package wide pass after priority code. | queued |

## First code-pass output target

Create `notes/08_CODE_CLOSE_READ_PASS1.md` with concrete source-level notes. No global judgement from code until this exists.

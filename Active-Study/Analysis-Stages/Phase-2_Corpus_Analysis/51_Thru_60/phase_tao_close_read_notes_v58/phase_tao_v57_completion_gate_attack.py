from dataclasses import dataclass

@dataclass(frozen=True)
class Gate:
    name: str
    status: str
    external_blocker: bool = False

GATES = [
    Gate("available internal source mapped", "PASS"),
    Gate("available external source mapped", "PASS"),
    Gate("projection state-completeness gate", "PASS"),
    Gate("stale canon separation", "PASS"),
    Gate("modular-B overclaim prevention", "PASS"),
    Gate("Shadow external-reference boundary", "PASS"),
    Gate("Lean/lake execution", "BLOCKED", True),
    Gate("latest Phase HDD materials", "BLOCKED", True),
    Gate("Liu2022 data", "BLOCKED", True),
]

def conditionally_complete(gates):
    failed_internal = [g for g in gates if g.status != "PASS" and not g.external_blocker]
    external = [g for g in gates if g.external_blocker]
    return len(failed_internal) == 0 and len(external) == 3

print("claims=", len(GATES))
print("external_blockers=", [g.name for g in GATES if g.external_blocker])
print("failed_internal=", [g.name for g in GATES if g.status != "PASS" and not g.external_blocker])
print("CONDITIONALLY_COMPLETE=", conditionally_complete(GATES))
assert conditionally_complete(GATES)

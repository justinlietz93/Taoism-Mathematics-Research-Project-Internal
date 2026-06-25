from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, List, Tuple

from .coupling import echo_gain, extract_transfer_from_memory, matrix_from_transfer, max_triangle_residual_from_transfer
from .overset import graph_from_history
from .scenarios import Scenario
from .walkers import run_voidwalkers


@dataclass
class ScenarioResult:
    name: str
    expected_admissible: bool
    visible_projection: Tuple[int, ...]
    true_coupling_signature: Tuple[Tuple[int, int, int], ...]
    discovered_edges: int
    total_edges: int
    discovered_all_edges: bool
    true_cycle_residual: int
    discovered_cycle_residual: int
    topology_spikes: int
    cycle_hits: int
    inhibition_max: float
    admitted: bool
    matrix_match: bool
    blind_error: float
    assisted_error: float
    coupling_echo_gain: float
    pass_case: bool

    def to_dict(self) -> dict:
        return asdict(self)


def run_scenario(sc: Scenario, ticks: int = 160, walkers: int = 16, seed: int = 0) -> ScenarioResult:
    graph = graph_from_history(sc.compiled)
    maps = run_voidwalkers(graph, ticks=ticks, walkers=walkers, seed=seed)
    discovered = extract_transfer_from_memory(graph, maps)
    true_matrix = sc.compiled.matrix()
    discovered_matrix = matrix_from_transfer(sc.compiled.n, sc.compiled.modulus, discovered)
    true_residual = graph.max_cycle_residual()
    discovered_residual = max_triangle_residual_from_transfer(sc.compiled.n, sc.compiled.modulus, discovered)
    snap = maps.snapshot(ticks)
    admitted = bool(len(discovered) == len(graph.edges()) and discovered_residual == 0 and snap["topology_spikes"] == 0)
    matrix_match = true_matrix == discovered_matrix
    eg = echo_gain(true_matrix, discovered_matrix, sc.compiled.modulus, seed=seed)
    if sc.expected_admissible:
        pass_case = admitted and matrix_match and eg["coupling_echo_gain"] >= 0.99
    else:
        pass_case = (not admitted) and snap["topology_spikes"] > 0 and discovered_residual != 0
    return ScenarioResult(
        name=sc.name,
        expected_admissible=bool(sc.expected_admissible),
        visible_projection=sc.compiled.visible_id(),
        true_coupling_signature=sc.compiled.coupling_signature(),
        discovered_edges=len(discovered),
        total_edges=len(graph.edges()),
        discovered_all_edges=len(discovered) == len(graph.edges()),
        true_cycle_residual=int(true_residual),
        discovered_cycle_residual=int(discovered_residual),
        topology_spikes=int(snap["topology_spikes"]),
        cycle_hits=int(snap["cycle_hits"]),
        inhibition_max=float(snap["inhibition_max"]),
        admitted=admitted,
        matrix_match=matrix_match,
        blind_error=float(eg["blind_error"]),
        assisted_error=float(eg["assisted_error"]),
        coupling_echo_gain=float(eg["coupling_echo_gain"]),
        pass_case=bool(pass_case),
    )

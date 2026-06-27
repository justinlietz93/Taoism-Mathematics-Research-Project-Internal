from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List

from .events import Event

@dataclass(frozen=True)
class TraceNormalForm:
    layers: tuple[tuple[str, ...], ...]

    def signature(self) -> str:
        return " | ".join("{" + ",".join(layer) + "}" for layer in self.layers)


def independent(a: Event, b: Event) -> bool:
    return not a.depends_on(b)


def foata_normal_form(events: Iterable[Event]) -> TraceNormalForm:
    """Greedy Cartier-Foata layering for the dependency relation.

    Earlier dependent events force later events to a later layer. Independent events may
    sit in the same layer. Tokens are sorted inside each layer to erase irrelevant
    linearization order.
    """
    layers: List[List[Event]] = []
    for ev in events:
        min_layer = 0
        for i, layer in enumerate(layers):
            if any(ev.depends_on(prev) for prev in layer):
                min_layer = i + 1
        while len(layers) <= min_layer:
            layers.append([])
        layers[min_layer].append(ev)
    token_layers = tuple(tuple(sorted(e.token() for e in layer)) for layer in layers if layer)
    return TraceNormalForm(token_layers)


def same_trace_class(a: Iterable[Event], b: Iterable[Event]) -> bool:
    return foata_normal_form(a).signature() == foata_normal_form(b).signature()

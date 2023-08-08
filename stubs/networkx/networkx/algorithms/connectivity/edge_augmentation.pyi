from collections.abc import Iterable
from typing import Any, TypeVar

from networkx.classes.graph import Graph

_N = TypeVar("_N")

def is_k_edge_connected(G: Graph[Any], k: int) -> Any: ...
def is_locally_k_edge_connected(G: Any, s: Any, t: Any, k: Any) -> Any: ...
def k_edge_augmentation(
    G: Graph[_N],
    k: int,
    avail: tuple[_N, _N] | tuple[_N, _N, dict[str, int]] | None = ...,
    weight: str | None = ...,
    partial: bool = ...,
) -> Iterable[tuple[_N, _N]]: ...

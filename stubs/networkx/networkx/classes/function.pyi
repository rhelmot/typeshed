from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Any, TypeVar, overload
from typing_extensions import Literal

from networkx.classes.graph import Graph
from networkx.classes.graphviews import subgraph_view as subgraph_view

__all__ = [
    "nodes",
    "edges",
    "degree",
    "degree_histogram",
    "neighbors",
    "number_of_nodes",
    "number_of_edges",
    "density",
    "is_directed",
    "freeze",
    "is_frozen",
    "subgraph",
    "subgraph_view",
    "induced_subgraph",
    "reverse_view",
    "edge_subgraph",
    "restricted_view",
    "to_directed",
    "to_undirected",
    "add_star",
    "add_path",
    "add_cycle",
    "create_empty_copy",
    "set_node_attributes",
    "get_node_attributes",
    "set_edge_attributes",
    "get_edge_attributes",
    "all_neighbors",
    "non_neighbors",
    "non_edges",
    "common_neighbors",
    "is_weighted",
    "is_negatively_weighted",
    "is_empty",
    "selfloop_edges",
    "nodes_with_selfloops",
    "number_of_selfloops",
    "path_weight",
    "is_path",
]
_T = TypeVar("_T")
_U = TypeVar("_U")

def nodes(G): ...
def edges(G, nbunch: Incomplete | None = ...): ...
def degree(G, nbunch: Incomplete | None = ..., weight: Incomplete | None = ...): ...
def neighbors(G, n): ...
def number_of_nodes(G): ...
def number_of_edges(G): ...
def density(G): ...
def degree_histogram(G): ...
def is_directed(G): ...
def freeze(G): ...
def is_frozen(G): ...
def add_star(G_to_add_to, nodes_for_star, **attr) -> None: ...
def add_path(G_to_add_to, nodes_for_path, **attr) -> None: ...
def add_cycle(G_to_add_to, nodes_for_cycle, **attr) -> None: ...
def subgraph(G, nbunch): ...
def induced_subgraph(G: Graph[_T], nbunch: _T | Iterable[_T] | None) -> Graph[_T]: ...
def edge_subgraph(G, edges): ...
def restricted_view(G, nodes, edges): ...
def reverse_view(digraph): ...
def to_directed(graph): ...
def to_undirected(graph): ...
def create_empty_copy(G, with_data: bool = ...): ...
def set_node_attributes(G: Graph[_T], values: dict[_T, Incomplete], name: str = ...) -> None: ...

# Can "Any scalar value" be enforced?
@overload
def set_node_attributes(G: Graph[Any], values, name: str = ...) -> None: ...
@overload
def set_node_attributes(G: Graph[_T], values: dict[_T, dict[Incomplete, Incomplete]], name: None = ...) -> None: ...
def get_node_attributes(G: Graph[_T], name: str) -> dict[_T, Incomplete]: ...
@overload
def set_edge_attributes(G: Graph[_T], values: dict[tuple[_T, _T], Incomplete], name: str = ...) -> None: ...
@overload
def set_edge_attributes(G: Graph[Any], values, name: None = ...) -> None: ...
def get_edge_attributes(G: Graph[_T], name: str) -> dict[tuple[_T, _T], Incomplete]: ...
def all_neighbors(graph: Graph[_T], node: _T) -> Iterable[_T]: ...
def non_neighbors(graph: Graph[_T], node: _T) -> Iterable[_T]: ...
def non_edges(graph: Graph[_T]) -> Iterable[tuple[_T, _T]]: ...
def common_neighbors(G: Graph[_T], u: _T, v: _T) -> Iterable[_T]: ...
def is_weighted(G: Graph[_T], edge: tuple[_T, _T] | None = ..., weight: str | None = ...) -> bool: ...
def is_negatively_weighted(G: Graph[_T], edge: tuple[_T, _T] | None = ..., weight: str | None = ...): ...
def is_empty(G: Graph[Any]) -> bool: ...
def nodes_with_selfloops(G: Graph[_T]) -> Iterable[_T]: ...
@overload
def selfloop_edges(
    G: Graph[_T], data: Literal[False] = False, keys: Literal[False] = False, default=None
) -> Iterable[tuple[_T, _T]]: ...
@overload
def selfloop_edges(
    G: Graph[_T], data: Literal[True], keys: Literal[False] = False, default=None
) -> Iterable[tuple[_T, _T, dict[str, Incomplete]]]: ...
@overload
def selfloop_edges(
    G: Graph[_T], data: str, keys: Literal[False] = False, default: _U | None = None
) -> Iterable[tuple[_T, _T, _U]]: ...
@overload
def selfloop_edges(G: Graph[_T], data: Literal[False], keys: Literal[True], default=None) -> Iterable[tuple[_T, _T, int]]: ...
@overload
def selfloop_edges(
    G: Graph[_T], data: Literal[False] = False, *, keys: Literal[True], default=None
) -> Iterable[tuple[_T, _T, int]]: ...
@overload
def selfloop_edges(
    G: Graph[_T], data: Literal[True], keys: Literal[True], default=None
) -> Iterable[tuple[_T, _T, int, dict[str, Incomplete]]]: ...
@overload
def selfloop_edges(
    G: Graph[_T], data: str, keys: Literal[True], default: _U | None = None
) -> Iterable[tuple[_T, _T, int, _U]]: ...
def number_of_selfloops(G: Graph[Any]) -> int: ...
def is_path(G, path) -> bool: ...
def path_weight(G, path, weight) -> int: ...

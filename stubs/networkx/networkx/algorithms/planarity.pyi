from collections.abc import Iterable
from typing import Any, Generic, TypeVar

import networkx as nx

def check_planarity(G: Any, counterexample: bool = ...) -> Any: ...

_N = TypeVar("_N")

class Interval:
    low: Any = ...
    high: Any = ...
    def __init__(self, low: Any | None = ..., high: Any | None = ...) -> None: ...
    def empty(self) -> Any: ...
    def copy(self) -> Any: ...
    def conflicting(self, b: Any, planarity_state: Any) -> Any: ...

class ConflictPair:
    left: Any = ...
    right: Any = ...
    def __init__(self, left: Any = ..., right: Any = ...) -> None: ...
    def swap(self) -> None: ...
    def lowest(self, planarity_state: Any) -> Any: ...

class LRPlanarity:
    G: Any = ...
    roots: Any = ...
    height: Any = ...
    lowpt: Any = ...
    lowpt2: Any = ...
    nesting_depth: Any = ...
    parent_edge: Any = ...
    DG: Any = ...
    adjs: Any = ...
    ordered_adjs: Any = ...
    ref: Any = ...
    side: Any = ...
    S: Any = ...
    stack_bottom: Any = ...
    lowpt_edge: Any = ...
    left_ref: Any = ...
    right_ref: Any = ...
    embedding: Any = ...
    def __init__(self, G: Any) -> None: ...
    def lr_planarity(self) -> Any: ...
    def lr_planarity_recursive(self) -> Any: ...
    def dfs_orientation(self, v: Any) -> Any: ...
    def dfs_orientation_recursive(self, v: Any) -> None: ...
    def dfs_testing(self, v: Any) -> Any: ...
    def dfs_testing_recursive(self, v: Any) -> Any: ...
    def add_constraints(self, ei: Any, e: Any) -> Any: ...
    def remove_back_edges(self, e: Any) -> None: ...
    def dfs_embedding(self, v: Any) -> Any: ...
    def dfs_embedding_recursive(self, v: Any) -> None: ...
    def sign(self, e: Any) -> Any: ...
    def sign_recursive(self, e: Any) -> Any: ...

class PlanarEmbedding(Generic[_N], nx.DiGraph[_N]):
    def get_data(self) -> dict[_N, list[_N]]: ...
    def set_data(self, data: dict[_N, list[_N]]) -> None: ...
    def neighbors_cw_order(self, v: _N) -> Iterable[_N]: ...
    def check_structure(self) -> None: ...
    def add_half_edge_ccw(self, start_node: _N, end_node: _N, reference_neighbor: _N) -> None: ...
    def add_half_edge_cw(self, start_node: _N, end_node: _N, reference_neighbor: _N) -> None: ...
    def connect_components(self, v: _N, w: _N) -> None: ...
    def add_half_edge_first(self, start_node: _N, end_node: _N) -> None: ...
    def next_face_half_edge(self, v: _N, w: _N) -> tuple[_N, _N]: ...
    def traverse_face(self, v: _N, w: _N, mark_half_edges: set[tuple[_N, _N]] | None = ...) -> list[_N]: ...
    def is_directed(self) -> bool: ...

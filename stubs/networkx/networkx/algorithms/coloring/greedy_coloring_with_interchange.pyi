# Stubs for networkx.algorithms.coloring.greedy_coloring_with_interchange (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from _typeshed import Incomplete

class _Node:
    node_id: Incomplete
    color: int
    adj_list: Incomplete
    adj_color: Incomplete
    def __init__(self, node_id, n) -> None: ...
    def assign_color(self, adj_entry, color) -> None: ...
    def clear_color(self, adj_entry, color) -> None: ...
    def iter_neighbors(self) -> None: ...
    def iter_neighbors_color(self, color) -> None: ...

class AdjEntry:
    node_id: Incomplete
    next: Incomplete
    mate: Incomplete
    col_next: Incomplete
    col_prev: Incomplete
    def __init__(self, node_id) -> None: ...

def greedy_coloring_with_interchange(original_graph, nodes): ...

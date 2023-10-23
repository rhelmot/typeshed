from _typeshed import Incomplete
from collections.abc import Iterator
from typing import TypeVar

from networkx.classes.graph import Graph

_T = TypeVar("_T")

def dfs_edges(G: Graph[_T], source: _T | None = None, depth_limit: int | None = None) -> Iterator[tuple[_T, _T]]: ...
def dfs_tree(G, source: Incomplete | None = None, depth_limit: Incomplete | None = None): ...
def dfs_predecessors(G, source: Incomplete | None = None, depth_limit: Incomplete | None = None): ...
def dfs_successors(G, source: Incomplete | None = None, depth_limit: Incomplete | None = None): ...
def dfs_postorder_nodes(G, source: Incomplete | None = None, depth_limit: Incomplete | None = None): ...
def dfs_preorder_nodes(G, source: Incomplete | None = None, depth_limit: Incomplete | None = None): ...
def dfs_labeled_edges(G, source: Incomplete | None = None, depth_limit: Incomplete | None = None) -> None: ...

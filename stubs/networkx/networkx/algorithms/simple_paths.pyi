from _typeshed import Incomplete
from collections.abc import Iterator
from typing import TypeVar

from networkx.classes.graph import Graph

_T = TypeVar("_T")

def is_simple_path(G: Graph[_T], nodes: list[_T]): ...
def all_simple_paths(G: Graph[_T], source: _T, target: _T, cutoff: Incomplete | None = ...) -> Iterator[list[_T]]: ...
def shortest_simple_paths(G: Graph[_T], source: _T, target: _T, weight: Incomplete | None = ...) -> Iterator[list[_T]]: ...

class PathBuffer:
    paths: Incomplete = ...
    sortedpaths: Incomplete = ...
    counter: Incomplete = ...
    def __init__(self) -> None: ...
    def __len__(self): ...
    def push(self, cost, path) -> None: ...
    def pop(self): ...

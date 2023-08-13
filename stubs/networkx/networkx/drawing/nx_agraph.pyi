from _typeshed import Incomplete
from collections.abc import Callable
from io import TextIOBase
from typing import TypeVar
from typing import Any, TypeVar

import pygraphviz
from networkx.classes.graph import Graph

_T = TypeVar("_T")

def from_agraph(A: Incomplete, create_using: Incomplete | None = ...) -> Graph[Incomplete]: ...
def to_agraph(N: Graph[Incomplete]) -> pygraphviz.agraph.AGraph: ...
def write_dot(G: Graph[Incomplete], path: str | TextIOBase) -> None: ...
def read_dot(path: str | TextIOBase) -> Graph[Incomplete]: ...
def graphviz_layout(G: Graph[_T], prog: str = ..., root: str | None = ..., args: str = ...) -> dict[_T, tuple[float, float]]: ...

pygraphviz_layout = graphviz_layout

def view_pygraphviz(
    G: Graph[_T],
    edgelabel: str | Callable[[_T], str] | None = ...,
    prog: str = ...,
    args: str = ...,
    suffix: str = ...,
    path: str | None = ...,
): ...

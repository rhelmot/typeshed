from _typeshed import Incomplete
from collections.abc import Callable, Iterable
from typing import overload
from typing_extensions import Literal

import numpy
import pandas.core.dtypes.base
from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph, _Node
from networkx.classes.multidigraph import MultiDiGraph
from networkx.classes.multigraph import MultiGraph

def to_pandas_adjacency(
    G: Graph[_Node],
    nodelist: list[_Node] | None = ...,
    dtype: numpy.dtype[Incomplete] | None = ...,
    order: Literal["C", "F"] | None = ...,
    multigraph_weight: Callable[[Iterable[float]], float] = ...,
    weight: str = ...,
    nonedge: float = ...,
) -> pandas.DataFrame: ...
@overload
def from_pandas_adjacency(df: pandas.DataFrame, create_using: type[Graph[Incomplete]] = ...) -> Graph[Incomplete]: ...
@overload
def from_pandas_adjacency(df: pandas.DataFrame, create_using: type[DiGraph[Incomplete]] = ...) -> DiGraph[Incomplete]: ...
@overload
def from_pandas_adjacency(df: pandas.DataFrame, create_using: type[MultiGraph[Incomplete]] = ...) -> MultiGraph[Incomplete]: ...
@overload
def from_pandas_adjacency(
    df: pandas.DataFrame, create_using: type[MultiDiGraph[Incomplete]] = ...
) -> MultiDiGraph[Incomplete]: ...
def to_pandas_edgelist(
    G: Graph[_Node],
    source: str | int = ...,
    target: str | int = ...,
    nodelist: list[_Node] | None = ...,
    dtype: pandas.core.dtypes.base.ExtensionDtype | None = ...,
    edge_key: str | int | None = ...,
) -> pandas.DataFrame: ...
@overload
def from_pandas_edgelist(
    df: pandas.DataFrame,
    source: str | int = ...,
    target: str | int = ...,
    edge_attr: str | int | Iterable[str | int] | Literal[True] | None = ...,
    create_using: type[Graph[Incomplete]] = ...,
) -> Graph[Incomplete]: ...
@overload
def from_pandas_edgelist(
    df: pandas.DataFrame,
    source: str | int = ...,
    target: str | int = ...,
    edge_attr: str | int | Iterable[str | int] | Literal[True] | None = ...,
    create_using: type[DiGraph[Incomplete]] = ...,
) -> DiGraph[Incomplete]: ...
@overload
def from_pandas_edgelist(
    df: pandas.DataFrame,
    source: str | int = ...,
    target: str | int = ...,
    edge_attr: str | int | Iterable[str | int] | Literal[True] | None = ...,
    create_using: type[MultiGraph[Incomplete]] = ...,
) -> MultiGraph[Incomplete]: ...
@overload
def from_pandas_edgelist(
    df: pandas.DataFrame,
    source: str | int = ...,
    target: str | int = ...,
    edge_attr: str | int | Iterable[str | int] | Literal[True] | None = ...,
    create_using: type[MultiDiGraph[Incomplete]] = ...,
) -> MultiDiGraph[Incomplete]: ...
def to_numpy_array(
    G: Graph[_Node],
    nodelist: list[_Node] | None = ...,
    dtype: numpy.dtype[Incomplete] | None = ...,
    order: Literal["C", "F"] | None = ...,
    multigraph_weight: Callable[[Iterable[float]], float] = ...,
    weight: str = ...,
    nonedge: float = ...,
) -> numpy.ndarray[Incomplete, numpy.dtype[Incomplete]]: ...
@overload
def from_numpy_array(
    A: numpy.ndarray[Incomplete, Incomplete], parallel_edges: bool = ..., create_using: type[Graph[Incomplete]] = ...
) -> Graph[Incomplete]: ...
@overload
def from_numpy_array(
    A: numpy.ndarray[Incomplete, Incomplete], parallel_edges: bool = ..., create_using: type[DiGraph[Incomplete]] = ...
) -> DiGraph[Incomplete]: ...
@overload
def from_numpy_array(
    A: numpy.ndarray[Incomplete, Incomplete], parallel_edges: bool = ..., create_using: type[MultiGraph[Incomplete]] = ...
) -> MultiGraph[Incomplete]: ...
@overload
def from_numpy_array(
    A: numpy.ndarray[Incomplete, Incomplete], parallel_edges: bool = ..., create_using: type[MultiDiGraph[Incomplete]] = ...
) -> MultiDiGraph[Incomplete]: ...

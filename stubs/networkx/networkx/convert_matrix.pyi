from _typeshed import Incomplete
from collections.abc import Callable, Iterable
from typing_extensions import Literal

import numpy
from networkx.classes.graph import Graph, _Node
from pandas import DataFrame
from pandas.core.dtypes.base import ExtensionDtype

def to_pandas_adjacency(
    G: Graph[_Node],
    nodelist: list[_Node] | None = None,
    dtype: numpy.dtype[Incomplete] | None = None,
    order: Literal["C", "F"] | None = None,
    multigraph_weight: Callable[[Iterable[float]], float] = ...,
    weight: str = "weight",
    nonedge: float = 0.0,
) -> DataFrame: ...
def from_pandas_adjacency(df: DataFrame, create_using: type[Graph[Incomplete]] | None = None) -> Graph[Incomplete]: ...
def to_pandas_edgelist(
    G: Graph[_Node],
    source: str | int = "source",
    target: str | int = "target",
    nodelist: list[_Node] | None = None,
    dtype: ExtensionDtype | None = None,
    edge_key: str | int | None = None,
) -> DataFrame: ...
def from_pandas_edgelist(
    df: DataFrame,
    source: str | int = "source",
    target: str | int = "target",
    edge_attr: str | int | Iterable[str | int] | Literal[True] | None = None,
    create_using: type[Graph[Incomplete]] | None = None,
) -> Graph[Incomplete]: ...
def to_numpy_array(
    G: Graph[_Node],
    nodelist: list[_Node] | None = None,
    dtype: numpy.dtype[Incomplete] | None = None,
    order: Literal["C", "F"] | None = None,
    multigraph_weight: Callable[[Iterable[float]], float] = ...,
    weight: str = "weight",
    nonedge: float = 0.0,
) -> numpy.ndarray[Incomplete, numpy.dtype[Incomplete]]: ...
def from_numpy_array(
    A: numpy.ndarray[Incomplete, Incomplete], parallel_edges: bool = False, create_using: type[Graph[Incomplete]] | None = None
) -> Graph[Incomplete]: ...

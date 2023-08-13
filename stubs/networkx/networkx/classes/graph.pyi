from _typeshed import Incomplete
from collections.abc import Callable, Collection, Hashable, Iterable, Iterator, Mapping, MutableMapping
from typing import ClassVar, Generic, TypeVar, overload
from typing_extensions import Self, TypeAlias

from networkx.classes.coreviews import AdjacencyView
from networkx.classes.digraph import DiGraph
from networkx.classes.reportviews import DiDegreeView, NodeView, OutEdgeView
from networkx.convert import Data

_Node = TypeVar("_Node", bound=Hashable)
Edge: TypeAlias = tuple[_Node, _Node]
EdgePlus: TypeAlias = Edge[_Node] | tuple[_Node, _Node, dict[str, Incomplete]]
MapFactory: TypeAlias = Callable[[], MutableMapping[str, Incomplete]]
NBunch: TypeAlias = None | _Node | Iterable[_Node]

class Graph(Collection[_Node], Generic[_Node]):
    node_dict_factory: ClassVar[MapFactory]
    node_attr_dict_factory: ClassVar[MapFactory]
    adjlist_outer_dict_factory: ClassVar[MapFactory]
    adjlist_inner_dict_factory: ClassVar[MapFactory]
    edge_attr_dict_factory: ClassVar[MapFactory]
    graph_attr_dict_factory: ClassVar[MapFactory]

    def to_directed_class(self) -> type[DiGraph[_Node]]: ...
    def to_undirected_class(self) -> type[Graph[_Node]]: ...
    def __init__(self, incoming_graph_data: Data[_Node] | None = None, **attr) -> None: ...

    adj: AdjacencyView[_Node, _Node, dict[str, Incomplete]]
    name: str

    def __getitem__(self, n: _Node) -> MutableMapping[Hashable, Incomplete]: ...
    def __iter__(self) -> Iterator[_Node]: ...
    def __contains__(self, n: object) -> bool: ...
    def __len__(self) -> int: ...
    def add_node(self, node_for_adding: _Node, **attr) -> None: ...
    def add_nodes_from(
        self, nodes_for_adding: Iterable[_Node | tuple[_Node, dict[str, Incomplete]]], **attr: Incomplete
    ) -> None: ...
    def remove_node(self, n: _Node) -> None: ...
    def remove_nodes_from(self, nodes: Iterable[_Node]) -> None: ...
    nodes: NodeView[_Node]
    def number_of_nodes(self) -> int: ...
    def order(self) -> int: ...
    def has_node(self, n: _Node) -> bool: ...
    def add_edge(self, u_of_edge: _Node, v_of_edge: _Node, **attr) -> None: ...
    def add_edges_from(self, ebunch_to_add: Iterable[EdgePlus[_Node]], **attr) -> None: ...
    def add_weighted_edges_from(
        self, ebunch_to_add: Iterable[tuple[_Node, _Node, Incomplete]], weight: str = "weight", **attr: Incomplete
    ) -> None: ...
    def remove_edge(self, u: _Node, v: _Node) -> None: ...
    def remove_edges_from(self, ebunch: Iterable[EdgePlus[_Node]]) -> None: ...
    @overload
    def update(self, edges: Graph[_Node], nodes: None = None) -> None: ...
    @overload
    def update(
        self, edges: Graph[_Node] | Iterable[EdgePlus[_Node]] | None = None, nodes: Iterable[_Node] | None = None
    ) -> None: ...
    def has_edge(self, u: _Node, v: _Node) -> bool: ...
    def neighbors(self, n: _Node) -> Iterable[_Node]: ...
    edges: OutEdgeView[_Node]
    def get_edge_data(self, u: _Node, v: _Node, default=None) -> Mapping[str, Incomplete]: ...
    def adjacency(self) -> Iterable[tuple[_Node, Mapping[_Node, Mapping[str, Incomplete]]]]: ...

    degree: DiDegreeView[_Node]

    def clear(self) -> None: ...
    def clear_edges(self) -> None: ...
    def is_multigraph(self) -> bool: ...
    def is_directed(self) -> bool: ...
    def copy(self, as_view: bool = False) -> Self: ...
    def to_directed(self, as_view: bool = False) -> DiGraph[_Node]: ...
    def to_undirected(self, as_view: bool = False) -> Graph[_Node]: ...
    def subgraph(self, nodes: Iterable[_Node]) -> Graph[_Node]: ...
    def edge_subgraph(self, edges: Iterable[Edge[_Node]]) -> Graph[_Node]: ...
    @overload
    def size(self, weight: None = None) -> int: ...
    @overload
    def size(self, weight: str) -> float: ...
    def number_of_edges(self, u: _Node | None = None, v: _Node | None = None) -> int: ...
    def nbunch_iter(self, nbunch: NBunch[_Node] = None) -> Iterable[_Node]: ...

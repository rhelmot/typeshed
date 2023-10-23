from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node

def enumerate_all_cliques(G: Graph[_Node]) -> Iterable[list[_Node]]: ...
def find_cliques(G: Graph[_Node], nodes: list[_Node] | None = None) -> Iterable[list[_Node]]: ...
def find_cliques_recursive(G: Graph[_Node], nodes: list[_Node] | None = None) -> Iterable[list[_Node]]: ...
def make_max_clique_graph(G: Graph[_Node], create_using: type[Graph[_Node]] | None = None) -> Graph[_Node]: ...
def make_clique_bipartite(
    G: Graph[_Node], fpos: None = None, create_using: type[Graph[_Node]] | None = None, name: None = None
) -> Graph[_Node]: ...
def graph_clique_number(G: Graph[_Node], cliques: list[_Node] | None = None) -> int: ...
def graph_number_of_cliques(G: Graph[_Node], cliques: list[_Node] | None = None) -> int: ...
def node_clique_number(G: Graph[_Node], nodes: list[_Node] | None = None, cliques: list[list[_Node]] | None = None) -> int: ...
def number_of_cliques(G: Graph[_Node], nodes: list[_Node] | None = None, cliques: list[list[_Node]] | None = None) -> int: ...
def cliques_containing_node(
    G: Graph[_Node], nodes: list[_Node] | None = None, cliques: list[list[_Node]] | None = None
) -> Iterable[list[_Node]]: ...

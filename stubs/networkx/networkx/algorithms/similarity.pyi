from _typeshed import Incomplete
from operator import *

def graph_edit_distance(
    G1,
    G2,
    node_match: Incomplete | None = None,
    edge_match: Incomplete | None = None,
    node_subst_cost: Incomplete | None = None,
    node_del_cost: Incomplete | None = None,
    node_ins_cost: Incomplete | None = None,
    edge_subst_cost: Incomplete | None = None,
    edge_del_cost: Incomplete | None = None,
    edge_ins_cost: Incomplete | None = None,
    upper_bound: Incomplete | None = None,
): ...
def optimal_edit_paths(
    G1,
    G2,
    node_match: Incomplete | None = None,
    edge_match: Incomplete | None = None,
    node_subst_cost: Incomplete | None = None,
    node_del_cost: Incomplete | None = None,
    node_ins_cost: Incomplete | None = None,
    edge_subst_cost: Incomplete | None = None,
    edge_del_cost: Incomplete | None = None,
    edge_ins_cost: Incomplete | None = None,
    upper_bound: Incomplete | None = None,
): ...
def optimize_graph_edit_distance(
    G1,
    G2,
    node_match: Incomplete | None = None,
    edge_match: Incomplete | None = None,
    node_subst_cost: Incomplete | None = None,
    node_del_cost: Incomplete | None = None,
    node_ins_cost: Incomplete | None = None,
    edge_subst_cost: Incomplete | None = None,
    edge_del_cost: Incomplete | None = None,
    edge_ins_cost: Incomplete | None = None,
    upper_bound: Incomplete | None = None,
) -> None: ...
def optimize_edit_paths(
    G1,
    G2,
    node_match: Incomplete | None = None,
    edge_match: Incomplete | None = None,
    node_subst_cost: Incomplete | None = None,
    node_del_cost: Incomplete | None = None,
    node_ins_cost: Incomplete | None = None,
    edge_subst_cost: Incomplete | None = None,
    edge_del_cost: Incomplete | None = None,
    edge_ins_cost: Incomplete | None = None,
    upper_bound: Incomplete | None = None,
    strictly_decreasing: bool = True,
): ...

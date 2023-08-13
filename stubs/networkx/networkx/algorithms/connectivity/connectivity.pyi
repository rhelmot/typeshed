# Stubs for networkx.algorithms.connectivity.connectivity (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from _typeshed import Incomplete

def local_node_connectivity(
    G,
    s,
    t,
    flow_func: Incomplete | None = None,
    auxiliary: Incomplete | None = None,
    residual: Incomplete | None = None,
    cutoff: Incomplete | None = None,
): ...
def node_connectivity(G, s: Incomplete | None = None, t: Incomplete | None = None, flow_func: Incomplete | None = None): ...
def average_node_connectivity(G, flow_func: Incomplete | None = None): ...
def all_pairs_node_connectivity(G, nbunch: Incomplete | None = None, flow_func: Incomplete | None = None): ...
def local_edge_connectivity(
    G,
    s,
    t,
    flow_func: Incomplete | None = None,
    auxiliary: Incomplete | None = None,
    residual: Incomplete | None = None,
    cutoff: Incomplete | None = None,
): ...
def edge_connectivity(
    G,
    s: Incomplete | None = None,
    t: Incomplete | None = None,
    flow_func: Incomplete | None = None,
    cutoff: Incomplete | None = None,
): ...

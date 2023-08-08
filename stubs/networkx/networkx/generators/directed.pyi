# Stubs for networkx.generators.directed (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def gn_graph(n: Any, kernel: Any | None = ..., create_using: Any | None = ..., seed: Any | None = ...) -> Any: ...
def gnr_graph(n: Any, p: Any, create_using: Any | None = ..., seed: Any | None = ...) -> Any: ...
def gnc_graph(n: Any, create_using: Any | None = ..., seed: Any | None = ...) -> Any: ...
def scale_free_graph(
    n: Any,
    alpha: float = ...,
    beta: float = ...,
    gamma: float = ...,
    delta_in: float = ...,
    delta_out: int = ...,
    create_using: Any | None = ...,
    seed: Any | None = ...,
) -> Any: ...
def random_k_out_graph(n: Any, k: Any, alpha: Any, self_loops: bool = ..., seed: Any | None = ...) -> Any: ...

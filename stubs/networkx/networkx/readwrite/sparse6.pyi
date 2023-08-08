# Stubs for networkx.readwrite.sparse6 (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def from_sparse6_bytes(string: Any) -> Any: ...
def to_sparse6_bytes(G: Any, nodes: Any | None = ..., header: bool = ...) -> Any: ...
def read_sparse6(path: Any) -> Any: ...
def write_sparse6(G: Any, path: Any, nodes: Any | None = ..., header: bool = ...) -> None: ...

from _typeshed import Incomplete
from typing import TypeVar

from networkx.classes.digraph import DiGraph

_T = TypeVar("_T")

def complement(G: Incomplete) -> Incomplete: ...
def reverse(G: DiGraph[_T], copy: bool = ...) -> DiGraph[_T]: ...

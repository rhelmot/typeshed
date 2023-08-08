from collections.abc import Iterable
from typing import Any
from typing_extensions import TypeAlias

import numpy
import scipy
from networkx.classes.graph import EdgePlus, Graph, _Node

Data: TypeAlias = (
    Graph[_Node]
    | dict[_Node, dict[_Node, dict[str, Any]]]
    | dict[_Node, Iterable[_Node]]
    | Iterable[EdgePlus[_Node]]
    | numpy.ndarray[_Node, Any]
    | scipy.sparse.base.spmatrix
)

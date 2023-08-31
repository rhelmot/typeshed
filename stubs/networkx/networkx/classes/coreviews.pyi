from _typeshed import Incomplete, Self
from collections.abc import Callable, Iterator, Mapping
from typing import Generic, TypeVar

_T = TypeVar("_T")
_U = TypeVar("_U")
_V = TypeVar("_V")

class AtlasView(Mapping[_T, dict[_U, _V]], Generic[_T, _U, _V]):
    def __init__(self, d: Mapping[_T, dict[_U, _V]]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __getitem__(self, key: _T) -> dict[_U, _V]: ...
    def copy(self: Self) -> Self: ...

class AdjacencyView(AtlasView[_T, _U, _V], Generic[_T, _U, _V]): ...
class MultiAdjacencyView(AdjacencyView[_T, _U, _V], Generic[_T, _U, _V]): ...

class UnionAtlas(Mapping[_T, dict[_U, _V]], Generic[_T, _U, _V]):
    def __init__(self, succ: AtlasView[_T, _U, _V], pred: AtlasView[_T, _U, _V]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __getitem__(self, key: _T) -> dict[_U, _V]: ...
    def copy(self: Self) -> Self: ...

class UnionAdjacency(Mapping[_T, dict[_U, _V]], Generic[_T, _U, _V]):
    def __init__(self, succ: AdjacencyView[_T, _U, _V], pred: AdjacencyView[_T, _U, _V]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __getitem__(self, key: _T) -> dict[_U, _V]: ...
    def copy(self: Self) -> Self: ...

class UnionMultiInner(UnionAtlas[_T, _U, _V], Generic[_T, _U, _V]): ...
class UnionMultiAdjacency(UnionAdjacency[_T, _U, _V], Generic[_T, _U, _V]): ...

class FilterAtlas(Mapping[_T, _U], Generic[_T, _U]):
    NODE_OK: Callable[[_T], bool]
    def __init__(self, d: Mapping[_T, _U], NODE_OK: Callable[[_T], bool]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __getitem__(self, key: _T) -> _U: ...
    def copy(self: Self) -> Self: ...

class FilterAdjacency(Mapping[_T, Mapping[_U, _V]], Generic[_T, _U, _V]):
    NODE_OK: Callable[[_T], bool]
    EDGE_OK: Callable[[_T, _T], bool]
    def __init__(
        self, d: Mapping[_T, Mapping[_U, _V]], NODE_OK: Callable[[_T], bool], EDGE_OK: Callable[[_T, _T], bool]
    ) -> None: ...
    def __len__(self) -> Incomplete: ...
    def __iter__(self) -> Incomplete: ...
    def __getitem__(self, node: _T) -> FilterAtlas[_U, _V]: ...
    def copy(self: Self) -> Self: ...

class FilterMultiInner(FilterAdjacency[_T, _U, _V], Generic[_T, _U, _V]): ...
class FilterMultiAdjacency(FilterAdjacency[_T, _U, _V], Generic[_T, _U, _V]): ...

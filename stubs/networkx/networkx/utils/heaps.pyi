# Stubs for networkx.utils.heaps (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from _typeshed import Incomplete

class MinHeap:
    class _Item:
        key: Incomplete
        value: Incomplete
        def __init__(self, key, value) -> None: ...

    def __init__(self) -> None: ...
    def min(self) -> None: ...
    def pop(self) -> None: ...
    def get(self, key, default: Incomplete | None = None) -> None: ...
    def insert(self, key, value, allow_increase: bool = False) -> None: ...
    def __nonzero__(self): ...
    def __bool__(self): ...
    def __len__(self): ...
    def __contains__(self, key): ...

class PairingHeap(MinHeap):
    class _Node(MinHeap._Item):
        left: Incomplete
        next: Incomplete
        prev: Incomplete
        parent: Incomplete
        def __init__(self, key, value) -> None: ...

    def __init__(self) -> None: ...
    def min(self): ...
    def pop(self): ...
    def get(self, key, default: Incomplete | None = None): ...
    def insert(self, key, value, allow_increase: bool = False): ...

class BinaryHeap(MinHeap):
    def __init__(self) -> None: ...
    def min(self): ...
    def pop(self): ...
    def get(self, key, default: Incomplete | None = None): ...
    def insert(self, key, value, allow_increase: bool = False): ...

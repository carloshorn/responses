from collections import Sequence
from . import BaseResponse 

from typing import (
    Iterator,
    Optional,
    List,
    Tuple,
)

from requests.adapters import PreparedRequest

class PopFirstKeepLastRegistry:
    _responses: Sequence[BaseResponse] = ...
    def __init__(self, responses: Optional[Sequence[BaseResponse]] = None) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[BaseResponse]: ...
    def __contains__(self, response: BaseResponse) -> bool: ...
    def clear(self) -> None: ...
    def index(self, response: BaseResponse) -> int: ...
    def find_match(self, request: PreparedRequest) -> Tuple[Optional[BaseResponse], List[Tuple[BaseResponse, str]]]: ...
    def add(self, response: BaseResponse) -> None: ...
    def remove(self, response: BaseResponse) -> None: ...
    def replace(self, response: BaseResponse) -> None: ...

class InsertionOrderRegistry(PopFirstKeepLastRegistry):
    ...

class StrictOrderRegistry(PopFirstKeepLastRegistry):
    ...
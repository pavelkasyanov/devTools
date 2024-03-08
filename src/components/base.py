from abc import abstractmethod
from typing import NoReturn, Optional


class UIComponent:
    name: Optional[str] = None

    def __init__(self, parent: object = None):
        self._parent = parent
        self._root = None

    @abstractmethod
    def init(self) -> 'UIComponent':
        ...

    def destroy(self) -> NoReturn:
        pass

    @property
    def component(self):
        return self._root

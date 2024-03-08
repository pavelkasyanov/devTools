from tkinter import ttk

from src.components.base import UIComponent

from .components import MainFrame


class JsonWidget(UIComponent):
    def __init__(self, parent: object = None):
        super().__init__(parent)
        self._root = None
        self.name = "Json"

    def init(self) -> UIComponent:
        self._root = MainFrame(self._parent).init().component
        return self

    def destroy(self):
        pass

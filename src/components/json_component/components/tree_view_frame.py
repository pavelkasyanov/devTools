from tkinter import BaseWidget, ttk

from src.components import UIComponent


class TreeViewFrame(UIComponent):
    def __init__(self, parent: object = None):
        super().__init__(parent)
        self.name = "Tree View"

    def init(self) -> BaseWidget:
        self._root = ttk.Frame(self._parent)
        return self

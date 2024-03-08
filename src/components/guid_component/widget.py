from tkinter import ttk

from src.components import UIComponent


class GUUIDWidget(UIComponent):
    def __init__(self, parent: object = None):
        super().__init__(parent)
        self._root = None
        self.name = "GUID"

    def init(self) -> UIComponent:
        self._root = ttk.Frame(self._parent)
        return self

    def destroy(self):
        pass
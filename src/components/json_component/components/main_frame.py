from tkinter import ttk, BOTH

from src.components import UIComponent

from .text_view_frame import TextViewFrame
from .tree_view_frame import TreeViewFrame


class MainFrame(UIComponent):
    def __init__(self, parent: object = None):
        super().__init__(parent)
        self._notebook = None

    def _text_frame_selected(self, _):
        print("text_frame_selected")

    def _tree_frame_selected(self, _):
        print("tree_frame_selected")

    def _tab_selected(self, event):
        selected_index = self._notebook.index(self._notebook.select())
        if selected_index == 0:
            self._text_frame_selected(event)
        elif selected_index == 1:
            self._tree_frame_selected(event)

    def init(self) -> UIComponent:
        self._root = ttk.Frame(self._parent)

        self._notebook = ttk.Notebook(self._root)
        self._notebook.pack(expand=True, fill=BOTH)

        text_frame = TextViewFrame(self._notebook).init()
        self._notebook.add(text_frame.component, text=text_frame.name)

        tree_frame = TreeViewFrame(self._notebook).init()
        self._notebook.add(tree_frame.component, text=tree_frame.name)

        self._notebook.bind("<<NotebookTabChanged>>", self._tab_selected)

        return self

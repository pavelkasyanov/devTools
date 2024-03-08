from tkinter import BaseWidget, ttk, Text, LEFT, Y, RIGHT, BOTH, TOP, END, StringVar
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Button, Label
from typing import NoReturn

from src.components import UIComponent
from src.components.json_component.components.utils import is_valid_json, format_json, minimize_json


class TextViewFrame(UIComponent):
    def __init__(self, parent: object = None):
        super().__init__(parent)
        self._error_text_lb = None
        self._error_text = None
        self._editor = None
        self.name = "Text View"
        self._is_data_valid = False

    def _on_editor_modified(self, _):
        print("_on_editor_modified")
        modified_text = self._editor_get_text()
        self._validate_text(modified_text)

    def _validate_text(self, data: str) -> NoReturn:
        self._is_data_valid = is_valid_json(data)
        if not self._is_data_valid:
            self._error_text.set("invalid json")
            self._error_text_lb.config(foreground="red")
        else:
            self._error_text.set("valid json")
            self._error_text_lb.config(foreground="green")

        self._root.update_idletasks()

    def _on_fmt_data(self) -> NoReturn:
        current_text = self._editor_get_text()
        new_text = format_json(current_text)
        self._editor_set_text(new_text)

    def _on_min_data(self) -> NoReturn:
        current_text = self._editor_get_text()
        new_text = minimize_json(current_text)
        self._editor_set_text(new_text)

    def _editor_get_text(self) -> str:
        return self._editor.get("1.0", END)

    def _editor_del_all_text(self) -> NoReturn:
        self._editor.delete("1.0", END)

    def _editor_replace_text(self, new_data: str, start: str = "1.0"):
        self._editor.insert(start, new_data)

    def _editor_set_text(self, new_data: str) -> NoReturn:
        self._editor_del_all_text()
        self._editor_replace_text(new_data)

    def init(self) -> UIComponent:
        self._root = ttk.Frame(self._parent)

        command_frame = ttk.Frame(self._root)
        minimize_btn = Button(master=command_frame, text="min", command=self._on_min_data)
        minimize_btn.pack(side=LEFT, expand=True)
        format_btn = Button(master=command_frame, text="ftm", command=self._on_fmt_data)
        format_btn.pack(side=LEFT, expand=True)
        command_frame.pack(side=TOP)

        text_frame = ttk.Frame(master=self._root)
        self._editor = ScrolledText(text_frame)
        self._editor.pack(side=TOP, expand=True, fill=BOTH)
        self._error_text = StringVar()
        self._error_text_lb = Label(master=text_frame, textvariable=self._error_text)
        self._error_text_lb.pack(side=TOP, expand=True, fill=BOTH)
        text_frame.pack(side=TOP)

        self._editor.bind("<KeyRelease>", self._on_editor_modified)

        # TODO: debug
        inserted_text = '''{"array":[1,2,3],"boolean":true,"color":"gold","null":null,"number":123,"object":{"a":"b","c":"d"},"string":"Hello World"}'''
        self._editor.insert(END, inserted_text)

        return self

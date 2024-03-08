import tkinter as Tkinter
from tkinter import ttk
from typing import List

from .components import COMPONENTS, UIComponent

root = Tkinter.Tk()

components: List[UIComponent] = []


def finish():
    for component in components:
        component.destroy()
    root.destroy()
    print("Закрытие приложения")


def run():
    root.title("devTools")
    root.protocol("WM_DELETE_WINDOW", finish)
    root.geometry("900x550")

    notebook = ttk.Notebook()
    notebook.pack(expand=True, fill=Tkinter.BOTH)

    for widget in COMPONENTS:
        frame = widget(notebook).init()
        notebook.add(frame.component, text=frame.name)
        components.append(frame)

    root.mainloop()

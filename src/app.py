import tkinter as Tkinter

root = Tkinter.Tk()


def finish():
    root.destroy()
    print("Закрытие приложения")


def run():
    root.title("devTools")
    root.protocol("WM_DELETE_WINDOW", finish)
    root.geometry("300x250")

    label = Tkinter.Label(text="Hello!")
    label.pack()

    root.mainloop()

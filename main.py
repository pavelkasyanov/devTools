import sys
import tkinter as Tkinter

from src import run


def main(argv: list):
    print(f'tkinter version: {Tkinter.Tcl().eval("info patchlevel")}')
    run()


if __name__ == '__main__':
    argv = sys.argv
    main(argv)
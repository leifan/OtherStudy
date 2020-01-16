

import tkinter
import os

from treeWindows import TreeWindows
from infoWindows import InfoWindows

win = tkinter.Tk()
win.title("treeFile")
win.geometry("900x400+200+50")
path = os.getcwd()

infoWin = InfoWindows(win)
treeWin = TreeWindows(win, path, infoWin)


win.mainloop()
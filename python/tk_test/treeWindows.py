import tkinter
from tkinter import ttk
import os

class TreeWindows(tkinter.Frame):
    def __init__(self, master, path, otherWin):
        frame = tkinter.Frame(master)
        frame.grid(row=0,column=0)
        #frame.pack()
        self.otherWin = otherWin
   
        self.tree = ttk.Treeview(frame)
        self.tree.pack(side=tkinter.LEFT, fill=tkinter.Y)
        
        root = self.tree.insert("", "end", text=self.getLastPath(path), open=True)
        self.loadTree(root, path)

        #滚动条
        self.sy = tkinter.Scrollbar(frame)
        self.sy.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.sy.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=self.sy.set)

        #绑定事件
        self.tree.bind("<<TreeviewSelect>>", self.func)
    
    def func(self, event):
        self.v = event.widget.selection()
        for sv in self.v:
            file = self.tree.item(sv)["text"]
            self.otherWin.ev.set(file)


    def loadTree(self, parent, parentPath):
        for fileName in os.listdir(parentPath):
            absPath = os.path.join(parentPath, fileName)
            #插入树枝
            treey = self.tree.insert(parent, "end", text=self.getLastPath(absPath))
            #判断是否为目录
            if os.path.isdir(absPath):
                self.loadTree(treey,absPath)

    def getLastPath(self, path):
        pathLsit = os.path.split(path)
        return pathLsit[-1]
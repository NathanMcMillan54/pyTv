from tkinter import *
import os


root = Tk()
root.title("test pyTv")
root.configure(background='#e6e6e6')


def addApp():
    os.system('sh ../addApp.sh')


BtnAddApp = Button(root, text="addApp", command=addApp)
BtnAddApp.pack()

root.mainloop()

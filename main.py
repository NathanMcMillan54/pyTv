from tkinter import *
import webbrowser
import os

print("Starting pyTv...")
print("Loading apps...")
print("Loading done")

root = Tk()
root.title("pyTv")
root.configure(background='#e6e6e6')


class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        pad = 3
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom


def opensettings():
    os.system('python apps/settings.py')


BtnSettings = Button(root, text="Settings", command=opensettings)
BtnSettings.grid(row=0, column=0)
BtnSettings.pack()

new0 = 0
url0 = "https://www.netflix.com/"


def openweb():
    webbrowser.open(url0, new=new0)


Btn = Button(root, text="  Netflix ", command=openweb, fg='#b30000')
Btn.pack()


new1 = 1
url1 = "https://www.youtube.com/"


def openweb():
    webbrowser.open(url1, new=new1)


Btn = Button(root, text="Youtube", command=openweb, fg='#ff0000')
Btn.pack()

app = FullScreenApp(root)
root.mainloop()

from tkinter import *
import time
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


t = time.localtime()
# 'a' is for short name of week day, 'd' is for day of month, 'B' is for month name, 'Y' is for year number
current_time = time.strftime("%a, %d, %B, %Y", t)


L = Label(root, text=current_time)
L.config(font=("Courier", 14))
L.pack()

BtnSettings = Button(root, text="Settings", command=opensettings)
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

from tkinter import *
import webbrowser

root = Tk()
root.title("Settings")
root.configure(background='#e6e6e6')

L = Label(root, text="Settings")
L.config(font=("Courier", 14))
L.pack()


new = 1
url = "https://sbfomos.org/pytv"


def openweb():
    webbrowser.open(url, new=new)


Btn = Button(root, text="Help", command=openweb, fg='#0066ff')
Btn.pack()


root.geometry("500x500+400+100")
root.mainloop()

from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("500x500")

e = Entry(top)
e.pack()
e.focus_set()


def CallBack():
    print(e.get())
B = Button(top, text="hello", width=10, command=CallBack)
B.pack()
top.mainloop()

from tkinter import *
from turtle import bgcolor

root = Tk()

def Hello():
    Hello1 = Label(root, text=e.get())
    Hello1.grid(row=2, column=1)

e = Entry(root, width=100)
e.grid(row=1, column=0)

button1 = Button(root, text="What did you wrote?", command=Hello)
button1.grid(row=2, column=0)
root.mainloop()
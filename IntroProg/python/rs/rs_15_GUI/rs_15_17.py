from tkinter import *

root = Tk()

def process_event(event):
    print("You have activated the button")


my_button = Button(root, text="Bonjour")
my_button.grid(row=0, column=0)
my_button.bind("<Enter>", process_event)
radioradio = Radiobutton(root, text="bonjour")
radioradio.grid(row=1, column=1)

root.mainloop()
"""Hello world with Tkinter"""
import tkinter as tk

root = tk.Tk()
root.title="Hello World"

label = tk.Label(root, text="Hello world", padx=30, pady=30)
label.pack()


#Start the GUI event loop
root.mainloop()
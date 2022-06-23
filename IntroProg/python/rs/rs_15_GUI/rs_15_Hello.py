from curses import init_color
from email import message
from email.mime import application
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import colorchooser

#Create a windows
application_window = tk.Tk()

#Create the user interface
my_label = ttk.Label(application_window, text="HelloWorld")
my_label.grid(row=1, column=1)

#Create a message box
messagebox.showinfo("Information", "Informative message")
messagebox.showerror("Erreur", "Error message")
messagebox.showwarning("Warning", "Warning message")

#Yes-No question
from tkinter import messagebox

answer = messagebox.askokcancel("Question","Do you want to open this file?")
answer = messagebox.askretrycancel("Question", "Do you want to try that again?")
answer = messagebox.askyesno("Question","Do you like Python?")
answer = messagebox.askyesnocancel("Question", "Continue playing?")


#Choose color

rgb_color, web_color = colorchooser.askcolor(parent=application_window, initialcolor=(255, 0, 0))
#Start GUI
window.mainloop()
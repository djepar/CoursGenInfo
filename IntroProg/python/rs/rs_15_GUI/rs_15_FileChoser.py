from mimetypes import init
import tkinter as tk
from tkinter import filedialog

import os

application_window = tk.Tk()

#Tuple of the file types. 
my_filetypes = [('all files', '*'), ('text file', '.txt')]

#Ask the user to select a folder.
answer = filedialog.askdirectory(parent=application_window, initialdir=os.getcwd(), title="Please select a folder")

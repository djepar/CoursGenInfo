"""Survey test"""
import tkinter as tk

#Root
root = tk.Tk()
root.title("Survey")
root.geometry('640x480+300+300')
root.resizable(False, False)



#Widgets
title = tk.Label(root, text="You must take this survey!!!!!!",font="Arial 16 bold", bg="black", fg="green")
title.pack()

#Functions
'''
def Inputting():
    name = name_inp.get()
    print("Your name is : {}".format(name))
    return None
'''

#Personal information
name_label = tk.Label(root, text="What is your name?")
name_label.pack()
name_inp = tk.Entry(root)



root.mainloop()
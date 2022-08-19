from tkinter import *


application_window = Tk()

def Hello():
    Hello1 = Label(application_window, text="Helloworld")
    Hello1.grid(row=2, column=1)


my_button = Button(application_window, text="Example", padx=50, pady=50)
my_button2 = Button(application_window, text="Example")
my_button3 = Button(application_window, text="Bonjour", command=Hello)

my_button.grid(row=0,column=0)

my_button2.grid(row=0, column=1)

my_button3.grid(row=1, column=0)

application_window.mainloop()
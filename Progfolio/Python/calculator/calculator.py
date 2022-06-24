from curses import window
from sqlite3 import Row
from tkinter import *

def main():
    #Create the entire GUI program
    program = Calculator()

    #Start the GUI event loop
    program.window.mainloop()

class Calculator:

    def __init__(self):
        self.window = Tk()
        self.window = title="Calculator"
        self.operator_frame, self.screen_frame = self.create_frames()

'''
    def create_frames(self):
        screen_frame = Frame(self.window, bg='red', width=300, height=300)
        screen_frame.grid(row=1, column=1)

        operator_frame = Frame(self.window, bg='green', width=100, height=300)
        operator_frame.grid(row=1, column=2)

        return operator_frame, screen_frame
'''
    def button_add():
        return 
    def create_button(self):
# Define buttons
        button0 = Button(self.window, text="0", padx= 40, pady= 20, command=button_add)
        button1 = Button(self.window, text="1", padx= 40, pady= 20, command=button_add)
        button2 = Button(self.window, text="2", padx= 40, pady= 20, command=button_add)
        button3 = Button(self.window, text="3", padx= 40, pady= 20, command=button_add)
        button4 = Button(self.window, text="4", padx= 40, pady= 20, command=button_add)
        button5 = Button(self.window, text="5", padx= 40, pady= 20, command=button_add)
        button6 = Button(self.window, text="6", padx= 40, pady= 20, command=button_add)
        button7 = Button(self.window, text="7", padx= 40, pady= 20, command=button_add)
        button8 = Button(self.window, text="8", padx= 40, pady= 20, command=button_add)
        button9 = Button(self.window, text="9", padx= 40, pady= 20, command=button_add)

# Putting the number on the scree
button1.grid(row= , column=0)
button2.grid(row= , column=1)
button3.grid(row= , column=2)

button4.grid(row= , column=0)
button5.grid(row= , column=1)
button6.grid(row= , column=2)


button7.grid(row= , column=0)
button8.grid(row= , column=1)
button9.grid(row= , column=2)

button0.grid(row= , column=)

if __name__ == "__main__":
    main()
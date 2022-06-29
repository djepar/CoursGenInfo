from tkinter import *


window = Tk()
window.title="Calculator"

e = Entry(window, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

e.delete(0, END)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0,END)

def button_plus():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)
    global operator 
    operator = '+'
    return f_num

def button_Minus():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)
    global operator
    operator = '-'
    return f_num

def button_Multi():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)
    global operator
    operator = '*'
    return f_num

def button_Div():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)
    global operator
    operator = '/'
    return f_num

def Trigo():
    


        

def button_eq():
    second_number = e.get()
    e.delete(0, END)
    if operator == '+':
        e.insert(0, f_num + int(second_number))
    elif operator == '-':
        e.insert(0, f_num - int(second_number))
    elif operator == '*':
        e.insert(0, f_num * int(second_number))
    elif operator == '/':
        e.insert(0, f_num / int(second_number))
      
        
clicked = StringVar()
clicked.set("cos")


# Define button_s
button_0 = Button(window, text="0", padx= 40, pady= 20, command=lambda: button_click(0))
button_1 = Button(window, text="1", padx= 40, pady= 20, command=lambda: button_click(1))
button_2 = Button(window, text="2", padx= 40, pady= 20, command=lambda: button_click(2))
button_3 = Button(window, text="3", padx= 40, pady= 20, command=lambda: button_click(3))
button_4 = Button(window, text="4", padx= 40, pady= 20, command=lambda: button_click(4))
button_5 = Button(window, text="5", padx= 40, pady= 20, command=lambda: button_click(5))
button_6 = Button(window, text="6", padx= 40, pady= 20, command=lambda: button_click(6))
button_7 = Button(window, text="7", padx= 40, pady= 20, command=lambda: button_click(7))
button_8 = Button(window, text="8", padx= 40, pady= 20, command=lambda: button_click(8))
button_9 = Button(window, text="9", padx= 40, pady= 20, command=lambda: button_click(9))
button_Plus = Button(window, text="+", padx= 40, pady= 20, command= button_plus)
button_Eq = Button(window, text="=", padx= 91, pady= 20, command= button_eq)
button_Clear = Button(window, text="Clear", padx= 79, pady= 20, command= button_clear)
button_minus = Button(window, text="-", padx= 40, pady= 20, command= button_Minus)
button_multi = Button(window, text="*", padx= 40, pady= 20, command= button_Multi)
button_div = Button(window, text="/", padx= 40, pady= 20, command= button_Div)
#button_dot = Button(window, text=".", padx= 40, pady= 20, command= button_Dot)
trigo = OptionMenu(window, clicked, "cos", "sin", "tan")

'''

# Trig option 
Trigo.option_add(label="cos", command=button_clear)
Trigo.option_add(lavel="sin", command=button_clear)
Trigo.option_add(lavel="tan", command=button_clear)
'''
# Putting the number on the scree
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)


button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_Clear.grid(row=4, column=1, columnspan=2)
button_Plus.grid(row=5, column=0)
button_Eq.grid(row=5, column=1, columnspan=2)
button_minus.grid(row=6,column=0)
button_multi.grid(row=6, column=1)
button_div.grid(row=6, column=2)
trigo.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

#Start the GUI event loop
window.mainloop()
#Chapter 1 : Drawing Polygons with Turtles of Peter Farrel Math Adventures with Python 

from cgi import test
import turtle

from pip import main


""""
Doesn't work like this. We are going the old fashion ways
    https://www.tutorialspoint.com/turtle-programming-in-python
def square_turtle():
    # "From indicate that we're importing something from outside our file. 
    # We then give the name of the module we want to iimport from, which is turtle in this case. " (p. 18, Farrel. 2019)
    from turtle import *
forward(100)
"""

def creatingTurtle_and_Screen():
    #create the screen and put it black. 
    window_01 = turtle.Screen()
    window_01.bgcolor("black")
    #Creating the turtle
    pen_turtle = turtle.Turtle()
    pen_turtle.color("green")
    pen_turtle.pensize(1)
    return pen_turtle

def test_turtle_01(test_turtle):
    test_turtle.forward(150)
    test_turtle.rt(15)

    test_turtle.forward(150)
    test_turtle.right(15)

    test_turtle.forward(150)
    turtle.done()

def polygon_01(poylgon_turtle, nbr_side):
    inner_degree = ((nbr_side-2)*180)/nbr_side
    for i in range(1, nbr_side+1):
        poylgon_turtle.forward(80)
        #First thing to find out
        #How to we calculate the internal sum of angle of any polygon?
        poylgon_turtle.right(180-inner_degree)
    turtle.done()

def polygon_02(poylgon_turtle, nbr_side, length):
    inner_degree = ((nbr_side-2)*180)/nbr_side
    for i in range(1, nbr_side+1):
        poylgon_turtle.forward(length)
        #First thing to find out
        #How to we calculate the internal sum of angle of any polygon?
        poylgon_turtle.right(180-inner_degree)
    turtle.done()


#This function take a polygon and copy it 60 times with a 5 degrees differences
def looping_polygon_01(poylgon_turtle, nbr_side):
    inner_degree = ((nbr_side-2)*180)/nbr_side
    for j in range(1, 60):
        for i in range(1, nbr_side+1):
            poylgon_turtle.forward(80)

            #First thing to find out
            #How to we calculate the internal sum of angle of any polygon?
            poylgon_turtle.right(180-inner_degree)
        poylgon_turtle.right(5)
    turtle.done()


#this looping polygon make smaller polygon for each cycle
def looping_polygon_02(poylgon_turtle, nbr_side):
    inner_degree = ((nbr_side-2)*180)/nbr_side
    for j in range(1, 60):
        for i in range(1, nbr_side+1):
            poylgon_turtle.forward(120-(j*2))

            #First thing to find out
            #How to we calculate the internal sum of angle of any polygon?
            poylgon_turtle.right(180-inner_degree)
        poylgon_turtle.right(5)
    turtle.done()


#a polygon where you can choose the length and the nbr of side. 


main_turtle = creatingTurtle_and_Screen()
#test_turtle_01(main_turtle, 4)


looping_polygon_02(main_turtle, 4)
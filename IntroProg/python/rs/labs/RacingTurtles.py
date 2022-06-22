import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("The Amazing Turtles Race")

TurtleA = turtle.Turtle()
TurtleA.color("light green")
TurtleB = turtle.Turtle()
TurtleB.color("red")

TurtleA.penup()
TurtleB.penup()
TurtleA.goto(-40, -60)
TurtleA.left(90)
TurtleA.pendown()
TurtleB.goto(-80,-60)
TurtleB.pendown()
TurtleB.left(90)
for i in range (0, 20):
    NumA = random.randint(0, 20)
    TurtleA.forward(NumA)
    NumB = random.randint(0, 20)
    TurtleB.forward(NumB)




    
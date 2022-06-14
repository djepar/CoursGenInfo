import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
lucien = turtle.Turtle()
lucien.shape("turtle")
lucien.color("blue")
for i in range(0,12):
    lucien.penup()
    lucien.forward(75)
    lucien.pendown()
    lucien.forward(20)
    lucien.penup()
    lucien.forward(15)
    lucien.stamp()
    lucien.penup()
    lucien.forward(-110)
    lucien.left(30)

input()
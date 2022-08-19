#dessin artistique beurk
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
lucien = turtle.Turtle()
lucien.shape("arrow")
lucien.color("blue")

walk = 0
for i in range(1000):
    walk = i
    lucien.penup()
    lucien.forward(walk)
    lucien.stamp()
    lucien.left(3)

input()
#The same exercice as 4.7 

import turtle
import random


wn = turtle.Screen()

drunkpirate = turtle.Turtle()

randomexperience = [160, -43, 270, -97, -43, 200, -940, 17, -86]


def randomwalk(n):
    for i in range(0,7):
        drunkpirate.left(randomexperience[n])
        drunkpirate.forward(100)

for element in randomexperience:
    randomwalk(element)

wn.exitonclick()

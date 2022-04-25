#Write a program that asks the user for the number of sides,
# the length of the side, the color, and the fill color of a regular polygon. 
# The program should draw the polygon and then fill it in.

import turtle
wn = turtle.Screen()
polygons = turtle.Turtle()
numberofside = int(input("How many side do your polygons have? "))
lenght = int(input("What is the lenght of each side ? "))
color_polygon = input("What is the color? ")
polygons.color(color_polygon)
polygons.shape("turtle")
for x in range(numberofside+1):
    polygons.forward(lenght)
    polygons.left(360/numberofside)
wn.exitonclick()   

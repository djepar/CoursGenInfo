#Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):

# An equilateral triangle
# A square
# A hexagon (six sides)
# An octagon (eight sides)

import turtle
wn = turtle.Screen()
polygons = turtle.Turtle()
numberofside = int(input("How many side do your polygons have? "))
for x in range(numberofside+1):
    polygons.forward(100)
    polygons.left(360/numberofside)
wn.exitonclick()    
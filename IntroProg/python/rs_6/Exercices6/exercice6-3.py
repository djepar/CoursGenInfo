import turtle

def drawpolygon(someturtle, somesides, somesize):
    for i in range(somesides+1):
        angle = 360/somesides
        someturtle.forward(somesize)
        someturtle.left(angle)
wn = turtle.Screen()
wn.bgcolor("black")

someturtle = turtle.Turtle()
someturtle.color("pink")

drawpolygon(someturtle, 5, 20)

wn.exitonclick()


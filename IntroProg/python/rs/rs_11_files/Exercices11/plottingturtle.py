#found here : https://www.geeksforgeeks.org/draw-graph-grid-using-turtle-in-python/
import turtle

sc = turtle.Screen()
trtl = turtle.Turtle()

def drawy(val):
    trtl.forward(300)
    trtl.up()
    trtl.setpos(val,300)
    trtl.down()

    trtl.backward(300)
    trtl.up()
    trtl.setpos(val+10,0)
    trtl.down()

def drawx(val):
    trtl.forward(300)
    trtl.up()
    trtl.setpos(300, val)
    trtl.down()

    trtl.backward(300)

    trtl.up()
    trtl.setpos(0,val+10)
    trtl.down()

def lab():
    trtl.penup()
    trtl.setpos(155, 155)
    trtl.pendown()

    trtl.write(0, font=("Verdana", 12, "bold"))

    trtl.penup()
    trtl.setpos(290, 155)
    trtl.pendown()

    trtl.write("x", font=("Verdana", 12, "bold"))

    trtl.write("x", font=("Verdana", 12, "bold"))

    trtl.penup()
    trtl.setpos(155, 290)
    trtl.pendown()

    trtl.write("y", font=("Verdana", 12, "bold"))

sc.setup(800, 800)
trtl.speed(0)
trtl.left(90)
trtl.color('lightgreen')

for i in range(30):
    drawy(10*(i+1))

trtl.right(90)
trtl.up()
trtl.setpos(0,0)
trtl.down()

for i in range(30):
    drawx(10*(i+1))

#axis
trtl.color('green')

#set position for x axis
trtl.up()
trtl.setpos(0,150)
trtl.down()

#x-axis
trtl.forward(300)

#set position for y axis
trtl.left(90)
trtl.up()
trtl.setpos(150,0)
trtl.down()

#y-axis
trtl.forward(300)

#labeling
lab()

#hide the turtle
trtl.hideturtle()


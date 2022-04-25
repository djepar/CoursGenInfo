import turtle



squary = turtle.Turtle() # Une tortue qui aime les carrés
wn = turtle.Screen()
wn.bgcolor("lightgreen")
squary.color("hotpink")


def drawSquar(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)


for i in range(1,5):
    drawSquar(squary, i*20)
    squary.penup()
    squary.forward(-10)
    squary.right(90)
    squary.forward(10)
    squary.right(-90)
    squary.pendown()
    


wn.exitonclick()


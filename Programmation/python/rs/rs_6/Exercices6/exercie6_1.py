import turtle



squary = turtle.Turtle() # Une tortue qui aime les carrés


def drawSquar(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

nbsquare = int(input("How many square? "))
for i in range(nbsquare):
    drawSquar(squary, 25)
    squary.penup()
    squary.forward(25*2)
    squary.pendown()
        

input()




        
import turtle

def triangle(TriangleLen, t):
    for i in range(3):
        t.forward(TriangleLen)
        t.left(120)

def Sierpinski(TriangleLen,t, degree):
    if degree > 1:
#        triangle(TriangleLen, t)
        TriangleLen = TriangleLen / 2
        t.forward(TriangleLen)
        t.left(60)
        triangle(TriangleLen, t)
        Sierpinski(TriangleLen, t, degree-1)


def main():
    t = turtle.Turtle()
    win = turtle.Screen()
    t.up()
    t.left(90)
    t.backward(300)
    t.right(90)
    t.backward(300)
    t.down()
    Sierpinski(400, t, 10)
    win.exitonclick()

main()

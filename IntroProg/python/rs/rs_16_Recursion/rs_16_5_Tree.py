import turtle
import random
def tree(branchLen,t):
    t.width(branchLen/10)
    color = ((str(branchLen+30), str(150-branchLen), '0'))
    t.color = color
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-10,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.up()
    t.backward(100)
    t.down()
    t.left(90)
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()
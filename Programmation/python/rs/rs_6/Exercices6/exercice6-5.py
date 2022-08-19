import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

def spiral(someturtle):
    length = 1
    for i in range(84):
        for x in range(1,3):
            someturtle.forward(length)
            someturtle.left(90)   #put 89 to have a tilted form
            length = length+2

     
                          
        
someturtle = turtle.Turtle()
someturtle.color("blue")
someturtle.speed("fastest")

spiral(someturtle)


wn.exitonclick()

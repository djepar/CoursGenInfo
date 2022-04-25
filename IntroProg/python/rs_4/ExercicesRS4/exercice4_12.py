import turtle
spider = turtle.Turtle()
numberlegs = input("How many legs do your spider have? ")
numberlegs = int(numberlegs)
for i in range(0,numberlegs):
    spider.pendown()
    spider.forward(100)
    spider.penup()
    spider.forward(-100)
    spider.left(360/numberlegs)

input()



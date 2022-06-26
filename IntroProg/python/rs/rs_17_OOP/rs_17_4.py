import math


class Point:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def DistFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def __str__(self):
        return "x=" + str(self.x) + ",y=" + str(self.y)

    def halfway(self, target):
        mx = (self.x + target.x) /2
        my = (self.y + target.y) / 2
        return Point(mx, my)
    
    def reflex_x(self):
        return Point(self.x*-1, self.y)

    def slopeFromOrigin(self):
        if self.x == 0:
            return None
        else: 
            return self.y/self.x
        
    def get_line_to(self, Point):
        if self.x - Point.x == 0:
            return None
        else : 
            a = (self.y - Point.y) / (self.x - Point.x)
            b = ((self.x * a) - self.y) * -1
            return (a,b)
    def move(self, mx, my):
        self.x = self.x+mx 
        self.y = self.y+my
    
class Rectangle:
    def __init__ (self, initP, initW, initH):
        self.location = initP
        self.width = initW
        self.height = initH

    def __str__ (self):
        return "location=" + str(self.location) + ",width=" + str(self.width) + ",height=" + str(self.height)

    def area(self):
        return self.width * self.height 

    def perimeter(self):
        return self.width*2 + self.height*2   

    def contains(self, point):
        if point.x < self.location.x + self.width and point.y < self.location.x+self.height:
            return True
        else :
            return False
    
    def diagonal(self):
        return (self.width**2 + self.height)** 0.5



def Dist2Point(point1, point2):
    xdiff = point2.getX() - point1.getX()
    ydiff = point2.getY() - point1.getY()

    dist = math.sqrt(xdiff**2 + ydiff**2)
    return dist
p = Point(4,11)
q = Point(6,15)

rec = Rectangle(p, 4, 5)
print(rec)
print(rec.diagonal())

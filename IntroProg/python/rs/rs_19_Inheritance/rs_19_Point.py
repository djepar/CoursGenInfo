
from tkinter import Label


class Point:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

class LabeledPoint (Point):
    def __init__(self, initX, initY, label):
        super().__init__(initX, initY)
        self.label = label

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y) + " (" + self.label + ")"

pt = Point(5,10)
labeledPt = LabeledPoint(7, 6, "Here")

ptStr = str(pt)
print(ptStr)
labeledPtStr = str(labeledPt)
print(labeledPt)

point3 = LabeledPoint(8,8, "bonjour")

print(point3)
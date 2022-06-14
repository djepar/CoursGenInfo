'''
Create a turtle
Read the 

'''
import turtle

def ArrangingData():
    labdat = open("labdata.txt", "r")
    xlist = []
    ylist = []
    for aline in labdat:
        items = aline.split()
        xlist.append(items[0])
        ylist.append(items[1])
    print(xlist)
    print(ylist)
    labdat.close
    return [xlist, ylist]
dataArrange = ArrangingData()
print(dataArrange)

def plotregression(dataArrange):
    wn = turtle.Screen()
    wn.bgcolor("light green")
    wn.title("Turtle")
    dataTurtle = turtle.Turtle()
    for i in range(0, len(dataArrange[0])):
        dataTurtle.goto(dataArrange[0][i], dataArrange[1][i])
        dataTurtle.stamp
        
    

plotregression(dataArrange)
import matplotlib.pyplot as plt

def ArrangingData():
    labdat = open("labdata.txt", "r")
    xlist = []
    ylist = []
    for aline in labdat:
        items = aline.split()
        xlist.append(int(items[0]))
        ylist.append(int(items[1]))
#    print(xlist)
#    print(ylist)
    labdat.close
    return [xlist, ylist]

data = ArrangingData()
#x and y axis values
x = data[0]
y = data[1]
# plotting the points
plt.scatter(x,y)

#naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a little to my graph
plt.title('Hello')

# function to show the plot
plt.show()


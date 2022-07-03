"""
Write a short Python function that takes a sequence of integer values 
and determines if there is a distinct pair of numbers in the sequence whose product is odd.
"""


list = [1,2,3,4,5,6,7,8,9,10]
def oddPair(list):
    for i in range(0, len(list)):
        for j in range(0,  len(list)):
            if i != j:
                if (i * j) % 2 != 0:
                    print("{} * {} = {}".format(i,j, i*j))
                    return True

oddPair(list)


def listy(length):
    list = [0]
    x = 4
    for i in range(length):
        x += 2
        list.append(x)
    print(list)
    return list





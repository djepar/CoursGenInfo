list = [0,2,3,4,5,6,7]

def reverse(list):
    newlist = []
    for i in range(len(list)-1, 0, -1):
        newlist.append(list[i])
    return newlist

print(reverse(list))
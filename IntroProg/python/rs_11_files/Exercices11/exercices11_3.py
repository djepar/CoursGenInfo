stdfile = open("studentdata.txt", "r")

for aline in stdfile:
    items = aline.split()
    min = int(items[1])
    max = 0
    index = 1
    length = len(items)
    while index < length:
        if int(items[index]) < min:
            min = int(items[index])
        if int(items[index]) > max:
            max = int(items[index])
        index += 1
    print("for {}, the min is {} and the max is {}".format(items[0], min, max))

stdfile.close
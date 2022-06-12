stdfile = open("studentdata.txt", "r")

for aline in stdfile:
    items = aline.split()
    index = 1
    sum = 0
    length = len(items) 

    while index < length:
        sum = sum + float(items[index])
        index += 1

    average = sum / (index-1)   
    
    print("{} have an average grade of {} ".format(items[0], average))

stdfile.close()
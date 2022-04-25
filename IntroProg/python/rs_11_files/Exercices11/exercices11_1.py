stdfile = open("studentdata.txt", "r")

for aline in stdfile:
    items = aline.split()
    if len(items[1:])>6:
        print(items[0])
stdfile.close()
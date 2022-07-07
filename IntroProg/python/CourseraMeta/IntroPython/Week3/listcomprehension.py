list = [1,2,3,4,5]
newlist = [x-1 for x in list if x % 2 == 0]
print(newlist)

listiteration = [x for x in range(1,100, 7) if x % 5 == 0]
print(listiteration)

newlist99 = [x for x in range(0, 99)]
for el in newlist99:
    stringL = str(el)
    stringL = stringL[1:]
    if stringL != "":
        stringL = int(stringL)
        if stringL == el/7 :
            print("This number{} minus first digit = the number divide by 7".format(el))

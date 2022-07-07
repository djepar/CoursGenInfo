list = []
for i in range(0, 99999999, 57):
    list.append(i)
print(list)

for el in list:
    stringy = str(el)
    stringy = stringy[1:]
    if stringy != '':
        intStringy = int(stringy)
        if el / 57 == intStringy:
            print("This number :  {}, when the first digit is removed is = to the number / 57 ".format(el))

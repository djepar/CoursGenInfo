listA = [5,4,3,2,1]
listB = [32,5,-3, 12, 600, 2, 1, 4, 4, 7]
def sorting(list):
    sorted = False
    while sorted == False:
        sorted = True
        for i in range(len(list)-1):
            
            if list[i] > list[i+1]:
                buff = list[i]
                list[i] = list[i+1]
                list[i+1] = buff
                sorted = False
    return list
listA = sorting(listA)
listB = sorting(listB)
print(listA)
print(listB)
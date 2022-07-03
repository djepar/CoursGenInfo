def minmax(list):
    min = 10000
    max = 0
    swapmin = 0
    swapmax = 0
    notPerfect = False
    while(notPerfect == False):
        notPerfect = True
        for el in list:
            if min > el:
                swapmin = el
                min = el
                notPerfect = False
            if max < el:
                swapmax = el
                max = el
                notPerfect = False
    MinMax = ()
    MinMax = (min, max)
    return MinMax

list = [32,45,90,0,4,56]
print(minmax(list))


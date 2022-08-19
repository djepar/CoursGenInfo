import math

def square_or_square_root(arr):
    for i in range(0, len(arr)):
        root  = math.sqrt(arr[i])
        if int(root) ** 2 == arr[i]:
            arr[i] = int(root)
        else: 
            arr[i] = arr[i]**2
        i+=1
    return arr

square_or_square_root([4, 3, 9, 7, 2, 1 ])
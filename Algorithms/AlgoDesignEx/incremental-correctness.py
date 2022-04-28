# Incremental Correctness of page 16.

def Increment(y):
    if y == 0:
        return 1
    else : 
        if y % 2 == 1:
            return (2 * Increment(y/2))
        else : 
            return (y+1)

print(Increment(5))
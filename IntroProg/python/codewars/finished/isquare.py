import math

def is_square(n):
    if n >= 0:        
        root  = math.sqrt(n)
        if int(root) ** 2 == n:
            return True
        else:
            return False
    else: 
        return False
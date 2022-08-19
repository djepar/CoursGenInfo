def sum (int) : 
    if (int == 0) :
        return 0
    else :
        return int + sum(int-1)

print(sum(5))
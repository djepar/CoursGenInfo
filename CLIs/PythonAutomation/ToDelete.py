def flip(d, a):
    if d == "R":
        a.sort()
        return a
    elif d == "L":
        a.reverse()
    return a
print(flip('R', [3, 2, 1, 2]))
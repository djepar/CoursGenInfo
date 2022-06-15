"""
Interlokcing Binary Pairs
"""

def interlockable(a,b):
    a = str(bin(a))
    b = str(bin(b))
    Value = True
    index = 0
    if a < b:
        smallest = a
    else:
        smallest = b
    for i in range(1, len(smallest), 1):
        print("a = {} and b = {}".format(a[-i], b[-i]))
        if a[-i] == 1 and b[-i] == 1:
            Value = False
            print(Value)
    return Value

print(interlockable(3, 6))
string = "Bonjour"
 
def Reversing(str):
    newstring = ""
    for i in range(len(str), 0, -1):
        newstring += str[i-1]
    return newstring

def SlicingReverse(str):
    return str[::-1]

def RecursiveReverse(str):
    if len(str) == 0:
        return str
    else: 
        return RecursiveReverse(str[1:]) + str[0]
print(Reversing(string))
print(RecursiveReverse(string))
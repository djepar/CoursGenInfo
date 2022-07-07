"""
This isn't a pure function because it's change the global state of a var
"""

pushkilist = [1,2,3]

def addto(item):
    return pushkilist.append(item)

addto(5)
print(pushkilist)


# Doing it with function

def addtoPure(list, add):
    return list.append(add)

addtoPure(pushkilist, 9999)
print(pushkilist)
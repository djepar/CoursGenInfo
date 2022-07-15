f = open("magicbox.txt", "r")
meta_set = frozenset()
number = "123456789"
for aline in f:
    temporarySet = frozenset()
    for char in aline:
        if char in number:
            temporaryNumber = int(char)
            temporarySet.add(temporaryNumber)
    meta_set.update(temporarySet)
print(meta_set)
f.close()
def IsMultiple(x, multiple):
    if int(x/multiple) == x/multiple:
        return True
    else:
        return False

print(IsMultiple(15, 3))
print(IsMultiple(20, 9))
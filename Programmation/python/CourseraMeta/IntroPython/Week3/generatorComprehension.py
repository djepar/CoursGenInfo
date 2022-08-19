listIteration = [x for x in range(0,100, 5)]
print(listIteration)
gen_obj = (x for x in listIteration)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end=" ")


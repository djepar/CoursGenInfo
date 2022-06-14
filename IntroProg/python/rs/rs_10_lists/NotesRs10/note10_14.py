#L'operateur de point (dot operator) permet d'accéder à la méthode intégré de liste d'objets
# The dot operator can also be used to access built-in methods of list objects

#append : permet d'ajouter un argument à la fin de la liste
mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist.insert(1,12) #Insert 12 à la position 1, "shift other item up"
print(mylist)
print(mylist.count(12)) #Combien de fois 12 est dans ma liste

print(mylist.index(3)) #Trouve l'index du premier 3 dans ma liste

print(mylist.count(5)) #Combien de fois 3 est dans ma liste

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

mylist.remove(5) #Retire le premier 5 de la liste
print(mylist)

lastitem = mylist.pop()
print(lastitem)
print(mylist)
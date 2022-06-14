#L'opérateur de répétition(repetition operator) crée une copie de référence
origlist = [45, 76, 34, 55]
print(origlist*3)

#Si la liste réfère à une nouvelle liste, un problème surgit. 
newlist = [origlist]*3
print(newlist)

#regardons ce qui arrive lorsque nous modifions une valeur d'origlist
origlist[1] = 99
print(newlist)
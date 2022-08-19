#Il est possible de performer une 'list traversal' 
# en utilisant une itération par objet ou une itération par index

fruits = ['apple', 'orange', 'banana', 'cherry']
for afruit in fruits: #iteration by item
    print(afruit)

crimes__du_Capitalisme = ['famine', 'Sociéte de Classe', 'Guerres imperialiste']

for position in range(len(crimes__du_Capitalisme)): #iteration by index
    print(crimes__du_Capitalisme[position])

#Puisque les listes sont 'mutables'
#Il est parfois désiré de traverser la liste et de la modifer en même temps. 
# Le code qui suit fait un carré de tous les nombres entre 1 et 5 en utilisant une itération par position
numbers = [1,2,3,4,5]
print(numbers)

for i in range(len(numbers)):
    numbers[i] = numbers[i]**2

print(numbers)
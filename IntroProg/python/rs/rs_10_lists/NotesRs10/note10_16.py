#La méthode 'append' ajoute un nouvel item à la fin d'une liste
#Il est également possible d'ajouter un item à la fin d'une liste gràce au 'concatenation operator'

#Prennons l'exemple suivant : nous voulons ajouter
# à une liste comprenant 3 intégrals, le mot 'cat' à la fin

origlist = [45, 32, 88]
origlist.append("cat")
print(origlist)

#Pour utiliser la "concatenation", nous devons écrire un assignation de 'statement' qui utilise 'the accumulator pattern'
origlist = origlist + ["dog"]
print(origlist)

#with append, la liste est simplement modifiée
# avec la concatenation par contre, une nouvelle liste est crée
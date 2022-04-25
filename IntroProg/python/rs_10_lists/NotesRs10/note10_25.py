#10.25 Strings and Lists
#Deux des méthodes les plus utiles sur des 'strings' impliquent l'utilisation de liste
#Pour séparer un 'string' en list de mots.
#Par défault, tout nombre de charactère:espace bland est considéré comme des 'word bondary'

song=  "The rain in Spain..."
wds = song.split()
print(wds)

#Un argument optionnel est le 'delimiter' qui est utilisé pour spécifier quel character est utilisé comme word bondaries
# Dans l'exemple suivant, le string 'ai' est utilisé comme delimiter

xfs = song.split('ai') 
print(xfs) #Le delimiter n'apparait pas dans le résultat

#L'inverse de split est join. 
#Il permet de  choisir un 'separator string' et de le joindre a la liste grâce à une colle(glue) entre chaque élément

xyz = ['red', 'blue', 'green']
glue = ';'
s = glue.join(xyz)
print(s, xyz)
print('***'.join(xyz))
print(''.join(xyz))
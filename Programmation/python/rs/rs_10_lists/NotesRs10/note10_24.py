#10.24 Nested Lists
#Une 'nested list' est une liste qui apparait comme élément d'une autre liste. 
#Pour extraire un élément d'une 'nested list', il y a deux étapes
# 1. Extraire la 'nested list'
# 2. Extraire, l'item qui nous intéresse
#Il est possible de combiner les éptales en utilisant des 'braket operators' qui évaluat de gauche à droite

nested = ['hello', 2.0, 5, [10,20]]
innerlist = nested[3]
print(innerlist)
item = innerlist[1]
print(item)

print(nested[3][1])
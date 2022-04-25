#Puisque qu'une variable réfère à un objet, si nous assignons une variable a un objet, les deux variable refèeres au même objet
a = [81,  82, 83]
b = a
print(a is b)

#Parce que la même list a deux différents noms : a et b (voir ce qui suit), nous les appelons 'aliased'.
#Un changement fait à  un alias change l'autre.

c = [81,  82, 83]
d = [81,  82, 83]

print(c == d)
print(c is d)

d[0] = 5
print(c)

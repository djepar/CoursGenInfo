#10.20 Pure functions
#Écrire la même liste que pour 10.20 mais cette fois si avec une pure function
#Une pure function ne produit pas de side effect
#Ces functions sont seulement appelées à l'aide de paramètres(qui ne peuvent être modifiés) et d'une valeur de retour

def doubleStuff(a_list):
    #Return a new list in which contains doubles of the elements in a_list
    new_list = []
    for value in a_list:
        new_elem = 2*value
        new_list.append(new_elem)
    return new_list

things = [2,5,9]
print(things)
things = doubleStuff(things)
print(things)

#10.21 Quelle méthode est meilleure?
#En général, la pure function permet moins de bug et est plus facile à programmer
#La plupart des codes peuvent être programmer des deux méthodes
#Certains langages de programmation n'acceptent que les pure functions
#Mieux vaut s'habituer à écrire en pure function mais les modifiers peuvent être très utile par moment 
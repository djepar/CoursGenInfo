#10.22 Function that produces list

#La version pure de doubleStuff utilise un motif important pour notre boîte à outil
#Lorsque nous avons besoin d'écire une fonction qui crée et retourne une liste nous pouvons utiliser ce motif :
#initialize a result variable to be an empty list
#loop
#   create a new element
#   append it to result
#return the result

#Si nous avons déjà une méthode qui teste un nombre premier.
#Voici maintenant une fonction qui retourne tous les nombres premiers plus petit que n

def is_prime(nombre): #faire cette fonction
    for i in range(1, nombre+1):
        if nombre % i == 0:
            return True
        else: 
            return False

def primesupto(n):
    result = []
    for i in range(2,n):
        if is_prime(i):
            result.append(i)
    return result



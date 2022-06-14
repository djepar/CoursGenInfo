#Si nous voulons modifier une list et garder l'original, nous avons besoin de faire une copie de la liste.
#Ce processus ce nomme clonage 'cloning'. 
#La méthode la plus facile est avec le slice operator

a = [81, 82, 83]
b = a[:] #concoit un clone en utilisant le slice
print(a is b)
print(a)
print(b)
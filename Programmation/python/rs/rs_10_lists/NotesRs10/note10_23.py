#10.23 List Comprehensions
#La liste précédente créait une séquence de valeur basés sur certain critère. 
#Une façon facile de faire ce type de processus est d'utiliser 'a list comprehension'
#La syntaxe générale de cette opération :
# [<expression> for <item> in <sequence> if <condition>]
# La clause est optionnelle. Par exemple

mylist = [1,2,3,4,5]
yourlist = [item* 2 for item in mylist]
print(yourlist)
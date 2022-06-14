#Prennons le problème d'ajouter tous les objets (item) d'une liste
#Le programme qui suit 'computes the sum of a list of numbers'
sum = 0
for num in[1, 3, 5, 7, 9]:
    sum = sum + num
print(sum)

long_names = 0
for name in ["Joe", 'Sally', 'Amy', 'Brad', "Andre"]:
    if len(name) > 3:
        long_names += 1
print(long_names)



s = "what if we went to the zoo"
num_vowels = 0
for i in s:
    if i in ['a', 'e', 'i', 'o', 'u']:
        num_vowels += 1
print(num_vowels)

#On peut aussi utiliser le == pour faire une opération similaire

word = "onomatopoeia"
o_count = 0
for c in word:
     if c == 'o':
         o_count = o_count +1 
print("There are" + str(o_count) + "o's in " + word)

#10.18.1 Accumulating the Max Value

#On peut utiliser 'the accumulation pattern' avec des conditionnels afin d'obtenir une valeur minimum ou maximum. 
#L'exemple qui suit démontre comment nous pouvons utiliser une valeur maximum à partir d'une liste d'intégrales.

nums = [9,3,8,11,5,29,2]
best_num = 0
for n in nums:
    if n > best_num:
        best_num = n
print(best_num)

#Le code actuel est problématique dans la mesure ou tous les nombres sont négatifs
#Pour résoudre cela, on initialise la variable de l'accumulateur avec le premier numéro sur la liste
nums = [9,3,8,11,5,29,2]
best_num = nums[0]
for n in nums:
    if n > best_num:
        best_num = n
print(best_num)

#10.18.2 Accumulating a String Result
#Convertie une liste d'item en string

scores = [85, 95, 70]
result =''
for score in scores:
        result= result+ str(score)+ ','
print("The scores are" + result)


#Faire une amélioration pour que la phrase soit : 
# 'The scores are 85, 95, and 70

scores = [85, 95, 70]
result = ''
for score in range(len(scores)):
    if score == scores[-1]:
        result = result + "and" + str(score) + ',' 
    else:
        result = result + str(score) + ','
print("The scores are " + result)




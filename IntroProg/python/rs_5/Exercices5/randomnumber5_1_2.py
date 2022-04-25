#5.1 : Use a for statement to print 10 random numbers.
import random
for x in range(0, 10):
    print(random.randrange(0,10))

#5.2 :Repeat the above exercise but this time print 10 random numbers between 25 and 35, inclusive.
for x in range(0, 10):
    print(random.randrange(25,36))

#Ajouter les nombres dans une liste
list = []
for x in range(0, 10):
    list.append(random.randrange(25,36))
    print(list)


#Chapter 4 : Transforming and storing numbers with algebra

#Brute force first-degree equation

from ast import Return
import math
from re import X

def brute_first_degree():
    var = -100
    while 2 * var + 5 != 13:
        var += 1
    return var

print(brute_first_degree())

#resolving first degree equation that are in the form  ax + b = c
def resolving_first_degree_01(a, b, c):
    return (c - b) / a    

print(resolving_first_degree_01(2, 5, 13))
print(resolving_first_degree_01(-34, 67, 0))

#resolving first degree equation that are in the form  ax + b = cx + d
def resolving_first_degree_02(a, b, c, d):
    return (b - d) / (c - a)  

print(resolving_first_degree_02(12, 18, -34, 67))

#resolving degree equation that are in the form  ax + b = cx + d with FRACTIONS


print(resolving_first_degree_02(1/2, 2/3, 1/5, 7/8))

#the parameter are called coefficients
def resolving_second_degree_01(a, b, c):
    rep = []
    if a == 0:
        return "Oh darling, we cannot do that if a = 0"
    
    
    rep.append((-b + (math.sqrt((b**2)-(4*a*c))))/(2 * a))
    rep.append((-b - (math.sqrt((b**2)-(4*a*c))))/(2 * a))
    return rep

print(resolving_second_degree_01(1, 3, -10))



#cette partie ne fonctionne pas
#a function that evaluates a specific equation for the brute force solving of third degree
def g(x):
    return 6 * x**3 + 31 * x ** 2 + 3 * x - 10

def brute_third_degree():
    x = -100
    while x < 100:
        if g(x) == 0:
            return x
        x += 1


print(brute_third_degree())


def g(x):
    return 6 * x**3 + 31 * x ** 2 + 3 * x - 10

def average(a,b):
    return (a+b)/2.0

def guess():
    highest_bound = 0
    lowest_bound = -1
    for i in range(20) :
        midpt =  average(lowest_bound, highest_bound)
        if g(midpt) == 0 :
            print("The root is : ", midpt)
            return midpt
        elif g(midpt) < 0 :
            highest_bound = midpt
        else:
            lowest_bound = midpt
    return midpt

x = guess()

print(x, g(x))
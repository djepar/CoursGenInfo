#Write a function to compute the factorial of a number

from math import factorial


def Factorial(Num):
    if Num == 0:
        return 1
    else:
        return Num * Factorial(Num-1)

print(Factorial(10))
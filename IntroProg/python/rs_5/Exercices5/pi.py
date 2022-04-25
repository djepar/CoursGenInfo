#Search on the internet for a way to calculate an approximation for pi. 
# There are many that use simple arithmetic. 
# Write a program to compute the approximation and then print that value as well as the value of math.pi from the math module.
import math
r = float(input('r: '))
c = (2*math.pi*r)
d = (2*r)
z = (c/d)
print(z)

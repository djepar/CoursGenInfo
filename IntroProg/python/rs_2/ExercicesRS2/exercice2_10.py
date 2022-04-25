#Write a program that will compute MPG for a car. 
#Prompt the user to enter the number of miles driven and the number of gallons used. 
#Print a nice message with the answer.

gallons = int(input("How many gallons have you used during your journey? "))
miles = int(input("How many miles have you drive during your journey? "))
ratio = miles/ gallons
str(ratio, gallons, miles)
print("You drove ", miles + "miles by means of ", gallons,"for a ratio of", ratio)
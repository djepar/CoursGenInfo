#Chapter 3 : Guessing and Checking with Conditionals

def factorisation(number):
    factor_list = []
    for i in range(1, number+1):
        if number % i == 0:
            factor_list.append(i)
    return factor_list

#Exercise 3-1 Finding the greatest commont factor of two numbers

def greatest_common_factor(num1, num2):
    factorList = []
    biggestNum = 0
    if num1 <= num2 :
        biggestNum = num2
    else :
        biggestNum = num1
    for i in range(1, biggestNum):
        if num1 % i == 0 and num2 % i == 0:
            factorList.append(i)
    return max(factorList)

def finding_square_root(square):
    low = 0
    high = square
    guess = average(low, high)
    for i in range(1, square):
        if round(guess**2) == square:
            return guess
        elif guess**2 > square:
            high = guess
        elif guess**2 < square:
            low = guess
        guess = average(low, high)


def average(a,b):
    return (a+b)/2



'''
print(factorisation(25))
print(factorisation(120))
print(greatest_common_factor(150, 138))
for i in range(4, 100):
    print(finding_square_root(i))


'''

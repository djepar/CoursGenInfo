"""It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights you would return home on a Saturday (day 6) Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the number of day of the week you will return on."""
#method 1 with list
day_of_the_week = ["Sunday", "Monday", "Thuesday", "Wednesday", "Thuesday", "Friday", "Saturday"]
startingday = input("Which day do you leave? ") 
startingday = int(startingday)
stay = int(input(("How long do you stay there? ")))


result = startingday+ stay

if result >= 7:
    result = result % 7
    print("result % 7 =", result)


print("You arrive on a ", day_of_the_week[result])

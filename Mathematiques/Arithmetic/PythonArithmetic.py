#this function calculate the sum of every numbers
def Sum(start, end):
    total = 0
    for i in range(start, end+1):
        total += i
    return total
def Sum_verbose(start, end):
    total = 0
    for i in range(start, end+1):
        total += i
        print("I + total = ", total)
    print("The total is : ", total)
    return total

def Average(list):
    total = 0
    for number in list:
        total += number
    return total/len(list)


#list of test
#print(Sum(0,5))
#print(Sum(10,11))
#Sum_verbose(0, 1000)

list_01 = [0,1,2,3,4,5,6]
d = [53, 28, 54, 84, 65, 60, 22, 93, 62, 27, 16, 25, 74, 42, 4, 42,
15, 96, 11, 70, 83, 97, 75]
print(Average(list_01))
print(Average(d))

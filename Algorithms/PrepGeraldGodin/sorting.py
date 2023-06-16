import random

random_numbers = []
for _ in range(100):
    random_numbers.append(random.randint(1, 1000))



def selection_sort(list):
    count = 0
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[j] < list[i]:
                count += 1
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    print("To sort with the sorting algo the table it's took : {}".format(count))
selection_sort(random_numbers)


def bubble_sort(list):
    count = 0
    n = len(list)
    for i in range(n - 1):
        for j in range(n - i - 1):
            count += 1
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[i]
                list[i] = temp
    print("To bubble sort the table it's took : {}".format(count))
    print(list)
bubble_sort(random_numbers)


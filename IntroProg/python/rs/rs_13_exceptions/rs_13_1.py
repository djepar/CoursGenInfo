from ast import In


try:
    list = [1, 2]
    print(list[3])
except IndexError:
    print("Erreur")

try:
    print(5/0)
except Exception as e:
    print("On ne divise pas par zero!!!!!")
    print(e)

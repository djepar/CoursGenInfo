
#This search return true if the element is in the list
def linearSearchBin(a_list, target):
    for el in a_list:
        if el == target:
            return True

a_list1 = [1,2,3,4,5,6]
a_list2  = ["Sapin", "Érable", "Pommier", "Olivier"]
assert(linearSearchBin(a_list1, 2), True)
assert(linearSearchBin(a_list1, 9), False)


"""
Encapsulation : to have methods and variables within the bounds (scopes) of a given unit (class). 
    To hide information, in python 
       
"""

class Alpha:
    def __init__(self):
        self._a = 2 #  protected member that can be used by the class and its subclasses
        self.__b = 2 #private member that can only be accessed from within the class Alpha


"""
Polymorphism : In Python, everything is an object. 
Polymorphism refers to an object that can take many forms. 
"""

#The many forms of '+'

string = "Bonj"
string2 = "our"
stringTotal = string + string2
print("String = {}, String2 = {}, StringTotal = {}".format(string, string2, stringTotal))
list = [1,2,3]
list2 = [4,5,6]
listTotal = list + list2
print("list = {}, list2 = {}, listtotal = {}".format(list, list2, listTotal))
number1 = 1
number2 = 2
print(number1 + number2)

"""
Inheritance
    class Parent():
        Members of the parent class
    class Child(Parent):
        Inherited members from parent class
        Additional members of the child class
"""


"""
Abstraction : the implementation of abstract classes and methods
From the abc module
from abc import ABC,   
class ClassName(ABC):
    pass

"""


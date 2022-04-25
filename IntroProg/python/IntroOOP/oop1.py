#Object Orientated Programming in Python
#https://youtu.be/JeznW_7DlB0
#create a class
class Dog:
    def __init__(self, name, age): #every time we create a Dog, it's will have this 
        self.name = name
        self.age = age
        pass
    def bite(self, x):
        return x+1

    def get_name(self):
        return self.name

    def get_age():
        return self.age
    
    def set_age(self, age):
        return self.age
    
    def bark(self): #all class Dog can now bark 
        print("bark") 

d = Dog("Tim", 34) #instanciated the class Dog
d2 = Dog("Bill", 12)
print(d.name) #name is an attribute of every Dog because of the __init__
print(d2.name)
print(d.get_name(), d2.get_name())
print(d.get_age(), d2.get_age())


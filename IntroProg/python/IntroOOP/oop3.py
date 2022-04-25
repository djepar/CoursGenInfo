
class Pet:
    def __init__(self, name, age):
        self.name= name
        self.age = age

    def speak(self):
        print("I don't know what I say")
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def speak(self):
        print("Meow")

    

class Dog(Pet):
    def speak(self):
        print("bark")

class Fish(Pet):
    pass
p = Pet("Tim", 19)
p.show()
p.speak()
c =Cat("Bill", 34, "Brown")
c.show()
c.speak()
d =Dog("Jill", 55)
d.show()
d.speak()


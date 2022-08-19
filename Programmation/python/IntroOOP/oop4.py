
class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.number_of_people +=1
    
    @classmethod
    def number_ofpeople(cls):
        return cls.number_of_people()

    @classmethod
    def add_person(cls):
        cls.number_of_people +=1

p1 = Person("tim")
p2 = Person("jill")


print(p1.number_of_people)
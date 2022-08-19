class Person:
    def __init__(self, name):
        self.name = name
    def greet(self, target):
        return "Hello %s, my name is %s" % (target, self.name)
        
jack = Person("Jack")
jill = Person("Jill")   

print(jack.greet("Jill"))
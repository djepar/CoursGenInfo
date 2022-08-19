#The is operator
a = "banana"
b = "banana"

#the is operator should return True if those two variable refer to the same "banana"
print(a is b)

#Pourquoi? "Since strings are immutable, Python can optimize resources by making two names that refer to the same string literal value refer to the same object."

# Does not work with list because they are not immutable
a = [81, 82, 83]
b = [81, 82, 83]

print(a is b)

print(a == b)

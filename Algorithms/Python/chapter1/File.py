f = open("bonjour.txt", "a")

for i in range(20):
    f.write("Bonjour, ca va?!?")
f.close

f = open("bonjour.txt", "r")
print(f.read())
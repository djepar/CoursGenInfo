f = open("bonjour.txt", "a")

for i in range(20):
    f.writelines("aaaaaaaa/n")
f.close

f = open("bonjour.txt", "r")
print(f.read())
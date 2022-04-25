infile = open("ccdata2.txt", "r")
aline = infile.readline()

print(aline)

linelist = infile.readlines()
print(len(linelist))
print(linelist[0:4])

infile = open("ccdata2.txt", 'r')
filestring = infile.read()
print(len(filestring))

print(filestring[:256])
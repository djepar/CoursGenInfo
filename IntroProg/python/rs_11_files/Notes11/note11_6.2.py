infile = open("ccdata2.txt", "r")
outfile = open("emissiondata.txt", "w") #document qui sera créé

aline = infile.readline()
outfile.write("Year \tEmmision\n")
while aline:
    items = aline.split()
    dataline = items[0] + '\t' + items[2]
    outfile.write(dataline + '\n')
    aline = infile.readline()

infile.close()
outfile.close()
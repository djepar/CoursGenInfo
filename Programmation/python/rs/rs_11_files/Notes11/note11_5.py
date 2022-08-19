infile = open("ccdata2.txt", "r")
for aline in infile:

    values = aline.split()
    print('In', values[0], 'the average temp. was', values[1], '°C and CO2 emmisions were', values[2], 'gigatons.')
 
infile.close()
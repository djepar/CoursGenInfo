import re
def chuck_push_ups(st): 
    if type(st) != str:
        return "FAIL!!"
    pattern = r'\"+.[^\"]*"'
    strofBin = re.sub(pattern, "", st)
    print(strofBin)
    print(strofBin)
    listofBin = strofBin.split(" ")
    newlist = []
    for el in listofBin: 
        newlist.append(re.sub("\D[2-9]", "", el))
    print(listofBin)
    listofBin = newlist
    listofBin = [int(x,2) for x in listofBin if len(x) > 0]
    if len(listofBin) == 0:
        return "CHUCK SMASH!!"
    sortedBin = sorted(listofBin, reverse=True)
    return sortedBin[0]


print(chuck_push_ups('1e33gidlkm "Chuck" 10 "Stop that!" 11 "Your vest looks stupid" 100 101 110'))
      
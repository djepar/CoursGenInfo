import sys
import re
import operator
import csv
from collections import OrderedDict


def createDicts(errorFile):
    errorsDict = {}
    per_user = {}
    pattern = r"([A-Z]{4,}: )([a-zA-Z ]{4,} )(\[\#\d{4}\] )?\(([a-z\.]{2,})\)"
    f = open(errorFile, "r")
    lines = f.readlines()
    for line in lines:
        matches = re.search(pattern, line)
        if matches[1] == "INFO: ":
            if matches[4] in per_user:
                print("Matches4 in peruser {}".format(matches[4]))
                if "INFO" in per_user[matches[4]]:  
                    per_user[matches[4]]["INFO"] += 1   
                    print(per_user[matches[4]]["INFO"])
            else:
                per_user[matches[4]] = {"INFO" : 1}
                print(per_user[matches[4]]["INFO"])
        elif matches[1] == "ERROR: ":
            if matches[2] in errorsDict:
                errorsDict[matches[2]] +=1
            else:
                errorsDict[matches[2]] =1
            if matches[4] in per_user:
                if "ERROR" in per_user[matches[4]]:
                    per_user[matches[4]]["ERROR"] += 1 
            else:
                per_user[matches[4]] = {"ERROR" : 1}
    f.close()
    #print(errorsDict, per_user)
    return errorsDict, per_user
def sortValue(dic):
    dic  = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
    dic = dict(OrderedDict(dic))
    return dic

def sortUsername(list):
    list  = sorted(list.items(), key=operator.itemgetter(0))
    list = dict(OrderedDict(list))
    return list

def creatingCsvError(dic, headerCSV):
    with open('test1.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headerCSV)
        for key, val in dic.items():
            temprow = [key[:-1], val]
            writer.writerow(temprow)
"""
def creatingCsvInfo(dic, headerCSV):
    with open('test2.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headerCSV)
        for username, subDic1, subDic2 in dic.items():
            temprow = [username, subDic1["ERROR"]]
            print("username : {} subDic : {} subdic2 {}".format(username, subDic1, subDic2))

            writer.writerow(temprow)
"""
def main():
    dictError, per_user = createDicts(sys.argv[1])
    print(per_user)
    dictErrorList = sortValue(dictError)
    headerError = ["Error", "Count"]
    headerUser = ["Username", "INFO", "ERROR"]
    listUser = sortUsername(per_user)
    print(dictErrorList, type(dictErrorList)) 
    creatingCsvError(dictErrorList, headerError)
    #creatingCsvInfo(listUser, headerUser)

main()
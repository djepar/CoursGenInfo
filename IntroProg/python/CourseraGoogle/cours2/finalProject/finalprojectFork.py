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
                if "INFO" in per_user[matches[4]]:
                    per_user[matches[4]]["INFO"] += 1   
            else:
                per_user[matches[4]] = {"INFO" : 1}
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
    print(errorsDict, per_user)
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
        writer = csv.DictWriter(csvfile, fieldnames=headerCSV)
        writer.writeheader()
        for el in dic:
            
        writer.writerows(dic)

def creatingCsvInfo(dic, headerCSV):
    with open('test2.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headerCSV)
        writer.writeheader()
        writer.writerows(dic)

def main():
    dictError, per_user = createDicts(sys.argv[1])
    print("The type of dictError : {}".format(type(dictError)))
    dictErrorList = sortValue(dictError)
    headerError = ["Error", "Count"]
    headerUser = ["Username", "INFO", "ERROR"]
    listUser = sortUsername(per_user)
    print(dictError, type(dictError))
    print(listUser, type(listUser))
    creatingCsvError(dictErrorList, headerError)
    creatingCsvInfo(listUser, headerUser)

main()
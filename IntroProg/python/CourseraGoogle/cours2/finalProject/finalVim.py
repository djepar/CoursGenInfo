#!/usr/bin/env python3
import sys
import re
import operator
import csv
from collections import OrderedDict

def createDicts(errorFile):
    errorsDict = {}
    per_user = {}
    pattern = r"([A-Z]{4,5})([a-zA-Z ]{4,} )(\[\#\d{4}\] )?\(([a-z\.]{2,})\)"
    f = open(errorFile, "r")
    lines = f.readlines()
    for line in lines:
        matches = re.search(pattern, line)
        if matches != None:
            if matches.group(1) == "INFO":
                if matches.group(4) in per_user:
                    if "INFO" in per_user[matches.group(4)]:
                        per_user[matches.group(4)]["INFO"] += 1
                    else:
                        per_user[matches.group(4)]["INFO"] = 1
                else:
                    per_user[matches.group(4)] = {"INFO" :1}




            elif matches.group(1) == "ERROR":
                if matches.group(4) in errorsDict:
                    errorsDict[matches.group(4)] +=1
                else:
                    errorsDict[matches.group(2)] =1
                if matches.group(4) in per_user:
                    if "ERROR" in per_user[matches.group(4)]:
                        per_user[matches.group(4)]["ERROR"] += 1
                    else:
                        per_user[matches.group(4)] = {"ERROR" : 1}
    f.close()
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
    with open('error_message.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headerCSV)
        for key, val in dic.items():
            temprow = [key[:-1], val]
            writer.writerow(temprow)



def creatingCsvInfo(dic, headerCSV):
    with open("user_statistics.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headerCSV)
        for username, subDic in dic.items():
            temprow = [username]
            if "INFO" in subDic:
                temprow.append(subDic["INFO"])
            else:
                temprow.append(0)
            if "ERROR" in subDic:
                temprow.append(subDic["ERROR"])
            else:
                temprow.append(0)
            writer.writerow(temprow)
def main():
    dicError, per_user = createDicts(sys.argv[1])
    dictErrorList = sortValue(dicError)
    headerError = ["Error", "Count"]
    headerUser = ["Username", "INFO", "ERROR"]
    listUser = sortUsername(per_user)
    creatingCsvError(dictErrorList, headerError)
    creatingCsvInfo(listUser, headerUser)


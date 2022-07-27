"""
Task # 1.2 - 2.1 Creating a dictionary and store info/error count 
"""
import sys
import re
import operator
# Error Count
"""
def count(errorFile):
    errorsDict = {}
    userErrorDict = {}
    userInfoDict = {}
    pattern = r"([A-Z]{4,}: )([a-zA-Z ]{4,} )(\[\#\d{4}\] )?\(([a-z\.]{2,})\)"
    f = open(errorFile, "r")
    lines = f.readlines()
    for line in lines:
        matches = re.search(pattern, line)
        print(matches[4])
        if matches[2] in errorsDict:
            errorsDict[matches[2]] +=1
        else:
            errorsDict[matches[2]] =1
        print(matches[1])
        if str(matches[1]) == "INFO:":
            if matches[4] in userInfoDict:
                userInfoDict[matches[4]] += 1
            else:
                userInfoDict[matches[4]] = 1
        if matches[1] == "ERROR:":
            if matches[4] in userErrorDict:
                userErrorDict[matches[4]] += 1
            else:
                userErrorDict[matches[4]] = 1
    f.close()
    print("UserInfoDict = : ", userInfoDict)
    print("UserErrorDict = : ", userErrorDict)
    return errorsDict, userInfoDict, userErrorDict



 """
def createDicts(errorFile):
    errorsDict = {}
    userErrorDict = {}
    userInfoDict = {}
    pattern = r"([A-Z]{4,}: )([a-zA-Z ]{4,} )(\[\#\d{4}\] )?\(([a-z\.]{2,})\)"
    f = open(errorFile, "r")
    lines = f.readlines()
    for line in lines:
        matches = re.search(pattern, line)
        print(matches[1])
        if str(matches[1]) == "INFO: ":
            if matches[4] in userInfoDict:
                userInfoDict[matches[4]] += 1
            else:
                userInfoDict[matches[4]] = 1
        elif matches[1] == "ERROR: ":
            if matches[2] in errorsDict:
                errorsDict[matches[2]] +=1
            else:
                errorsDict[matches[2]] =1
            if matches[4] in userErrorDict:
                userErrorDict[matches[4]] += 1
            else:
                userErrorDict[matches[4]] = 1
    f.close()
    return errorsDict, userInfoDict, userErrorDict

def sortValue(list):
    list  = sorted(list.items(), key=operator.itemgetter(1), reverse=True)
    return list

def sortUsername(list):
    list  = sorted(list.items(), key=operator.itemgetter(0))
    return list


def main():
    dict1, dict2, dict3 = createDicts(sys.argv[1])
    print(dict1, dict2, dict3)
    dict1 = sortValue(dict1)
    dict2 = sortUsername(dict2)
    dict3 = sortUsername(dict3)
    print(dict1, dict2, dict3)
main()
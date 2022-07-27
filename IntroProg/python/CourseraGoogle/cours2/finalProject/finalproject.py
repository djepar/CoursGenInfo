import sys
import re
import operator
import csv
def createDicts(errorFile):
    errorsDict = {}
    userErrorDict = {}
    userInfoDict = {}
    pattern = r"([A-Z]{4,}: )([a-zA-Z ]{4,} )(\[\#\d{4}\] )?\(([a-z\.]{2,})\)"
    f = open(errorFile, "r")
    lines = f.readlines()
    for line in lines:
        matches = re.search(pattern, line)
        if str(matches[1]) == "INFO: ":
            if matches[4] in userInfoDict:
                print("yo")
                userInfoDict[matches[4]] += 1
            else:
                print("chilliwax")
                userInfoDict[matches[4]] = 1
        elif matches[1] == "ERROR: ":
            if matches[2] in errorsDict:
                errorsDict[matches[2]] +=1
            else:
                errorsDict[matches[2]] =1
            if matches[4] in userErrorDict:
                print("bonjour")
                userErrorDict[matches[4]] += 1
            else:
                print("salut")
                userErrorDict[matches[4]] = 1
    f.close()
    print(errorsDict, userInfoDict, userErrorDict)
    return errorsDict, userInfoDict, userErrorDict

def sortValue(dic):
    dic  = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
    return dic

def sortUsername(list, list2):
    list  = sorted(list.items(), key=operator.itemgetter(0))
    for el in list:
        if el[0] in list2: 
            el = el + ((list2[el[0]],))
    print(list)
    return list

def creatingCsvError(dic, headerCSV):
    with open('test1.csv', 'w+') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headerCSV)
        print(type(dic))
        for keyy in dic.items():
            writer.writerow(keyy)

def creatingCsvInfo(dic,dic2, headerCSV):
    with open('test2.csv', 'w+') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = headerCSV)
        writer.writeheader()
        for key, val in dic.items():
            writer.writerow([key, val, dic2[key]])    

def main():
    dictError, dictUserInfo, dictUserError = createDicts(sys.argv[1])
    print("The type of dictError : {}".format(type(dictError)))
    dictErrorList = sortValue(dictError)
    print(dictError)
    print("The type of dictErrorList : {}".format(type(dictErrorList)))
    print(dictErrorList)
    headerError = ["Error", "Count"]
    headerUser = ["Username", "INFO", "ERROR"]
    listUser = sortUsername(dictUserInfo, dictUserError)

    print(listUser)
    #creatingCsvError(dictErrorList, headerError)
    #creatingCsvInfo(dictInfo, dictError, headerUser)

main()
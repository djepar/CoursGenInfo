import csv

filename = "/Users/admin/Documents/informatique/CoursGenInfo/Algorithms/CourseraIntro/Week2/crime.csv"
fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)

    for row in csvreader:
        print(row)
        rows.append(row)
        print("Total no. of rows: %d"%(csvreader.line_num))
print('Field names are:' + ', '.join(field for field in fields))



crimeRate = {}
for col in rows:
    print(col)
    colll = col[1]
    crimeRate[col[0]] = colll[:-1]

print(crimeRate)
sortedlist = sorted(crimeRate.items(), key=lambda x:float(x[1]))
print("--------------------------------------------------------------------")
print(sortedlist)


def binarySearch(target, a_list):
    newlist = a_list
    listVisor = []
    mid = len(newlist) // 2
    count = 0
    while newlist[mid][1] != target[1]:
        if newlist[mid][1] < target[1]:
            print("The visor is {}".format(newlist[mid]))
            listVisor.append(newlist[mid])
            newlist= newlist[:mid]
            print("The element is higher than mid ({}) \n The new list after {} count is : {} \n ".format(mid,count,newlist))
            count += 1
            mid = len(newlist) // 2
        else:
            listVisor.append(newlist[mid])
            print("The visor is {}".format(newlist[mid]))
            newlist = newlist[mid:]
            print("The element is lower than mid ({}) \n The new list after {} count is : {} \n ".format(mid,count,newlist)) 
            count +=1
            mid = len(newlist) // 2
    print(mid)
    print("The visor is {}".format(newlist[mid]))
    if newlist[mid][1] == target[1]:
        return listVisor
       


#print(binarySearch(('Kensington', '-16.70'), sortedlist))
print(crimeRate.keys())
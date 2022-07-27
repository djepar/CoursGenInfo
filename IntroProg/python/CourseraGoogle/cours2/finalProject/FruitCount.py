import csv
def fruits(fruitLog):
    fruitDic = {}
    f = open(fruitLog, "r")
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line in fruitDic:
            fruitDic[line] += 1
        else :
            fruitDic[line] = 1
    return fruitDic

fruity = fruits("fruitlog.txt")
print(fruity)
heady = ["Fruit", "Count"]
def csvFruit(fruitList, headerish):
    with open('fruity.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headerish)
        for keyy in fruitList.items():
            writer.writerow(keyy)

csvFruit(fruity, heady)
import re
with open("LatinFont.txt", 'r') as Latin:
    allLatins = Latin.readlines()
    count = 1
    newfiles = []
    pattern = "\s*\<p\>([a-zA-Z 0-9]*)\<\/p\>\s*"

    for el in allLatins:
        if count % 4 == 2:
            police = re.search(pattern, el)
            print(police.group(1))
            newfiles.append(police.group(1))
        count += 1
Latin.close
print(newfiles)

with open("latinFontDone.txt", 'w') as latinDone:
    for el in newfiles:
        elWithoutSpace = el.replace(" ", "")
        latinDone.write("\t\t<li> \n")
        latinDone.write("\t\t\t<p>{}</p> \n".format(el))
        latinDone.write("\t\t\t<p id=\'{}\'>Almost before we knew it, we had left the ground.</p> \n".format(elWithoutSpace))
        latinDone.write("\t\t</li> \n ")
latinDone.close
with open("latinCSS.txt", "w") as latinCSS:
    for el in newfiles:
        elWithoutSpace = el.replace(" ", "")
        latinCSS.write("#{}".format(elWithoutSpace) + "{" + " font-family: '{}'".format(el) +"}\n")
latinCSS.close


with open("alldeva.txt", 'r') as deva:
    allDeva = deva.readlines()
    count = 1
    newfilesDeva = []
    pattern = "\s*\<p\>([a-zA-Z 0-9]*)\<\/p\>\s*"

    for el in allDeva:
        if count % 4 == 2:
            police = re.search(pattern, el)
            print(police.group(1))
            newfilesDeva.append(police.group(1))
        count += 1
deva.close
print(newfilesDeva)

with open("devaFontDone.txt", 'w') as devaDone:
    for el in newfiles:
        elWithoutSpace = el.replace(" ", "")
        devaDone.write("\t\t<li> \n")
        devaDone.write("\t\t\t<p>{}</p> \n".format(el))
        devaDone.write("\t\t\t<p id=\'{}\'>Almost before we knew it, we had left the ground.</p> \n".format(elWithoutSpace))
        devaDone.write("\t\t</li> \n ")
devaDone.close
with open("devaCSS.txt", "w") as devaCSS:
    for el in newfiles:
        elWithoutSpace = el.replace(" ", "")
        devaCSS.write("#{}".format(elWithoutSpace) + "{" + " font-family: '{}'".format(el) +"}\n")
devaCSS.close
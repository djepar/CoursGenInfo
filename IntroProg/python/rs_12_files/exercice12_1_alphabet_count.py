def alphabet_count(astring):
    astring = astring.lower()
    
    print(astring)
    dict = {"a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0, "h" : 0, "i" : 0, "j" : 0, "k": 0, "l" : 0, "o" : 0, "p" : 0, "q" : 0, "r" : 0, "s" : 0, "t" : 0, "u" : 0, "w": 0, "x" : 0, "y": 0, "z" :0}
    for char in astring:
     for akey in dict:
      if dict[akey] == char:
        dict[akey] = dict[akey] + 1
        print(dict[akey])
        
        
newstring = "ThiS is String with Upper and lower case Letters"
alphabet_count(newstring)
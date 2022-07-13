"""
For the 9 box magic box
"""
list_possible_choices = []
newlist = ()
for i in range(1,10):
    print(list_possible_choices)
    sub_list = []
    sub_list.append(i)
    for j in range(1, 10):
        if len(sub_list) == 1:            
            sub_list.append(j)
        else: 
            sub_list[1] = j     
        for k in range(1, 10):
            valide = False
            if len(sub_list) == 2:            
                sub_list.append(k)
            else: 
                sub_list[2] = k
            if sub_list[0] + sub_list[1] + sub_list[2] == 15:
                if sub_list[0] != sub_list[1] and sub_list[0] != sub_list[2] and sub_list[1] != sub_list[2]:
                    valide = True
                if valide == True:
                    print(sub_list)
                    a = sub_list
                #print("{} +  {} +  {} = 15 = {}".format(sub_list[0],sub_list[1],sub_list[2],sub_list[0] + sub_list[1] + sub_list[2] == 15))
print(newlist)
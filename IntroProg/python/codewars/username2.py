

import re
def validate(username, password):
    len_user = len(username)
    if len_user == 0:
        return False
    listUser = []
    if len_user % 2 == 0:
        max_len = int(len_user / 2)
    else :
        max_len = (len_user // 2) 
    for i in range(0, max_len+1):
        if len(username[i:i+4]) >= max_len:
            listUser.append(username[i:i+max_len])
    print(listUser)
    for el in listUser:
        if el in password:
            return False
    return True
    

    
    


print(validate("sword", "password" ))
#print(validate("asdfghjkl", "lkjhgfdsa"))
#print(validate("username", "myname"))
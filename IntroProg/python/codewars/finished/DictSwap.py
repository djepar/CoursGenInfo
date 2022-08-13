def switch_dict(dic):
    newdict= {}

    for key, val in dic.items():
        if val in newdict:
            newdict[val].append(key)
        else :
            print("val {} and type {} key {} and type {}".format(val, type(val), key, type(key)))
            newdict[val] = [key]
    return newdict




before = {
          'Ice': 'Cream',
          'Age': '21',
          'Light': 'Cream',
          'Double': 'Cream'
          }

print(switch_dict(before))
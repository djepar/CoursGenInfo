def tower_builder(n_floors):
    pyramid = []
    for i in range(n_floors):
        string = " "
        for j in range(i, n_floors):
            string+= " "
        for j in range(i):
            string+="*"
        for j in range(i+1):
            string+=" "
        pyramid.append(string)
    return pyramid
   




print(tower_builder(3))
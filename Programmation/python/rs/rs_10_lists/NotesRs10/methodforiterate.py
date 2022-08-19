words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]

for i in words: #method 1
    print(i)

 
length = len(words) #method 2
for k in range(length):
        print(words[k])


f = 0
while f < length: #method 3
    print(words[f])
    f += 1

[print(j) for j in words] #method 4

for v, val in enumerate(words):
    print(v, ",", val)

import numpy as geek

a = geek.arange(9)
a=a.reshape(3,3)
for x in geek.nditer(a):
    print(x)
import random

colortype = {0:"white", 1:"yellow", 2:"purple", 3:"red"}
class Ghost:
    def __init__(self):
        Ghost.color = colortype.get(random.randint(0,3))

ghosts = [Ghost().color for _ in range(100)]
print(ghosts)
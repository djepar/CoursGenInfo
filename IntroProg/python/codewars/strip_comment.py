import re
bonjour = "bonjour--$--la police--$--pourquoi faites vous--$--cela"
salut = re.sub("$", "", bonjour)
print(salut)
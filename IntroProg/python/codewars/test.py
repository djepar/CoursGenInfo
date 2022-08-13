import re
bonjour = '1ee1gf00t10h1011tr00 '
salut = re.sub("[\D2-9]", "", bonjour)
print(salut)
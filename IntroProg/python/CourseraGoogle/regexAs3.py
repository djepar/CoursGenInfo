import re
def newDom(oldDom):
    newDom = "bonjour"
    pattern = r"([\w\.\-])+([\.]+edu)"
    return re.sub(pattern, newDom+r"\2", oldDom)

print(newDom("allo.edu"))
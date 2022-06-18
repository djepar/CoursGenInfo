def sponge_meme(s):
    s = s.lower()
    index = 0
    newstring = ""
    for char in s:
        if char == " ":
            newstring += " "
        elif index % 2 != 0:
            newstring += char.upper()
        else:
            newstring += char
        index += 1
    return newstring

hello = sponge_meme("bonJOUR")
print(hello)
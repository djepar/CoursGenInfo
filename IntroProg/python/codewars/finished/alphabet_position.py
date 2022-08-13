from re import L


print(ord("a"), ord("z"))
# The alphabet start at -96
import re
def alphabet_position(st):
    newstring = ""
    for el in st:
        if re.match(r"[A-Za-z]", el):
            print("the letter is : {} and the ord is {}".format(el, str(ord(el.lower())-96)))

            newstring += str(ord(el.lower())-96) + " "
    return newstring

print(alphabet_position("The sunset sets at twelve o' clock."))
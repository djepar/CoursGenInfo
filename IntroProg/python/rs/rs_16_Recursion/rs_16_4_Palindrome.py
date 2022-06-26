#Return inverse of a string
def ReverseStr(string):
    if len(string) == 1:
        return string[-1].lower()
    else:
        return string[-1] + ReverseStr(string[0:-1])

print(ReverseStr("Bonjour"))

#Is this a palindrome?

def IsPalindrome(string):
    string = string.lower()
    string = string.replace(" ", "")
    if string == ReverseStr(string):
        return True
    else :
        return False

print(IsPalindrome("Live not on evil"))
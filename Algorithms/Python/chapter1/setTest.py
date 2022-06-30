s1 = {1,2,3,4,5,8}
s2 = {1,2,3,9}
s3 = s1 | s2
print("Is s2 a subset of s1 : {}".format(s2 <= s1))
print("The intersection of s1 and s2 is  : {}".format(s1 & s2))
print("s1 | s2 = {}".format(s3))
print("The set of elements in s1 but not s2 : {}".format(s1 - s2))
print("The set of elements in precisely one of s1 or s2 {}".format(s1 ^ s2))
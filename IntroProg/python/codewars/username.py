"""
You are writing a password validator for a website. You want to discourage users from using their username as part of their password, or vice-versa, because it is insecure. Since it is unreasonable to simply not allow them to have any letters in common, you come up with this rule:

For any password and username pair, the length of the longest common substring should be less than half the length of the shortest of the two.

In other words, you won't allow users to have half their password repeated in their username, or half their username repeated in their password.

Write a function validate(username, password) which returns true if your rule is followed, false otherwise.

Assume:

Both the username and the password may contain uppercase letters, lowercase letters, numbers, spaces, and the following special/punctation characters: !@#$%^&*()_+{}:"<>?[];',.
The username and password will each be less than 100 characters.
"""
import re
def validate(username, password):
    len_user = len(username)
    if len_user == 0:
        return False
    max_len = len_user // 2
    pattern = "[" + username + "]" + "{max_len, }"
    print(pattern)
    print(re.findall(pattern, password))
    return len(re.findall(pattern, password)) < 0
    


print(validate("sword", "password" ))
(validate("", ""), False)
print(validate("asdfghjkl", "lkjhgfdsa"))

"""
test.assert_equals(validate("", ""), False)
        test.assert_equals(validate("username", "myname"), False)
        test.assert_equals(validate("sword", "password" ), False)
        test.assert_equals(validate("qwertyuiop", "asdfghjkl"), True)
        test.assert_equals(validate("MASH", "M*A*S*H"), True)
        test.assert_equals(validate("asdfghjkl", "lkjhgfdsa"), True)

"""
import re

def rearrange_name(a_name):
    pattern = r"^([\w .]*), ([\w .]*)$"
    result = re.search(pattern, a_name)
    if result is None:
        return a_name
    return "{} {}".format(result[2], result[1])

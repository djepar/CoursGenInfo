def get_middle(s):
    len_s = len(s)
    min = int((len(s) / 2)-1)
    max = int((len(s) / 2) +1)
    if len_s % 2 == 1:
        return s[len_s // 2]
    else :
        return s[min:max:]
    
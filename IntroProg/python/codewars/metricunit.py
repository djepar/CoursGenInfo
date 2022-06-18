#https://www.codewars.com/kata/5264f5685fda8ed370000265/train/python
def meters(x):
    if x < 1000:
        return "{}m".format(x)
    elif x < 1000000:
        return "{}km".format(int(x/1000))
    elif x < 1000000000: 
        return "{}Mm".format(int(x/1000000))
    elif x < 1000000000:
        return "{}Tm".format(int(x/1000000000))
    elif x < 1000000000000:
        return "{}Pm".format(int(x/1000000000000))
    elif x < 1000000000000000:
        return "{}Em".format(int(x/1000000000000000))
    elif x < 1000000000000000000:
        return "{}Zm".format(int(x/1000000000000000000))
    elif x < 1000000000000000000000:
        return "{}Ym".format(int(x/1000000000000000000000))
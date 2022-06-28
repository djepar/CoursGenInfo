def sumnums(lo, hi):
    """returns the sum of the numbers in the range [lo..hi]"""

    """Precondition lo < hi"""
    assert lo < hi

    sum = 0
    for i in range(lo, hi+1):
        sum += i
    return sum

print(sumnums(1, 3))
#print(sumnums(3, 1))
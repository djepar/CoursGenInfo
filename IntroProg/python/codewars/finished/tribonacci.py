def tribonacci(signature, n):
    if len(signature) > n:
        return signature[:n]
    newlist = signature
    iter = 3
    print(newlist[-1]+newlist[-2]+newlist[-3])
    while len(newlist) < n:
        newlist.append(newlist[-1]+newlist[-2]+newlist[-3])
        iter += 1
    return newlist
print(tribonacci([1, 1, 1], 10))
"""
assert(tribonacci([1, 1, 1], 10), [1, 1, 1, 3, 5, 9, 17, 31, 57, 105])
assert(tribonacci([0, 0, 1], 10), [0, 0, 1, 1, 2, 4, 7, 13, 24, 44])
assert(tribonacci([0, 1, 1], 10), [0, 1, 1, 2, 4, 7, 13, 24, 44, 81])
assert(tribonacci([1, 0, 0], 10), [1, 0, 0, 1, 1, 2, 4, 7, 13, 24])
assert(tribonacci([0, 0, 0], 10), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
assert(tribonacci([1, 2, 3], 10), [1, 2, 3, 6, 11, 20, 37, 68, 125, 230])
assert(tribonacci([3, 2, 1], 10), [3, 2, 1, 6, 9, 16, 31, 56, 103, 190])
assert(tribonacci([1, 1, 1], 1), [1])
assert(tribonacci([300, 200, 100], 0), [])
"""

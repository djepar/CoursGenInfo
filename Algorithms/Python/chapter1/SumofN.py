def sumofn(n):
    if n == 0:
        return n
    else:
        return n-1 + sumofn(n-1)

print(sumofn(5))

"""Write a short Python function that takes a positive integer
 n and returns the sum of the squares of all the odd positive integers smaller than n."""

def sumofNOdd(n):
    if n == 0 or n % 2 != 0:
        return 0
    else:
        return n-1 + sumofNOdd(n-2)

print(sumofNOdd(10))

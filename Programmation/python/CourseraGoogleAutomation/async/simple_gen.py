#from https://www.youtube.com/watch?v=F19R_M4Nay4
from typing import List
# def fib(n: int) -> List[int]:
#     numbers = []
#     current, nxt = 0,1
#     while len(numbers) < n:
#         current, nxt = nxt, current + nxt
#         numbers.append(current)
#     return numbers
# result = fib(50)
# print(result)


# If we don't know the position of the number
def fib():
    current, nxt = 0 , 1
    while True:
        current, nxt = nxt, current + nxt
        yield current 

result = fib()

for n in result: 
    print(n, end=',')
    if n > 10000:
        break

print()
print("Done")
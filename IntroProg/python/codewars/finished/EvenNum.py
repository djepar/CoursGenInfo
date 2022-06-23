def even_numbers(arr,n):
    even = []
    for num in arr:
        if num % 2 == 0: 
            even.append(num)

    print(even)
    return even[-n:]

print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
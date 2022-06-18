def countingletterA(string):
    counter = 0
    for letter in string:
        if letter == 'a' or letter == 'A':
            counter += 1
    print("there is {} in a".format(counter))
    return count

countingletterA("Arma")
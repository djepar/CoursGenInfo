"""
Write a function named readposint that uses the input dialog to prompt the user for a positive integer 
and then checks the input to confirm that it meets the requirements. 
It should be able to handle 
inputs that cannot be converted to int,
 as well as negative int, and edge cases 
 (e.g. when the user closes the dialog, or does not enter anything at all.)
"""


def readposint():
    try:
        posint = input("Write a positive integer please : ")

    except KeyboardInterrupt:
            print("Sorry, something seems like not working, please try again. \n")
            readposint()

    return posint

positiveInt = readposint()
print(positiveInt)

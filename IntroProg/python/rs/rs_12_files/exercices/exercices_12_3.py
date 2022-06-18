from re import A
import urllib.request
def CreatingAlice():
    Alice_book = urllib.request.urlopen("https://www.gutenberg.org/files/11/11-0.txt")
    dta = Alice_book.read()
    return dta

book = CreatingAlice()
book = str(book)
booking = open('alice.txt', 'w')

booking.write(book)
booking.close()

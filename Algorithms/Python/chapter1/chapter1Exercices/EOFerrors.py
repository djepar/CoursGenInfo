def creatingFile():
    f = open("text.txt", "w")
    for i in range(50):
        f.write("Bonjour le monde")
    f.close()


def ReadingFile():
    NotEofError = True
    f = open("text.txt", "r")
    while(NotEofError == True):
        if EOFError:
            NotEofError = False
            print("NOOOOOOOOOOOOOOO")    
        print(f.readlines())

    
    f.close()

ReadingFile()
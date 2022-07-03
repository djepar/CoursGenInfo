def readfile(path, mode):
    try:
        f = open(path, mode)
    except FileNotFoundError:
        "the file is not available" 
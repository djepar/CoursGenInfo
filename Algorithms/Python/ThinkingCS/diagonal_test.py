grid = [[0 for column in range(9)] for row in range(9)]
print(grid)
def one_sweeping(grid):   #for /
    newgrid = grid
    for row in newgrid:
        for column in row: #for /
            if (row - 1) != "/" and (column - 1) != "/":
                if row + 1 != "/" and column - 1 != "/":
                    if column - 1 != "\\":
                        if row-1 != "\\":
                            if row + 1 != "\\":
                                return True
                            else:
                                return False
                        else:
                            return False
                    else: 
                        return False
                return False
            else :
                return False
print()
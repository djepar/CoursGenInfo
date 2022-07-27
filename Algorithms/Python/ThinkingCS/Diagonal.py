"""
In a 9x9 grid, draw 16 diagonals

"""
grid = [[0 for column in range(9)] for row in range(9)]
print(grid)

def sweeping(grid):
    newgrid = grid
    for rows in newgrid:
        for column in newgrid:
            if 
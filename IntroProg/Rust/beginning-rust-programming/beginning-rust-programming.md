Beginning Rust Programming
2021, by Ric Messier
John Wiley & Sons, Inc., Indianapolis, Indiana

# Chapter 1 : Game of life

Rules : 
- "If a cell is currently alive, but it has fewer than two neighbors, it will die because of lack of support. 
- If a cell is currently alive and has two or three neighbors, it will survive to the next generation.
- If a cell is currently alive and has more than three neighbors, it dies from overpopulation.
- If a cell is currently dead but has exactly three neighbors, it will come back to life. 

Pseudo code rules (by JP)
```

for i in 0..74
    for i in 0.74
        if border-cell() == 3 or border-cell() == 2
            grid[i][j] = alive
        elif border-cell() < 2 and grid[i][j] == alive
            grid[i][j] = death
        elif border-cell() > 3 and grid[i][j] == alive
            grid[i][j] = death
        elif border-cell() == 3 and grid[i][j] == death  //this one is irrelevant because of the first if. 
            grid[i][j] = death
        

def border-cell(grid[i][j]):
    return how many cell touch the current cell
```











LIVRE DE MARDE QUI NE FONCTIONNE PAS!!!!!!!












```
```
```
```
```

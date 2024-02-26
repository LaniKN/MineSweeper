from variables import UNKNOWN, player_grid, key_grid, size
from mineDecider import mineDecider

def createKey():
    for i in range(size):
        col = []
        for j in range(size):
            space = mineDecider()
            col.append(space)
        key_grid.append(col)


def createPlayerGrid():
    a=1
    for i in range(size):
        col = []
        for j in range(size+1):
            if j == 0:
                col.append(a)
                a+=1
            else:
                col.append(UNKNOWN)
        player_grid.append(col)
    player_grid.insert(0, [' ', *range(1,size+1) ])


def show_grid():
    symbols = {-2:"F", -1:"."}
    for row in range(len(player_grid)):
        for col in range(len(player_grid[row])):
            value = player_grid[row][col]
            if value in symbols:
                symbol = symbols[value]
            else:
                symbol = str(value)
            print(f"{symbol} ", end='')
        print("")
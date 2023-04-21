from variables import MINE, player_grid, key_grid
from turnFuncts import gameAskTurn
from gameMain import gameOver
from boardFunct import show_grid

def isMine(coord):
    rowIndex = coord[1]
    itemIndex = coord[0]
    print(player_grid[rowIndex][itemIndex])
    if key_grid[rowIndex][itemIndex] == MINE:
       gameOver()
    else:
        digSpace(rowIndex-1, itemIndex-1, rowIndex, itemIndex)
       
    gameAskTurn()


def digSpace(rowIndexKey, itemIndexKey, rowIndexUI, itemIndexUI):
        space = key_grid[rowIndexKey][itemIndexKey]
        player_grid[rowIndexUI].insert(itemIndexUI, space)
        show_grid()
        gameAskTurn()

from firstMoveFunct import firstMove
from mineCount import countMines
from boardFunct import createKey, createPlayerGrid, show_grid

def myGame():  
    
    
    difficulty = input('What size game to you want?\n1: 5x5\n2: 7x7\n3: 9x9\n')
    print()
    
    #creating board ------------
    if difficulty == '1': #5x5
        size = 5
        player_grid = createPlayerGrid(size)
        show_grid(player_grid)
        key_grid = surroundingSpaces(firstMove(player_grid, createKey(key_grid, size), size))
        minesNum = countMines(key_grid, size)
        print()
        gameAskTurn(minesNum,player_grid,key_grid)
    elif difficulty == '2': #7x7
        size = 7
        key_grid = surroundingSpaces(firstMove(player_grid, createKey(key_grid, size), size))
        minesNum = countMines(key_grid, size)
        player_grid = createPlayerGrid(size)
        boardShow(player_grid)
        print()
        gameAskTurn(minesNum,player_grid,key_grid)
    elif difficulty == '3': #9x9
        size = 9
        key_grid = surroundingSpaces(firstMove(player_grid, createKey(key_grid, size), size))
        minesNum = countMines(key_grid, size)
        player_grid = createPlayerGrid(size)
        gridShow(player_grid)
        print()
        gameAskTurn(minesNum,player_grid,key_grid)
    else:
        print("Please choose an option between 1 and 3!")
        myGame(player_grid, key_grid, minesNum, difficulty)
    
from variables import player_grid, minesNum, key_grid
from firstMoveFunct import firstMove
from mineCount import countMines
from boardFunct import createKey, createPlayerGrid, show_grid
from turnFuncts import play, gameAskTurn
from spacesAround import surroundingSpaces


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
        gameAskTurn()
    elif difficulty == '2': #7x7
        size = 7
        key_grid = surroundingSpaces(firstMove(player_grid, createKey(key_grid, size), size))
        minesNum = countMines(key_grid, size)
        player_grid = createPlayerGrid(size)
        show_grid(player_grid)
        print()
        gameAskTurn()
    elif difficulty == '3': #9x9
        size = 9
        key_grid = surroundingSpaces(firstMove(player_grid, createKey(key_grid, size), size))
        minesNum = countMines(key_grid, size)
        player_grid = createPlayerGrid(size)
        show_grid(player_grid)
        print()
        gameAskTurn()
    else:
        print("Please choose an option between 1 and 3!")
        myGame()
    

def gameOver():
    print()
    show_grid()
    playAgain = input("Oh No! You've hit a mine!! Would you like to play again? (y/n)?\n")
    if playAgain.lower() == 'y':
        player_grid = []
        key_grid = []
        minesNum = 0
        myGame()
    else:
        print("Okay! Thank you for Playing!\n")





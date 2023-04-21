from variables import player_grid, minesNum, key_grid, FLAG, UNKNOWN
from boardFunct import show_grid
from checkMine import isMine


def askPlayerCoordFlag():
   xCoord = int(input("What x-coordinate would you like to place your flag on?\n"))
   yCoord = int(input("what y-coordinate would you like to place your flag on?\n"))
   coord = [xCoord, yCoord]
   return coord

def askPlayerCoordMine():
   xCoord = int(input("What x-coordinate would you like to mine?\n"))
   yCoord = int(input("what y-coordinate would you like to place your flag on?\n"))
   coord = [xCoord, yCoord]
   #[col, row]
   return coord

def gameAskTurn():

    show_grid(player_grid)
    
    print("\nFlags: ", minesNum)
    turnChoice = input('Would you like to mine or place flags? M, F?\n').upper()
    play(turnChoice, minesNum, player_grid, key_grid)

def play(turnChoice, coord):
    
    if turnChoice == 'F':
        coord = askPlayerCoordFlag()
        print(coord)
        set_flag(coord[1], coord[0])
    elif turnChoice == 'M':
        coord = askPlayerCoordMine()
        isMine(coord)
    else:
        print("Sorry! That is an invalid answer!\n")
        gameAskTurn()

def set_flag(row, col):
    if player_grid[row][col] == UNKNOWN:
        player_grid[row][col] = FLAG
    elif player_grid[row][col] == FLAG:
        player_grid[row][col] = UNKNOWN
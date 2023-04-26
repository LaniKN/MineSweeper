player_grid = []
key_grid = []
EMPTY = 0
MINE = -3
UNKNOWN = -1
FLAG = -2
minesNum = 0
flagNum = 0


def myGame():  
    global size, minesNum, flagNum
    difficulty = input('What size game to you want?\n1: 5x5\n2: 7x7\n3: 9x9\n')
    print()
    
    #creating board ------------
    if difficulty == '1': #5x5
        size = 5
        createPlayerGrid()
        createKey()
        print()
        show_grid()
        firstMove()
        surroundingSpaces()
        countMines()
        print(minesNum, "\nFlags: ", flagNum)
        print()
        gameAskTurn()
    elif difficulty == '2': #7x7
        size = 7
        createPlayerGrid()
        createKey()
        print()
        show_grid()
        firstMove()
        surroundingSpaces()
        countMines()
        print()
        gameAskTurn()
    elif difficulty == '3': #9x9
        size = 9
        createPlayerGrid()
        createKey()
        print()
        show_grid()
        firstMove()
        surroundingSpaces()
        countMines()
        print()
        gameAskTurn()
    else:
        print("Please choose an option between 1 and 3!")
        myGame()


def gameAskTurn():
    global flagNum
    show_grid()
    
    print("\nFlags: ", flagNum)
    turnChoice = input('Would you like to mine or place flags? M, F?\n').upper()
    play(turnChoice)


#-- Initialize
def countMines():
    global minesNum, size, flagNum, key_grid, MINE
    count = 0
    for i in range(size):
        for j in range(size):
            if key_grid[i][j] == MINE:
                count+=1
    minesNum = count
    flagNum = count

def createKey():
    global size, key_grid
    for i in range(size):
        col = []
        for j in range(size):
            space = mineDecider()
            col.append(space)
        key_grid.append(col)

def createPlayerGrid():
    global size, player_grid
    for i in range(size):
        row = []
        for j in range(size):
            row.append(-1)
        player_grid.append(row)




def show_grid():
    global player_grid, UNKNOWN, FLAG, key_grid
    symbols = {-2:"F", -1:".", -3:"X"}
    for row in range(len(player_grid)):
        for col in range(len(player_grid[row])):
            value = player_grid[row][col]
            keyVal = key_grid[row][col]
            if value in symbols:
                symbol = symbols[value]
            else:
                symbol = str(keyVal)
            print(f"{symbol} ", end='')
        print("")

def show_grid_key():
    global key_grid, MINE
    #add in symbols for MINE, EMPTY in grid to show.
    symbols = {-3:"X", 0:"O"}
    for row in range(len(key_grid)):
        for col in range(len(key_grid[row])):
            if key_grid[row][col] in symbols:
                value = symbols[key_grid[row][col]]
            else:
                value = str(key_grid[row][col])
            print(f"{value} ", end='')
        print("")
    print()
        


def mineDecider():
    global MINE, EMPTY
    import random
    num = random.randint(0,15)
    if num > 7:
        space = MINE
    else:
        space = 0
        
    if size == 5 and num > 12:
        mineDecider()
    elif size == 7 and num >= 25:
        mineDecider()
    elif size == 9 and num > 40:
        mineDecider()
    return space


def surroundingSpaces():
    global key_grid, EMPTY, MINE
    #row
    for row in key_grid:
        #item
        for item in row:
            #variables that reset each loop-------------------------------------------------------------------------
            countMines = 0
            lstAbove = []
            lstSides = []
            lstBelow = []
            row = key_grid[key_grid.index(row)]
            rowIndex = key_grid.index(row)
            nextItem = row.index(item) + 1
            prevItem = row.index(item) - 1
            prevRow = key_grid.index(row) - 1
            nextRow = key_grid.index(row) + 1
            itemIndex = key_grid[rowIndex].index(item)
            #If the item in the key is an open space, it will go on to count surrounding mines----------------------
            if item == EMPTY:
                
                #1st column -----------------------------------------------------------------------------------------
                if itemIndex == 0:

                    lstSides.append(key_grid[rowIndex][nextItem])

                    
                    if rowIndex != 0:
                        lstAbove.append(key_grid[prevRow][itemIndex])
                        lstAbove.append(key_grid[prevRow][nextItem])
                        
                    
                    
                    if rowIndex != len(key_grid)-1:
                        lstBelow.append(key_grid[nextRow][itemIndex])
                        lstBelow.append(key_grid[nextRow][nextItem])
                       
                
                # middle columns ------------------------------------------------------------------------------------
                if itemIndex > 0 and itemIndex < len(key_grid[rowIndex])-1:

                    lstSides.append(key_grid[rowIndex][prevItem])
                    lstSides.append(key_grid[rowIndex][nextItem])
                    print("LstSides: ", lstSides)
                   
                    
                    if rowIndex != 0:
                        lstAbove.append(key_grid[prevRow][prevItem])
                        lstAbove.append(key_grid[prevRow][itemIndex])
                        lstAbove.append(key_grid[prevRow][nextItem])
                        print("lstAbove: ", lstAbove)
                        
                    
                    
                    if rowIndex != len(key_grid)-1:
                        lstBelow.append(key_grid[nextRow][prevItem])
                        lstBelow.append(key_grid[nextRow][itemIndex])
                        lstBelow.append(key_grid[nextRow][nextItem])
                        print("lstBelow: ", lstBelow)
                        show_grid_key()
                        
                
                #last column------------------------------------------------------------------------------------------
                if itemIndex == len(key_grid[rowIndex])-1:
                    lstSides.append(key_grid[rowIndex][prevItem])
                   
                    
                    if rowIndex != 0:
                        lstAbove.append(key_grid[prevRow][prevItem])
                        lstAbove.append(key_grid[prevRow][itemIndex])
                    
                    
                    if rowIndex != len(key_grid)-1:
                        lstBelow.append(key_grid[nextRow][prevItem])
                        lstBelow.append(key_grid[nextRow][itemIndex])

                
                
                # counting X's around space -----------------------------------------------------------------------
                for item in lstAbove:
                    if item == MINE:
                        countMines += 1
                for item in lstSides:
                    if item == MINE:
                        countMines += 1
                for item in lstBelow:
                    if item == MINE:
                        countMines +=1
               
                        
                # Repacing EMPTY with the number of surrounding mines ------------------------------------------------
                key_grid[rowIndex].insert(itemIndex, countMines)
                del key_grid[rowIndex][nextItem]
                



def askPlayerCoordFlag():
    xCoord = int(input("What x-coordinate would you like to place your flag on?\n"))-1
    yCoord = int(input("what y-coordinate would you like to place your flag on?\n"))-1
    coord = [xCoord, yCoord]
    return coord

def askPlayerCoordMine():
   xCoord = int(input("What x-coordinate would you like to mine?\n"))-1
   yCoord = int(input("what y-coordinate would you like to place your flag on?\n"))-1
   coord = [xCoord, yCoord]
   #[col, row]
   return coord

def gameAskTurn():

    show_grid()
    
    print("\nFlags: ", minesNum)
    turnChoice = input('Would you like to mine or place flags? M, F?\n').upper()
    play(turnChoice)

def play(turnChoice):
    
    if turnChoice == 'F':
        coord = askPlayerCoordFlag()
        print("play coord: ", coord)
        set_flag(coord[1], coord[0])
        gameAskTurn()
    elif turnChoice == 'M':
        coord = askPlayerCoordMine()
        isMine(coord)
        gameAskTurn()
    else:
        print("Sorry! That is an invalid answer!\n")
        gameAskTurn()

def set_flag(row, col):
    global player_grid,minesNum, flagNum

    if player_grid[row][col] == UNKNOWN:
        player_grid[row][col] = FLAG
    elif player_grid[row][col] == FLAG:
        player_grid[row][col] = UNKNOWN

    if key_grid[row][col] == MINE:
        minesNum -= 1
        flagNum -= 1
    else:
        flagNum -= 1

    



def isMine(coord):
    global MINE, key_grid, player_grid
    rowIndex = coord[1]
    itemIndex = coord[0]
    print(player_grid[rowIndex][itemIndex])
    if key_grid[rowIndex][itemIndex] == MINE:
       digSpace(rowIndex, itemIndex)
       gameOver()
    else:
        digSpace(rowIndex, itemIndex)
        gameAskTurn()
    


def digSpace(rowIndex, itemIndex):
        space = key_grid[rowIndex][itemIndex]
        player_grid[rowIndex].insert(itemIndex, space)
        del player_grid[rowIndex][itemIndex+1]
        


def gameOver():
    global player_grid, key_grid
    print()
    show_grid_key()
    player_grid = []
    key_grid = []
    playAgain = input("Oh No! You've hit a mine!! Would you like to play again? (y/n)?\n")
    if playAgain.lower() == 'y':
        myGame()
    else:
        print("Okay! Thank you for Playing!\n")
        exit()


def firstMove():
    print()
    coordCol = int(input("What x-coordinate would you like to first dig up?\n"))-1
    coordRow = int(input("What y-coordinate would you like to first dig up?\n"))-1
    rowIndex = coordRow
    itemIndex = coordCol
    nextItem = itemIndex + 1
    prevItem = itemIndex - 1
    prevRow = rowIndex - 1
    nextRow = rowIndex + 1
    
    if size == 5:
        #1st column -------------------
        if itemIndex == 0:
            #item space turns to O
            key_grid[rowIndex].insert(itemIndex, EMPTY)
            del key_grid[rowIndex][nextItem]
            
            #right space turns to O
            key_grid[rowIndex].insert(nextItem, EMPTY)
            del key_grid[rowIndex][nextItem+1]



            digSpace(rowIndex, itemIndex)
            digSpace(rowIndex, nextItem)
            
        
        # middle columns ------------
        if itemIndex > 0 and itemIndex < len(key_grid[rowIndex])-1:
            #left space turns to O
            key_grid[rowIndex].insert(prevItem, EMPTY)
            del key_grid[rowIndex][itemIndex]
            
            #item space turns to O
            key_grid[rowIndex].insert(itemIndex, EMPTY)
            del key_grid[rowIndex][nextItem]
            
            #right space turns to O
            key_grid[rowIndex].insert(nextItem, EMPTY)
            del key_grid[rowIndex][nextItem+1]


            digSpace(rowIndex, prevItem)
            digSpace(rowIndex, itemIndex)
            digSpace(rowIndex, nextItem)
                
        
        #last column-------------
        if itemIndex == len(key_grid[rowIndex])-1:
            #left space turns to O
            key_grid[rowIndex].insert(prevItem, EMPTY)
            del key_grid[rowIndex][itemIndex]
            
            #item space turns to O
            key_grid[rowIndex].insert(itemIndex, EMPTY)
            del key_grid[rowIndex][nextItem]


            digSpace(rowIndex, prevItem)
            digSpace(rowIndex, itemIndex)
        
        #clear top space
        if (prevRow >= 0) and rowIndex != 0:     
            key_grid[prevRow].insert(itemIndex, EMPTY)
            del key_grid[prevRow][nextItem]


            digSpace(prevRow, itemIndex)
        
        #clear bottom space
        if nextRow != size:
            key_grid[nextRow].insert(itemIndex, 0)
            del key_grid[nextRow][nextItem]
            

            digSpace(nextRow, itemIndex)


            
        
    #for sizes 7x7 and 9x9----------------------------------------------------------------------------
    else:
        #1st column -----------
        if itemIndex == 0:
            #item space turns to O
            key_grid[rowIndex].insert(itemIndex, EMPTY)
            del key_grid[rowIndex][nextItem]
            
            #right space turns to O
            key_grid[rowIndex].insert(nextItem, EMPTY)
            del key_grid[rowIndex][nextItem+1]

            digSpace(rowIndex, itemIndex)
            digSpace(rowIndex, nextItem) 
            
        
        # middle columns -------------
        if itemIndex > 0 and itemIndex < len(key_grid[rowIndex])-1:
            #left space turns to O
            key_grid[rowIndex].insert(prevItem, EMPTY)
            del key_grid[rowIndex][itemIndex]
            
            #item space turns to O
            key_grid[rowIndex].insert(itemIndex, EMPTY)
            del key_grid[rowIndex][nextItem]
            
            #right space turns to O
            key_grid[rowIndex].insert(nextItem, EMPTY)
            del key_grid[rowIndex][nextItem+1]

            digSpace(rowIndex, prevItem)
            digSpace(rowIndex, itemIndex)
            digSpace(rowIndex, nextItem)
             
        
        #last column-------------
        if itemIndex == len(key_grid[rowIndex])-1:
            #left space turns to O
            key_grid[rowIndex].insert(prevItem, EMPTY)
            del key_grid[rowIndex][itemIndex]
            
            #item space turns to O
            key_grid[rowIndex].insert(itemIndex, EMPTY)
            del key_grid[rowIndex][nextItem]
            
            digSpace(rowIndex, prevItem)
            digSpace(rowIndex, itemIndex)
        
        #3 spaces above coord
        if (prevRow >= 0) and rowIndex != 0:
            #space above coord, will always change to 'O' if coord given is not in first row
            key_grid[prevRow].insert(itemIndex, EMPTY)
            del key_grid[prevRow][nextItem]

            digSpace(prevRow, itemIndex)
            
            #col index on first col
            if itemIndex == 0:
                key_grid[prevRow].insert(nextItem, EMPTY)
                del key_grid[prevRow][nextItem+1]

                digSpace(prevRow, nextItem)
                
            #col index on last col
            elif itemIndex == len(key_grid[rowIndex])-1:
                key_grid[prevRow].insert(prevItem, EMPTY)
                del key_grid[prevRow][itemIndex]

                digSpace(prevRow, prevItem)
                
            #index in middle columns
            else:
                key_grid[prevRow].insert(nextItem, EMPTY)
                del key_grid[prevRow][nextItem+1]
                key_grid[prevRow].insert(prevItem, EMPTY)
                del key_grid[prevRow][itemIndex]

                digSpace(prevRow, prevItem)
                digSpace(prevRow, nextItem)
            
            
        #3 spaces below coord
        if nextRow != size:
            #space below coord, will always change to 'O' if coord given is not in first row
            key_grid[nextRow].insert(itemIndex, EMPTY)
            del key_grid[nextRow][nextItem]

            digSpace(nextRow, itemIndex)
            
            #col index on first col
            if prevItem >=0 and itemIndex != 0:
                key_grid[nextRow].insert(nextItem, EMPTY)
                del key_grid[nextRow][nextItem+1]
                key_grid[nextRow].insert(prevItem, EMPTY)
                del key_grid[nextRow][itemIndex]

                digSpace(nextRow, nextItem)
                
            #col index on last col
            elif itemIndex == len(key_grid[rowIndex])-1:
                key_grid[nextRow].insert(prevItem, EMPTY)
                del key_grid[nextRow][itemIndex]

                digSpace(nextRow, prevItem)

            
            #index in middle columns
            else:
                key_grid[prevRow].insert(nextItem, EMPTY)
                del key_grid[prevRow][nextItem+1]
                key_grid[prevRow].insert(prevItem, EMPTY)
                del key_grid[prevRow][itemIndex]

                digSpace(nextRow, prevItem)
                digSpace(nextRow, nextItem)

            

    

myGame()


    


player_grid = []
key_grid = []
EMPTY = 0
MINE = 1
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
    global player_grid, UNKNOWN, EMPTY, FLAG, key_grid
    symbols = {-2:"F", -1:"."}
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
        


def mineDecider():
    global MINE, EMPTY
    import random
    num = random.randint(0,15)
    if num > 7:
        space = -3
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
    for j in key_grid:
        #item
        for i in j:
            #variables that reset each loop-------------------------------------------------------------------------
            countMines = 0
            lstAbove = []
            lstSides = []
            lstBelow = []
            row = key_grid[key_grid.index(j)]
            rowIndex = key_grid.index(j)
            nextItem = row.index(i) + 1
            prevItem = row.index(i) - 1
            prevRow = key_grid.index(j) - 1
            nextRow = key_grid.index(j) + 1
            itemIndex = key_grid[rowIndex].index(i)
            #If the item in the key is an open space, it will go on to count surrounding mines----------------------
            if i == EMPTY:
                
                #1st column -----------------------------------------------------------------------------------------
                if itemIndex == 0:

                    if key_grid[rowIndex][nextItem] == MINE or key_grid[rowIndex][nextItem] == EMPTY:
                        lstSides.append(key_grid[rowIndex][nextItem])
                   
                    
                    if rowIndex > 0:
                        lstAbove.append(key_grid[prevRow])
                        lstAbove = lstAbove[itemIndex:nextItem+1:1]
                        
                    
                    
                    if rowIndex < len(key_grid)-1:
                        lstBelow.append(key_grid[nextRow])
                        lstBelow = lstBelow[itemIndex:nextItem+1:1]
                       
                
                # middle columns ------------------------------------------------------------------------------------
                if itemIndex > 0 and itemIndex < len(key_grid[rowIndex])-1:

                    if key_grid[rowIndex][prevItem] == MINE or key_grid[rowIndex][prevItem] == EMPTY:
                        lstSides.append(key_grid[rowIndex][prevItem])
                    if key_grid[rowIndex][nextItem] == MINE or key_grid[rowIndex][nextItem] == EMPTY:
                        lstSides.append(key_grid[rowIndex][nextItem])
                   
                    
                    if rowIndex > 0:
                        lstAbove.append(key_grid[prevRow])
                        lstAbove = lstAbove[prevItem:nextItem+1:1]
                        
                    
                    
                    if rowIndex < len(key_grid)-1:
                        lstBelow = key_grid[nextRow]
                        lstBelow = lstBelow[prevItem:nextItem+1:1]
                        
                
                #last column------------------------------------------------------------------------------------------
                if itemIndex == len(key_grid[rowIndex])-1:
                    if key_grid[rowIndex][prevItem] == MINE or key_grid[rowIndex][prevItem] == EMPTY:
                        lstSides.append(key_grid[rowIndex][prevItem])
                   
                    
                    if rowIndex > 0:
                        lstAbove.append(key_grid[prevRow])
                        lstAbove = lstAbove[prevItem:itemIndex+1:1]
                    
                    
                    if rowIndex < len(key_grid)-1:
                        lstBelow.append(key_grid[nextRow])
                        lstBelow = lstBelow[prevItem:itemIndex+1:1]


                
                
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

    show_grid()
    
    print("\nFlags: ", minesNum)
    turnChoice = input('Would you like to mine or place flags? M, F?\n').upper()
    play(turnChoice)

def play(turnChoice):
    
    if turnChoice == 'F':
        coord = askPlayerCoordFlag()
        print(coord)
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
    rowIndex = coord[1]-1
    itemIndex = coord[0]-1
    print(player_grid[rowIndex][itemIndex])
    if key_grid[rowIndex][itemIndex] == MINE:
       gameOver()
    else:
        digSpace(rowIndex, itemIndex)
        show_grid()
        gameAskTurn()
    


def digSpace(rowIndex, itemIndex):
        space = key_grid[rowIndex][itemIndex]
        player_grid[rowIndex].insert(itemIndex, space)
        del player_grid[rowIndex][itemIndex+1]
        




def gameOver():
    global player_grid, key_grid
    print()
    show_grid()
    player_grid = []
    key_grid = []
    playAgain = input("Oh No! You've hit a mine!! Would you like to play again? (y/n)?\n")
    if playAgain.lower() == 'y':
        myGame()
    else:
        print("Okay! Thank you for Playing!\n")


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
            key_grid[nextRow].insert(itemIndex, EMPTY)
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


    


player_grid = []
key_grid = []
EMPTY = 0
MINE = 1
UNKNOWN = -1
FLAG = -2
minesNum = 0
flagNum = 0


def myGame():  
    global size
    difficulty = input('What size game to you want?\n1: 5x5\n2: 7x7\n3: 9x9\n')
    print()
    
    #creating board ------------
    if difficulty == '1': #5x5
        size = 5
        createPlayerGrid()
        createKey()
        show_grid()
        print("Should be visible")
        firstMove()
        surroundingSpaces()
        countMines()
        print()
        gameAskTurn()
    elif difficulty == '2': #7x7
        
        createPlayerGrid()
        createKey()
        show_grid()
        print("Should be visible")
        firstMove()
        surroundingSpaces()
        countMines()
        print()
        gameAskTurn()
    elif difficulty == '3': #9x9
       
        createPlayerGrid()
        createKey()
        show_grid()
        print("Should be visible")
        firstMove()
        surroundingSpaces()
        countMines()
        print()
        gameAskTurn()
    else:
        print("Please choose an option between 1 and 3!")
        myGame()


def gameAskTurn():

    show_grid()
    
    print("\nFlags: ", minesNum)
    turnChoice = input('Would you like to mine or place flags? M, F?\n').upper()
    play(turnChoice)


#-- Initialize
def countMines():
    global minesNum, size, flagNum
    count = 0
    for i in range(size):
        for j in range(size):
            if key_grid[i][j] == MINE:
                count+=1
    minesNum = count
    flagNum = count

def createKey():
    global size
    for i in range(size):
        col = []
        for j in range(size):
            space = mineDecider()
            col.append(space)
        key_grid.append(col)

def createPlayerGrid():
    global size
    a=1
    for i in range(size):
        col = []
        for j in range(size+1):
            if j == 0:
                col.append(a)
                a+=1
            else:
                col.append(UNKNOWN)
                print(col)
        player_grid.append(col)
    print(player_grid)

def show_grid():
    
    symbols = {-2:"F", -1:"."}
    for row in range(len(player_grid)):
        for col in range(len(player_grid[row])):
            value = player_grid[row][col]
            if value in symbols:
                symbol = symbols[value]
            else:
                symbol = str(value)
            print(f'{symbol}work', end='')
        print("")


def mineDecider():
    import random
    num = random.randint(0,15)
    if num > 7:
        space = MINE
    else:
        space = EMPTY
        
    if size == 5 and num > 12:
        mineDecider()
    elif size == 7 and num >= 25:
        mineDecider()
    elif size == 9 and num > 40:
        mineDecider()
    return space


def surroundingSpaces():
    
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
                        lstSides += key_grid[rowIndex][nextItem]
                   
                    
                    if rowIndex > 0:
                        lstAbove = key_grid[prevRow]
                        lstAbove = lstAbove[itemIndex:nextItem+1:1]
                        
                    
                    
                    if rowIndex < len(key_grid)-1:
                        lstBelow += key_grid[nextRow]
                        lstBelow = lstBelow[itemIndex:nextItem+1:1]
                       
                
                # middle columns ------------------------------------------------------------------------------------
                if itemIndex > 0 and itemIndex < len(key_grid[rowIndex])-1:
                    if key_grid[rowIndex][prevItem] == MINE or key_grid[rowIndex][prevItem] == EMPTY:
                        lstSides += key_grid[rowIndex][prevItem]
                    if key_grid[rowIndex][nextItem] == UNKNOWN or key_grid[rowIndex][nextItem] == EMPTY:
                        lstSides += key_grid[rowIndex][nextItem]
                   
                    
                    if rowIndex > 0:
                        lstAbove = key_grid[prevRow]
                        lstAbove = lstAbove[prevItem:nextItem+1:1]
                        
                    
                    
                    if rowIndex < len(key_grid)-1:
                        lstBelow += key_grid[nextRow]
                        lstBelow = lstBelow[prevItem:nextItem+1:1]
                        
                
                #last column------------------------------------------------------------------------------------------
                if itemIndex == len(key_grid[rowIndex])-1:
                    
                    if key_grid[rowIndex][prevItem] == MINE or key_grid[rowIndex][prevItem] == EMPTY:
                        lstSides += key_grid[rowIndex][prevItem]
                   
                    
                    if rowIndex > 0:
                        lstAbove = key_grid[prevRow]
                        lstAbove = lstAbove[prevItem:itemIndex+1:1]
                    
                    
                    if rowIndex < len(key_grid)-1:
                        lstBelow += key_grid[nextRow]
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
                
    return key_grid



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




def gameOver():
    print()
    show_grid()
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
    nextRow = rowIndex +1
    
    if size == 5:
        #1st column -------------------
        if itemIndex == 0:
            #item space turns to O
            key_grid[rowIndex].insert(itemIndex, EMPTY)
            del key_grid[rowIndex][nextItem]
            
            #right space turns to O
            key_grid[rowIndex].insert(nextItem, EMPTY)
            del key_grid[rowIndex][nextItem+1]


            digSpace(rowIndex, itemIndex, rowIndex+1, itemIndex+1)
            digSpace(rowIndex, nextItem, rowIndex+1, nextItem+1)
            
        
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

            digSpace(rowIndex, prevItem, rowIndex+1, prevItem+1)
            digSpace(rowIndex, itemIndex, rowIndex+1, itemIndex+1)
            digSpace(rowIndex, nextItem, rowIndex+1, nextItem+1)
                
        
        #last column-------------
        if itemIndex == len(key_grid[rowIndex])-1:
            #left space turns to O
            key_grid[rowIndex].insert(prevItem, EMPTY)
            del key_grid[rowIndex][itemIndex]
            
            #item space turns to O
            key_grid[rowIndex].insert(itemIndex, EMPTY)
            del key_grid[rowIndex][nextItem]

            digSpace(rowIndex, prevItem, rowIndex+1, prevItem+1)
            digSpace(rowIndex, itemIndex, rowIndex+1, itemIndex+1)
        
        #clear top space
        if (prevRow >= 0) and rowIndex != 0:     
            key_grid[prevRow].insert(itemIndex, EMPTY)
            del key_grid[prevRow][nextItem]

            digSpace(prevRow, itemIndex, prevRow+1, itemIndex+1)
        
        #clear bottom space
        if nextRow != size:
            key_grid[nextRow].insert(itemIndex, EMPTY)
            del key_grid[nextRow][nextItem]

            digSpace(nextRow, itemIndex, nextRow+1, itemIndex+1)


            
        
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

            digSpace(rowIndex, itemIndex, rowIndex+1, itemIndex+1)
            digSpace(rowIndex, nextItem, rowIndex+1, nextItem+1) 
            
        
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

            digSpace(rowIndex, prevItem, rowIndex+1, prevItem+1)
            digSpace(rowIndex, itemIndex, rowIndex+1, itemIndex+1)
            digSpace(rowIndex, nextItem, rowIndex+1, nextItem+1)
             
        
        #last column-------------
        if itemIndex == len(key_grid[rowIndex])-1:
            #left space turns to O
            key_grid[rowIndex].insert(prevItem, EMPTY)
            del key_grid[rowIndex][itemIndex]
            
            #item space turns to O
            key_grid[rowIndex].insert(itemIndex, EMPTY)
            del key_grid[rowIndex][nextItem]
            
            digSpace(rowIndex, prevItem, rowIndex+1, prevItem+1)
            digSpace(rowIndex, itemIndex, rowIndex+1, itemIndex+1)
        
        #3 spaces above coord
        if (prevRow >= 0) and rowIndex != 0:
            #space above coord, will always change to 'O' if coord given is not in first row
            key_grid[prevRow].insert(itemIndex, EMPTY)
            del key_grid[prevRow][nextItem]

            digSpace(prevRow, itemIndex, prevRow+1, itemIndex+1)
            
            #col index on first col
            if itemIndex == 0:
                key_grid[prevRow].insert(nextItem, EMPTY)
                del key_grid[prevRow][nextItem+1]

                digSpace(prevRow, nextItem, prevRow+1, nextItem+1)
                
            #col index on last col
            elif itemIndex == len(key_grid[rowIndex])-1:
                key_grid[prevRow].insert(prevItem, EMPTY)
                del key_grid[prevRow][itemIndex]

                digSpace(prevRow, prevItem, prevRow+1, prevItem+1)
                
            #index in middle columns
            else:
                key_grid[prevRow].insert(nextItem, EMPTY)
                del key_grid[prevRow][nextItem+1]
                key_grid[prevRow].insert(prevItem, EMPTY)
                del key_grid[prevRow][itemIndex]

                digSpace(prevRow, prevItem, prevRow+1, prevItem+1)
                digSpace(prevRow, nextItem, prevRow+1, nextItem+1)
            
            
        #3 spaces below coord
        if nextRow != size:
            #space below coord, will always change to 'O' if coord given is not in first row
            key_grid[nextRow].insert(itemIndex, EMPTY)
            del key_grid[nextRow][nextItem]

            digSpace(nextRow, itemIndex, nextRow+1, itemIndex+1)
            
            #col index on first col
            if prevItem >=0 and itemIndex != 0:
                key_grid[nextRow].insert(nextItem, EMPTY)
                del key_grid[nextRow][nextItem+1]
                key_grid[nextRow].insert(prevItem, EMPTY)
                del key_grid[nextRow][itemIndex]

                digSpace(nextRow, nextItem, nextRow+1, nextItem+1)
                
            #col index on last col
            elif itemIndex == len(key_grid[rowIndex])-1:
                key_grid[nextRow].insert(prevItem, EMPTY)
                del key_grid[nextRow][itemIndex]

                digSpace(nextRow, prevItem, nextRow+1, prevItem+1)

            
            #index in middle columns
            else:
                key_grid[prevRow].insert(nextItem, EMPTY)
                del key_grid[prevRow][nextItem+1]
                key_grid[prevRow].insert(prevItem, EMPTY)
                del key_grid[prevRow][itemIndex]

                digSpace(nextRow, prevItem, nextRow+1, prevItem+1)
                digSpace(nextRow, nextItem, nextRow+1, nextItem+1)
            

    

myGame()


    


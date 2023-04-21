from variables import key_grid, MINE, EMPTY, UNKNOWN


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
            if i == "O":
                
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







from variables import EMPTY, player_grid, key_grid, size


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
                
        
        #last column-------------
        if itemIndex == len(key_grid[rowIndex])-1:
            #left space turns to O
            key_grid[rowIndex].insert(prevItem, EMPTY)
            del key_grid[rowIndex][itemIndex]
            
            #item space turns to O
            key_grid[rowIndex].insert(itemIndex, EMPTY)
            del key_grid[rowIndex][nextItem]
        
        if (prevRow >= 0) and rowIndex != 0:     
            key_grid[prevRow].insert(itemIndex, EMPTY)
            del key_grid[prevRow][nextItem]
        
        if nextRow != size:
            key_grid[nextRow].insert(itemIndex, EMPTY)
            del key_grid[nextRow][nextItem]
            
        
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
                
        
        #last column-------------
        if itemIndex == len(key_grid[rowIndex])-1:
            #left space turns to O
            key_grid[rowIndex].insert(prevItem, EMPTY)
            del key_grid[rowIndex][itemIndex]
            
            #item space turns to O
            key_grid[rowIndex].insert(itemIndex, EMPTY)
            del key_grid[rowIndex][nextItem]
            
        
        #3 spaces above coord
        if (prevRow >= 0) and rowIndex != 0:
            #space above coord, will always change to 'O' if coord given is not in first row
            key_grid[prevRow].insert(itemIndex, EMPTY)
            del key_grid[prevRow][nextItem]
            
            #col index on first col
            if itemIndex == 0:
                key_grid[prevRow].insert(nextItem, EMPTY)
                del key_grid[prevRow][nextItem+1]
                
            #col index on last col
            elif itemIndex == len(key_grid[rowIndex])-1:
                key_grid[prevRow].insert(prevItem, EMPTY)
                del key_grid[prevRow][itemIndex]
                
            #index in middle columns
            else:
                key_grid[prevRow].insert(nextItem, EMPTY)
                del key_grid[prevRow][nextItem+1]
                key_grid[prevRow].insert(prevItem, EMPTY)
                del key_grid[prevRow][itemIndex]
            
            
        #3 spaces below coord
        if nextRow != size:
            #space below coord, will always change to 'O' if coord given is not in first row
            key_grid[nextRow].insert(itemIndex, EMPTY)
            del key_grid[nextRow][nextItem]
            
            #col index on first col
            if prevItem >=0 and itemIndex != 0:
                key_grid[nextRow].insert(nextItem, EMPTY)
                del key_grid[nextRow][nextItem+1]
                key_grid[nextRow].insert(prevItem, EMPTY)
                del key_grid[nextRow][itemIndex]
                
            #col index on last col
            elif itemIndex == len(key_grid[rowIndex])-1:
                key_grid[nextRow].insert(prevItem, EMPTY)
                del key_grid[nextRow][itemIndex]
            
            #index in middle columns
            else:
                key_grid[prevRow].insert(nextItem, EMPTY)
                del key_grid[prevRow][nextItem+1]
                key_grid[prevRow].insert(prevItem, EMPTY)
                del key_grid[prevRow][itemIndex]
            
            
            #to clear spaces that have changed in key above ---------------------------------------
            clearSpaceFirst(rowIndex+1,prevRow+1, nextRow+1, itemIndex+1, prevItem+1, nextItem+1, key_grid, player_grid, size)
            
                
    return key_grid
    


    
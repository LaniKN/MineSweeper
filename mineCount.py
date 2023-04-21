

#------------ Coutning how many bombs are in play, will translate to how many flags we'll need -------------#
def countMines(boardKey, size):
    count = 0
    for i in range(size):
        for j in range(size):
            if boardKey[i][j] == 'X':
                count+=1
    return count
        
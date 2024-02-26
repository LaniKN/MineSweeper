from variables import EMPTY, MINE, size


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
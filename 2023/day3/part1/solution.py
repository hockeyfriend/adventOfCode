
def checkForSymbols(lines, linePos, charPos, symbols):
    """
    Check if given position is surrounded by a symbol
    """
    maxLineIndex = len(lines) - 1
    lineLength = len(line[0]) - 1

    previosLineExists = True if linePos > 0 else False
    preceedingLineExists = True if linePos < maxLineIndex else False

    # check for symbol abvoe digit
    if previosLineExists:
        if lines[linePos - 1][charPos] in symbols: return True

    # check for symbol abvoe digit
    if preceedingLineExists:
        if lines[linePos - 1][charPos] in symbols: return True
    
    # check if PREECEDING CHAR is a symbol
    if charPos + 1 <= lineLength: # check if next character is in the line (or if you are already at the end of the line)
        # if preceeding char on previous line is a symbol
        if previosLineExists:
            if lines[linePos - 1][charPos + 1] in symbols: return True
        
        # if preceeding char on current line is a symbol
        if lines[linePos][charPos + 1] in symbols: return True

        # if preceeding char on preeceding line is a symbol
        if preceedingLineExists:
            if lines[linePos + 1][charPos + 1] in symbols: return True

    # check if PREVIOUS CHAR is in the line (or if you are already at the start of the line)
    if charPos - 1 >= 0:
        # if previous char on previous line is a symbol
        if previosLineExists:
            if lines[linePos - 1][charPos - 1] in symbols: return True

        # if privious char on current line is a symbol
        if lines[linePos][charPos - 1] in symbols: return True

        # if previous char on preceeding line is a symbol
        if preceedingLineExists:
            if lines[linePos + 1][charPos - 1] in symbols: return True

def firstDigit(line, charPos):
    """
    returns the first digit of number at char pos:
    line = '134.....4556.....7587'
                      ^
                      |
                    char pos
    
    recursive func: at the end it should return 4 in this example 
    """

    # guard statment return if given position is not a digit
    if not line[charPos].isdigit():
        return -1

    # previous char
    prevCharIdx = charPos -1

    if prevCharIdx >= 0:
        prevChar = line[prevCharIdx]
        
        # preceeding char is a digit
        if prevChar.isdigit():
            return firstDigit(line, prevCharIdx)
        else:
            # previour Char is not digit -> means at charPos must be first digit
            return charPos
    else:
        # we are at the first char in line
        char = line[charPos]
        if char.isdigit():
            return charPos
        else:
            return charPos + 1
        
def lastDigit(line, charPos):
    """
    returns the last digit of number at char pos:
    line = '134.....4556.....7587'
                      ^
                      |
                    char pos
    
    recursive func: at the end it should return 6 in this example 
    """
    # preceeding char
    precCharIdx = charPos + 1
    lineLength = len(line) - 1

    if precCharIdx <= lineLength: # precChar exisits
        precChar = line[precCharIdx]
        
        # preceeding char is a digit
        if precChar.isdigit():
            firstDigit(line, precCharIdx)
        else:
            return precCharIdx
    else:
        # we are at the end of line
        char = line[charPos]
        if char.isdigit():
            return charPos
        else:
            return charPos - 1

def parseNumber(line, charPos):
    # first digit
    lstDigitPos = firstDigit(line, charPos)
    lastDigitPos = lastDigit(line, charPos)

    if lstDigitPos == None or lastDigitPos == None:
        print("\n", lstDigitPos, charPos, lastDigitPos)
    numb = str(line[lstDigitPos:lastDigitPos+1])

    return numb, lastDigitPos

if __name__ == '__main__':
    """
    For every digit we have to check if its souronded by symbol
    """
    with open("puzzle.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        lines = lines[:4]
    
    symbols = ['*', '+', '=', '%', '-', '#', '@', '/', '&', '$']
    

    linePos = 0
    for  line in lines:
        if line.find("\n"):
            line = line[:-2]
        
        lineLength = len(line) - 1
        print(line)
        charPos = 0
        while charPos <= lineLength:
            char = line[charPos]
            print(char, end="")
            if char.isdigit():
                if checkForSymbols(lines, linePos, charPos, symbols):
                    numb, lastDigitPos = parseNumber(line, charPos)
                    print(numb)
                    charPos = lastDigitPos + 1
                    continue

            charPos += 1
        linePos += 1
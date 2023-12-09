
with open("puzzle.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()


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
    # preceeding char
    precCharIdx = charPos -1

    if precCharIdx >= 0:
        precChar = line[precCharIdx]
        
        # preceeding char is a digit
        if precChar.isdigit():
            firstDigit(line, precCharIdx)
        else:
            return precCharIdx
    else:
        # we are at the first char in line
        char = line[charPos]
        if char.isdigit():
            return charPos
        else:
            return charPos + 1

def parseNumber(line, lineNumb, charPos):
    # first digit
    fstDigit = firstDigit()


"""
For every digit we have to check if its souronded by symbol
"""
symbols = ['*', '+', '=', '%', '-', '#', '@', '/', '&', '$']

linePos = 0
for  line in lines:

    charPos = 0
    for char in line:
        if char.isdigit():
            if checkForSymbols(lines, linePos, charPos, symbols):
                parseNumber()
        charPos += 1
    
    linePos += 1
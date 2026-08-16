import os

def checkPos(lines, x, y):
    if x < 0 or y < 0 or y >= len(lines) or x >= len(lines[0]):
        return None

    char = lines[y][x]
    if char.isdigit():
        return int(char)
    else:
        return None

def getGearNumbers(lines, xIdx, yIdx):
    idxHits = set()
    gearNumbers = []

    for i in [1, 0, -1]:
        for k in [1, 0, -1]:
            if i == 0 and k == 0:
                continue

            x = xIdx + k
            y = yIdx + i

            if (x,y) in idxHits:
                continue

            if checkPos(lines, x, y) is not None:
                idxHits.add((x, y))
                centralDigit = lines[y][x]
                
                gearNumber = ""   
                xForward = x

                while True:
                    xForward -= 1
                    if(xForward == -1):
                        break

                    if lines[y][xForward].isdigit():
                        idxHits.add((xForward,y))
                        gearNumber = lines[y][xForward] + gearNumber
                    else:
                        break
                
                gearNumber += centralDigit

                xBackward = x

                while True:
                    xBackward += 1
                    if(xBackward == len(lines[y])):
                        break

                    if lines[y][xBackward].isdigit():
                        idxHits.add((xBackward, y))
                        gearNumber += lines[y][xBackward]
                    else:
                        break
                
                gearNumbers.append(int(gearNumber))

    return gearNumbers

def calcGearRatio(lines, x, y):
    gearNumbers = getGearNumbers(lines, x,y)

    if len(gearNumbers) <= 1:
        return 0
    
    prod = 1
    for num in gearNumbers:
        prod *= num
    return prod

def main():
    p = os.path.join(os.path.dirname(__file__), "puzzle.txt")

    with open(p, "r", encoding="utf-8") as file:
        lines = file.read().splitlines()

    symbol = "*"
    sum = 0
    lineIndex = 0

    for line in lines:
        searchIdx = 0

        while True:
            fstSymbolIdx = line.find(symbol, searchIdx)
            
            if fstSymbolIdx >= 0:
                searchIdx = fstSymbolIdx + 1
                gearRatio = calcGearRatio(lines, fstSymbolIdx, lineIndex)
                sum += gearRatio
            else:
                break
        lineIndex += 1
    print(sum)

if __name__ == "__main__":
    main()

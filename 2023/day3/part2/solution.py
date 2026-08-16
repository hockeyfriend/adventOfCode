import os


class GearRatioCalculator:
    def __init__(self, lines):
        self.lines = lines
        self.gearSymbol = "*"

    def checkPos(self, x, y):
        """Check if position is valid and contains a digit.
        
        Returns:
            int or None: The digit at the position, or None if invalid.
        """
        if x < 0 or y < 0 or y >= len(self.lines) or x >= len(self.lines[0]):
            return None

        char = self.lines[y][x]
        if char.isdigit():
            return char
        else:
            return None

    def getGearNumbers(self, x, y):
        """Get all numbers adjacent to a gear at position (x, y).
        
        Returns:
            list: List of numbers adjacent to the gear.
        """
        idxHits = set()
        gearNumbers = []

        # Check all 8 surrounding positions
        for i in [1, 0, -1]:
            for k in [1, 0, -1]:
                if i == 0 and k == 0:
                    continue

                posX = x + k
                posY = y + i

                if (posX, posY) in idxHits:
                    continue

                centralDigit = self.checkPos(posX, posY)
                if centralDigit is not None:
                    idxHits.add((posX, posY))

                    # Build complete number by scanning left
                    gearNumber = ""
                    xForward = posX

                    while True:
                        xForward -= 1
                        if xForward == -1:
                            break

                        if self.lines[posY][xForward].isdigit():
                            idxHits.add((xForward, posY))
                            gearNumber = self.lines[posY][xForward] + gearNumber
                        else:
                            break

                    gearNumber += centralDigit

                    # Build complete number by scanning right
                    xBackward = posX

                    while True:
                        xBackward += 1
                        if xBackward == len(self.lines[posY]):
                            break

                        if self.lines[posY][xBackward].isdigit():
                            idxHits.add((xBackward, posY))
                            gearNumber += self.lines[posY][xBackward]
                        else:
                            break

                    gearNumbers.append(int(gearNumber))

        return gearNumbers

    def calcGearRatio(self, x, y):
        """Calculate gear ratio for a gear at position (x, y).
        
        Returns:
            int: The product of the two adjacent numbers, or 0 if not exactly 2 numbers.
        """
        gearNumbers = self.getGearNumbers(x, y)

        if len(gearNumbers) != 2:
            return 0

        prod = 1
        for num in gearNumbers:
            prod *= num
        return prod

    def solve(self):
        """Solve the puzzle by calculating sum of all gear ratios.
        
        Returns:
            int: Sum of all gear ratios.
        """
        total = 0
        lineIndex = 0

        for line in self.lines:
            searchIdx = 0

            while True:
                gearIdx = line.find(self.gearSymbol, searchIdx)

                if gearIdx >= 0:
                    searchIdx = gearIdx + 1
                    gearRatio = self.calcGearRatio(gearIdx, lineIndex)
                    total += gearRatio
                else:
                    break
            lineIndex += 1

        return total


def main():
    p = os.path.join(os.path.dirname(__file__), "puzzle.txt")

    with open(p, "r", encoding="utf-8") as file:
        lines = file.read().splitlines()

    calculator = GearRatioCalculator(lines)
    result = calculator.solve()
    print(result)


if __name__ == "__main__":
    main()

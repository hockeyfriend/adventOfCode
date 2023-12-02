# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def findDigits(string):
    numbers = {}
    digitPattern = {
        '0': 0,    '1' : 1,   '2' : 2,     '3' : 3,     '4' : 4,    '5' : 5,    '6' : 6,     '7' : 7,     '8' : 8,    '9' : 9, 
                 'one' : 1, 'two' : 2, 'three' : 3,  'four' : 4, 'five' : 5,  'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9
    }
    for pattern in digitPattern:
        firstOccuranceIndex = string.find(pattern)
        
        if(firstOccuranceIndex > -1): # pattern found
            numbers[firstOccuranceIndex] = digitPattern[pattern]

        try:
            lastOccuranceIndex = string.rindex(pattern)
            numbers[lastOccuranceIndex] = digitPattern[pattern]
        except ValueError:
            pass
    return numbers

if __name__ == "__main__":
    with open("puzzle1.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    sum = 0
    count = 1
    for line in lines:
        numbers = findDigits(line)
        firstIndex = min(numbers.keys())
        lastIndex = max(numbers.keys())

        firstDigit = numbers[firstIndex]
        lastDigit = numbers[lastIndex]
        
        numb = 10 * firstDigit + lastDigit
        sum += numb
        print("Count: " + str(count) + " Sum: " + str(sum) + " Number: " + str(numb))
        count += 1
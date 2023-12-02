# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

with open("puzzle1.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

sum = 0
for line in lines:
    numbers = []
    for char in line:
        if(char.isdigit()):
            numbers.append(char)
    numb = int(numbers[0] + numbers[-1])
    sum += numb
    print("Sum: " + str(sum) + " Number: " + str(numb))
def checkRoundVality(rounds):
    res = rounds.split(", ") # Res Looks like ['1 green', '1 blue', '1 red']
    for cube in res:
        sep = cube.split() 
        color = sep[-1] # 'green'
        number = int(sep[0]) # 1

        if  number > configuration[color]:
            return False
    
    return True
    

with open("puzzle2.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

configuration = {'red' : 12, 'green' : 13, 'blue' : 14}
sumIDs = 0

for line in lines:
    line = line[:-1] # cut of newline '\n'

    gameIdSplit = line.split(": ") # Res looks like: ['Game 1', '1 green, 1 blue, 1 red; 3 green, 1 blue, 1 red; 4 green, 3 blue, 1 red; 4 green, 2 blue, 1 red; 3 blue, 3 green\n']

    gameId = int(gameIdSplit[0].split("Game ")[-1]) # Isolates gameId for example above == 1
    
    gameString = gameIdSplit[-1] # Res Looks like '1 green, 1 blue, 1 red; 3 green, 1 blue, 1 red; 4 green, 3 blue, 1 red; 4 green, 2 blue, 1 red; 3 blue, 3 green\n'
    game = gameString.split("; ")

    gameCorrect = True
    for rounds in game:
        if not checkRoundVality(rounds):        
            gameCorrect = False
            break

    print(f"GameId: {gameId}, {gameString} GameResult: {gameCorrect}")
    if gameCorrect:
        sumIDs += gameId

print(sumIDs)
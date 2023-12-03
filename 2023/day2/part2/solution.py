
def getHighestDraw(gameString):
    allDraws = gameString.replace(";", ",") # '1 green, 1 blue, 1 red, 3 green, 1 blue, 1 red, 4 green, 3 blue, 1 red, 4 green, 2 blue, 1 red, 3 blue, 3 green\n' 
    allDraws = allDraws.split(",") # ['1 green', '1 blue', '1 red', '3 green', '1 blue', ...]

    highDraw = {'red' : 0, 'green' : 0, 'blue' : 0}
    for draw in allDraws:
        sep = draw.split() 
        color = sep[-1] # 'green'
        number = int(sep[0]) # 1

        if  number > highDraw[color]:
            highDraw[color] = number

    return highDraw

if __name__ == '__main__':
    with open("puzzle2.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    configuration = {'red' : 12, 'green' : 13, 'blue' : 14}
    sum = 0

    for line in lines:
        if(line.find('\n') > -1):
            line = line[:-1] # cut of newline '\n'

        gameIdSplit = line.split(": ") # Res looks like: ['Game 1', '1 green, 1 blue, 1 red; 3 green, 1 blue, 1 red; 4 green, 3 blue, 1 red; 4 green, 2 blue, 1 red; 3 blue, 3 green\n']

        gameId = int(gameIdSplit[0].split("Game ")[-1]) # Isolates gameId for example above == 1
        
        gameString = gameIdSplit[-1] # Res Looks like '1 green, 1 blue, 1 red; 3 green, 1 blue, 1 red; 4 green, 3 blue, 1 red; 4 green, 2 blue, 1 red; 3 blue, 3 green\n'
        
        round = gameString.split("; ") # Res Looks like ['1 green, 1 blue, 1 red', '3 green, 1 blue, 1 red', '4 green, 3 blue, 1 red', '4 green, 2 blue, 1 red; 3 blue, 3 green']

        if gameId == 100:
            print(gameString)
        res = getHighestDraw(gameString)
        
        prod = res["red"] * res["green"] * res["blue"]
        sum += prod    
        print(f"GameId: {gameId}, {gameString} GameProd: {prod}")
            
 
    print(sum)
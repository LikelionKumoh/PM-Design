import random




def gamestage(MapSize):
    print(MapSize)
    for i in range(MapSize):
        for j in range(MapSize):
            print(Map[i][j], end=" ")
        print('')

def CheckMap(x,y):
    if(Map[x][y] =='🔺'):
        print(' GO TO HELL \n GO TO HELL \n GO TO HELL \n GO TO HELL \n GO TO HELL \n GO TO HELL \n GO TO HELL \n GO TO HELL \n GO TO HELL \n GO TO HELL \n GO TO HELL \n GO TO HELL \n GO TO HELL \n GO TO HELL \n ')
        return True
    if(Map[x][y] == '💠'):
        print('You ve found a way out for your life! Congratulations...but we ll see you soon')
        return True




MapSize = int(input('How big of a playground do we play? : '))
BombCount = int(input('How many do you want me to have? : '))
global x, y
x = 0
y = 0



Map = []

for _ in range(MapSize):
    Sublist = ['⬜' for _ in range(MapSize)]
    Map.append(Sublist)

for _ in range(BombCount):
    RandomRow = random.randrange(1,2000) % MapSize
    RandomCol = random.randrange(1,2000) % MapSize
    Map[RandomRow][RandomCol] = '🔺'

RandomRow = random.randrange(1,2000) % MapSize
RandomCol = random.randrange(1,2000) % MapSize
Map[RandomRow][RandomCol] = '💠'
Map[x][y] = '🔳'





while True:
    gamestage(MapSize)
    print(' 1. move up \n 2. move down \n 3. move right \n 4. move left \n 5. Dont press this button ')
    
    select = int(input('What number are you going to pick? haha..'))

    if(select == 1 and x > 0):
        Map[x][y] = '⬜'
        x -= 1
        if(CheckMap(x,y)):
            break
        Map[x][y] = '🔳'

    elif(select == 2 and x < MapSize-1):
        Map[x][y] = '⬜'
        x += 1
        if(CheckMap(x,y)):
            break
        Map[x][y] = '🔳'

    elif(select == 3 and y < MapSize-1):
        Map[x][y] = '⬜'
        y += 1
        if(CheckMap(x,y)):
            break
        Map[x][y] = '🔳'

    elif(select == 4 and y > 0):
        Map[x][y] = '⬜'
        y -= 1
        if(CheckMap(x,y)):
            break
        Map[x][y] = '🔳'

    elif(select == 5):
        print('i believe you will come back, GET UP')
        break
    
    else:
        print('We ve never played like that! press the number again ')
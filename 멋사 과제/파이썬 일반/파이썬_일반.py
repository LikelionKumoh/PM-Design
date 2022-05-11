import random
import time

map_size=int(input("맵크기를 입력해주세요. : "))
bomb_cnt=int(input("폭탄 갯수를 입력해주세요. : "))

mapList = []
userx=0
usery=0

def creatmap(mapsize, bomb):

    for _ in range(mapsize):
        sublist= ["⬜" for _ in range(mapsize)]
        mapList.append(sublist)

    mapList[0][0] = '🔳'

    while True:
        x=random.randint(0, mapsize-1)
        y=random.randint(0, mapsize-1)
        if(x!=0 or y!=0):
            mapList[x][y]="💠"
            break

    for _ in range(bomb):
        while True:
            x=random.randint(0, mapsize-1)
            y=random.randint(0, mapsize-1)
            if(x!=0 or y!=0):
                mapList[x][y]="🔺"
                break
        
creatmap(map_size, bomb_cnt)

def pointmove(t):
    global userx, usery

    nx=userx
    ny=usery

    if (t == 1):
        nx=nx+1
        ny=ny
        if(nx > -1 and nx < map_size):
            if(mapList[nx][ny] == '⬜'):
                mapList[nx][ny] = '🔳'
                mapList[nx - 1][ny] = '⬜'
                userx = nx
                usery = ny
                return True
            else:
                return False

    if (t == 2):
        nx=nx
        ny=ny+1
        if(ny > -1 and ny < map_size):
            if(mapList[nx][ny] == '⬜'):
                mapList[nx][ny] = '🔳'
                mapList[nx][ny-1] = '⬜'
                userx = nx
                usery = ny
                return True
            else:
                return False

    if (t == 3):
        nx=nx-1
        ny=ny
        if(nx > -1 and nx < map_size):
            if(mapList[nx][ny] == '⬜'):
                mapList[nx][ny] = '🔳'
                mapList[nx+1][ny] = '⬜'
                userx = nx
                usery = ny
                return True
            else:
                return False

    if (t == 4):
        nx=nx
        ny=ny-1
        if(ny > -1 and ny < map_size):
            if(mapList[nx][ny] == '⬜'):
                mapList[nx][ny] = '🔳'
                mapList[nx][ny+1] = '⬜'
                userx = nx
                usery = ny
                return True
            else:
                return False

print("==========게임을 시작하겠습니다.==========")

while True:
    for r in range(map_size):
        for f in range(map_size):
            print(mapList[r][f], end = "")
        print()

    print("1. 아래로 이동\n2. 오른쪽 이동\n3. 위로 이동\n4. 왼쪽으로 이동\n5. 종료\n")
    menunum = int(input("메뉴를 선택 해 주세요. : "))

    if(menunum == 1):
        if(pointmove(1)):
            print("아래로 이동합니다.")
            time.sleep(2)
            continue
        else:
            print("게임을 종료하겠습니다.")
            time.sleep(2)
            break

    elif(menunum == 2):
        if(pointmove(2)):
            print("오른쪽으로 이동합니다.")
            time.sleep(2)
            continue
        else:
            print("게임을 종료하겠습니다.")
            time.sleep(2)
            break

    elif(menunum == 3):
        if(pointmove(3)):
            print("위로 이동합니다.")
            time.sleep(2)
            continue
        else:
            print("게임을 종료하겠습니다.")
            time.sleep(2)
            break
    
    elif(menunum == 4):
        if(pointmove(4)):
            print("왼쪽로 이동합니다.")
            time.sleep(2)
            continue
        else:
            print("게임을 종료하겠습니다.")
            time.sleep(2)
            break

    elif(menunum == 5):
        print("게임을 종료하겠습니다.")
        time.sleep(2)
        break
    
    else:
        print("옵션에 있는 메뉴 번호를 선택 해 주세요.")
        time.sleep(2)
        continue
    

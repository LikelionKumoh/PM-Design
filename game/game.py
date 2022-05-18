import random
import time

n=0
m=0

list_input=int(input("맵 크기를 지정하여 주세요 : "))
bomb = int(input("폭탄 개수를 정해 주세요 : "))

#이중리스트
main_list = []

def asdf(a,b):    
    for _ in range(a):
        sublist = ['⬜' for _ in range(a)]
        main_list.append(sublist)

    main_list[0][0] = '🔳'

#보석 좌표 지정
    while True:
        k = random.randint(0,a-1)
        l = random.randint(0,a-1)
        if k !=0 or l !=0:
            main_list[k][l]='💠'
            break

#폭탄 좌표 지정
    for _ in range(b):
        while True:
            k = random.randint(0,a-1)
            l = random.randint(0,a-1)
            if main_list[k][l] !='💠' and main_list[k][l] !='🔳':
                main_list[k][l]='🔺'
                break

asdf(list_input,bomb)

def fdasf(i):
    global n, m

    if i == 1:
        nx=n+1
        my=m

        if nx>-1 and nx < list_input:
            if main_list[nx][my] == '⬜':
                main_list[nx][my] = '🔳'
                main_list[nx-1][my] = '⬜'
                n=nx
                m=my
                return True
            else: 
                return False
        else:
            return False
    elif i == 2:
        nx=n-1
        my=m
        if nx>-1 and nx < list_input:
            if main_list[nx][my] == '⬜':
                main_list[nx][my] = '🔳'
                main_list[nx+1][my] = '⬜'
                n=nx
                m=my
                return True
            else: 
                return False
        else:
            return False
    elif i == 3:
        nx=n
        my=m+1
        if my>-1 and my<list_input:
            if main_list[nx][my] == '⬜':
                main_list[nx][my] = '🔳'
                main_list[nx][my-1] = '⬜'
                n=nx
                m=my
                return True
            else: 
                return False
        else:
            return False
    elif i == 4:
        nx=n
        my=m-1
        if my>-1 and my<list_input:
            if main_list[nx][my] == '⬜':
                main_list[nx][my] = '🔳'
                main_list[nx][my+1] = '⬜'
                n=nx
                m=my
                return True
            else: 
                return False
        else:
            return False

while True:
    for i in range(list_input):
        for j in range(list_input):
            print(main_list[i][j], end='')
        print()

    print("1.아래로 이동\n2.위로 이동\n3.오른쪽 이동\n4.왼쪽 이동\n5.게임 종료\n")

    main_number = int(input("원하는 숫자를 입력하여 주세요 :"))

    if main_number ==1:
        if fdasf(1):
            print("\n아래로 이동\n")
            time.sleep(2)
        else:
            print('게임을 종료합니다.')
            time.sleep(2)
            break
    elif main_number ==2:
        print("\n위로 이동\n")
        if fdasf(2):
            print("\n아래로 이동\n")
            time.sleep(2)
        else:
            print('게임을 종료합니다.')
            time.sleep(2)
            break
    elif main_number ==3:
        print("\n오른쪽 이동\n")
        if fdasf(3):
            print("\n아래로 이동\n")
            time.sleep(2)
        else:
            print('게임을 종료합니다.')
            time.sleep(2)
            break
    elif main_number ==4:
        if fdasf(4):
            print("\n아래로 이동\n")
            time.sleep(2)
        else:
            print('게임을 종료합니다.')
            time.sleep(2)
            break
    elif main_number ==5:
        print("\n게임 종료\n")
        break
    else:
        print("\n이용이 불가능한 값입니다\n")
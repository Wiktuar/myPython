
list = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def printList(list):
    for i in list:  
        for j in i:
            print(f' {j}', end = " |");0
        print('\n --  --  --')

printList(list)

# функция хода
def move(data):
    iList = []
    while True:
        iList = input().split()
        if list[int(iList[0])][int(iList[1])] == " ":
            list[int(iList[0])][int(iList[1])] = data;
            printList(list)
            break
        else:
            print("Ячейка занята. Введите другой адрес")

def getIsWin():
    isWin = False;
    if (list[0][0] == list[0][1] == list[0][2] and list[0][0] != " "): isWin = True
    elif (list[1][0] == list[1][1] == list[1][2] and list[1][0] != " "): isWin = True
    elif (list[2][0] == list[2][1] == list[2][2] and list[2][0] != " "): isWin = True

    elif (list[0][0] == list[1][0] == list[2][0] and list[0][0] != " "): isWin = True
    elif (list[0][1] == list[1][1] == list[2][1] and list[0][1] != " "): isWin = True
    elif (list[0][2] == list[1][2] == list[2][2] and list[0][2] != " "): isWin = True

    elif (list[0][0] == list[1][1] == list[2][2] and list[0][0] != " "): isWin = True
    elif (list[0][2] == list[1][1] == list[2][0] and list[0][2] != " "): isWin = True
    return isWin

# ход первого игрока
def human1():
    move("X");
    return getIsWin()

# ход второго игрока   
def human2():
    move("0");
    return getIsWin()
        

count = 0;
while(True):
    if(human1() == True):
        print("Первый игрок выиграл!")
        break
   
    count+=1
   
    if(count == 9):
        print("Ничья!!!")
        break
    
    if(human2() == True):
        print("Второй игрок выиграл!")
        break
    
    count+=1

    if(count == 9):
        print("Ничья!!!")
        break





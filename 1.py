import random;

total = 120;

# ход человека
def human():
    humanData = 50;
    while  humanData < 1 or humanData > 28:
        print("Введите число от 1 до 28");
        humanData = int(input());
        print('Вы ввели', humanData);

    return humanData;
        
# ход "глупого" компьютера 
def computer():
   computerData = random.randint(1, 28);
   print('Компьютер ввел', computerData);
   return computerData;

# ход "умного" компьютера. Он всегда выигрывает. 
def computer(total):
   computerData = total % 29;
   print('Компьютер ввел', computerData);
   return computerData;

# игровой цикл
while total != 0:
    total -= human();
    print('Осталось конфет', total);
    if(total <= 0):
        print("Human win!");
        break;

    total -= computer(total);
    print('Осталось конфет', total);
    if(total <= 0):
        print("Computer win!");

    
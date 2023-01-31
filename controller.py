import view as v
import model as m

def start():
    print("Вы зашли как: \n 1 - ученик \n 2 -учитель")
    data = int(input())
    if data == 1:
        v.showPuple()
    else:
        v.showAllPuples("c:\help\\puples.txt")
        print("Что Вы хотите сделать: \n 1 - добавить ученика \n 2 - добавить оценки")
        data = int(input())
        if data == 1:
            m.addPuple()
        else:
            m.addGrade()

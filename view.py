# метод просмотра списка учеников
def showAllPuples(path):
    listOfPuples = []
    data = open(path, 'r')
    for line in data:
        listOfPuples.append(line[:len(line) - 1])   
    data.close() 

    for puple in listOfPuples:
        print(puple)

# метод просмотра списка своих оценок учеником
def showPuple():
    print("Введите Ваше имя и фамилию")
    puple = input()
    data = open('C:\help\\puples\\' + puple + '.txt', 'r')
    for d in data:
        print(d)
    data.close()



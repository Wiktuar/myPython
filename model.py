# метод добавления ученика
def addPuple():
    output = open("C:\help\\puples.txt", 'a')
    puple = input()
    output.writelines(puple + "\n")
    output.close()
# ученик одновременно добавляется в файл с учениками, где хранится список всех учеников,
# но и создается в отдельной папке файл, где хранятся оценки ученика по предметам
    newPuple = open('C:\help\\puples\\' + puple + '.txt', 'w+')
    subjects = []
# в этом цикле можно добавить первичный список предметов и оценок. Они щаписываются в файл ученика
    while(True):
        subject = input()
        if(subject == 'OK'): break
        subjects.append(subject)
    
    for s in subjects:
        newPuple.writelines(s + '\n')

    newPuple.close()

# метод добавления оценки
def addGrade():
    print("Введите имя и фамилию ученика")
    puple = input()
    data = open('C:\help\\puples\\' + puple + '.txt', 'r')
    subject_dictionary = {}
    subject_list = []
# здесь выводятся все оценки ученика и одновременно они записываются в словарь
# на основе которого потом они будут редактироваться
    for d in data:
        subject_list = d.split(':')
        print(subject_list[0] + ":" + subject_list[1])
        subject_dictionary[subject_list[0]] = subject_list[1]
        subject_list.clear()

    data.close()
# выбирается предмет для изменения оценки
    print("Введите название предмета, по котрому Вы хотите добавить оценку")
    subject = input()
    grades = subject_dictionary[subject]
    print(grades)
# оценка добавляется в строку оценок и потом весь файл с оценками заново переписывается на основе словаря
    print("Введите оценки ученика")
    grade = input()
    grades = grades + " " + grade
    subject_dictionary[subject] = grades

    data1 = open('C:\help\\puples\\' + puple + '.txt', 'w')
    for key in subject_dictionary.keys():
        data1.writelines(key[0: -2] + " :" + subject_dictionary[key] + '\n')

    data1.close()

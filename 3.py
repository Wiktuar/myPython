list = [1, 4, 4, 4, 5, 5] 

bool = False #если совпадение нашлось, то эта переменная переключается в True
             # что означает необходимость удаления элемента с которым савниваются все
             # все прочие в последовательности

for i in range(len(list) - 1):
    bool = False
    if i == 0: continue
    index = i
    for j in range(index + 1, len(list)):
        if list[i] == list[j]:
            list[j] = 0
            bool = True
    if bool == True: list[i] = 0

resultList = []

# в итоговый список добавляем все элементы, неравные нулю 
for i in list:
    if i == 0: continue
    resultList.append(i)

print(resultList)
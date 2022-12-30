list = [2, 4, 6, 8, 10, 12]
resultList = []

for i in range(0, round(len(list) / 2)):
    resultList.append(list[i] * list[len(list) - 1 - i])

print(resultList)
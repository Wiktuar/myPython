list = [1.1, 1.2, 3.1, 5, 10.01]
resultList = []

for i in list:
    resultList.append(round(i % 1, 2))

max = resultList[0]
min = resultList[0]

for i in range(1, len(resultList)):
    if resultList[i] == 0: 
        continue
    if resultList[i] > max:
        max = resultList[i]
    if resultList[i] < min:
        min = resultList[i]

print(max - min)
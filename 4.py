import random

k = int(input())

list = []

for i in range(k+1):
    list.append(random.randint(0, 100))

print(list)

s = "x"
finalstr = ""
while True:
    if k == 0:
        finalstr += (f'{list[len(list) - 1]}')
        break
    if k == 1:
        finalstr += (f'{list[len(list) - 2]}{s}+')
        k -= 1
        continue
    finalstr += (f'{list[len(list) - (k+1)]}{s}^{k}+')
    k -= 1

print(finalstr)
digit = int(input())
list = []
for i in range(-digit, digit+1):
    list.append(i)

indexes = [1, 2, 3, 5, 7]
result = 1

for i in indexes:
    result*=list[i]

print(result)


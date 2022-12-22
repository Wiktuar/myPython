x = int(input('Введите число: '))
y = int(input('Введите число: '))

if x > 0 and y > 0:
    print('Первая четверть')
elif x > 0 and y < 0:
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
else:
    print('Четвертая четверть')
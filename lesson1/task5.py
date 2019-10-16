print('Программа расчета для спортсмена')

distance = int(input('Введите растояние: '))
aim = int(input('Введите желаемое растояние: '))
day = 0

while True:
    distance = distance + int((10 * distance / 100))
    day += 1

    if distance >= aim:
        break
    else:
        continue
print(f'Дней нужно бегать: {day}')
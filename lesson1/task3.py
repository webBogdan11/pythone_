print('Программа самая большая цифра')

n = int(input('Введите число: '))
mult = 1
max = 0

while  n > 0:
    mult *= 10
    a = n % mult
    n = n - a

    if a / (mult / 10) > max:
        max = a / (mult / 10)

print(f'Вот ваш результат: {int(max)}')



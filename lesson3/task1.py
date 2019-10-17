print('Деление')


def calc_divide ():
    while True:

        num1 = input('Введите делимое: ')
        num2 = input('Введите делитель: ')

        try:
            num1 = int(num1)
            num2 = int(num2)
        except ValueError as e:
            print(f'e - Это не число. Введите данные снова')
            continue

        if num1 == 0 or num2 == 0:
            print('Делить на ноль нельзя, введите еще раз данные')
        else:
            return num1 / num2


print(calc_divide())
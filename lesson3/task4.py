print('Возведение в целую степень')


def my_func(x, y):

    if x > 0 and y < 0:
        return x ** y
    else:
        print('Неверный типа данных')


print(my_func(3, -4))
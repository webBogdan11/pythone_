print('Сума чисел')


def sum_of_numbers():
    result = 0
    flag = True
    while flag:
        numbers = input('Введите числе через пробел: ').split(' ')
        numbers_for_sum = []

        for item in numbers:
            if item.isdigit():
                numbers_for_sum.append(int(item))
            else:
                flag = False

        result = result + sum(numbers_for_sum)
        print(result)
    return 'Неправильный ввод'


print(sum_of_numbers())
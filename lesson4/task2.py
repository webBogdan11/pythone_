"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""
print('Numbers')

list_of_numbers = input('Введите числа через пробел: ').split(' ')

try:
    for itm in list_of_numbers:
        itm = int(itm)
        print(itm)

except ValueError as e:
    print(f'Неправильный ввод {e}')
    exit()

print(list_of_numbers)


def seeker(list_numbs):
    first_itm = list_numbs[0]

    for el in list_numbs:
        if el > first_itm:
            yield el
        first_itm = el


for element in seeker(list_of_numbers):
    print(element)

assert 'first test', list(seeker([1, 5, 4, 7, 8, -1, 0, 2])) == [5, 7, 8, 0, 2]
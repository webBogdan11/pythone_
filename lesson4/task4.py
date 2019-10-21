"""
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
обязательно использовать генератор
"""

list_of_numbers = input('Введите числа через пробел: ').split(' ')
list_for_use = []
try:
    for el in list_of_numbers:
        list_for_use.append(int(el))

except ValueError as e:
    print(f'Неправильный ввод {e}')
    exit()

print(list_for_use)


def definer(list_of_numb):
    for itm in list_of_numb:

        if list_of_numb.count(itm) == 1:
            yield itm


for element in definer(list_for_use):
    print(element)

assert 'control test', list(definer([1, 1, 2, 2, 3, 4, 5, 3])) == [4, 5]

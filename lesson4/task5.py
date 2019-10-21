"""
Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные числа
от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from random import randint
from functools import reduce

i = 1
my_list = []
while i <= 4:
    my_list.append(randint(100, 1000))
    i = i + 1

print(my_list)

result = reduce(lambda x, y : x * y, my_list)
print(result)
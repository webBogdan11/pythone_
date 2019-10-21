"""
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""

from itertools import count
from itertools import cycle

my_count = count
for el in my_count(5):
    print(el)

my_cycle = cycle
for el in cycle('gelloi'):
    print(el)


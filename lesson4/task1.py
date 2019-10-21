"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

args = argv

production_in_hours = args[1]
rate = args[2]
bonus = args[3]

try:
    production_in_hours = int(production_in_hours)
    rate = int(rate)
    bonus = int(bonus)
except ValueError as e:
    print(f'Неверный ввод данных {e}')
    exit()


def salary_counter(prod_im_hours, rt, bn):
    salary = (prod_im_hours * rt) + bn
    return salary


print(salary_counter(production_in_hours, rate, bonus))

assert salary_counter(20, 60, 23) == 1223, 'salary_counter(20, 60, 23)'
assert salary_counter(12, 56, 24) == 696, 'salary_counter(20, 60, 23)'

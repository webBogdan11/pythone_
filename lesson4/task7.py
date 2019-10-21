"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fibo_gen().
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
from itertools import count


def fibo(n):
    i = 1
    result = 1
    while i <= n:
        result = result * i
        i = i + 1
    return result


def fibo_gen():
    start_number = 1
    for _ in count(1):
        yield fibo(start_number)
        start_number = 1 + start_number


cnt = 0
for item in fibo_gen():

    if cnt < 15:
        print(item)
    else:
        break
    cnt = 1 + cnt


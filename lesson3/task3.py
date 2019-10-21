print('Сумма наибольших')


def my_func (num1, num2, num3):
    list_of_numbers = [num1, num2, num3]

    first_max = max(list_of_numbers)
    list_of_numbers.remove(first_max)
    second_max = max(list_of_numbers)

    return first_max + second_max


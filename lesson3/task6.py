print('Программа регистер')


def int_func(string):
    return string.lower().capitalize()


strings = input('Введите строки через пробел: ')
strings = strings.split(' ')
result_list = []

for item in strings:
    result_list.append(int_func(item))

result_string = ' '.join(result_list)

print(result_string)
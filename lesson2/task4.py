print('Строки')

lines = input('Введите слова разделенные пробелами: ').split(' ')
print(lines)

count = 1
for element in lines:
    if len(element) <= 10:
        result = f'{count} - {element}'
        count += 1
        print(result)
    else:
        element = element[0:10]
        result = f'{count} - {element}'
        count += 1
        print(result)
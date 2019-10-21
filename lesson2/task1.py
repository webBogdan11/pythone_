print("Проверка типа")

list_of_elements = [2, 3, 'hello', [1, 2], {1, 0, 3, }, {'hello': 1, 'good': 2}, (1, 2, 3)]

for key in list_of_elements:
    print(f'{type(key)}')

print(list_of_elements[:-1])
print(list_of_elements)
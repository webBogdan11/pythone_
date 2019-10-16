print('Обмен значений соседних элементов')

elements = input('Заполните список элементами: ')

"""
Преоброзование в списке строки в числа 
"""

elements = elements.split(', ')
for element in elements:
    if element.isdigit():
        elements[elements.index(element)] = int(element)

print(elements)

"""
Обмен значениями  
"""

list_of_elements = elements
i = 0

if len(list_of_elements) %  2 == 0:          # parity check
    while i < len(list_of_elements):
        list_of_elements[i], list_of_elements[i+1] = list_of_elements[i+1], list_of_elements[i]
        i = i + 2
else:
    while i < len(list_of_elements):
        if i == len(list_of_elements) - 1:
            break
        list_of_elements[i], list_of_elements[i+1] = list_of_elements[i+1], list_of_elements[i]
        i = i + 2

print(list_of_elements)
print('Времена года')

month = int(input('Введите число от 1 до 12: '))

time_of_year_in_dict = {
    (12, 1, 2): 'Зима',
    (3, 4, 5): 'Весна',
    (6, 7, 8): 'Лето',
    (9, 10, 11): 'Осень'
}

for key in time_of_year_in_dict:

    for item in key:

        if item == month:
            print(f'{time_of_year_in_dict[key]} - на словарях')


time_of_year_in_list = ['Зима', 'Весна', 'Лето', 'Осень' ]

if month >= 1 and month <= 12:
        if month <= 2 or month == 12:
            print(f'{time_of_year_in_list[0]} - на листах')

        elif month >= 3 and month <= 5:
            print(f'{time_of_year_in_list[1]} - на листах')

        elif month >= 6 and month <= 8:
            print(f'{time_of_year_in_list[2]} - на листах')

        elif month >= 9 and month <= 11:
            print(f'{time_of_year_in_list[3]} - на листах')
else:
    print('error')
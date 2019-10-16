print('Программа расчёта')
proceeds = int(input('Введите вашу выручка: '))
costs =  int(input('Введите ваши издержки: '))
difference = proceeds - costs

if difference > 0:
    print('Ваш финансвой результат прибыль')
    rentability = int(difference / proceeds * 100)
    print(f'Ваша рентабельность: {rentability}%')

    amount_of_staff = int(input('Введите количество работников: '))

    profit_per_employee = proceeds / amount_of_staff
    print(f'Прибыль на одного сотрудника: {int(profit_per_employee)}')

else:
    print('Ваш финансвой результат убыток')
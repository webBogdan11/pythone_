print('Товары')

amount_of_items = int(input('Введите количество товаров: '))

names = []
prices = []
quantity = []
units = []
database = []

number_of_current_product = 1

while number_of_current_product <= amount_of_items:

    current_name = input(f'Введите имя товара №{number_of_current_product}: ')
    names.append(current_name)

    current_price = int(input(f'Введите цену на товар №{number_of_current_product}: '))
    prices.append(current_price)

    current_amount = int(input(f'Введите количество на товар №{number_of_current_product}: '))
    quantity.append(current_amount)

    current_unit = input(f'Введите еденици измерения на товар №{number_of_current_product}: ')
    units.append(current_unit)

    dict_of_database = {
        'Название': current_name,
        'Цена': current_price,
        'Количество': current_amount,
        'eд': current_unit,
    }

    print(dict_of_database)

    database_item = (number_of_current_product, dict_of_database)
    print(database_item)
    database.append(database_item)

    number_of_current_product = number_of_current_product + 1

print(database)

data_for_analytics = {
    'Название': names,
    'Цена': prices,
    'Количество': quantity,
    'ед.': units
}

print(data_for_analytics)
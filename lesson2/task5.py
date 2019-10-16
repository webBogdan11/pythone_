print('Структура рейтинг')

my_list = [7, 5, 3, 3, 2]

request = input('Введите число: ')

if request.isdigit():

    new_item = int(request)                                     # create the variable with our data

    if new_item in my_list:                                     # check availability our variable in the list
        my_list.insert(my_list.index(new_item), new_item)       # add variable if it is in the list

    else:                                                       # we start this branch of code for another case
        if new_item < my_list[len(my_list) - 1]:                # first of all we check case for the smallest number
            my_list.append(new_item)

        else:                                                   # this case for number among our list
            for element in my_list:                             # start the cycle where we compare our item with other

                if new_item > element:
                    my_list.insert(my_list.index(element), new_item)
                    break

                else:
                    continue

    print(my_list)

else:
    print('error')



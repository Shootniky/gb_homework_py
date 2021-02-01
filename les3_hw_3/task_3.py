""" 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
, и возвращает сумму наибольших двух аргументов. """


def my_func(num_1, num_2, num_3):
    try:
        num_1, num_2, num_3 = int(num_1), int(num_2), int(num_3)
    except ValueError:
        return 'Ошибка ввода данных!'
    my_list = [num_1, num_2, num_3]
    try:
        my_list.remove(min(my_list))
        return f'Сумма двух наибольших чисел, введённых вами - равняется {sum(my_list)}'
    except TypeError:
        return "Вы ввели не число!"


print(my_func(input('Введите первое число - '), input('Введите второе число - '), input('Введите второе число - ')
              ))

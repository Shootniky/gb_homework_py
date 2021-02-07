""" 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
, и возвращает сумму наибольших двух аргументов. """


def my_func(num_1, num_2, num_3):
    try:
        num_1, num_2, num_3 = int(num_1), int(num_2), int(num_3)
    except ValueError:
        return 'Ошибка ввода данных!'
    my_list = [num_1, num_2, num_3]
    return f'Сумма двух наибольших чисел, введённых вами, равняется {sum(sorted(my_list)[1:])}'


print(my_func(input('Введите первое число - '), input('Введите второе число - '), input('Введите третье число - ')
              ))
my_func = lambda num_1, num_2, num_3: (num_1 + num_2 + num_3) - min(num_1, num_2, num_3)

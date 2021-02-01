""" 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль. """


def div(num_1, num_2):
    try:
        num_1, num_2 = int(num_1), int(num_2)
        div_num = num_1 / num_2
    except ValueError:
        return 'Ошибка ввода данных!'
    except ZeroDivisionError as e:
        return f'Вы пытаетесь делить на 0 ({e})'
    return round(div_num, 4)


print(div(input('Введите первое число - '), input('Введите второе число - ')))

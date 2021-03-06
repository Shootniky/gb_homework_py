""" 4. Программа принимает действительное положительное число x и целое
отрицательное число y. Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y). При решении
задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение
в степень с помощью оператора **. Второй — более сложная реализация без
оператора **, предусматривающая использование цикла. """


def my_func(x, y):
    return 1 if y == 0 or x < 0 else my_func(x, y + 1) * 1 / x


try:
    print(my_func(int(input('Введите первое число - ')), int(input('Введите второе число - '))))
except ValueError:
    print('Ошибка ввода данных!')

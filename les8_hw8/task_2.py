""" 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться
 с ошибкой. """


class MyException(Exception):
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    @staticmethod
    def divisional(dividend, divider):
        try:
            return dividend / divider
        except Exception:
            return f'Ошибка: На 0 делить нельзя!'


operation = MyException(45, 1200)
print(operation.divisional(12, -0.001))
print(operation.divisional(45, 0))
print(operation.divisional(-1200, 45))
print(operation.divisional(1200, 45))

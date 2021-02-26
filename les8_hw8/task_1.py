""" 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый,
с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных. """


class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        print(cls, date_as_string)
        return date1

    @staticmethod
    def date_static(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        if day <= 31 and day != 0 and month <= 12 and month != 0 and year <= 2021:
            print(date_as_string)
            return day, month, year
        else:
            print('Ошибка ввода данных')


date = '26-02-2021'
first_method = Date.from_string(date)
second_method = Date.date_static(date)
date = '62-02-2021'
first_method_2 = Date.from_string(date)
second_method_2 = Date.date_static(date)
date = '12-32-2021'
first_method_3 = Date.from_string(date)
second_method_3 = Date.date_static(date)
date = '12-12-2041'
first_method_4 = Date.from_string(date)
second_method_4 = Date.date_static(date)

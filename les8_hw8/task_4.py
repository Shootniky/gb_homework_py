""" 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.Эти классы — конкретные типы
оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники. """


class Stock:
    """Класс, описывающий склад оргтехники"""
    # print("Класс, описывающий склад оргтехники")


class OfficeWarehouse(Stock):

    def __init__(self, production, color):
        self.manufact = production
        self.color = color


class Printer(OfficeWarehouse):

    def __init__(self, production, color, printer):
        super().__init__(production, color)
        self.printer = printer

    @staticmethod
    def name():
        print("Принтер:", end=' ')

    def print_type(self):
        return self.printer


class Scanner(OfficeWarehouse):

    def __init__(self, production, color, scanner):
        super().__init__(production, color)
        self.sc_sensor = scanner

    @staticmethod
    def name():
        print("Сканер:", end='  ')

    def sensor_type(self):
        return self.sc_sensor


class Xerox(OfficeWarehouse):

    def __init__(self, production, color, xerox):
        super().__init__(production, color)
        self.xerox = xerox

    @staticmethod
    def name():
        print("Ксерокс:", end=' ')

    def wi_fi_module(self):
        return self.xerox


device_1 = Printer('Canon', 'белый', 'струйный')
device_1.name()
print(f'\tпроизводитель: {device_1.manufact}\tцвет: {device_1.color} \tтип принтера: {device_1.print_type()}')
device_2 = Scanner('Epson', 'серый', 'CIS')
device_2.name()
print(f'\tпроизводитель: {device_2.manufact} \tцвет: {device_2.color} \tтип сенсора: {device_2.sensor_type()}')
device_3 = Xerox('Cuosera', 'серый', 'есть')
device_3.name()
print(f'\tпроизводитель: {device_3.manufact} \tцвет: {device_3.color} \tWi-Fi модуль: {device_3.wi_fi_module()}')

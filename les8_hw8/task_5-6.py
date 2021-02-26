""" 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
оргтехники на склад и передачу в определенное подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП."""


class Stock:
    """Класс, описывающий склад оргтехники"""
    # print("Класс, описывающий склад оргтехники")


class OfficeWarehouse(Stock):

    def __init__(self, production, color):
        self.manufact = production
        self.color = color


class Printer(OfficeWarehouse):
    amount_printers = 0

    def __init__(self, production, color, printer):
        super().__init__(production, color)
        self.printer = printer
        Printer.amount_printers += 1

    @staticmethod
    def name():
        return "'Принтер':"

    def print_type(self):
        return self.printer

    def __str__(self):
        return "\tпроизводитель: {} \tцвет: {}  \tтип принтера: {}".format(self.manufact, self.color, self.print_type())


class Scanner(OfficeWarehouse):
    amount_scanners = 0

    def __init__(self, producer, color, scanner):
        super().__init__(producer, color)
        self.sc_sensor = scanner
        Scanner.amount_scanners += 1

    @staticmethod
    def name():
        return "'Сканер':"

    def type_sensor(self):
        return self.sc_sensor

    def __str__(self):
        return "\tпроизводитель: {} \tцвет: {} \tтип сенсора: {}".format(self.manufact, self.color, self.sc_sensor)


class Xerox(OfficeWarehouse):
    amount_xerox = 0

    def __init__(self, production, color, xer_wi_fi):
        super().__init__(production, color)
        self.xer_wi_fi = xer_wi_fi
        Xerox.amount_xerox += 1

    @staticmethod
    def name():
        return "'Ксерокс':"

    def wi_fi_module(self):
        return self.xer_wi_fi

    def __str__(self):
        return "\tпроизводитель: {} \tцвет: {}   \tWi-Fi модуль: {}".format(self.manufact, self.color, self.xer_wi_fi)


device_1_printer = Printer('Canon', 'белый', 'струйный')
device_2_printer = Printer('Brother', 'серый', 'лазер, диод')
device_3_printer = Printer('Epson', 'чёрный', 'лазер, матрица')
print(device_1_printer.name(), device_2_printer.amount_printers, "шт.")
print(device_1_printer.__str__())
print(device_2_printer.__str__())
print(device_3_printer.__str__())

device_4_scanner = Scanner('Cuosera', 'серый', 'CIS')
device_5_scanner = Scanner('Samsung', 'белый', 'CCD')
device_6_scanner = Scanner('Cuosera', 'чёрный', 'CIS')
print(device_4_scanner.name(), device_5_scanner.amount_scanners, "шт.")
print(device_4_scanner.__str__())
print(device_5_scanner.__str__())
print(device_6_scanner.__str__())

device_7_xerox = Xerox('Samsung', 'чёрный', 'есть')
device_8_xerox = Xerox('Epson', 'серый', 'есть')
device_9_xerox = Xerox('Xerox', 'чёрный', 'есть')
device_10_xerox = Xerox('Cuosera', 'белый', 'нет')
print(device_7_xerox.name(), device_8_xerox.amount_xerox, "шт.")
print(device_7_xerox.__str__())
print(device_8_xerox.__str__())
print(device_9_xerox.__str__())
print(device_10_xerox.__str__())

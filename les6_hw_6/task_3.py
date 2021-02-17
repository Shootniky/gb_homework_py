""" 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут должен
быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
на базе класса Worker. В классе Position реализовать методы получения полного
имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров)."""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{sum(self._income.values())}'


manager = Position('Garry', 'Thompson', 'HR', 230900, 10000)
manager_2 = Position('Freya', 'Davidson', 'designer', 240100, 12000)
print(f'Полное имя сотрудника: {manager.get_full_name()}')
print(f'Занимаемая должность: {manager.position}')
print(f'Доход с учётом премии: {manager.get_total_income()}')
print(10 * '-------')
print(f'Полное имя сотрудника: {manager_2.get_full_name()}')
print(f'Занимаемая должность: {manager_2.position}')
print(f'Доход с учётом премии: {manager_2.get_total_income()}')

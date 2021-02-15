""" 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Выполните вызов методов и также покажите результат. """
speedy = 'Я превышаю'


class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Новая машина: {self.name}, цвет: ({self.color}), скорость: {self.speed}, '
              f'машина полицейская - {self.is_police}')

    def go(self):
        print(f'{self.name}: Замечено: машина поехала')

    def stop(self):
        print(f"{self.name}: Замечено: машина остановилась")

    def turn(self, direction):
        print(f"{self.name}: Замечено: машина повернула {'налево' if direction == 0 else 'направо'}")

    def show_speed(self):
        print(f'Скорость: {self.speed}')

    def speed_increase(self):
        print(f'Скорость: {self.speed}')


class WorkCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Замечено превышение! Скорость: {self.speed}')
        else:
            print(f'Скорость: {self.speed}')


class TownCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Замечено превышение! Скорость: {self.speed}')
        else:
            print(f'Скорость: {self.speed}')


class SportCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


town = TownCar('Reno', 'blue', 0)
town.go()
town.turn(0)
town.turn(1)
town.show_speed()
town.speed = 40
town.show_speed()
town.speed = 80
town.show_speed()

work = WorkCar('Tatra', 'gray', 0)
work.go()
work.turn(0)
work.turn(1)
work.show_speed()
work.speed = 40
work.show_speed()
work.speed = 60
work.show_speed()

police = PoliceCar('Citroen', 'white', 0)
police.go()
police.turn(0)
police.turn(1)
police.show_speed()
police.speed = 40
police.show_speed()
police.speed = 60
police.show_speed()
police.speed = 90
police.show_speed()

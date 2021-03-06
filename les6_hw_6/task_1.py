""" 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color
(цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках метода
 реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго
(желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между
режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
выводить соответствующее сообщение и завершать скрипт. """

import time
import itertools


class TrafficLight:
    __color = [["red", [7, 31]], ["yellow", [2, 33]], ["green", [5, 32]]]

    def running(self):
        for light in itertools.cycle(self.__color):
            print(f"\r\033[{light[1][1]}m\033[3m{light[0]}\033[2m", end="")
            time.sleep(light[1][0])


t_1 = TrafficLight()
t_1.running()

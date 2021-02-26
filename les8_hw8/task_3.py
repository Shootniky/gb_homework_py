""" 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на
 наличие только чисел. Проверить работу исключения на реальном примере. Необходимо
запрашивать у пользователя данные и заполнять список. Класс-исключение должен
контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и
строки. При вводе пользователем очередного элемента необходимо реализовать проверку
типа элемента и вносить его в список, только если введено число. Класс-исключение
должен не позволить пользователю ввести текст (не число) и отобразить соответствующее
сообщение. При этом работа скрипта не должна завершаться. """


class NotStringError(Exception):
    def __str__(self):
        return 'Внимание! Неверное значение введённых данных!'


number_list = []
stop = False


def control_value(element):
    if element.isdigit():
        number_list.append(int(element))
    elif element.replace('.', '').isdigit():
        number_list.append(float(element))
    else:
        raise NotStringError(element)


while not stop:
    data = input("Введите числа через пробел. Для выхода введите команду: 'stop' >>> ").split()
    for el in data:
        try:
            control_value(el.rstrip(','))
        except NotStringError as exception:
            if el.rstrip(',').lower() == 'stop':
                stop = True
            else:
                print(f"'{el.rstrip(',')}' - это строка, добавлена не будет")
                continue

print(number_list)
"""2. Пользователь вводит время в секундах. Переведите время в часы,
минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк. """

user_date = int(input('Пользователь вводит время в секундах:  '))


if user_date > 345600:
    print('Пользователь ввёл слишком большое число, за гранью четвёртых суток!!! Программа завершена. ')
    quit()


def time(seconds):
    hour = seconds // 3600
    minute = seconds % 3600 // 60
    second = seconds % 3600 % 60
    return '{:02d}:{:02d}:{:02d}'.format(hour, minute, second)


time_in = time(user_date)
print(time_in)

"""2. Пользователь вводит время в секундах. Переведите время в часы,
минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк. """


user_data = int(input('Пользователь вводит время в секундах: '))

if user_data > 345600:
    print('Пользователь ввёл время в секундах больше чем четверо суток. Программа будет завершена!')
    quit()

minute, second = divmod(user_data, 60)
hour, minute = divmod(minute, 60)

print(f'{hour:d}:{minute:02d}:{second:02d}')

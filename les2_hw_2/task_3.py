""" 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict. """

# with a list
month = 0
months = ['Декабрь', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
          'Ноябрь']
try:
    month = int(input('Пользователь вводит месяц числом от 1 до 12: '))
except ValueError as e:
    print(e)
winter = months[0:3]
spring = months[3:6]
summer = months[6:9]
autumn = months[9:12]
if 2 < month < 6:
    print('Ваш месяц весенний', spring)
elif month == 6 and month < 9:
    print('Ваш месяц летний', summer)
elif month == 9 and month < 12:
    print('Ваш месяц осенний', autumn)
elif month == 1 or month == 2 or month == 12:
    print('Ваш месяц зимний', winter)
elif month > 12 or month < 1 and month == int:
    print('Вы ввели числа за пределами периода года 1-12!')

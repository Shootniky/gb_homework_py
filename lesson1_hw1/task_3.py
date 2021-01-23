""" 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369. """

user_number = input('Введите ваше число, и мы его проапгрейдим: ')

print(f'Ваше число - {user_number}. Сейчас мы возьмём {user_number} + {user_number}{user_number} +'
      f'{user_number}{user_number}{user_number}')
result = int(user_number) + int(f'{user_number}{user_number}') + int(f'{user_number}{user_number}{user_number}')
print(f'И получим результат: {result}')
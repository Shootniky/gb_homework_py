""" 4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции. """

less_number = '1'
user_number = input('Пользователь вводит целое положительное число: ')
for number in user_number:
    if number > less_number:
        less_number = number
result = int(less_number)
print(f'Самая большая цифра в числе {user_number} - цифра {less_number}')

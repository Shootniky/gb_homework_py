""" 4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции. """

user_number = int(input('Пользователь вводит целое положительное число: '))
name = user_number
result = -1
while user_number > 10:
    quotient = user_number % 10
    user_number //= 10
    if quotient > result:
        result = quotient
print(f'Самая большая цифра в числе {name} - цифра {result}')

""" 1. Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран. """

name = 'имя'
age = 'возраст'
gender = 'пол'
male = 'мужчина'
female = 'женщина'
yours = 'ваш'
print(f'Здесь какое-то {yours}е {name} и {yours} {age}, и {yours} {gender}!')
user_name = input(f'Введите пожалуйста {yours}е имя с большой буквы: ')
user_age = float(input('Введите числом сколько вам лет: '))
user_gender = input(f'{yours} {gender} - {male} или {female}? ')
age = 'лет'
print(f'{yours}e {name} - {user_name}, {yours} {gender} - {user_gender}, {yours} возраст - {user_age} {age}')
age = 'возраст'
male_pensioner = 61.5
female_pensioner = 56.6
if user_age >= male_pensioner and user_gender == male:
    print(f'Дорогой, {user_name}, {yours} {age} по законодательству РФ 2021 года - пенсионный.')
elif 100 - user_age >= female_pensioner and user_gender == female:
    print(f'Дорогая, {user_name}, {yours} {age} по законодательству РФ 2021 года - пенсионный.')
else:
    print(f'{yours} {age} не пенсионный, не забудьте оплатить налоги!')

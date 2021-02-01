""" 2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры
как именованные аргументы. Реализовать вывод данных о пользователе
одной строкой. """


def personal_inf(**kwargs):
    return ' '.join(kwargs.values())


name = input('Введите ваше имя - ')
surname = input('Введите вашу фамилию - ')
birthday = input('Введите дату рождения - ')
city = input('Введите свой город - ')
email = input('Введите ваш email - ')
phone = input('Введите ваш номер телефона - ')

print(personal_inf(name=name, surname=surname, birthday=birthday, city=city, email=email, phone=phone))

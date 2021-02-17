""" 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км. """

day = 'день'
counter = 0
start = 2
print(f'Достижение за 1й {day}: {start}')
finish = 3
result = start + (2 * 0.1)
print(f'Достижение за 2й {day}: {result}')
result = result + (result * 0.1)
print(f'Достижение за 3й {day}: {result}')
result = result + (result * 0.1)
print(f'Достижение за 4й {day}: {result}')
result = result + (result * 0.1)
print(f'Достижение за 5й {day}: {result}')
result = result + (result * 0.1)
print(f'Достижение за 6й {day}: {result}')

while start < finish:
    start = float(input('Пользователь вводит результат тренировки дня: '))
    counter = counter + 1
    if start == 2:
        print(f'{counter}-й {day}: ' "%.0f" % start)
    elif start < 2 or start > 4:
        print('Вы ввели неверные значения для этой задачи. Повторите ввод')
        quit()
    elif start == 2.2:
        print(f'{counter}-й {day}: ' "%.1f" % start)
    else:
        print(f'{counter}-й {day}: {start:.2f}')
print(f'Ответ: на {counter}-й {day} спортсмен достиг результата — не менее 3 км.')
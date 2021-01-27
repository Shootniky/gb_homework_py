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

ls = []
day = 'день'
counter = 0
start = 2
ls.append(start)
print(f'Достижение за 1й {day}: {start}')
finish = 3
result = start + (2 * 0.1)
ls.append(result)
print(f'Достижение за 2й {day}: {result}')
result = result + (result * 0.1)
ls.append(result)
print(f'Достижение за 3й {day}: {result}')
result = result + (result * 0.1)
ls.append(result)
print(f'Достижение за 4й {day}: {result}')
result = result + (result * 0.1)
ls.append(result)
print(f'Достижение за 5й {day}: {result}')
result = result + (result * 0.1)
ls.append(result)
print(f'Достижение за 6й {day}: {result}')
print(ls)
for a in ls:
    result = input('Пользователь вводит результат тренировки дня: ')
    counter = counter + 1
    results = float(result)
    if a == ls[-1]:
        print(f'{counter}-й {day}: {results:.2f}')
        print('Ответ: на 6-й день спортсмен достиг результата — не менее 3 км')
    elif results < ls[0] or results > ls[-1]:
        print('Вы ввели неправильное значение! Повторите ввод!')
        break
    elif results < ls[2]:
        results = str(result)
        print(f'{counter}-й {day}: {results}')
    elif results < ls[-1] > ls[0]:
        print(f'{counter}-й {day}: {results:.2f}')

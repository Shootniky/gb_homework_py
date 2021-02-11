""" 3. Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов. Определить, кто из сотрудников имеет
оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
средней величины дохода сотрудников. """

with open('file_3.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    working = {line.split()[1]: float(line.split()[2]) for line in lines}
    print(f'Средняя заработная плата сотрудников = {round(sum(working.values()) / len(working), 3)}\n'
          f'Сотрудники, чья зп меньше 20000 рублей за текущий период: '
          f'{[pay[0] for pay in working.items() if pay[1] < 20000]}')
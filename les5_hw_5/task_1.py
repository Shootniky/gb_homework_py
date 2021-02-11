""" 1. Создать программно файл в текстовом формате, записать в него построчно
данные, вводимые пользователем. Об окончании ввода данных свидетельствует
пустая строка. """

with open('file.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Введите новую строку: ')
        print('----Чтобы закончить ввод -  оставьте строку пустой!---')
        if not line:
            break
        f.write(f'{line}\n')
file_a = 'file.txt'
f = open(file_a, 'r', encoding='utf-8')
print(f'Вы записали в файл следующее:\n{f.read()}')
f.close()

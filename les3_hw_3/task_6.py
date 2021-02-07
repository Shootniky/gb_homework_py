""" 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских
букв и возвращающую его же, но с прописной первой буквой. Например,
print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем
регистре. Сделать вывод исходной строки, но каждое слово должно начинаться
с заглавной буквы. Необходимо использовать написанную ранее функцию
int_func(). """


def int_func(latin_word):
    latin_alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    return latin_word.title() if not set(latin_word).difference(latin_alphabet) else False


lines = input('Введите строку из слов строчными буквами через пробел: ').split()
for word in lines:
    result = int_func(word)
    if result:
        print(int_func(word), ' ')

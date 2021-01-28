""" 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове. """

counter = 0
words = input('Enter here your words: ').split(' ')

for word in words:
    counter += 1
    if len(word) >= 10:
        word = word[:10]
    print(counter, word)

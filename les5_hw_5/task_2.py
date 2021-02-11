""" 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
 выполнить подсчет количества строк, количества слов в каждой строке. """
with open('file_2.txt', 'r', encoding='utf-8') as f:
    pages = [f'{line}. {" ".join(count.split())} - {len(count.split())} слов ' for line, count in enumerate(f, 1)]
    lines = len(pages)
    print(*pages, f'Количество строк в файле: {lines}', sep='\n')
f.close()

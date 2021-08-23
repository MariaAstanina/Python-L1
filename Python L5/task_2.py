# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет
# количества строк, количества слов в каждой строке.

with open('for_task_2.txt') as f_obj:
    lines = 0
    for num, line in enumerate(f_obj, 1):
        #print(f'В {num} строке {" ".join(line.split()).count(" ") + 1} слов')
        print(f'В {num} строке {len(line.split())} слов')
print(f'В файле {num} строк ')

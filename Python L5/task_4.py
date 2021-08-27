# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

numerals = ('Один', 'Два', 'Три', 'Четыре')
with open('for_task_4.txt', 'r', encoding='utf-8') as f_read, open('new_for_task_4.txt', 'w', encoding='utf-8') as f_write:
    for line in f_read:
        line_list = line.split(' — ')
        line_list[0] = numerals[int(line_list[1])-1]
        f_write.write(' — '.join(line_list))


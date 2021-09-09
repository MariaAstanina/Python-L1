# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
sum_salary = 0
print('Сотрудники с окладом менее 20 тыс.:')
with open('for_task_3.txt', encoding='utf-8') as f_obj:
    for num, line in enumerate(f_obj, 1):
        new_list = line.split()
        sum_salary += float(new_list[1])
        print(new_list[0]) if float(new_list[1]) < 20_000 else False
print(f'Средняя величина дохода сотрудников - {sum_salary / num} руб.')

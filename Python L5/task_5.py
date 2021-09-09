# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран
from functools import reduce


def new_data():
    with open('for_task_5_numbers.txt', 'w') as f_obj:
        f_obj.write(input('Введите числа через пробел - '))


def my_sum(s):
    return sum(map(int, s.split()))


def main():
    new_data()
    with open('for_task_5_numbers.txt') as f_out:
        print(f'Сумма введенных чисел - {my_sum(f_out.readline())}')


main()

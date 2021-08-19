# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n). Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
from math import factorial
from itertools import count


def fact(n):
    for el in count(1):
        yield print(f'{el}! = {factorial(el)}')
        if el == n:
            break
        else:
            el += 1


def main():
    n = int(input('Введите число - '))
    for el in fact(n):
        pass

main()

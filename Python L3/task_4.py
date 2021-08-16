# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def exponentation(base=float, exponent=int):
    """Функция фыполняет операцию возведения числа в степерь"""
    temp = 1
    for exp in range(abs(exponent)):
        temp = temp * base
    if exponent >= 0:
        return temp
    else:
        return 1 / temp


def main():
    try:
        print(exponentation(float(input('Введите основание степени - ')), int(input('Введите показатель степени - '))))
    except ValueError:
        print(f'Ошибка: Ожидалось число')


main()

# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def devision(dividend=float, divisor=float):
    """Функция реализует операцию деления двух чисел. Предусмотрена обработка деления на ноль """
    try:
        return (dividend / divisor)
    except ZeroDivisionError:
        return f'Ошибка: divisor = {divisor} Вы пытаетесь разделить на ноль'


def main():
    try:
        print(devision(float(input('Введите делимое - ')), float(input('Введите делитель - '))))
    except ValueError:
        print('Ошибка: Вы ввели не числа')


main()
